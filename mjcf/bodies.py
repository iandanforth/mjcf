from mjcf.element import Element


class Body(Element):
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
        childclass=None,
        mocap="false",
        name=None,
        pos=None,
        user="0 0 ...",
        axisangle=None,
        euler=None,
        quat=None,
        xyaxes=None,
        zaxis=None,
    ):
        super().__init__()
        self.childclass = childclass
        self.mocap = mocap
        self.name = name
        self.pos = pos
        self.user = user
        self.axisangle = axisangle
        self.euler = euler
        self.quat = quat
        self.xyaxes = xyaxes
        self.zaxis = zaxis
        self._attribute_names = ['childclass', 'mocap', 'name', 'pos', 'user', 'axisangle', 'euler', 'quat', 'xyaxes', 'zaxis']


class Inertial(Element):
    """

    This element specifies the mass and inertial properties of the body. If this
    element is not included in a given body, the inertial properties are
    inferred from the geoms attached to the body. When a compiled MJCF model is
    saved, the XML writer saves the inertial properties explicitly using this
    element, even if they were inferred from geoms. The inertial frame is such
    that its center coincides with the center of mass of the body, and its axes
    coincide with the principal axes of inertia of the body. Thus the inertia
    matrix is diagonal in this frame.

    """
    def __init__(
        self,
        mass,
        pos,
        diaginertia=None,
        fullinertia=None,
        axisangle=None,
        euler=None,
        quat=None,
        xyaxes=None,
        zaxis=None,
    ):
        super().__init__()
        self.mass = mass
        self.pos = pos
        self.diaginertia = diaginertia
        self.fullinertia = fullinertia
        self.axisangle = axisangle
        self.euler = euler
        self.quat = quat
        self.xyaxes = xyaxes
        self.zaxis = zaxis
        self._attribute_names = ['mass', 'pos', 'diaginertia', 'fullinertia', 'axisangle', 'euler', 'quat', 'xyaxes', 'zaxis']


class Joint(Element):
    """

    This element creates a joint. As explained in Kinematic tree, a joint
    creates motion degrees of freedom between the body where it is defined and
    the body's parent. If multiple joints are defined in the same body, the
    corresponding spatial transformations (of the body frame relative to the
    parent frame) are applied in order. If no joints are defined, the body is
    welded to its parent. Joints cannot be defined in the world body. At runtime
    the positions and orientations of all joints defined in the model are stored
    in the vector mjData.qpos, in the order in which the appear in the kinematic
    tree. The linear and angular velocities are stored in the vector
    mjData.qvel. These two vectors have different dimensionality when free or
    ball joints are used, because such joints represent rotations as unit
    quaternions.

    """
    def __init__(
        self,
        armature="0",
        axis="0 0 1",
        class_=None,
        damping="0",
        frictionloss="0",
        limited="false",
        margin="0",
        name=None,
        pos="0 0 0",
        range="0 0",
        ref="0",
        springdamper="0 0",
        springref="0",
        stiffness="0",
        type="hinge",
        user="0 0 ...",
        solimpfriction=None,
        solimplimit=None,
        solreffriction=None,
        solreflimit=None,
    ):
        super().__init__()
        self.armature = armature
        self.axis = axis
        self.class_ = class_
        self.damping = damping
        self.frictionloss = frictionloss
        self.limited = limited
        self.margin = margin
        self.name = name
        self.pos = pos
        self.range = range
        self.ref = ref
        self.springdamper = springdamper
        self.springref = springref
        self.stiffness = stiffness
        self.type = type
        self.user = user
        self.solimpfriction = solimpfriction
        self.solimplimit = solimplimit
        self.solreffriction = solreffriction
        self.solreflimit = solreflimit
        self._attribute_names = ['armature', 'axis', 'class_', 'damping', 'frictionloss', 'limited', 'margin', 'name', 'pos', 'range', 'ref', 'springdamper', 'springref', 'stiffness', 'type', 'user', 'solimpfriction', 'solimplimit', 'solreffriction', 'solreflimit']


class Freejoint(Element):
    """

    This element creates a free joint whose only attribute is name. The same
    effect can be achieved with the joint element, however in that case default
    settings intended for actuated joints may also affect the free joint
    (depending on how the defaults classes are specified), which is usually
    undesirable. To avoid this complication, the freejoint element was
    introduced. It is merely an XML shortcut. The compiler transforms it into a
    regular joint in mjModel. If the XML model is saved, it will appear as a
    regular joint of type "free".

    """
    def __init__(
        self,
        name=None,
    ):
        super().__init__()
        self.name = name
        self._attribute_names = ['name']


class Geom(Element):
    """

    This element creates a geom, and attaches it rigidly to the body within
    which the geom is defined. Multiple geoms can be attached to the same body.
    At runtime they determine the appearance and collision properties of the
    body. At compile time they can also determine the inertial properties of the
    body, depending on the presence of the inertial element and the setting of
    the inertiafromgeom attribute of compiler. This is done by summing the
    masses and inertias of all geoms attached to the body with geom group in the
    range specified by the inertiagrouprange attribute of compiler. The geom
    masses and inertias are computed using the geom shape, a specified density
    or a geom mass which implies a density, and the assumption of uniform
    density.

    Geoms are not strictly required for physics simulation. One can create and
    simulate a model that only has bodies and joints. Such a model can even be
    visualized, using equivalent inertia boxes to represent bodies. Only contact
    forces would be missing from such a simulation. We do not recommend using
    such models, but knowing that this is possible helps clarify the role of
    bodies and geoms in MuJoCo.

    """
    def __init__(
        self,
        class_=None,
        conaffinity="1",
        condim="3",
        contype="1",
        density="1000",
        fitscale="1",
        friction="1 0.005 0.0001",
        fromto=None,
        gap="0",
        group="0",
        hfield=None,
        margin="0",
        mass=None,
        material=None,
        mesh=None,
        name=None,
        pos="0 0 0",
        rgba="0.5 0.5 0.5 1",
        size="0 0 0",
        solmix="1",
        type="sphere",
        user="0 0 ...",
        axisangle=None,
        euler=None,
        quat=None,
        solimp=None,
        solref=None,
        xyaxes=None,
        zaxis=None,
    ):
        super().__init__()
        self.class_ = class_
        self.conaffinity = conaffinity
        self.condim = condim
        self.contype = contype
        self.density = density
        self.fitscale = fitscale
        self.friction = friction
        self.fromto = fromto
        self.gap = gap
        self.group = group
        self.hfield = hfield
        self.margin = margin
        self.mass = mass
        self.material = material
        self.mesh = mesh
        self.name = name
        self.pos = pos
        self.rgba = rgba
        self.size = size
        self.solmix = solmix
        self.type = type
        self.user = user
        self.axisangle = axisangle
        self.euler = euler
        self.quat = quat
        self.solimp = solimp
        self.solref = solref
        self.xyaxes = xyaxes
        self.zaxis = zaxis
        self._attribute_names = ['class_', 'conaffinity', 'condim', 'contype', 'density', 'fitscale', 'friction', 'fromto', 'gap', 'group', 'hfield', 'margin', 'mass', 'material', 'mesh', 'name', 'pos', 'rgba', 'size', 'solmix', 'type', 'user', 'axisangle', 'euler', 'quat', 'solimp', 'solref', 'xyaxes', 'zaxis']


class Site(Element):
    """
    This element creates a site, which is a simplified and restricted kind of
    geom. A small subset of the geom attributes are available here; see the geom
    element for their detailed documentation. Semantically sites represent
    locations of interest relative to the body frames. Sites do not participate
    in collisions and computation of body masses and inertias. The geometric
    shapes that can be used to render sites are limited to a subset of the
    available geom types. However sites can be used in some places where geoms
    are not allowed: mounting sensors, specifying via-points of spatial tendons,
    constructing slider-crank transmissions for actuators.
    """
    def __init__(
        self,
        class_=None,
        group="0",
        material=None,
        name=None,
        pos="0 0 0",
        rgba="0.5 0.5 0.5 1",
        size="0 0 0",
        type="sphere",
        user="0 0 ...",
        axisangle=None,
        euler=None,
        quat=None,
        xyaxes=None,
        zaxis=None,
    ):
        super().__init__()
        self.class_ = class_
        self.group = group
        self.material = material
        self.name = name
        self.pos = pos
        self.rgba = rgba
        self.size = size
        self.type = type
        self.user = user
        self.axisangle = axisangle
        self.euler = euler
        self.quat = quat
        self.xyaxes = xyaxes
        self.zaxis = zaxis
        self._attribute_names = ['class_', 'group', 'material', 'name', 'pos', 'rgba', 'size', 'type', 'user', 'axisangle', 'euler', 'quat', 'xyaxes', 'zaxis']


class Camera(Element):
    """
    This element creates a camera, which moves with the body where it is
    defined. To create a fixed camera, define it in the world body. The cameras
    created here are in addition to the default free camera which is always
    defined and is adjusted via the visual element. In HAPTIX such user-defined
    cameras can be enabled from the Render dialog, while in Pro they are enabled
    programmatically. Internally MuJoCo uses a flexible camera model, where the
    viewpoint and projection surface are adjusted independently so as to obtain
    oblique projections needed for virtual environments. This functionality
    however is not accessible through MJCF. Instead, the cameras created with
    this element (as well as the free camera) have a viewpoint that is always
    centered in front of the projection surface. The viewpoint coincides with
    the center of the camera frame. The camera is looking along the -Z axis of
    its frame. The +X axis points to the right, and the +Y axis points up. Thus
    the frame position and orientation are the key adjustments that need to be
    made here.
    """
    def __init__(
        self,
        class_=None,
        fovy="45",
        ipd="0.068",
        mode="fixed",
        name=None,
        pos="0 0 0",
        target=None,
        user="0 0 ...",
        axisangle=None,
        euler=None,
        quat=None,
        xyaxes=None,
        zaxis=None,
    ):
        super().__init__()
        self.class_ = class_
        self.fovy = fovy
        self.ipd = ipd
        self.mode = mode
        self.name = name
        self.pos = pos
        self.target = target
        self.user = user
        self.axisangle = axisangle
        self.euler = euler
        self.quat = quat
        self.xyaxes = xyaxes
        self.zaxis = zaxis
        self._attribute_names = ['class_', 'fovy', 'ipd', 'mode', 'name', 'pos', 'target', 'user', 'axisangle', 'euler', 'quat', 'xyaxes', 'zaxis']


class Light(Element):
    """
    This element creates a light, which moves with the body where it is defined.
    To create a fixed light, define it in the world body. The lights created
    here are in addition to the default headlight which is always defined and is
    adjusted via the visual element. MuJoCo relies on the standard lighting
    model in OpenGL (fixed functionality) augmented with shadow mapping. The
    effects of lights are additive, thus adding a light always makes the scene
    brighter. The maximum number of lights that can be active simultaneously is
    8, counting the headlight. The light is shining along the direction
    specified by the dir attribute. It does not have a full spatial frame with
    three orthogonal axes.
    """
    def __init__(
        self,
        active="true",
        ambient="0 0 0",
        attenuation="1 0 0",
        castshadow="true",
        class_=None,
        cutoff="45",
        diffuse="0.7 0.7 0.7",
        dir="0 0 -1",
        directional="false",
        exponent="10",
        mode="fixed",
        name=None,
        pos="0 0 0",
        specular="0.3 0.3 0.3",
        target=None,
    ):
        super().__init__()
        self.active = active
        self.ambient = ambient
        self.attenuation = attenuation
        self.castshadow = castshadow
        self.class_ = class_
        self.cutoff = cutoff
        self.diffuse = diffuse
        self.dir = dir
        self.directional = directional
        self.exponent = exponent
        self.mode = mode
        self.name = name
        self.pos = pos
        self.specular = specular
        self.target = target
        self._attribute_names = ['active', 'ambient', 'attenuation', 'castshadow', 'class_', 'cutoff', 'diffuse', 'dir', 'directional', 'exponent', 'mode', 'name', 'pos', 'specular', 'target']
