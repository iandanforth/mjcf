from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="inverted pendulum",
    )
    compiler = e.Compiler(
        inertiafromgeom="true",
    )
    default = e.Default(
    )
    option = e.Option(
        gravity="0 0 -9.81",
        integrator="RK4",
        timestep="0.02",
    )
    size = e.Size(
        nstack="3000",
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        default,
        option,
        size,
        worldbody,
        actuator,
    ])
    joint = e.Joint(
        armature="0",
        damping="1",
        limited="true",
    )
    geom = e.Geom(
        contype="0",
        friction="1 0.1 0.1",
        rgba="0.7 0.7 0 1",
    )
    tendon = e.Tendon(
    )
    motor = e.Motor(
        ctrlrange="-3 3",
    )
    default.add_children([
        joint,
        geom,
        tendon,
        motor,
    ])
    rail = e.Geom(
        name="rail",
        pos="0 0 0",
        quat="0.707 0 0.707 0",
        rgba="0.3 0.3 0.7 1",
        size="0.02 1",
        type="capsule",
    )
    cart = e.Body(
        name="cart",
        pos="0 0 0",
    )
    worldbody.add_children([
        rail,
        cart,
    ])
    slide = e.Motor(
        gear="100",
        joint="slider",
        name="slide",
    )
    actuator.add_children([
        slide,
    ])
    slider = e.Joint(
        axis="1 0 0",
        limited="true",
        name="slider",
        pos="0 0 0",
        range="-1 1",
        type="slide",
    )
    cart_1 = e.Geom(
        name="cart",
        pos="0 0 0",
        quat="0.707 0 0.707 0",
        size="0.1 0.1",
        type="capsule",
    )
    pole = e.Body(
        name="pole",
        pos="0 0 0",
    )
    cart.add_children([
        slider,
        cart_1,
        pole,
    ])
    hinge = e.Joint(
        axis="0 1 0",
        name="hinge",
        pos="0 0 0",
        range="-90 90",
        type="hinge",
    )
    cpole = e.Geom(
        fromto="0 0 0 0.001 0 0.6",
        name="cpole",
        rgba="0 0.7 0.7 1",
        size="0.049 0.3",
        type="capsule",
    )
    pole.add_children([
        hinge,
        cpole,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('inverted_pendulum_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()