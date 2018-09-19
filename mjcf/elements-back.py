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


class Actuator(Element):
    """

    This is a grouping element for actuator definitions. Recall the discussion
    of MuJoCo's Actuation model in the Computation chapter, and the Actuator
    shortcuts discussed earlier in this chapter. The first 13 attributes of all
    actuator-related elements below are the same, so we document them only once,
    under the general actuator.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class General(Element):
    """

    This element creates a general actuator, providing full access to all
    actuator components and allowing the user to specify them independently.

    """
    def __init__(
        self,
        biasprm="0 0 0",
        biastype="none",
        class_=None,
        cranklength="0",
        cranksite=None,
        ctrllimited="false",
        ctrlrange="0 0",
        dynprm="1 0 0",
        dyntype="none",
        forcelimited="false",
        forcerange="0 0",
        gainprm="1 0 0",
        gaintype="fixed",
        gear="1 0 0 0 0 0",
        joint=None,
        jointinparent=None,
        name=None,
        site=None,
        slidersite=None,
        tendon=None,
        user="0 0 ...",
    ):
        super().__init__()
        self.biasprm = biasprm
        self.biastype = biastype
        self.class_ = class_
        self.cranklength = cranklength
        self.cranksite = cranksite
        self.ctrllimited = ctrllimited
        self.ctrlrange = ctrlrange
        self.dynprm = dynprm
        self.dyntype = dyntype
        self.forcelimited = forcelimited
        self.forcerange = forcerange
        self.gainprm = gainprm
        self.gaintype = gaintype
        self.gear = gear
        self.joint = joint
        self.jointinparent = jointinparent
        self.name = name
        self.site = site
        self.slidersite = slidersite
        self.tendon = tendon
        self.user = user
        self._attribute_names = ['biasprm', 'biastype', 'class_', 'cranklength', 'cranksite', 'ctrllimited', 'ctrlrange', 'dynprm', 'dyntype', 'forcelimited', 'forcerange', 'gainprm', 'gaintype', 'gear', 'joint', 'jointinparent', 'name', 'site', 'slidersite', 'tendon', 'user']


class Motor(Element):
    """

    This and the next three elements are the Actuator shortcuts discussed
    earlier. When a such shortcut is encountered, the parser creates a general
    actuator and sets its dynprm, gainprm and biasprm attributes to the internal
    defaults shown above, regardless of any default settings. It then adjusts
    dyntype, gaintype and biastype depending on the shortcut, parses any custom
    attributes (beyond the 13 common ones), and translates them into regular
    attributes (i.e. attributes of the general actuator type) as explained here.

    This element creates a direct-drive actuator. The underlying general
    attributes are set as follows:



    Attribute
    Setting
    Attribute
    Setting


    dyntype
    none
    dynprm
    1 0 0


    gaintype
    fixed
    gainprm
    1 0 0


    biastype
    none
    biasprm
    0 0 0

    This element does not have custom attributes. It only has common attributes,
    which are:

    """
    def __init__(
        self,
        class_=None,
        cranksite=None,
        ctrllimited="false",
        ctrlrange="0 0",
        forcelimited="false",
        forcerange="0 0",
        gear="1 0 0 0 0 0",
        joint=None,
        jointinparent=None,
        name=None,
        site=None,
        slidersite=None,
        tendon=None,
        user="0 0 ...",
    ):
        super().__init__()
        self.class_ = class_
        self.cranksite = cranksite
        self.ctrllimited = ctrllimited
        self.ctrlrange = ctrlrange
        self.forcelimited = forcelimited
        self.forcerange = forcerange
        self.gear = gear
        self.joint = joint
        self.jointinparent = jointinparent
        self.name = name
        self.site = site
        self.slidersite = slidersite
        self.tendon = tendon
        self.user = user
        self._attribute_names = ['class_', 'cranksite', 'ctrllimited', 'ctrlrange', 'forcelimited', 'forcerange', 'gear', 'joint', 'jointinparent', 'name', 'site', 'slidersite', 'tendon', 'user']


class Position(Element):
    """

    This element creates a position servo. The underlying general attributes are
    set as follows:
    
    Attribute
    Setting
    Attribute
    Setting


    dyntype
    none
    dynprm
    1 0 0


    gaintype
    fixed
    gainprm
    kp 0 0


    biastype
    affine
    biasprm
    0 -kp 0

    This element has one custom attribute in addition to the common attributes:

    """
    def __init__(
        self,
        kp="1",
        class_=None,
        cranklength=None,
        cranksite=None,
        ctrllimited=None,
        ctrlrange=None,
        forcelimited=None,
        forcerange=None,
        gear=None,
        joint=None,
        name=None,
        slidersite=None,
        tendon=None,
        user=None,
    ):
        super().__init__()
        self.kp = kp
        self.class_ = class_
        self.cranklength = cranklength
        self.cranksite = cranksite
        self.ctrllimited = ctrllimited
        self.ctrlrange = ctrlrange
        self.forcelimited = forcelimited
        self.forcerange = forcerange
        self.gear = gear
        self.joint = joint
        self.name = name
        self.slidersite = slidersite
        self.tendon = tendon
        self.user = user
        self._attribute_names = ['kp', 'class_', 'cranklength', 'cranksite', 'ctrllimited', 'ctrlrange', 'forcelimited', 'forcerange', 'gear', 'joint', 'name', 'slidersite', 'tendon', 'user']


class Velocity(Element):
    """

    This element creates a velocity servo. Note that in order create a PD
    controller, one has to define two actuators: a position servo and a velocity
    servo. This is because MuJoCo actuators are SISO while a PD controller takes
    two control inputs (reference position and reference velocity). The
    underlying general attributes are set as follows:
    
    Attribute
    Setting
    Attribute
    Setting


    dyntype
    none
    dynprm
    1 0 0


    gaintype
    fixed
    gainprm
    kv 0 0


    biastype
    affine
    biasprm
    0 0 -kv


    This element has one custom attribute in addition to the common attributes:

    """
    def __init__(
        self,
        kv="1",
        class_=None,
        cranklength=None,
        cranksite=None,
        ctrllimited=None,
        ctrlrange=None,
        forcelimited=None,
        forcerange=None,
        gear=None,
        joint=None,
        name=None,
        slidersite=None,
        tendon=None,
        user=None,
    ):
        super().__init__()
        self.kv = kv
        self.class_ = class_
        self.cranklength = cranklength
        self.cranksite = cranksite
        self.ctrllimited = ctrllimited
        self.ctrlrange = ctrlrange
        self.forcelimited = forcelimited
        self.forcerange = forcerange
        self.gear = gear
        self.joint = joint
        self.name = name
        self.slidersite = slidersite
        self.tendon = tendon
        self.user = user
        self._attribute_names = ['kv', 'class_', 'cranklength', 'cranksite', 'ctrllimited', 'ctrlrange', 'forcelimited', 'forcerange', 'gear', 'joint', 'name', 'slidersite', 'tendon', 'user']


class Cylinder(Element):
    """

    This element is suitable for modeling pneumatic or hydrolic cylinders. The
    underlying general attributes are set as follows:

    Attribute
    Setting
    Attribute
    Setting


    dyntype
    filter
    dynprm
    timeconst 0 0


    gaintype
    fixed
    gainprm
    area 0 0


    biastype
    affine
    biasprm
    bias

    This element has four custom attributes in addition to the common
    attributes:

    """
    def __init__(
        self,
        area="1",
        bias="0 0 0",
        diameter=None,
        timeconst="1",
        class_=None,
        cranklength=None,
        cranksite=None,
        ctrllimited=None,
        ctrlrange=None,
        forcelimited=None,
        forcerange=None,
        gear=None,
        joint=None,
        name=None,
        slidersite=None,
        tendon=None,
        user=None,
    ):
        super().__init__()
        self.area = area
        self.bias = bias
        self.diameter = diameter
        self.timeconst = timeconst
        self.class_ = class_
        self.cranklength = cranklength
        self.cranksite = cranksite
        self.ctrllimited = ctrllimited
        self.ctrlrange = ctrlrange
        self.forcelimited = forcelimited
        self.forcerange = forcerange
        self.gear = gear
        self.joint = joint
        self.name = name
        self.slidersite = slidersite
        self.tendon = tendon
        self.user = user
        self._attribute_names = ['area', 'bias', 'diameter', 'timeconst', 'class_', 'cranklength', 'cranksite', 'ctrllimited', 'ctrlrange', 'forcelimited', 'forcerange', 'gear', 'joint', 'name', 'slidersite', 'tendon', 'user']


class Sensor(Element):
    """

    This is a grouping element for sensor definitions. It does not have
    attributes. The outputs of all sensors are concatenated in the field
    mjData.sensordata which has size mjModel.nsensordata. This data is not used
    in any internal computations.
    
    In addition to the sensors created with the elements below, the top-level
    function mj_step computes the quantities mjData.cacc, mjData.cfrc_int and
    mjData.crfc_ext corresponding to body accelerations and interaction forces.
    Some of these quantities are used to compute the output of certain sensors
    (force, acceleration etc.) but even if no such sensors are defined in the
    model, these quantities themselves are "features" that could be of interest
    to the user.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class SensorTouch(Element):
    """

    This element creates a touch sensor. The active sensor zone is defined by a
    site which must be either a box or an ellipsoid. If a contact point falls
    within the site's volume, and involves a geom attached to the same body as
    the site, the corresponding contact force is included in the sensor reading.
    If a contact point falls outside the sensor zone, but the normal ray
    intersects the sensor zone, it is also included. This re-projection feature
    is needed because, without it, the contact point may leave the sensor zone
    from the back (due to soft contacts) and cause an erroneous force reading.
    The output of this sensor is non-negative scalar. It is computed by adding
    up the (scalar) normal forces from all included contacts. An example of
    touch sensor zones for a robotic hand can be found in the Sensors section in
    the MuJoCo HATPIX chapter.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorAccelerometer(Element):
    """

    This element creates a 3-axis accelerometer. The sensor is mounted at a
    site, and has the same position and orientation as the site frame. This
    sensor outputs three numbers, which are the linear acceleration of the site
    (including gravity) in local coordinates.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorVelocimeter(Element):
    """

    This element creates a 3-axis velocimeter. The sensor is mounted at a site,
    and has the same position and orientation as the site frame. This sensor
    outputs three numbers, which are the linear velocity of the site in local
    coordinates.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorGyro(Element):
    """

    This element creates a 3-axis gyroscope. The sensor is mounted at a site,
    and has the same position and orientation as the site frame. This sensor
    outputs three numbers, which are the angular velocity of the site in local
    coordinates. This sensor is often used in conjunction with an accelerometer
    mounted at the same site, to simulate an inertial measurement unit (IMU).

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorForce(Element):
    """

    This element creates a 3-axis force sensor. The sensor outputs three
    numbers, which are the interaction force between a child and a parent body,
    expressed in the site frame defining the sensor. The convention is that the
    site is attached to the child body, and the force points from the child
    towards the parent. To change the sign of the sensor reading, use the scale
    attribute. The computation here takes into account all forces acting on the
    system, including contacts as well as external perturbations. Using this
    sensor often requires creating a dummy body welded to its parent (i.e.
    having no joint elements).

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorTorque(Element):
    """

    This element creates a 3-axis torque sensor. This is similar to the force
    sensor above, but measures torque rather than force.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorMagnetometer(Element):
    """

    This element creates a magnetometer. It measures the magnetic flux at the
    sensor site position, expressed in the sensor site frame. The output is a 3D
    vector.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorRangefinder(Element):
    """

    This element creates a rangefinder. It measures the distance to the nearest
    geom surface, along the ray defined by the positive Z-axis of the sensor
    site. If the ray does not intersect any geom surface, the sensor output is
    -1. If the origin of the ray is inside a geom, the surface is still sensed
    (but not the inner volume). Geoms attached to the same body as the sensor
    site are excluded. Invisible geoms, defined as geoms whose rgba (or whose
    material rgba) has alpha=0, are also excluded. Note however that geoms made
    invisible in the visualizer by disabling their geom group are not excluded;
    this is because sensor calculations are independent of the visualizer.

    """
    def __init__(
        self,
        site,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.site = site
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['site', 'cutoff', 'name', 'noise', 'user']


class SensorJointpos(Element):
    """

    This and the remaining sensor elements do not involve sensor-specific
    computations. Instead they copy into the array mjData.sensordata quantities
    that are already computed. This element creates a joint position or angle
    sensor. It can be attached to scalar joints (slide or hinge). Its output is
    scalar.

    """
    def __init__(
        self,
        joint,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.joint = joint
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['joint', 'cutoff', 'name', 'noise', 'user']


class SensorJointvel(Element):
    """

    This element creates a joint velocity sensor. It can be attached to scalar
    joints (slide or hinge). Its output is scalar.

    """
    def __init__(
        self,
        joint,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.joint = joint
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['joint', 'cutoff', 'name', 'noise', 'user']


class SensorTendonpos(Element):
    """

    This element creates a tendon length sensor. It can be attached to both
    spatial and fixed tendons. Its output is scalar.

    """
    def __init__(
        self,
        tendon,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.tendon = tendon
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['tendon', 'cutoff', 'name', 'noise', 'user']


class SensorTendonvel(Element):
    """

    This element creates a tendon velocity sensor. It can be attached to both
    spatial and fixed tendons. Its output is scalar.

    """
    def __init__(
        self,
        tendon,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.tendon = tendon
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['tendon', 'cutoff', 'name', 'noise', 'user']


class SensorActuatorpos(Element):
    """

    This element creates an actuator length sensor. Recall that each actuator
    has a transmission which has length. This sensor can be attached to any
    actuator. Its output is scalar.

    """
    def __init__(
        self,
        actuator,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.actuator = actuator
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['actuator', 'cutoff', 'name', 'noise', 'user']


class SensorActuatorvel(Element):
    """

    This element creates an actuator velocity sensor. This sensor can be
    attached to any actuator. Its output is scalar.

    """
    def __init__(
        self,
        actuator,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.actuator = actuator
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['actuator', 'cutoff', 'name', 'noise', 'user']


class SensorActuatorfrc(Element):
    """

    This element creates an actuator force sensor. The quantity being sensed is
    the scalar actuator force, not the generalized force contributed by the
    actuator (the latter is the product of the scalar force and the vector of
    moment arms determined by the transmission). This sensor can be attached to
    any actuator. Its output is scalar.

    """
    def __init__(
        self,
        actuator,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.actuator = actuator
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['actuator', 'cutoff', 'name', 'noise', 'user']


class SensorBallquat(Element):
    """

    This element creates a quaternion sensor for a ball joints. It outputs 4
    numbers corresponding to a unit quaternion.

    """
    def __init__(
        self,
        joint,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.joint = joint
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['joint', 'cutoff', 'name', 'noise', 'user']


class SensorBallangvel(Element):
    """

    This element creates a ball joint angular velocity sensor. It outputs 3
    numbers corresponding to the angular velocity of the joint. The norm of that
    vector is the rotation speed in rad/s and the direction is the axis around
    which the rotation takes place.

    """
    def __init__(
        self,
        joint,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.joint = joint
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['joint', 'cutoff', 'name', 'noise', 'user']


class SensorFramepos(Element):
    """

    This element creates a sensor that returns the 3D position of the spatial
    frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFramequat(Element):
    """

    This element creates a sensor that returns the unit quaternion specifying
    the orientation of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFramexaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the X-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFrameyaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the Y-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFramezaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the Z-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFramelinvel(Element):
    """

    This element creates a sensor that returns the 3D linear velocity of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFrameangvel(Element):
    """

    This element creates a sensor that returns the 3D angular velocity of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFramelinacc(Element):
    """

    This element creates a sensor that returns the 3D linear acceleration of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorFrameangacc(Element):
    """

    This element creates a sensor that returns the 3D angular acceleration of
    the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class SensorSubtreecom(Element):
    """

    This element creates sensor that returns the center of mass of the kinematic
    subtree rooted at a specified body, in global coordinates.

    """
    def __init__(
        self,
        body,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.body = body
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['body', 'cutoff', 'name', 'noise', 'user']


class SensorSubtreelinvel(Element):
    """

    This element creates sensor that returns the linear velocity of the center
    of mass of the kinematic subtree rooted at a specified body, in global
    coordinates.

    """
    def __init__(
        self,
        body,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.body = body
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['body', 'cutoff', 'name', 'noise', 'user']


class SensorSubtreeangmom(Element):
    """

    This element creates sensor that returns the angular momentum around the
    center of mass of the kinematic subtree rooted at a specified body, in
    global coordinates.

    """
    def __init__(
        self,
        body,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.body = body
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['body', 'cutoff', 'name', 'noise', 'user']


class SensorUser(Element):
    """

    This element creates a user sensor. MuJoCo does not know how to compute the
    output of this sensor. Instead the user should install the callback
    mjcb_sensor which is expected to fill in the sensor data in
    mjData.sensordata. The specification in the XML is used to allocate space
    for this sensor, and also determine which MuJoCo object it is attached to
    and what stage of computation it needs before the data can be computed. Note
    that the MuJoCo object referenced here can be a tuple, which in turn can
    reference a custom collection of MuJoCo objects - for example several bodies
    whose center of mass is of interest.

    """
    def __init__(
        self,
        datatype,
        dim,
        needstage,
        objname,
        objtype,
        cutoff=None,
        name=None,
        noise=None,
        user=None,
    ):
        super().__init__()
        self.datatype = datatype
        self.dim = dim
        self.needstage = needstage
        self.objname = objname
        self.objtype = objtype
        self.cutoff = cutoff
        self.name = name
        self.noise = noise
        self.user = user
        self._attribute_names = ['datatype', 'dim', 'needstage', 'objname', 'objtype', 'cutoff', 'name', 'noise', 'user']


class Keyframe(Element):
    """

    This is a grouping element for keyframe definitions. It does not have
    attributes. Keyframes can be used to create a library of states that are of
    interest to the user, and to initialize the simulation state to one of the
    states in the library. They are not needed by any MuJoCo computations. The
    number of keyframes allocated in mjModel is the larger of the nkey attribute
    of size, and the number of elements defined here. If fewer than nkey
    elements are defined here, the undefined keyframes have all their data set
    to 0, except for the qpos attribute which is set to mjModel.qpos0. The user
    can also set keyframe data in mjModel at runtime; this data will then appear
    in the saved MJCF model. Note that in HAPTIX the simulation state can be
    copied into a selected keyframe and vice versa; see Sim dialog in the MuJoco
    HAPTIX chapter. In Pro this has to be done programmatically.

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []


class Key(Element):
    """

    This element sets the data for one of the keyframes. They are set in the
    order in which they appear here.

    """
    def __init__(
        self,
        act="0 0 ...",
        qpos=None,
        qvel="0 0 ...",
        time="0",
    ):
        super().__init__()
        self.act = act
        self.qpos = qpos
        self.qvel = qvel
        self.time = time
        self._attribute_names = ['act', 'qpos', 'qvel', 'time']


class Worldbody(Element):
    """

    This element is used to construct the kinematic tree via nesting. The
    element worldbody is used for the top-level body, while the element body is
    used for all other bodies. The top-level body is a restricted type of body:
    it cannot have child elements inertial and joint, and also cannot have any
    attributes. It corresponds to the origin of the world frame, within which
    the rest of the kinematic tree is defined. Its body name is automatically
    defined as "world".

    """
    def __init__(
        self,
    ):
        super().__init__()
        self._attribute_names = []
