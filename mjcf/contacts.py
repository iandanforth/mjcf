from mjcf.element import Element


class Contact(Element):
    """

    This is a grouping element and does not have any attributes. It groups
    elements that are used to adjust the generation of candidate contact pairs
    for collision checking. Collision detection was described in detail in the
    Computation chapter, thus the description here is brief.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class Pair(Element):
    """

    This element creates a predefined geom pair, which will be checked for
    collision if the collision attribute of option is set to "all" or
    "predefined". Unlike dynamically generated pairs whose properties are
    inferred from the corresponding geom properties, the pairs created here
    specify all their properties explicitly or through defaults, and the
    properties of the individual geoms are not used. Anisotropic friction can
    only be created with this element.

    """
    def __init__(
        self,
        geom1,
        geom2,
        class_=None,
        condim="3",
        friction="1 1 0.005 0.0001 0.0001",
        gap="0",
        margin="0",
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.geom1 = geom1
        self.geom2 = geom2
        self.class_ = class_
        self.condim = condim
        self.friction = friction
        self.gap = gap
        self.margin = margin
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['geom1', 'geom2', 'class_', 'condim', 'friction', 'gap', 'margin', 'solimp', 'solref']


class Exclude(Element):
    """

    This element is used to exclude a pair of bodies from collision checking.
    Unlike all other contact-related elements which refer to geoms, this element
    refers to bodies. Experience has shown that exclusion is more useful on the
    level of bodies. The collision between any geom defined in the first body
    and any geom defined in the second body is excluded. The exclusion rules
    defined here are applied only when the collision attribute of option is set
    to "all" or "dynamic". Setting this attribute to "predefined" disables the
    exclusion mechanism and the geom pairs defined with the pair element above
    are checked for collisions.

    """
    def __init__(
        self,
        body1,
        body2,
    ):
        super().__init__()
        self.body1 = body1
        self.body2 = body2
        self._attribute_names = ['body1', 'body2']
