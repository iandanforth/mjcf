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


def get_type_default(detail):
    """
    Splits a 'detail' string into the type and default parts
    """
    parts = detail.split(",")
    attr_type = parts[0].strip()
    # Sometimes a default value is actually in multiple parts
    default_parts = parts[1:]
    if len(default_parts) > 1:
        attr_default = "\"BAD DEFAULT\""
    else:
        attr_default = ",".join(default_parts).strip()

    if "optional" in attr_default \
        or "required" in attr_default \
        or "default" in attr_default:
        attr_default = None
    return attr_type, attr_default


def get_clean_name(attr_name_node):
    text = attr_name_node.text
    parts = text.split(" ")
    name = parts[0]
    name = name.replace("\"", "")
    if name == "class":
        name = "class_"
    return name


def get_attributes_from_node(node):
    attr_template = {
        "type": SENTINEL,
        "default": SENTINEL,
        "description": SENTINEL
    }

    attributes = []
    dl_data = node.findNext("dl")
    for dl_item in dl_data:
        if isinstance(dl_item, Tag):
            attr_name_node = dl_item.find("b")
            # Make sure we're dealing with an attribute name line
            # TODO - Handle sublists of attributes
            #      a, b, c,
            #      a, b, c: int, 1
            if attr_name_node and ":" in dl_item.text:
                attribute = copy(attr_template)
                attr_name = get_clean_name(attr_name_node)
                if "," in attr_name:
                    continue
                attr_detail = dl_item.text.split(":")[1]
                attr_type, attr_default = get_type_default(attr_detail)
                attr_desc = dl_item.findNext("dd").text.strip()

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

    elements = add_worldbody(elements)

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
