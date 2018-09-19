from mjcf.element import Element


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
        apirate="100",
        collision="all",
        cone="pyramidal",
        density="0",
        gravity="0 0 -9.81",
        impedance="sigmoid",
        impratio="1",
        integrator="Euler",
        iterations="100",
        jacobian="auto",
        mpr_iterations="50",
        mpr_tolerance="1e-6",
        noslip_iterations="0",
        noslip_tolerance="1e-6",
        o_margin="0",
        o_solimp="0.8 0.8 0.01",
        o_solref="0.02 1",
        reference="spring",
        solver="Newton",
        timestep="0.002",
        tolerance="1e-8",
        viscosity="0",
        wind="0 0 0",
    ):
        super().__init__()
        self.apirate = apirate
        self.collision = collision
        self.cone = cone
        self.density = density
        self.gravity = gravity
        self.impedance = impedance
        self.impratio = impratio
        self.integrator = integrator
        self.iterations = iterations
        self.jacobian = jacobian
        self.mpr_iterations = mpr_iterations
        self.mpr_tolerance = mpr_tolerance
        self.noslip_iterations = noslip_iterations
        self.noslip_tolerance = noslip_tolerance
        self.o_margin = o_margin
        self.o_solimp = o_solimp
        self.o_solref = o_solref
        self.reference = reference
        self.solver = solver
        self.timestep = timestep
        self.tolerance = tolerance
        self.viscosity = viscosity
        self.wind = wind
        self._attribute_names = ['apirate', 'collision', 'cone', 'density', 'gravity', 'impedance', 'impratio', 'integrator', 'iterations', 'jacobian', 'mpr_iterations', 'mpr_tolerance', 'noslip_iterations', 'noslip_tolerance', 'o_margin', 'o_solimp', 'o_solref', 'reference', 'solver', 'timestep', 'tolerance', 'viscosity', 'wind']


class Flag(Element):
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
        actuation="enable",
        clampctrl="enable",
        constraint="enable",
        contact="enable",
        energy="disable",
        equality="enable",
        filterparent="enable",
        frictionloss="enable",
        fwdinv="disable",
        gravity="enable",
        limit="enable",
        override="disable",
        passive="enable",
        refsafe="enable",
        sensornoise="disable",
        warmstart="enable",
    ):
        super().__init__()
        self.actuation = actuation
        self.clampctrl = clampctrl
        self.constraint = constraint
        self.contact = contact
        self.energy = energy
        self.equality = equality
        self.filterparent = filterparent
        self.frictionloss = frictionloss
        self.fwdinv = fwdinv
        self.gravity = gravity
        self.limit = limit
        self.override = override
        self.passive = passive
        self.refsafe = refsafe
        self.sensornoise = sensornoise
        self.warmstart = warmstart
        self._attribute_names = ['actuation', 'clampctrl', 'constraint', 'contact', 'energy', 'equality', 'filterparent', 'frictionloss', 'fwdinv', 'gravity', 'limit', 'override', 'passive', 'refsafe', 'sensornoise', 'warmstart']
