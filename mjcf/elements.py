class Element(object):
    def __init__(self):
        pass


class Include(Element):
    """

    This element does not strictly speaking belong to MJCF. Instead it is a
    meta-element, used to assemble multiple XML files in a single document
    object model (DOM) before parsing. The included file must be a valid XML
    file with a unique top-level element. This top-level element is removed by
    the parser, and the elements below it are inserted at the location of the
    include element. At least one element must be inserted as a result of this
    procedure. The include element can be used where ever an XML element is
    expected in the MJFC file. Nested includes are allowed, however a given XML
    file can be included at most once in the entire model. After all the
    included XML files have been assembled into a single DOM, it must correspond
    to a valid MJCF model. Other than that, it is up to the user to decide how
    to use includes and how to modularize large files if desired.

    """
    def __init__(
        self,
        file=None,
    ):
        self.file = file
        self._attribute_names = ['file']


class Mujoco(Element):
    """

    The unique top-level element, identifying the XML file as an MJCF model
    file.

    """
    def __init__(
        self,
        model="MuJoCo Model",
    ):
        self.model = model
        self._attribute_names = ['model']


class Compiler(Element):
    """

    This element is used to set options for the built-in parser and compiler.
    After parsing and compilation it no longer has any effect. The settings here
    are global and apply to the entire model.

    """
    def __init__(
        self,
        boundmass="0",
        boundinertia="0",
        settotalmass="-1",
        balanceinertia="BAD DEFAULT",
        strippath="BAD DEFAULT",
        coordinate="BAD DEFAULT",
        angle="BAD DEFAULT",
        fitaabb="BAD DEFAULT",
        eulerseq="xyz",
        meshdir=None,
        texturedir=None,
        discardvisual="BAD DEFAULT",
        convexhull="BAD DEFAULT",
        inertiafromgeom="BAD DEFAULT",
        inertiagrouprange="0 4",
    ):
        self.boundmass = boundmass
        self.boundinertia = boundinertia
        self.settotalmass = settotalmass
        self.balanceinertia = balanceinertia
        self.strippath = strippath
        self.coordinate = coordinate
        self.angle = angle
        self.fitaabb = fitaabb
        self.eulerseq = eulerseq
        self.meshdir = meshdir
        self.texturedir = texturedir
        self.discardvisual = discardvisual
        self.convexhull = convexhull
        self.inertiafromgeom = inertiafromgeom
        self.inertiagrouprange = inertiagrouprange
        self._attribute_names = ['boundmass', 'boundinertia', 'settotalmass', 'balanceinertia', 'strippath', 'coordinate', 'angle', 'fitaabb', 'eulerseq', 'meshdir', 'texturedir', 'discardvisual', 'convexhull', 'inertiafromgeom', 'inertiagrouprange']


class CompilerLengthrange(Element):
    """

    To be written.

    """
    def __init__(
        self,
        timestep="0.002",
        apirate="100",
        gravity="0 0 -9.81",
        wind="0 0 0",
        magnetic="0 -0.5 0",
        density="0",
        viscosity="0",
        impratio="1",
        o_margin="0",
        o_solref="0.02 1",
        o_solimp="0.8 0.8 0.01",
        integrator="BAD DEFAULT",
        collision="BAD DEFAULT",
        impedance="BAD DEFAULT",
        reference="BAD DEFAULT",
        cone="BAD DEFAULT",
        jacobian="BAD DEFAULT",
        solver="BAD DEFAULT",
        iterations="100",
        tolerance="1e-8",
        noslip_iterations="0",
        noslip_tolerance="1e-6",
        mpr_iterations="50",
        mpr_tolerance="1e-6",
    ):
        self.timestep = timestep
        self.apirate = apirate
        self.gravity = gravity
        self.wind = wind
        self.magnetic = magnetic
        self.density = density
        self.viscosity = viscosity
        self.impratio = impratio
        self.o_margin = o_margin
        self.o_solref = o_solref
        self.o_solimp = o_solimp
        self.integrator = integrator
        self.collision = collision
        self.impedance = impedance
        self.reference = reference
        self.cone = cone
        self.jacobian = jacobian
        self.solver = solver
        self.iterations = iterations
        self.tolerance = tolerance
        self.noslip_iterations = noslip_iterations
        self.noslip_tolerance = noslip_tolerance
        self.mpr_iterations = mpr_iterations
        self.mpr_tolerance = mpr_tolerance
        self._attribute_names = ['timestep', 'apirate', 'gravity', 'wind', 'magnetic', 'density', 'viscosity', 'impratio', 'o_margin', 'o_solref', 'o_solimp', 'integrator', 'collision', 'impedance', 'reference', 'cone', 'jacobian', 'solver', 'iterations', 'tolerance', 'noslip_iterations', 'noslip_tolerance', 'mpr_iterations', 'mpr_tolerance']


class Option(Element):
    """

    This element is is one-to-one correspondence with the low level structure
    mjOption contained in the field mjModel.opt of mjModel. These are simulation
    options and do not affect the compilation process in any way; they are
    simply copied into the low level model. Even though mjOption can be modified
    by the user at runtime, it is nevertheless a good idea to adjust it properly
    through the XML.

    """
    def __init__(
        self,
        timestep="0.002",
        apirate="100",
        gravity="0 0 -9.81",
        wind="0 0 0",
        magnetic="0 -0.5 0",
        density="0",
        viscosity="0",
        impratio="1",
        o_margin="0",
        o_solref="0.02 1",
        o_solimp="0.8 0.8 0.01",
        integrator="BAD DEFAULT",
        collision="BAD DEFAULT",
        impedance="BAD DEFAULT",
        reference="BAD DEFAULT",
        cone="BAD DEFAULT",
        jacobian="BAD DEFAULT",
        solver="BAD DEFAULT",
        iterations="100",
        tolerance="1e-8",
        noslip_iterations="0",
        noslip_tolerance="1e-6",
        mpr_iterations="50",
        mpr_tolerance="1e-6",
    ):
        self.timestep = timestep
        self.apirate = apirate
        self.gravity = gravity
        self.wind = wind
        self.magnetic = magnetic
        self.density = density
        self.viscosity = viscosity
        self.impratio = impratio
        self.o_margin = o_margin
        self.o_solref = o_solref
        self.o_solimp = o_solimp
        self.integrator = integrator
        self.collision = collision
        self.impedance = impedance
        self.reference = reference
        self.cone = cone
        self.jacobian = jacobian
        self.solver = solver
        self.iterations = iterations
        self.tolerance = tolerance
        self.noslip_iterations = noslip_iterations
        self.noslip_tolerance = noslip_tolerance
        self.mpr_iterations = mpr_iterations
        self.mpr_tolerance = mpr_tolerance
        self._attribute_names = ['timestep', 'apirate', 'gravity', 'wind', 'magnetic', 'density', 'viscosity', 'impratio', 'o_margin', 'o_solref', 'o_solimp', 'integrator', 'collision', 'impedance', 'reference', 'cone', 'jacobian', 'solver', 'iterations', 'tolerance', 'noslip_iterations', 'noslip_tolerance', 'mpr_iterations', 'mpr_tolerance']


class OptionFlag(Element):
    """

    This element sets the flags that enable and disable different parts of the
    simulation pipeline. The actual flags used at runtime are represented as the
    bits of two integers, namely mjModel.opt.disableflags and
    mjModel.opt.enableflags, used to disable standard features and enable
    optional features respectively. The reason for this separation is that
    setting both integers to 0 restores the default. In the XML we do not make
    this separation explicit, except for the default attribute values - which
    are "enable" for flags corresponding to standard features, and "disable" for
    flags corresponding to optional features. In the documentation below, we
    explain what happens when the setting is different from its default.

    """
    def __init__(
        self,
        constraint="BAD DEFAULT",
        equality="BAD DEFAULT",
        frictionloss="BAD DEFAULT",
        limit="BAD DEFAULT",
        contact="BAD DEFAULT",
        passive="BAD DEFAULT",
        gravity="BAD DEFAULT",
        clampctrl="BAD DEFAULT",
        warmstart="BAD DEFAULT",
        filterparent="BAD DEFAULT",
        actuation="BAD DEFAULT",
        refsafe="BAD DEFAULT",
        override="BAD DEFAULT",
        energy="BAD DEFAULT",
        fwdinv="BAD DEFAULT",
        sensornoise="BAD DEFAULT",
    ):
        self.constraint = constraint
        self.equality = equality
        self.frictionloss = frictionloss
        self.limit = limit
        self.contact = contact
        self.passive = passive
        self.gravity = gravity
        self.clampctrl = clampctrl
        self.warmstart = warmstart
        self.filterparent = filterparent
        self.actuation = actuation
        self.refsafe = refsafe
        self.override = override
        self.energy = energy
        self.fwdinv = fwdinv
        self.sensornoise = sensornoise
        self._attribute_names = ['constraint', 'equality', 'frictionloss', 'limit', 'contact', 'passive', 'gravity', 'clampctrl', 'warmstart', 'filterparent', 'actuation', 'refsafe', 'override', 'energy', 'fwdinv', 'sensornoise']


class Size(Element):
    """

    This element specifies size parameters that cannot be inferred from the
    number of elements in the model. Unlike the fields of mjOption which can be
    modified at runtime, sizes are structural parameters and should not be
    modified after compilation.

    """
    def __init__(
        self,
        njmax="-1",
        nconmax="-1",
        nstack="-1",
        nuserdata="0",
        nkey="0",
        nuser_body="0",
        nuser_jnt="0",
        nuser_geom="0",
        nuser_site="0",
        nuser_cam="0",
        nuser_tendon="0",
        nuser_actuator="0",
        nuser_sensor="0",
    ):
        self.njmax = njmax
        self.nconmax = nconmax
        self.nstack = nstack
        self.nuserdata = nuserdata
        self.nkey = nkey
        self.nuser_body = nuser_body
        self.nuser_jnt = nuser_jnt
        self.nuser_geom = nuser_geom
        self.nuser_site = nuser_site
        self.nuser_cam = nuser_cam
        self.nuser_tendon = nuser_tendon
        self.nuser_actuator = nuser_actuator
        self.nuser_sensor = nuser_sensor
        self._attribute_names = ['njmax', 'nconmax', 'nstack', 'nuserdata', 'nkey', 'nuser_body', 'nuser_jnt', 'nuser_geom', 'nuser_site', 'nuser_cam', 'nuser_tendon', 'nuser_actuator', 'nuser_sensor']


class Visual(Element):
    """

    This element is is one-to-one correspondence with the low level structure
    mjVisual contained in the field mjModel.vis of mjModel. The settings here
    affect the visualizer, or more precisely the abstract phase of visualization
    which yields a list of geometric entities for subsequent rendering. The
    settings here are global, in contrast with the element-specific visual
    settings. The global and element-specific settings refer to non-overlapping
    properties. Some of the global settings affect properties such as
    triangulation of geometric primitives that cannot be set per element. Other
    global settings affect the properties of decorative objects, i.e. objects
    such as contact points and force arrows which do not correspond to model
    elements. The visual settings are grouped semantically into several
    subsections.
    
    This element is a good candidate for the file include mechanism. One can
    create an XML file with coordinated visual settings corresponding to a
    "theme", and then include this file in multiple models.

    """
    def __init__(
        self,
        fovy="45",
        ipd="0.068",
        linewidth="1",
        glow="0.3",
        offwidth="640",
        offheight="480",
    ):
        self.fovy = fovy
        self.ipd = ipd
        self.linewidth = linewidth
        self.glow = glow
        self.offwidth = offwidth
        self.offheight = offheight
        self._attribute_names = ['fovy', 'ipd', 'linewidth', 'glow', 'offwidth', 'offheight']


class Global(Element):
    """

    While all settings in mjVisual are global, the settings here could not be
    fit into any of the other subsections. So this is effectively a
    miscellaneous subsection.

    """
    def __init__(
        self,
        fovy="45",
        ipd="0.068",
        linewidth="1",
        glow="0.3",
        offwidth="640",
        offheight="480",
    ):
        self.fovy = fovy
        self.ipd = ipd
        self.linewidth = linewidth
        self.glow = glow
        self.offwidth = offwidth
        self.offheight = offheight
        self._attribute_names = ['fovy', 'ipd', 'linewidth', 'glow', 'offwidth', 'offheight']


class Quality(Element):
    """

    This element specifies settings that affect the quality of the rendering.
    Larger values result in higher quality but possibly slower speed. Note that
    both HAPTIX and Pro display the frames per second (FPS). The target FPS is
    60 Hz; if the number shown in the visualizer is substantially lower, this
    means that the GPU is over-loaded and the visualization should somehow be
    simplified.

    """
    def __init__(
        self,
        shadowsize="1024",
        offsamples="4",
        numslices="28",
        numstacks="16",
        numarrows="10",
        numquads="4",
    ):
        self.shadowsize = shadowsize
        self.offsamples = offsamples
        self.numslices = numslices
        self.numstacks = numstacks
        self.numarrows = numarrows
        self.numquads = numquads
        self._attribute_names = ['shadowsize', 'offsamples', 'numslices', 'numstacks', 'numarrows', 'numquads']


class Headlight(Element):
    """

    This element is used to adjust the properties of the headlight. There is
    always a built-in headlight, in addition to any lights explicitly defined in
    the model. The headlight is a directional light centered at the current
    camera and pointed in the direction in which the camera is looking. It does
    not cast shadows (which would be invisible anyway). Note that lights are
    additive, so if explicit lights are defined in the model, the intensity of
    the headlight would normally need to be reduced.

    """
    def __init__(
        self,
        ambient="0.1 0.1 0.1",
        diffuse="0.4 0.4 0.4",
        specular="0.5 0.5 0.5",
        active="1",
    ):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.active = active
        self._attribute_names = ['ambient', 'diffuse', 'specular', 'active']


class Map(Element):
    """

    This element is used to specify scaling quantities that affect both the
    visualization and built-in mouse perturbations. Unlike the scaling
    quantities in the next element which are specific to spatial extent, the
    quantities here are miscellaneous.

    """
    def __init__(
        self,
        stiffness="100",
        stiffnessrot="500",
        force="0.005",
        torque="0.1",
        alpha="0.3",
        fogstart="3",
        fogend="10",
        znear="0.2",
        zfar="50",
        shadowclip="1",
        shadowscale="0.6",
    ):
        self.stiffness = stiffness
        self.stiffnessrot = stiffnessrot
        self.force = force
        self.torque = torque
        self.alpha = alpha
        self.fogstart = fogstart
        self.fogend = fogend
        self.znear = znear
        self.zfar = zfar
        self.shadowclip = shadowclip
        self.shadowscale = shadowscale
        self._attribute_names = ['stiffness', 'stiffnessrot', 'force', 'torque', 'alpha', 'fogstart', 'fogend', 'znear', 'zfar', 'shadowclip', 'shadowscale']


class Scale(Element):
    """

    The settings in this element control the spatial extent of various
    decorative objects. In all cases, the rendered size equals the mean body
    size (see statistic element below) multiplied by the value of an attribute
    documented below.

    """
    def __init__(
        self,
        forcewidth="0.1",
        contactwidth="0.3",
        contactheight="0.1",
        connect="0.2",
        com="0.4",
        camera="0.3",
        light="0.3",
        selectpoint="0.2",
        jointlength="1.0",
        jointwidth="0.1",
        actuatorlength="0.7",
        actuatorwidth="0.2",
        framelength="1.0",
        framewidth="0.1",
        constraint="0.1",
        slidercrank="0.2",
    ):
        self.forcewidth = forcewidth
        self.contactwidth = contactwidth
        self.contactheight = contactheight
        self.connect = connect
        self.com = com
        self.camera = camera
        self.light = light
        self.selectpoint = selectpoint
        self.jointlength = jointlength
        self.jointwidth = jointwidth
        self.actuatorlength = actuatorlength
        self.actuatorwidth = actuatorwidth
        self.framelength = framelength
        self.framewidth = framewidth
        self.constraint = constraint
        self.slidercrank = slidercrank
        self._attribute_names = ['forcewidth', 'contactwidth', 'contactheight', 'connect', 'com', 'camera', 'light', 'selectpoint', 'jointlength', 'jointwidth', 'actuatorlength', 'actuatorwidth', 'framelength', 'framewidth', 'constraint', 'slidercrank']


class Rgba(Element):
    """

    The settings in this element control the color and transparency (rgba) of
    various decorative objects. We will call this combined attribute "color" to
    simplify terminology below. All values should be in the range [0 1]. An
    alpha value of 0 disables the rendering of the corresponding object.

    """
    def __init__(
        self,
        fog="0 0 0 1",
        force="1 0.5 0.5 1",
        inertia="0.8 0.2 0.2 0.6",
        joint="0.2 0.6 0.8 1",
        actuator="0.9 0.4 0.4 1",
        com="0.9 0.9 0.9 1",
        camera="0.6 0.9 0.6 1",
        light="0.6 0.6 0.9 1",
        selectpoint="0.9 0.9 0.1 1",
        connect="0.2 0.2 0.8 1",
        contactpoint="0.9 0.6 0.2 1",
        contactforce="0.7 0.9 0.9 1",
        contactfriction="0.9 0.8 0.4 1",
        contacttorque="0.9 0.7 0.9 1",
        constraint="0.9 0 0 1",
        slidercrank="0.5 0.3 0.8 1",
        crankbroken="0.9 0 0 1",
    ):
        self.fog = fog
        self.force = force
        self.inertia = inertia
        self.joint = joint
        self.actuator = actuator
        self.com = com
        self.camera = camera
        self.light = light
        self.selectpoint = selectpoint
        self.connect = connect
        self.contactpoint = contactpoint
        self.contactforce = contactforce
        self.contactfriction = contactfriction
        self.contacttorque = contacttorque
        self.constraint = constraint
        self.slidercrank = slidercrank
        self.crankbroken = crankbroken
        self._attribute_names = ['fog', 'force', 'inertia', 'joint', 'actuator', 'com', 'camera', 'light', 'selectpoint', 'connect', 'contactpoint', 'contactforce', 'contactfriction', 'contacttorque', 'constraint', 'slidercrank', 'crankbroken']


class Statistic(Element):
    """

    This element is used to override model statistics computed by the compiler.
    These statistics are not only informational but are also used to scale
    various components of the rendering and perturbation. We provide an override
    mechanism in the XML because it is sometimes easier to adjust a small number
    of model statistics than a larger number of visual parameters.

    """
    def __init__(
        self,
        meanmass=None,
        meaninertia=None,
        meansize=None,
        extent=None,
        center=None,
    ):
        self.meanmass = meanmass
        self.meaninertia = meaninertia
        self.meansize = meansize
        self.extent = extent
        self.center = center
        self._attribute_names = ['meanmass', 'meaninertia', 'meansize', 'extent', 'center']


class Default(Element):
    """

    This element is used to create a new defaults class; see Default settings
    above. Defaults classes can be nested, inheriting all attribute values from
    their parent. The top-level defaults class is always defined; it is called
    "main" if omitted.

    
    """
    def __init__(
        self,
        class_=None,
    ):
        self.class_ = class_
        self._attribute_names = ['class_']


class DefaultMesh(Element):
    """

    This element sets the attributes of the dummy mesh element of the defaults
    class.

    The only mesh attribute available here is: scale.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultMaterial(Element):
    """

    This element sets the attributes of the dummy material element of the
    defaults class.
    
    All material attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultJoint(Element):
    """

    This element sets the attributes of the dummy joint element of the defaults
    class.
    
    All joint attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultGeom(Element):
    """

    This element sets the attributes of the dummy geom element of the defaults
    class.
    
    All geom attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultSite(Element):
    """

    This element sets the attributes of the dummy site element of the defaults
    class.
    
    All site attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultCamera(Element):
    """

    This element sets the attributes of the dummy camera element of the defaults
    class.
    
    All camera attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultLight(Element):
    """

    This element sets the attributes of the dummy light element of the defaults
    class.
    
    All light attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultPair(Element):
    """

    This element sets the attributes of the dummy pair element of the defaults
    class.
    
    All pair attributes are available here except:
    class, geom1, geom2.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultEquality(Element):
    """

    This element sets the attributes of the dummy equality element of the
    defaults class. The actual equality constraints have types depending on the
    sub-element used to define them. However here we are setting attributes
    common to all equality constraint types, which is why we do not make a
    distinction between types.
    
    The equality sub-element attributes available here are:
    active, solref, solimp.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultTendon(Element):
    """

    This element sets the attributes of the dummy tendon element of the defaults
    class. Similar to equality constraints, the actual tendons have types, but
    here we are setting attributes common to all types.
    
    All tendon sub-element attributes are available here except:
    name, class.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultGeneral(Element):
    """

    This element sets the attributes of the dummy general element of the
    defaults class.
    
    All general attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultMotor(Element):
    """

    This and the next three elements set the attributes of the general element
    using Actuator shortcuts. It does not make sense to use more than one such
    shortcut in the same defaults class, because they set the same underlying
    attributes, replacing any previous settings.
    
    All motor attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultPosition(Element):
    """

    All position attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultVelocity(Element):
    """

    All velocity attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultCylinder(Element):
    """

    All cylinder attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class DefaultMuscle(Element):
    """

    All muscle attributes are available here except:
    name, class, joint, jointinparent, site, tendon, slidersite, cranksite.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class Custom(Element):
    """

    This is a grouping element for custom numeric and text elements. It does not
    have attributes.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class Numeric(Element):
    """

    This element creates a custom numeric array in mjModel.

    """
    def __init__(
        self,
        name=None,
        size=None,
        data="0 0 ...",
    ):
        self.name = name
        self.size = size
        self.data = data
        self._attribute_names = ['name', 'size', 'data']


class Text(Element):
    """

    This element creates a custom text field in mjModel. It could be used to
    store keyword commands for user callbacks and other custom computations.

    """
    def __init__(
        self,
        name=None,
        data=None,
    ):
        self.name = name
        self.data = data
        self._attribute_names = ['name', 'data']


class Tuple(Element):
    """

    This element creates a custom tuple, which is a list of MuJoCo objects. The
    list is created by referencing the desired objects by name.

    """
    def __init__(
        self,
        name=None,
    ):
        self.name = name
        self._attribute_names = ['name']


class Tupleelement(Element):
    """

    This adds an element to the tuple.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
        prm="0",
    ):
        self.objtype = objtype
        self.objname = objname
        self.prm = prm
        self._attribute_names = ['objtype', 'objname', 'prm']


class Asset(Element):
    """

    This is a grouping element for defining assets. It does not have attributes.
    Assets are created in the model so that they can be referenced from other
    model elements; recall the discussion of Assets in the Overview chapter.

    """
    def __init__(
        self,
        name=None,
        type="BAD DEFAULT",
        cube="BAD DEFAULT",
        file=None,
        gridsize="1 1",
        gridlayout="............",
        builtin="BAD DEFAULT",
        gradient="BAD DEFAULT",
        rgb1="0.8 0.8 0.8",
        rgb2="0.5 0.5 0.5",
        mark="BAD DEFAULT",
        markrgb="0 0 0",
        random="0.01",
        width="0",
        height="0",
    ):
        self.name = name
        self.type = type
        self.cube = cube
        self.file = file
        self.gridsize = gridsize
        self.gridlayout = gridlayout
        self.builtin = builtin
        self.gradient = gradient
        self.rgb1 = rgb1
        self.rgb2 = rgb2
        self.mark = mark
        self.markrgb = markrgb
        self.random = random
        self.width = width
        self.height = height
        self._attribute_names = ['name', 'type', 'cube', 'file', 'gridsize', 'gridlayout', 'builtin', 'gradient', 'rgb1', 'rgb2', 'mark', 'markrgb', 'random', 'width', 'height']


class Texture(Element):
    """

    This element creates a texture asset, which is then referenced from a
    material asset, which is finally referenced from a model element that needs
    to be textured. MuJoCo provides access to the texture mapping mechanism in
    OpenGL. Texture coordinates are generated automatically in GL_OBJECT_PLANE
    mode, using either 2D or cube mapping. MIP maps are always enabled in
    GL_LINEAR_MIPMAP_LINEAR mode. The texture color is combined with the object
    color in GL_MODULATE mode. The texture data can be loaded from PNG files,
    with provisions for loading cube and skybox textures. Alternatively the data
    can be generated by the compiler as a procedural texture. Because different
    texture types require different parameters, only a subset of the attributes
    below are used for any given texture.

    """
    def __init__(
        self,
        name=None,
        type="BAD DEFAULT",
        cube="BAD DEFAULT",
        file=None,
        gridsize="1 1",
        gridlayout="............",
        builtin="BAD DEFAULT",
        gradient="BAD DEFAULT",
        rgb1="0.8 0.8 0.8",
        rgb2="0.5 0.5 0.5",
        mark="BAD DEFAULT",
        markrgb="0 0 0",
        random="0.01",
        width="0",
        height="0",
    ):
        self.name = name
        self.type = type
        self.cube = cube
        self.file = file
        self.gridsize = gridsize
        self.gridlayout = gridlayout
        self.builtin = builtin
        self.gradient = gradient
        self.rgb1 = rgb1
        self.rgb2 = rgb2
        self.mark = mark
        self.markrgb = markrgb
        self.random = random
        self.width = width
        self.height = height
        self._attribute_names = ['name', 'type', 'cube', 'file', 'gridsize', 'gridlayout', 'builtin', 'gradient', 'rgb1', 'rgb2', 'mark', 'markrgb', 'random', 'width', 'height']


class Hfield(Element):
    """

    This element creates a height field asset, which can then be referenced from
    geoms with type "hfield". A height field, also known as terrain map, is a 2D
    matrix of elevation data. The data can be specified in one of three ways:

    """
    def __init__(
        self,
        name=None,
        file=None,
        nrow="0",
        ncol="0",
        size=None,
    ):
        self.name = name
        self.file = file
        self.nrow = nrow
        self.ncol = ncol
        self.size = size
        self._attribute_names = ['name', 'file', 'nrow', 'ncol', 'size']


class Mesh(Element):
    """

    This element creates a mesh asset, which can then be referenced from geoms.
    If the referencing geom type is "mesh" the mesh is instantiated in the
    model, otherwise a geometric primitive is automatically fitted to it; see
    geom element below.
    

    MuJoCo works with triangulated meshes loaded from binary STL files. Software
    such as MeshLab can be used to convert from other mesh formats to STL. While
    any collection of triangles can be loaded as a mesh and rendered, collision
    detection works with the convex hull of the mesh as explained in Collision
    detection in the Computation chapter. See also the convexhull attribute of
    the compiler element which controls the automatic generation of convex
    hulls. Since the STL format does not support color, the mesh appearance is
    controlled by the referencing geom, similarly to height fields. We are
    considering support for richer file formats which also specify color, but
    this functionality is not yet available.
    

    Poorly designed meshes can display rendering artifacts. In particular, the
    shadow mapping mechanism relies on having some distance between front and
    back-facing triangle faces. If the faces are repeated, with opposite normals
    as determined by the vertex order in each triangle, this causes shadow
    aliasing. The solution is to remove the repeated faces (which can be done in
    MeshLab) or use a better designed mesh.
    

    The size of the mesh is determined by the 3D coordinates of the vertex data
    in the mesh file, multiplied by the components of the scale attribute below.
    Scaling is applied separately for each coordinate axis. Note that negative
    scaling values can be used to flip the mesh; this is a legitimate operation.
    The size parameters of the referening geoms are ignored, similarly to height
    fields.
    

    Positioning and orienting is complicated by the fact that vertex data are
    often designed relative to coordinate frames whose origin is not inside the
    mesh. In contrast, MuJoCo expects the origin of a geom's local frame to
    coincide with the geometric center of the shape. We resolve this discrepancy
    by pre-processing the mesh in the compiler, so that it is centered around
    (0,0,0) and its principal axes of inertia are the coordinate axes. We also
    save the translation and rotation offsets needed to achieve such alignment.
    These offsets are then applied to the referencing geom's position and
    orientation; see also mesh attribute of geom below. Fortunately most meshes
    used in robot models are designed in a coordinate frame centered at the
    joint. This makes the corresponding MJCF model intuitive: we set the body
    frame at the joint, so that the joint position is (0,0,0) in the body frame,
    and simply reference the mesh. Below is an MJCF model fragment of a forearm,
    containing all the information needed to put the mesh where one would expect
    it to be. The body position is specified relative to the parent body, namely
    the upper arm (not shown). It is offset by 35 cm which is the typical length
    of the human upper arm. If the mesh vertex data were not designed in the
    above convention, we would have to use the geom position and orientation to
    compensate, but in practice this is rarely needed.

    """
    def __init__(
        self,
        name=None,
        class_=None,
        file=None,
        scale="1 1 1",
    ):
        self.name = name
        self.class_ = class_
        self.file = file
        self.scale = scale
        self._attribute_names = ['name', 'class_', 'file', 'scale']


class Material(Element):
    """

    This element creates a material asset. It can be referenced from geoms,
    sites and tendons to set their appearance. Note that all these elements also
    have a local rgba attribute, which is more convenient when only colors need
    to be adjusted, because it does not require creating materials and
    referencing them. Materials are useful for adjusting appearance properties
    beyond color. However once a material is created, it is more natural the
    specify the color using the material, so that all appearance properties are
    grouped together.

    """
    def __init__(
        self,
        name=None,
        class_=None,
        texture=None,
        texrepeat="1 1",
        texuniform="BAD DEFAULT",
        emission="0",
        specular="0.5",
        shininess="0.5",
        reflectance="0",
        rgba="1 1 1 1",
    ):
        self.name = name
        self.class_ = class_
        self.texture = texture
        self.texrepeat = texrepeat
        self.texuniform = texuniform
        self.emission = emission
        self.specular = specular
        self.shininess = shininess
        self.reflectance = reflectance
        self.rgba = rgba
        self._attribute_names = ['name', 'class_', 'texture', 'texrepeat', 'texuniform', 'emission', 'specular', 'shininess', 'reflectance', 'rgba']


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
        name=None,
        childclass=None,
        mocap="BAD DEFAULT",
        pos=None,
        user="0 0 ...",
    ):
        self.name = name
        self.childclass = childclass
        self.mocap = mocap
        self.pos = pos
        self.user = user
        self._attribute_names = ['name', 'childclass', 'mocap', 'pos', 'user']


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
        pos=None,
        mass=None,
        diaginertia=None,
        fullinertia=None,
    ):
        self.pos = pos
        self.mass = mass
        self.diaginertia = diaginertia
        self.fullinertia = fullinertia
        self._attribute_names = ['pos', 'mass', 'diaginertia', 'fullinertia']


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
        name=None,
        class_=None,
        type="BAD DEFAULT",
        free="BAD DEFAULT",
        pos="0 0 0",
        axis="0 0 1",
        springdamper="0 0",
        limited="BAD DEFAULT",
        stiffness="0",
        range="0 0",
        margin="0",
        ref="0",
        springref="0",
        armature="0",
        damping="0",
        frictionloss="0",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.type = type
        self.free = free
        self.pos = pos
        self.axis = axis
        self.springdamper = springdamper
        self.limited = limited
        self.stiffness = stiffness
        self.range = range
        self.margin = margin
        self.ref = ref
        self.springref = springref
        self.armature = armature
        self.damping = damping
        self.frictionloss = frictionloss
        self.user = user
        self._attribute_names = ['name', 'class_', 'type', 'free', 'pos', 'axis', 'springdamper', 'limited', 'stiffness', 'range', 'margin', 'ref', 'springref', 'armature', 'damping', 'frictionloss', 'user']


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
        name=None,
        class_=None,
        type="BAD DEFAULT",
        plane="BAD DEFAULT",
        contype="1",
        conaffinity="1",
        condim="3",
        group="0",
        size="0 0 0",
        material=None,
        rgba="0.5 0.5 0.5 1",
        friction="1 0.005 0.0001",
        mass=None,
        density="1000",
        solmix="1",
        margin="0",
        gap="0",
        fromto=None,
        pos="0 0 0",
        hfield=None,
        mesh=None,
        fitscale="1",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.type = type
        self.plane = plane
        self.contype = contype
        self.conaffinity = conaffinity
        self.condim = condim
        self.group = group
        self.size = size
        self.material = material
        self.rgba = rgba
        self.friction = friction
        self.mass = mass
        self.density = density
        self.solmix = solmix
        self.margin = margin
        self.gap = gap
        self.fromto = fromto
        self.pos = pos
        self.hfield = hfield
        self.mesh = mesh
        self.fitscale = fitscale
        self.user = user
        self._attribute_names = ['name', 'class_', 'type', 'plane', 'contype', 'conaffinity', 'condim', 'group', 'size', 'material', 'rgba', 'friction', 'mass', 'density', 'solmix', 'margin', 'gap', 'fromto', 'pos', 'hfield', 'mesh', 'fitscale', 'user']


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
        name=None,
        class_=None,
        type="BAD DEFAULT",
        group="0",
        material=None,
        rgba="0.5 0.5 0.5 1",
        size="0 0 0",
        pos="0 0 0",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.type = type
        self.group = group
        self.material = material
        self.rgba = rgba
        self.size = size
        self.pos = pos
        self.user = user
        self._attribute_names = ['name', 'class_', 'type', 'group', 'material', 'rgba', 'size', 'pos', 'user']


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
        name=None,
        class_=None,
        mode="BAD DEFAULT",
        target=None,
        fovy="45",
        ipd="0.068",
        pos="0 0 0",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.mode = mode
        self.target = target
        self.fovy = fovy
        self.ipd = ipd
        self.pos = pos
        self.user = user
        self._attribute_names = ['name', 'class_', 'mode', 'target', 'fovy', 'ipd', 'pos', 'user']


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
        name=None,
        class_=None,
        mode="BAD DEFAULT",
        target=None,
        directional="BAD DEFAULT",
        castshadow="BAD DEFAULT",
        active="BAD DEFAULT",
        pos="0 0 0",
        dir="0 0 -1",
        attenuation="1 0 0",
        cutoff="45",
        exponent="10",
        ambient="0 0 0",
        diffuse="0.7 0.7 0.7",
        specular="0.3 0.3 0.3",
    ):
        self.name = name
        self.class_ = class_
        self.mode = mode
        self.target = target
        self.directional = directional
        self.castshadow = castshadow
        self.active = active
        self.pos = pos
        self.dir = dir
        self.attenuation = attenuation
        self.cutoff = cutoff
        self.exponent = exponent
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self._attribute_names = ['name', 'class_', 'mode', 'target', 'directional', 'castshadow', 'active', 'pos', 'dir', 'attenuation', 'cutoff', 'exponent', 'ambient', 'diffuse', 'specular']


class Contact(Element):
    """

    This is a grouping element and does not have any attributes. It groups
    elements that are used to adjust the generation of candidate contact pairs
    for collision checking. Collision detection was described in detail in the
    Computation chapter, thus the description here is brief.

    """
    def __init__(
        self,
        class_=None,
        geom1=None,
        geom2=None,
        condim="3",
        friction="1 1 0.005 0.0001 0.0001",
        margin="0",
        gap="0",
    ):
        self.class_ = class_
        self.geom1 = geom1
        self.geom2 = geom2
        self.condim = condim
        self.friction = friction
        self.margin = margin
        self.gap = gap
        self._attribute_names = ['class_', 'geom1', 'geom2', 'condim', 'friction', 'margin', 'gap']


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
        class_=None,
        geom1=None,
        geom2=None,
        condim="3",
        friction="1 1 0.005 0.0001 0.0001",
        margin="0",
        gap="0",
    ):
        self.class_ = class_
        self.geom1 = geom1
        self.geom2 = geom2
        self.condim = condim
        self.friction = friction
        self.margin = margin
        self.gap = gap
        self._attribute_names = ['class_', 'geom1', 'geom2', 'condim', 'friction', 'margin', 'gap']


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
        body1=None,
        body2=None,
    ):
        self.body1 = body1
        self.body2 = body2
        self._attribute_names = ['body1', 'body2']


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
        name=None,
        class_=None,
        active="BAD DEFAULT",
        body1=None,
        body2=None,
        anchor=None,
    ):
        self.name = name
        self.class_ = class_
        self.active = active
        self.body1 = body1
        self.body2 = body2
        self.anchor = anchor
        self._attribute_names = ['name', 'class_', 'active', 'body1', 'body2', 'anchor']


class EqualityConnect(Element):
    """

    This element creates an equality constraint that connects two bodies at a
    point. The point is not necessarily within the geoms volumes of either body.
    This constraint can be used to define ball joints outside the kinematic
    tree.

    """
    def __init__(
        self,
        name=None,
        class_=None,
        active="BAD DEFAULT",
        body1=None,
        body2=None,
        anchor=None,
    ):
        self.name = name
        self.class_ = class_
        self.active = active
        self.body1 = body1
        self.body2 = body2
        self.anchor = anchor
        self._attribute_names = ['name', 'class_', 'active', 'body1', 'body2', 'anchor']


class EqualityWeld(Element):
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
        body1=None,
        body2=None,
    ):
        self.body1 = body1
        self.body2 = body2
        self._attribute_names = ['body1', 'body2']


class EqualityJoint(Element):
    """

    This element constrains the position or angle of one joint to be a quartic
    polynomial of another joint. Only scalar joint types (slide and hinge) can
    be used.

    """
    def __init__(
        self,
        joint1=None,
        joint2=None,
        polycoef="0 1 0 0 0",
    ):
        self.joint1 = joint1
        self.joint2 = joint2
        self.polycoef = polycoef
        self._attribute_names = ['joint1', 'joint2', 'polycoef']


class EqualityTendon(Element):
    """

    This element constrains the length of one tendon to be a quartic polynomial
    of another tendon.

    """
    def __init__(
        self,
        tendon1=None,
        tendon2=None,
        polycoef="0 1 0 0",
    ):
        self.tendon1 = tendon1
        self.tendon2 = tendon2
        self.polycoef = polycoef
        self._attribute_names = ['tendon1', 'tendon2', 'polycoef']


class EqualityDistance(Element):
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
        geom1=None,
        geom2=None,
        distance="0",
    ):
        self.geom1 = geom1
        self.geom2 = geom2
        self.distance = distance
        self._attribute_names = ['geom1', 'geom2', 'distance']


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
        name=None,
        class_=None,
        limited="BAD DEFAULT",
        range="0 0",
        margin="0",
        frictionloss="0",
        width="0",
        material=None,
        rgba="0.5 0.5 0.5 1",
        stiffness="0",
        damping="0",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.limited = limited
        self.range = range
        self.margin = margin
        self.frictionloss = frictionloss
        self.width = width
        self.material = material
        self.rgba = rgba
        self.stiffness = stiffness
        self.damping = damping
        self.user = user
        self._attribute_names = ['name', 'class_', 'limited', 'range', 'margin', 'frictionloss', 'width', 'material', 'rgba', 'stiffness', 'damping', 'user']


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
        name=None,
        class_=None,
        limited="BAD DEFAULT",
        range="0 0",
        margin="0",
        frictionloss="0",
        width="0",
        material=None,
        rgba="0.5 0.5 0.5 1",
        stiffness="0",
        damping="0",
        user="0 0 ...",
    ):
        self.name = name
        self.class_ = class_
        self.limited = limited
        self.range = range
        self.margin = margin
        self.frictionloss = frictionloss
        self.width = width
        self.material = material
        self.rgba = rgba
        self.stiffness = stiffness
        self.damping = damping
        self.user = user
        self._attribute_names = ['name', 'class_', 'limited', 'range', 'margin', 'frictionloss', 'width', 'material', 'rgba', 'stiffness', 'damping', 'user']


class SpatialSite(Element):
    """

    This attribute specifies a site that the tendon path has to pass through.
    Recall that sites are rigidly attached to bodies.

    """
    def __init__(
        self,
        site=None,
    ):
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
        geom=None,
        sidesite=None,
    ):
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
        divisor=None,
    ):
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
    ):
        self._attribute_names = []


class FixedJoint(Element):
    """

    This element adds a joint to the computation of the fixed tendon length. The
    position or angle of each included joint is multiplied by the corresponding
    coef value, and added up to obtain the tendon length.

    """
    def __init__(
        self,
        joint=None,
        coef=None,
    ):
        self.joint = joint
        self.coef = coef
        self._attribute_names = ['joint', 'coef']


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
        name=None,
        class_=None,
        ctrllimited="BAD DEFAULT",
        forcelimited="BAD DEFAULT",
        ctrlrange="0 0",
        forcerange="0 0",
        gear="1 0 0 0 0 0",
        cranklength="0",
        joint=None,
        jointinparent=None,
        site=None,
        tendon=None,
        cranksite=None,
        slidersite=None,
        user="0 0 ...",
        dyntype="BAD DEFAULT",
        gaintype="BAD DEFAULT",
        biastype="BAD DEFAULT",
        dynprm="1 0 0",
        gainprm="1 0 0",
        biasprm="0 0 0",
    ):
        self.name = name
        self.class_ = class_
        self.ctrllimited = ctrllimited
        self.forcelimited = forcelimited
        self.ctrlrange = ctrlrange
        self.forcerange = forcerange
        self.gear = gear
        self.cranklength = cranklength
        self.joint = joint
        self.jointinparent = jointinparent
        self.site = site
        self.tendon = tendon
        self.cranksite = cranksite
        self.slidersite = slidersite
        self.user = user
        self.dyntype = dyntype
        self.gaintype = gaintype
        self.biastype = biastype
        self.dynprm = dynprm
        self.gainprm = gainprm
        self.biasprm = biasprm
        self._attribute_names = ['name', 'class_', 'ctrllimited', 'forcelimited', 'ctrlrange', 'forcerange', 'gear', 'cranklength', 'joint', 'jointinparent', 'site', 'tendon', 'cranksite', 'slidersite', 'user', 'dyntype', 'gaintype', 'biastype', 'dynprm', 'gainprm', 'biasprm']


class General(Element):
    """

    This element creates a general actuator, providing full access to all
    actuator components and allowing the user to specify them independently.

    """
    def __init__(
        self,
        name=None,
        class_=None,
        ctrllimited="BAD DEFAULT",
        forcelimited="BAD DEFAULT",
        ctrlrange="0 0",
        forcerange="0 0",
        gear="1 0 0 0 0 0",
        cranklength="0",
        joint=None,
        jointinparent=None,
        site=None,
        tendon=None,
        cranksite=None,
        slidersite=None,
        user="0 0 ...",
        dyntype="BAD DEFAULT",
        gaintype="BAD DEFAULT",
        biastype="BAD DEFAULT",
        dynprm="1 0 0",
        gainprm="1 0 0",
        biasprm="0 0 0",
    ):
        self.name = name
        self.class_ = class_
        self.ctrllimited = ctrllimited
        self.forcelimited = forcelimited
        self.ctrlrange = ctrlrange
        self.forcerange = forcerange
        self.gear = gear
        self.cranklength = cranklength
        self.joint = joint
        self.jointinparent = jointinparent
        self.site = site
        self.tendon = tendon
        self.cranksite = cranksite
        self.slidersite = slidersite
        self.user = user
        self.dyntype = dyntype
        self.gaintype = gaintype
        self.biastype = biastype
        self.dynprm = dynprm
        self.gainprm = gainprm
        self.biasprm = biasprm
        self._attribute_names = ['name', 'class_', 'ctrllimited', 'forcelimited', 'ctrlrange', 'forcerange', 'gear', 'cranklength', 'joint', 'jointinparent', 'site', 'tendon', 'cranksite', 'slidersite', 'user', 'dyntype', 'gaintype', 'biastype', 'dynprm', 'gainprm', 'biasprm']


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
    ):
        self._attribute_names = []


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
    ):
        self.kp = kp
        self._attribute_names = ['kp']


class Velocity(Element):
    """

    This element creates a velocity servo. Note that in order create a PD controller, one has to define two actuators: a position servo and a velocity servo. This is because MuJoCo actuators are SISO while a PD controller takes two control inputs (reference position and reference velocity). The underlying general attributes are set as follows:

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
    ):
        self.kv = kv
        self._attribute_names = ['kv']


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
        timeconst="1",
        area="1",
        diameter=None,
        bias="0 0 0",
    ):
        self.timeconst = timeconst
        self.area = area
        self.diameter = diameter
        self.bias = bias
        self._attribute_names = ['timeconst', 'area', 'diameter', 'bias']


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
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


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
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


class SensorAccelerometer(Element):
    """

    This element creates a 3-axis accelerometer. The sensor is mounted at a
    site, and has the same position and orientation as the site frame. This
    sensor outputs three numbers, which are the linear acceleration of the site
    (including gravity) in local coordinates.

    """
    def __init__(
        self,
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


class SensorVelocimeter(Element):
    """

    This element creates a 3-axis velocimeter. The sensor is mounted at a site,
    and has the same position and orientation as the site frame. This sensor
    outputs three numbers, which are the linear velocity of the site in local
    coordinates.

    """
    def __init__(
        self,
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


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
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


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
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


class SensorTorque(Element):
    """

    This element creates a 3-axis torque sensor. This is similar to the force
    sensor above, but measures torque rather than force.

    """
    def __init__(
        self,
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


class SensorMagnetometer(Element):
    """

    This element creates a magnetometer. It measures the magnetic flux at the
    sensor site position, expressed in the sensor site frame. The output is a 3D
    vector.

    """
    def __init__(
        self,
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


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
        site=None,
    ):
        self.site = site
        self._attribute_names = ['site']


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
        joint=None,
    ):
        self.joint = joint
        self._attribute_names = ['joint']


class SensorJointvel(Element):
    """

    This element creates a joint velocity sensor. It can be attached to scalar
    joints (slide or hinge). Its output is scalar.

    """
    def __init__(
        self,
        joint=None,
    ):
        self.joint = joint
        self._attribute_names = ['joint']


class SensorTendonpos(Element):
    """

    This element creates a tendon length sensor. It can be attached to both
    spatial and fixed tendons. Its output is scalar.

    """
    def __init__(
        self,
        tendon=None,
    ):
        self.tendon = tendon
        self._attribute_names = ['tendon']


class SensorTendonvel(Element):
    """

    This element creates a tendon velocity sensor. It can be attached to both
    spatial and fixed tendons. Its output is scalar.

    """
    def __init__(
        self,
        tendon=None,
    ):
        self.tendon = tendon
        self._attribute_names = ['tendon']


class SensorActuatorpos(Element):
    """

    This element creates an actuator length sensor. Recall that each actuator
    has a transmission which has length. This sensor can be attached to any
    actuator. Its output is scalar.

    """
    def __init__(
        self,
        actuator=None,
    ):
        self.actuator = actuator
        self._attribute_names = ['actuator']


class SensorActuatorvel(Element):
    """

    This element creates an actuator velocity sensor. This sensor can be
    attached to any actuator. Its output is scalar.

    """
    def __init__(
        self,
        actuator=None,
    ):
        self.actuator = actuator
        self._attribute_names = ['actuator']


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
        actuator=None,
    ):
        self.actuator = actuator
        self._attribute_names = ['actuator']


class SensorBallquat(Element):
    """

    This element creates a quaternion sensor for a ball joints. It outputs 4
    numbers corresponding to a unit quaternion.

    """
    def __init__(
        self,
        joint=None,
    ):
        self.joint = joint
        self._attribute_names = ['joint']


class SensorBallangvel(Element):
    """

    This element creates a ball joint angular velocity sensor. It outputs 3
    numbers corresponding to the angular velocity of the joint. The norm of that
    vector is the rotation speed in rad/s and the direction is the axis around
    which the rotation takes place.

    """
    def __init__(
        self,
        joint=None,
    ):
        self.joint = joint
        self._attribute_names = ['joint']


class SensorFramepos(Element):
    """

    This element creates a sensor that returns the 3D position of the spatial
    frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFramequat(Element):
    """

    This element creates a sensor that returns the unit quaternion specifying
    the orientation of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFramexaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the X-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFrameyaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the Y-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFramezaxis(Element):
    """

    This element creates a sensor that returns the 3D unit vector corresponding
    to the Z-axis of the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFramelinvel(Element):
    """

    This element creates a sensor that returns the 3D linear velocity of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFrameangvel(Element):
    """

    This element creates a sensor that returns the 3D angular velocity of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFramelinacc(Element):
    """

    This element creates a sensor that returns the 3D linear acceleration of the
    spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorFrameangacc(Element):
    """

    This element creates a sensor that returns the 3D angular acceleration of
    the spatial frame of the object, in global coordinates.

    """
    def __init__(
        self,
        objtype="BAD DEFAULT",
        objname=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self._attribute_names = ['objtype', 'objname']


class SensorSubtreecom(Element):
    """

    This element creates sensor that returns the center of mass of the kinematic
    subtree rooted at a specified body, in global coordinates.

    """
    def __init__(
        self,
        body=None,
    ):
        self.body = body
        self._attribute_names = ['body']


class SensorSubtreelinvel(Element):
    """

    This element creates sensor that returns the linear velocity of the center
    of mass of the kinematic subtree rooted at a specified body, in global
    coordinates.

    """
    def __init__(
        self,
        body=None,
    ):
        self.body = body
        self._attribute_names = ['body']


class SensorSubtreeangmom(Element):
    """

    This element creates sensor that returns the angular momentum around the
    center of mass of the kinematic subtree rooted at a specified body, in
    global coordinates.

    """
    def __init__(
        self,
        body=None,
    ):
        self.body = body
        self._attribute_names = ['body']


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
        objtype="BAD DEFAULT",
        objname=None,
        datatype="BAD DEFAULT",
        needstage="BAD DEFAULT",
        dim=None,
    ):
        self.objtype = objtype
        self.objname = objname
        self.datatype = datatype
        self.needstage = needstage
        self.dim = dim
        self._attribute_names = ['objtype', 'objname', 'datatype', 'needstage', 'dim']


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
        time="0",
        qpos=None,
        qvel="0 0 ...",
        act="0 0 ...",
    ):
        self.time = time
        self.qpos = qpos
        self.qvel = qvel
        self.act = act
        self._attribute_names = ['time', 'qpos', 'qvel', 'act']


class Key(Element):
    """

    This element sets the data for one of the keyframes. They are set in the
    order in which they appear here.

    """
    def __init__(
        self,
        time="0",
        qpos=None,
        qvel="0 0 ...",
        act="0 0 ...",
    ):
        self.time = time
        self.qpos = qpos
        self.qvel = qvel
        self.act = act
        self._attribute_names = ['time', 'qpos', 'qvel', 'act']
