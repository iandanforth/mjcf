from mjcf.element import Element


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
    ):
        super().__init__()
        self._attribute_names = []


class Global(Element):
    """

    While all settings in mjVisual are global, the settings here could not be
    fit into any of the other subsections. So this is effectively a
    miscellaneous subsection.

    """
    def __init__(
        self,
        fovy="45",
        glow="0.3",
        ipd="0.068",
        linewidth="1",
        offheight="480",
        offwidth="640",
    ):
        super().__init__()
        self.fovy = fovy
        self.glow = glow
        self.ipd = ipd
        self.linewidth = linewidth
        self.offheight = offheight
        self.offwidth = offwidth
        self._attribute_names = ['fovy', 'glow', 'ipd', 'linewidth', 'offheight', 'offwidth']


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
        numarrows="10",
        numquads="4",
        numslices="28",
        numstacks="16",
        offsamples="4",
        shadowsize="1024",
    ):
        super().__init__()
        self.numarrows = numarrows
        self.numquads = numquads
        self.numslices = numslices
        self.numstacks = numstacks
        self.offsamples = offsamples
        self.shadowsize = shadowsize
        self._attribute_names = ['numarrows', 'numquads', 'numslices', 'numstacks', 'offsamples', 'shadowsize']


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
        active="1",
        ambient="0.1 0.1 0.1",
        diffuse="0.4 0.4 0.4",
        specular="0.5 0.5 0.5",
    ):
        super().__init__()
        self.active = active
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self._attribute_names = ['active', 'ambient', 'diffuse', 'specular']


class Map(Element):
    """

    This element is used to specify scaling quantities that affect both the
    visualization and built-in mouse perturbations. Unlike the scaling
    quantities in the next element which are specific to spatial extent, the
    quantities here are miscellaneous.

    """
    def __init__(
        self,
        alpha="0.3",
        fogend="10",
        fogstart="3",
        force="0.005",
        shadowclip="1",
        shadowscale="0.6",
        stiffness="100",
        stiffnessrot="500",
        torque="0.1",
        zfar="50",
        znear="0.2",
    ):
        super().__init__()
        self.alpha = alpha
        self.fogend = fogend
        self.fogstart = fogstart
        self.force = force
        self.shadowclip = shadowclip
        self.shadowscale = shadowscale
        self.stiffness = stiffness
        self.stiffnessrot = stiffnessrot
        self.torque = torque
        self.zfar = zfar
        self.znear = znear
        self._attribute_names = ['alpha', 'fogend', 'fogstart', 'force', 'shadowclip', 'shadowscale', 'stiffness', 'stiffnessrot', 'torque', 'zfar', 'znear']


class Scale(Element):
    """

    The settings in this element control the spatial extent of various
    decorative objects. In all cases, the rendered size equals the mean body
    size (see statistic element below) multiplied by the value of an attribute
    documented below.

    """
    def __init__(
        self,
        actuatorlength="0.7",
        actuatorwidth="0.2",
        camera="0.3",
        com="0.4",
        connect="0.2",
        constraint="0.1",
        contactheight="0.1",
        contactwidth="0.3",
        forcewidth="0.1",
        framelength="1.0",
        framewidth="0.1",
        jointlength="1.0",
        jointwidth="0.1",
        light="0.3",
        selectpoint="0.2",
        slidercrank="0.2",
    ):
        super().__init__()
        self.actuatorlength = actuatorlength
        self.actuatorwidth = actuatorwidth
        self.camera = camera
        self.com = com
        self.connect = connect
        self.constraint = constraint
        self.contactheight = contactheight
        self.contactwidth = contactwidth
        self.forcewidth = forcewidth
        self.framelength = framelength
        self.framewidth = framewidth
        self.jointlength = jointlength
        self.jointwidth = jointwidth
        self.light = light
        self.selectpoint = selectpoint
        self.slidercrank = slidercrank
        self._attribute_names = ['actuatorlength', 'actuatorwidth', 'camera', 'com', 'connect', 'constraint', 'contactheight', 'contactwidth', 'forcewidth', 'framelength', 'framewidth', 'jointlength', 'jointwidth', 'light', 'selectpoint', 'slidercrank']
