from mjcf.element import Element


class Equality(Element):
    """

    This is a grouping element for equality constraints. It does not have
    attributes. See the Equality section of the Computation chapter for a
    detailed description of equality constraints. Several attributes are common
    to all equality constraint types, thus we document them only once, under the
    connect element.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class Connect(Element):
    """

    This element creates an equality constraint that connects two bodies at a
    point. The point is not necessarily within the geoms volumes of either body.
    This constraint can be used to define ball joints outside the kinematic
    tree.

    """
    def __init__(
        self,
        anchor,
        body1,
        active="true",
        body2=None,
        class_=None,
        name=None,
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.anchor = anchor
        self.body1 = body1
        self.active = active
        self.body2 = body2
        self.class_ = class_
        self.name = name
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['anchor', 'body1', 'active', 'body2', 'class_', 'name', 'solimp', 'solref']


class Weld(Element):
    """

    This element creates a weld equality constraint. It attaches two bodies to
    each other, removing all relative degrees of freedom between them (softly of
    course, like all other constraints in MuJoCo). The two bodies are not
    required to be close to each other. The relative body position and
    orientation being enforced by the constraint solver is the one in which the
    model was defined. Note that two bodies can also be welded together rigidly,
    by defining one body as a child of the other body, without any joint
    elements in the child body.

    """
    def __init__(
        self,
        body1,
        body2=None,
        active=None,
        class_=None,
        name=None,
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.body1 = body1
        self.body2 = body2
        self.active = active
        self.class_ = class_
        self.name = name
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['body1', 'body2', 'active', 'class_', 'name', 'solimp', 'solref']


class Joint(Element):
    """

    This element constrains the position or angle of one joint to be a quartic
    polynomial of another joint. Only scalar joint types (slide and hinge) can
    be used.

    """
    def __init__(
        self,
        joint1,
        joint2=None,
        polycoef="0 1 0 0 0",
        active=None,
        class_=None,
        name=None,
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.joint1 = joint1
        self.joint2 = joint2
        self.polycoef = polycoef
        self.active = active
        self.class_ = class_
        self.name = name
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['joint1', 'joint2', 'polycoef', 'active', 'class_', 'name', 'solimp', 'solref']


class Tendon(Element):
    """

    This element constrains the length of one tendon to be a quartic polynomial
    of another tendon.

    """
    def __init__(
        self,
        tendon1,
        polycoef="0 1 0 0",
        tendon2=None,
        active=None,
        class_=None,
        name=None,
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.tendon1 = tendon1
        self.polycoef = polycoef
        self.tendon2 = tendon2
        self.active = active
        self.class_ = class_
        self.name = name
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['tendon1', 'polycoef', 'tendon2', 'active', 'class_', 'name', 'solimp', 'solref']


class Distance(Element):
    """

    This element constrains the nearest distance between two geoms. When the
    distance attribute is set to 0 the two geom surfaces slide over each other,
    otherwise they slide over a virtual cushion with depth equal to the
    specified distance. This mechanism is implemented as a modification to the
    collision detector. For geom pairs handled by the general-purpose convex
    collider, large distance values in this constraint are handled
    approximately, due to the nature of the underlying collision algorithm.

    """
    def __init__(
        self,
        geom1,
        geom2,
        distance="0",
        active=None,
        class_=None,
        name=None,
        solimp=None,
        solref=None,
    ):
        super().__init__()
        self.geom1 = geom1
        self.geom2 = geom2
        self.distance = distance
        self.active = active
        self.class_ = class_
        self.name = name
        self.solimp = solimp
        self.solref = solref
        self._attribute_names = ['geom1', 'geom2', 'distance', 'active', 'class_', 'name', 'solimp', 'solref']
