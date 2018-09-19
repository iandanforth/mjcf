import os
from typing import List
from textwrap import wrap, fill
from operator import attrgetter
from copy import copy, deepcopy
from bs4 import BeautifulSoup
from bs4.element import Tag
from jinja2 import Environment, PackageLoader, select_autoescape

SENTINEL = "MISSING"


class MJScraper(object):

    def __init__(self, html_filepath="modeling.htm"):
        # MuJoCo Docs
        with open(html_filepath, 'r') as fh:
            self.soup = BeautifulSoup(fh, 'html.parser')

        self.frame_orientation_attrs = self._get_frame_orientation_attrs()
        self.sensor_attrs = self._get_sensor_attrs()
        self.solver_attrs = self._get_solver_attrs()

    @staticmethod
    def get_elem_nodes(soup):
        # Each element doc starts with an <h3> tag
        h3s = soup.find_all('h3')
        nodes = [elem for elem in h3s if elem['id']]
        return nodes

    @staticmethod
    def get_clean_attr_default(attr_default):
        """
        Cleans ambiguous strings
        """
        if "for MJCF" in attr_default:
            parts = attr_default.split(",")
            mjcf_default = parts[0]
            attr_default = mjcf_default.split(" ")[0]

        return attr_default

    @staticmethod
    def get_clean_name(name):
        name = name.replace("\"", "")
        if name == "class":
            name = "class_"
        return name

    @staticmethod
    def add_worldbody(elements):
        """
        Special case the world body as it doesn't have a separate description
        """
        worldbody = deepcopy(elements["body"])
        worldbody["attributes"] = []
        elements["worldbody"] = worldbody
        return elements

    @staticmethod
    def attributes_for_motors(elements):
        """
        Docs point back to actuator / general for details on these attributes
        """
        attrs = deepcopy(elements["general"]["attributes"])
        elements["motor"]["attributes"] = attrs

        return elements

    def _is_really_required(self, default_string):
        """
        Handle a couple annoying edge cases
        """
        # Assume attr 'sliderside' for actuators isn't really required
        if "slider-crank" in default_string:
            return False

        # Assume that 'class' isn't really required for default tags
        if "except at the top level" in default_string:
            return False

        return True

    def _parse_list_string(self, list_string, cls):
        if not list_string or list_string == 'required':
            return list_string

        # Split
        vals = list_string.split(" ")
        vals = [v.strip('\"') for v in vals]
        vals = [cls(v) for v in vals]
        return vals

    def _parse_val_string(self, val_string, cls):
        if not val_string or val_string == 'required':
            return val_string

        val_string = cls(val_string.strip("\""))

    def _pythonify_type_and_default(self, attr_type, attr_default):

        float_lists = ["real(2)", "real(3)", "real(4)", "real(5)", "real(6)"]

        orig_type = attr_type
        if attr_type == "real":
            attr_type = "float"
            attr_default = self._parse_val_string(attr_default, float)
        elif attr_type in float_lists:
            attr_type = "List[float]"
            attr_default = self._parse_list_string(attr_default, float)
        elif attr_type == "string":
            attr_type = "str"
        elif attr_type == "int(2)":
            attr_type = "List[int]"
            attr_default = self._parse_list_string(attr_default, int)
        elif attr_type == "int":
            attr_type = "int"
            attr_default = self._parse_val_string(attr_default, int)
        elif attr_type == ['false', 'true']:
            attr_type = "bool"
            if attr_default and attr_default != 'required':
                if attr_default == '"false"':
                    attr_default = False
                elif attr_default == '"true"':
                    attr_default = True
        else:
            attr_type = "str"

        print(orig_type, attr_type, attr_default)
        return attr_type, attr_default

    def _get_type_default(self, dl_item_text):
        """
        Splits a 'detail' string into the type and default parts
        """

        # Separate attr names from attr details
        parts = dl_item_text.split(":")
        if len(parts) > 1:
            detail = parts[1]
        else:
            return None, None, 3

        # Handle lists of valid strings
        if "[" in detail and "]" in detail:
            obi = detail.find("[")
            cbi = detail.find("]")
            valid_strings = detail[obi+1:cbi].split(",")
            attr_type = [s.strip() for s in valid_strings]
            attr_default = detail[cbi+2:].strip()  # e.g. move just past the ], in [false, true], "false"
            attr_default = self.get_clean_attr_default(attr_default)
        # Handle type, default style details
        else:
            detail_parts = detail.split(",")
            attr_type = detail_parts[0].strip()
            attr_default = detail_parts[1].strip()

        required = 2  # Used in a sort later. Optional attrs should sort after required ones
        if "required" in attr_default:
            if self._is_really_required(attr_default):
                attr_default = "required"
                required = 1
            else:
                attr_default = None
        elif "optional" in attr_default or "default" in attr_default:
            attr_default = None

        # Modify defaults based on type
        attr_type, attr_default = self._pythonify_type_and_default(
            attr_type,
            attr_default
        )

        return attr_type, attr_default, required

    def _get_names(self, name_node_text):
        parts = name_node_text.split(":")
        names_string = parts[0]
        names = [n.strip() for n in names_string.split(",")]
        names = [self.get_clean_name(n) for n in names]
        return names

    def _get_frame_orientation_attrs(self):
        """
        Get attributes used by elements that refer to an orientation frame
        """
        orientation_node = self.soup.find(id="COrientation")
        attrs = self._get_attributes_from_node(orientation_node)
        return attrs

    def _get_sensor_attrs(self):
        """
        Get attributes shared by all sensor elements
        """
        sensor_node = self.soup.find(id="CSensor")
        attrs = self._get_attributes_from_node(sensor_node)
        return attrs

    def _get_solver_attrs(self):
        """
        Get attributes related to solvers
        """
        solver_node = self.soup.find(id="CSolver")
        attrs = self._get_attributes_from_node(solver_node)
        return attrs

    def _banned_attr(self, attr_name):
        banned_attrs = ["magnetic"]
        if attr_name in banned_attrs:
            return True

        return False

    def _node_has_no_attrs(self, node):
        """
        Check to see if we can expect any attributes from this node
        """
        next_siblings = []
        for i, s in enumerate(node.next_siblings):
            if i > 5:
                break
            next_siblings.append(s.name)

        if next_siblings[3] == "h3":
            return True

        return False

    def _sort_attributes(self, attributes):
        attributes = sorted(attributes, key=lambda x: (x["required"], x["name"]))
        return attributes

    def _get_attributes_from_node(self, node):
        attr_template = {
            "type": SENTINEL,
            "default": SENTINEL,
            "description": SENTINEL
        }

        attributes = []

        if self._node_has_no_attrs(node):
            return attributes

        dl_data = node.findNext("dl")
        for dl_item in dl_data:
            if isinstance(dl_item, Tag) and dl_item.name == "dt":
                attr_name_node = dl_item.find("b")
                # Make sure we're dealing with an attribute name line
                if attr_name_node:
                    attr_names = self._get_names(attr_name_node.text)
                    attr_type, attr_default, attr_required = self._get_type_default(dl_item.text)
                    attr_desc = dl_item.findNext("dd").text.strip()

                    for attr_name in attr_names:
                        if self._banned_attr(attr_name):
                            continue
                        attribute = copy(attr_template)
                        attribute["name"] = attr_name
                        attribute["type"] = attr_type
                        attribute["default"] = attr_default
                        attribute["description"] = attr_desc
                        attribute["required"] = attr_required

                        attributes.append(attribute)

        attributes = self._sort_attributes(attributes)

        return attributes

    def _get_details_from_node(self, node):
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

        desc = "\n    ".join(wrap(desc, 74))
        element["description"] = desc

        # Attributes
        element["attributes"] = self._get_attributes_from_node(node)

        return element

    def _handle_special_cases(self, elements):
        elements = self.add_worldbody(elements)
        elements = self.attributes_for_motors(elements)
        return elements

    def get_elements(self):
        elem_nodes = self.get_elem_nodes(self.soup)
        elements = {}
        for elem in elem_nodes:
            # Name of the element
            elem_id = elem['id']
            elements[elem_id] = self._get_details_from_node(elem)

        elements = self._handle_special_cases(elements)

        return elements


def main():

    scraper = MJScraper()
    elements = scraper.get_elements()

    # Jinja2
    env = Environment(
        loader=PackageLoader('mjcf', 'templates'),
        autoescape=select_autoescape(['python']),
        trim_blocks=True,
        lstrip_blocks=True,
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
