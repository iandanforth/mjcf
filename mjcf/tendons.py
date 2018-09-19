from mjcf.element import Element


class Tendon(Element):
    """

    Grouping element for tendon definitions. The attributes of fixed tendons are
    a subset of the attributes of spatial tendons, thus we document them only
    once under spatial tendons. Tendons can be used to impose length limits,
    simulate spring, damping and dry friction forces, as well as attach
    actuators to them. When used in equality constraints, tendons can also
    represent different forms of mechanical coupling.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class Spatial(Element):
    """

    This element creates a spatial tendon, which is a minimum-length path
    passing through specified via-points and wrapping around specified obstacle
    geoms. The objects along the path are defined with the sub-elements site and
    geom below. One can also define pulleys which split the path in multiple
    branches. Each branch of the tendon path must start and end with a site, and
    if it has multiple obstacle geoms they must be separated by sites - so as to
    avoid the need for an iterative solver at the tendon level. The following
    example illustrates a multi-branch tendon acting as a finger extensor, with
    a counter-weight instead of an actuator.

    tendon.xml

    """
    def __init__(
        self,
        class_=None,
        damping="0",
        frictionloss="0",
        limited="false",
        margin="0",
        material=None,
        name=None,
        range="0 0",
        rgba="0.5 0.5 0.5 1",
        stiffness="0",
        user="0 0 ...",
        width="0",
        solimpfriction=None,
        solimplimit=None,
        solreffriction=None,
        solreflimit=None,
    ):
        super().__init__()
        self.class_ = class_
        self.damping = damping
        self.frictionloss = frictionloss
        self.limited = limited
        self.margin = margin
        self.material = material
        self.name = name
        self.range = range
        self.rgba = rgba
        self.stiffness = stiffness
        self.user = user
        self.width = width
        self.solimpfriction = solimpfriction
        self.solimplimit = solimplimit
        self.solreffriction = solreffriction
        self.solreflimit = solreflimit
        self._attribute_names = ['class_', 'damping', 'frictionloss', 'limited', 'margin', 'material', 'name', 'range', 'rgba', 'stiffness', 'user', 'width', 'solimpfriction', 'solimplimit', 'solreffriction', 'solreflimit']


class SpatialSite(Element):
    """

    This attribute specifies a site that the tendon path has to pass through.
    Recall that sites are rigidly attached to bodies.

    """
    def __init__(
        self,
        site,
    ):
        super().__init__()
        self.site = site
        self._attribute_names = ['site']


class SpatialGeom(Element):
    """

    This element specifies a geom that acts as an obstacle for the tendon path.
    If the minimum-length path does not touch the geom it has no effect;
    otherwise the path wraps around the surface of the geom. Wrapping is
    computed analytically, which is why we restrict the geom types allowed here
    to spheres and cylinders. The latter are treated as having infinite length
    for tendon wrapping purposes.

    """
    def __init__(
        self,
        geom,
        sidesite=None,
    ):
        super().__init__()
        self.geom = geom
        self.sidesite = sidesite
        self._attribute_names = ['geom', 'sidesite']


class SpatialPulley(Element):
    """

    This element starts a new branch in the tendon path. The branches are not
    required to be connected spatially. Similar to the transmissions described
    in the Actuation model section of the Computation chapter, the quantity that
    affects the simulation is the tendon length and its gradient with respect to
    the joint positions. If a spatial tendon has multiple branches, the length
    of each branch is divided by the divisor attribute of the pulley element
    that started the branch, and added up to obtain the overall tendon length.
    This is why the spatial relations among branches are not relevant to the
    simulation. The tendon.xml example above illustrated the use of pulleys.

    """
    def __init__(
        self,
        divisor,
    ):
        super().__init__()
        self.divisor = divisor
        self._attribute_names = ['divisor']


class Fixed(Element):
    """

    This element creates an abstract tendon whose length is defined as a linear
    combination of joint positions. Recall that the tendon length and its
    gradient are the only quantities needed for simulation. Thus we could define
    any scalar function of joint positions, call it "tendon", and plug it in
    MuJoCo. Presently the only such function is a fixed linear combination. The
    attributes of fixed tendons are a subset of the attributes of spatial
    tendons and have the same meaning as above.

    """
    def __init__(
        self,
        class_=None,
        damping=None,
        frictionloss=None,
        limited=None,
        margin=None,
        name=None,
        range=None,
        solimpfriction=None,
        solimplimit=None,
        solreffriction=None,
        solreflimit=None,
        stiffness=None,
        user=None,
    ):
        super().__init__()
        self.class_ = class_
        self.damping = damping
        self.frictionloss = frictionloss
        self.limited = limited
        self.margin = margin
        self.name = name
        self.range = range
        self.solimpfriction = solimpfriction
        self.solimplimit = solimplimit
        self.solreffriction = solreffriction
        self.solreflimit = solreflimit
        self.stiffness = stiffness
        self.user = user
        self._attribute_names = ['class_', 'damping', 'frictionloss', 'limited', 'margin', 'name', 'range', 'solimpfriction', 'solimplimit', 'solreffriction', 'solreflimit', 'stiffness', 'user']


class FixedJoint(Element):
    """

    This element adds a joint to the computation of the fixed tendon length. The
    position or angle of each included joint is multiplied by the corresponding
    coef value, and added up to obtain the tendon length.

    """
    def __init__(
        self,
        coef,
        joint,
    ):
        super().__init__()
        self.coef = coef
        self.joint = joint
        self._attribute_names = ['coef', 'joint']
