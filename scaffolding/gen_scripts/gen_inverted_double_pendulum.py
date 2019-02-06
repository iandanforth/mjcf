from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="cartpole",
    )
    compiler = e.Compiler(
        coordinate="local",
        inertiafromgeom="true",
    )
    custom = e.Custom(
    )
    default = e.Default(
    )
    option = e.Option(
        gravity="1e-5 0 -9.81",
        integrator="RK4",
        timestep="0.01",
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
        custom,
        default,
        option,
        size,
        worldbody,
        actuator,
    ])
    frame_skip = e.Numeric(
        data="2",
        name="frame_skip",
    )
    custom.add_children([
        frame_skip,
    ])
    joint = e.Joint(
        damping="0.05",
    )
    geom = e.Geom(
        contype="0",
        friction="1 0.1 0.1",
        rgba="0.7 0.7 0 1",
    )
    default.add_children([
        joint,
        geom,
    ])
    floor = e.Geom(
        name="floor",
        pos="0 0 -3.0",
        rgba="0.8 0.9 0.8 1",
        size="40 40 40",
        type="plane",
    )
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
        floor,
        rail,
        cart,
    ])
    slide = e.Motor(
        ctrllimited="true",
        ctrlrange="-1 1",
        gear="500",
        joint="slider",
        name="slide",
    )
    actuator.add_children([
        slide,
    ])
    slider = e.Joint(
        axis="1 0 0",
        limited="true",
        margin="0.01",
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
        type="hinge",
    )
    cpole = e.Geom(
        fromto="0 0 0 0 0 0.6",
        name="cpole",
        rgba="0 0.7 0.7 1",
        size="0.045 0.3",
        type="capsule",
    )
    pole2 = e.Body(
        name="pole2",
        pos="0 0 0.6",
    )
    pole.add_children([
        hinge,
        cpole,
        pole2,
    ])
    hinge2 = e.Joint(
        axis="0 1 0",
        name="hinge2",
        pos="0 0 0",
        type="hinge",
    )
    cpole2 = e.Geom(
        fromto="0 0 0 0 0 0.6",
        name="cpole2",
        rgba="0 0.7 0.7 1",
        size="0.045 0.3",
        type="capsule",
    )
    tip = e.Site(
        name="tip",
        pos="0 0 .6",
        size="0.01 0.01",
    )
    pole2.add_children([
        hinge2,
        cpole2,
        tip,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('inverted_double_pendulum_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()