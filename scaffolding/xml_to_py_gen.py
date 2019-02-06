import os
import io
import xmltodict
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_name_for_dict(d, default_name, prev_names):
    """
    Find a suitable name for this dictionary
    """
    name = default_name
    custom_name = d.get('@name')
    if custom_name is not None:
        name = custom_name

    counter = 1
    orig_name = name
    while name in prev_names:
        name = "{}_{}".format(orig_name, counter)
        counter += 1

    prev_names.append(name)

    return name


def fmt_add_children(parent, children, write_fn):
    write_fn("{}.add_children([".format(parent))
    for child in children:
        write_fn("    {},".format(child))
    write_fn("])")


def get_source_string(queue):
    source_string = ""
    current_parent = 'mujoco'
    children = []
    prev_names = []
    with io.StringIO() as fh:

        def write(string):
            print("    {}".format(string), file=fh)

        while queue:
            vertex = queue.pop(0)
            node_name = vertex["__name"]
            node_type = vertex["__type"]
            parent_name = vertex["__parent"]

            # Keep track of where we are in the hierarchy
            # If we've gone down a level it's time to print out our add_children()
            if parent_name != current_parent:
                fmt_add_children(current_parent, children, write)
                current_parent = parent_name
                children = [node_name]
            # As long as we're not the top node we're a child
            elif node_name != current_parent:
                children.append(node_name)

            # Each node should print out a class instantiation line
            write("{} = e.{}(".format(node_name, node_type.title()))

            # Append child nodes or print attributes
            for name, value in vertex.items():
                # Handle empty element
                value = value if value is not None else OrderedDict()
                is_dict = isinstance(value, OrderedDict)
                is_list = isinstance(value, list)
                # Handle child elements
                if is_dict or is_list:
                    # Make a list of child elements the common case
                    elements = value if is_list else [value]
                    for element in elements:
                        element["__parent"] = node_name
                        # Note: This modifies `prev_names` in place
                        element["__name"] = get_name_for_dict(
                            element,
                            name,
                            prev_names
                        )
                        element["__type"] = name
                        queue.append(element)
                # Handle element attributes
                else:
                    attr_name = name.replace("@", "")
                    if "__" not in attr_name:
                        write("    {}=\"{}\",".format(attr_name, value))
            write(")")

        # Handle lowest level remaining children
        fmt_add_children(current_parent, children, write)
        source_string = fh.getvalue()

    return source_string


def main():

    # Get a list of all the xml files we want to convert
    orig_xml_dir = "sample_models"
    files = os.listdir(orig_xml_dir)
    # Screen out anything that's not xml
    files = [f for f in files if 'xml' in f]

    py_script_dir = "gen_scripts"
    for f in files:
        # Load and parse the xml
        xml_path = os.path.join(orig_xml_dir, f)
        with open(xml_path, 'r') as fh:
            xml_string = fh.read()
        xml_dict = xmltodict.parse(xml_string)

        # Prepare nodes for traversal and top node
        items = list(xml_dict.items())
        start = items[0][1]
        start["__name"] = 'mujoco'
        start["__type"] = 'mujoco'
        start["__parent"] = 'mujoco'
        queue = [start]

        # BF traversal to get xml string
        source_string = get_source_string(queue)

        # Prepare Jinja2 env
        env = Environment(
            loader=FileSystemLoader('templates/'),
            autoescape=select_autoescape(['python']),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        template = env.get_template('gen_script.j2')

        model_name = f.split(".")[0]
        rendered = template.render(
            source_string=source_string,
            model_name=model_name
        )

        script_name = "gen_{}.py".format(model_name)
        sourcepath = os.path.join(py_script_dir, script_name)
        with open(sourcepath, 'w') as fh:
            fh.write(rendered)


if __name__ == '__main__':
    main()
