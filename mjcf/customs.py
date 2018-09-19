from mjcf.element import Element


class Custom(Element):
    """

    This is a grouping element for custom numeric and text elements. It does not
    have attributes.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class Numeric(Element):
    """

    This element creates a custom numeric array in mjModel.

    """
    def __init__(
        self,
        name,
        data="0 0 ...",
        size=None,
    ):
        super().__init__()
        self.name = name
        self.data = data
        self.size = size
        self._attribute_names = ['name', 'data', 'size']


class Text(Element):
    """

    This element creates a custom text field in mjModel. It could be used to
    store keyword commands for user callbacks and other custom computations.

    """
    def __init__(
        self,
        data,
        name,
    ):
        super().__init__()
        self.data = data
        self.name = name
        self._attribute_names = ['data', 'name']


class Tuple(Element):
    """

    This element creates a custom tuple, which is a list of MuJoCo objects. The
    list is created by referencing the desired objects by name.

    """
    def __init__(
        self,
        name,
    ):
        super().__init__()
        self.name = name
        self._attribute_names = ['name']


class Tupleelement(Element):
    """

    This adds an element to the tuple.

    """
    def __init__(
        self,
        objname,
        objtype,
        prm="0",
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.prm = prm
        self._attribute_names = ['objname', 'objtype', 'prm']
