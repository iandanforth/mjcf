from xmltodict import unparse

class Element(object):
    def __init__(self):
        self._attribute_names = []
        self._children = []

    def _to_dict(self):
        """
        Returns a dict ready for processing by xmltodict lib
        """
        element_name = self.__class__.__name__
        element_name = element_name.lower()
        outdict = {element_name: {}}
        for attr in self._attribute_names:
            k = "@{}".format(attr)
            v = getattr(self, attr)
            outdict[element_name][k] = v

        return outdict

    def xml(self):
        """
        Returns an XML string representation of this element
        """

        outdict = self._to_dict()
        print(outdict)
        return unparse(outdict, pretty=True)
