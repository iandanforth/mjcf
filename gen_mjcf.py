import os
from copy import copy, deepcopy
from bs4 import BeautifulSoup
from bs4.element import Tag
from jinja2 import Environment, PackageLoader, select_autoescape

SENTINEL = "MISSING"


def get_elem_nodes(soup):
    # Each element doc starts with an <h3> tag
    h3s = soup.find_all('h3')
    nodes = [elem for elem in h3s if elem['id']]
    return nodes


def get_clean_attr_default(attr_default):
    """
    Cleans ambiguous strings
    """
    if "for MJCF" in attr_default:
        parts = attr_default.split(",")
        mjcf_default = parts[0]
        attr_default = mjcf_default.split(" ")[0]

    return attr_default


def get_type_default(dl_item_text):
    """
    Splits a 'detail' string into the type and default parts
    """

    # Separate attr names from attr details
    parts = dl_item_text.split(":")
    if len(parts) > 1:
        detail = parts[1]
    else:
        return None, None

    # Handle lists of valid strings
    if "[" in detail and "]" in detail:
        obi = detail.find("[")
        cbi = detail.find("]")
        valid_strings = detail[obi+1:cbi].split(",")
        attr_type = [s.strip() for s in valid_strings]
        attr_default = detail[cbi+2:].strip()  # e.g. move just past the ], in [false, true], "false"
        attr_default = get_clean_attr_default(attr_default)
    # Handle type, default style details
    else:
        detail_parts = detail.split(",")
        attr_type = detail_parts[0].strip()
        attr_default = detail_parts[1].strip()

    if "optional" in attr_default \
        or "required" in attr_default \
        or "default" in attr_default:
        attr_default = None
    return attr_type, attr_default


def get_clean_name(name):
    name = name.replace("\"", "")
    if name == "class":
        name = "class_"
    return name


def get_names(name_node_text):
    parts = name_node_text.split(":")
    names_string = parts[0]
    names = [n.strip() for n in names_string.split(",")]
    names = [get_clean_name(n) for n in names]
    return names


def get_attributes_from_node(node):
    attr_template = {
        "type": SENTINEL,
        "default": SENTINEL,
        "description": SENTINEL
    }

    attributes = []
    dl_data = node.findNext("dl")
    for dl_item in dl_data:
        if isinstance(dl_item, Tag) and dl_item.name == "dt":
            attr_name_node = dl_item.find("b")
            # Make sure we're dealing with an attribute name line
            if attr_name_node:
                attr_names = get_names(attr_name_node.text)
                attr_type, attr_default = get_type_default(dl_item.text)
                attr_desc = dl_item.findNext("dd").text.strip()

                for attr_name in attr_names:
                    attribute = copy(attr_template)
                    attribute["name"] = attr_name
                    attribute["type"] = attr_type
                    attribute["default"] = attr_default
                    attribute["description"] = attr_desc

                    attributes.append(attribute)

    return attributes


def get_details_from_node(node):
    # Template element

    element = {
        "description": SENTINEL,
        "attributes": {}
    }

    # Element Description
    p = node.nextSibling.nextSibling
    desc = p.string
    if not desc:
        desc = p.text
    element["description"] = desc

    # Attributes
    element["attributes"] = get_attributes_from_node(node)

    return element


def add_worldbody(elements):
    """
    Special case the world body as it doesn't have a separate description
    """
    worldbody = deepcopy(elements["body"])
    worldbody["attributes"] = []
    elements["worldbody"] = worldbody
    return elements


def attributes_for_motors(elements):
    """
    Docs point back to actuator / general for details on these attributes
    """
    attrs = elements["general"]["attributes"]
    elements["motor"]["attributes"] = attrs

    return elements


def handle_special_cases(elements):
    elements = add_worldbody(elements)
    elements = attributes_for_motors(elements)
    return elements


def get_elements():
    # MuJoCo Docs
    with open("modeling.htm", 'r') as fh:
        soup = BeautifulSoup(fh, 'html.parser')

    elem_nodes = get_elem_nodes(soup)
    elements = {}
    for elem in elem_nodes:
        # Name of the element
        elem_id = elem['id']
        elements[elem_id] = get_details_from_node(elem)

    elements = handle_special_cases(elements)

    return elements


def main():

    elements = get_elements()

    # Jinja2
    env = Environment(
        loader=PackageLoader('mjcf', 'templates'),
        autoescape=select_autoescape(['python'])
    )

    template = env.get_template('mjcf_element.j2')

    elements_template = env.get_template('elements.j2')

    classes = []
    for elem_id, element in elements.items():
        docstring = element["description"]
        parts = [part.title() for part in elem_id.split("-")]
        elem_name = "".join(parts)
        attributes = element["attributes"]
        attribute_names = [a["name"] for a in attributes]
        inputs = dict(
            classname=elem_name,
            attributes=attributes,
            attribute_names=attribute_names,
            docstring=docstring,
        )
        rendered_class = template.render(**inputs)
        classes.append(rendered_class)

    rendered_elements = elements_template.render(classes=classes)
    sourcepath = os.path.join("mjcf", "generated", "elements.py")
    with open(sourcepath, 'w') as fh:
        fh.write(rendered_elements)


if __name__ == '__main__':
    main()
