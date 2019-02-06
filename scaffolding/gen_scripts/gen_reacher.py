from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="reacher",
    )
    compiler = e.Compiler(
        angle="radian",
        inertiafromgeom="true",
    )
    default = e.Default(
    )
    option = e.Option(
        gravity="0 0 -9.81",
        integrator="RK4",
        timestep="0.01",
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        default,
        option,
        worldbody,
        actuator,
    ])
    joint = e.Joint(
        armature="1",
        damping="1",
        limited="true",
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
    ground = e.Geom(
        conaffinity="0",
        contype="0",
        name="ground",
        pos="0 0 0",
        rgba="0.9 0.9 0.9 1",
        size="1 1 10",
        type="plane",
    )
    sideS = e.Geom(
        conaffinity="0",
        fromto="-.3 -.3 .01 .3 -.3 .01",
        name="sideS",
        rgba="0.9 0.4 0.6 1",
        size=".02",
        type="capsule",
    )
    sideE = e.Geom(
        conaffinity="0",
        fromto=" .3 -.3 .01 .3  .3 .01",
        name="sideE",
        rgba="0.9 0.4 0.6 1",
        size=".02",
        type="capsule",
    )
    sideN = e.Geom(
        conaffinity="0",
        fromto="-.3  .3 .01 .3  .3 .01",
        name="sideN",
        rgba="0.9 0.4 0.6 1",
        size=".02",
        type="capsule",
    )
    sideW = e.Geom(
        conaffinity="0",
        fromto="-.3 -.3 .01 -.3 .3 .01",
        name="sideW",
        rgba="0.9 0.4 0.6 1",
        size=".02",
        type="capsule",
    )
    root = e.Geom(
        conaffinity="0",
        contype="0",
        fromto="0 0 0 0 0 0.02",
        name="root",
        rgba="0.9 0.4 0.6 1",
        size=".011",
        type="cylinder",
    )
    body0 = e.Body(
        name="body0",
        pos="0 0 .01",
    )
    target = e.Body(
        name="target",
        pos=".1 -.1 .01",
    )
    worldbody.add_children([
        ground,
        sideS,
        sideE,
        sideN,
        sideW,
        root,
        body0,
        target,
    ])
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="200.0",
        joint="joint0",
    )
    motor_1 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="200.0",
        joint="joint1",
    )
    actuator.add_children([
        motor,
        motor_1,
    ])
    link0 = e.Geom(
        fromto="0 0 0 0.1 0 0",
        name="link0",
        rgba="0.0 0.4 0.6 1",
        size=".01",
        type="capsule",
    )
    joint0 = e.Joint(
        axis="0 0 1",
        limited="false",
        name="joint0",
        pos="0 0 0",
        type="hinge",
    )
    body1 = e.Body(
        name="body1",
        pos="0.1 0 0",
    )
    body0.add_children([
        link0,
        joint0,
        body1,
    ])
    target_x = e.Joint(
        armature="0",
        axis="1 0 0",
        damping="0",
        limited="true",
        name="target_x",
        pos="0 0 0",
        range="-.27 .27",
        ref=".1",
        stiffness="0",
        type="slide",
    )
    target_y = e.Joint(
        armature="0",
        axis="0 1 0",
        damping="0",
        limited="true",
        name="target_y",
        pos="0 0 0",
        range="-.27 .27",
        ref="-.1",
        stiffness="0",
        type="slide",
    )
    target_1 = e.Geom(
        conaffinity="0",
        contype="0",
        name="target",
        pos="0 0 0",
        rgba="0.9 0.2 0.2 1",
        size=".009",
        type="sphere",
    )
    target.add_children([
        target_x,
        target_y,
        target_1,
    ])
    joint1 = e.Joint(
        axis="0 0 1",
        limited="true",
        name="joint1",
        pos="0 0 0",
        range="-3.0 3.0",
        type="hinge",
    )
    link1 = e.Geom(
        fromto="0 0 0 0.1 0 0",
        name="link1",
        rgba="0.0 0.4 0.6 1",
        size=".01",
        type="capsule",
    )
    fingertip = e.Body(
        name="fingertip",
        pos="0.11 0 0",
    )
    body1.add_children([
        joint1,
        link1,
        fingertip,
    ])
    fingertip_1 = e.Geom(
        contype="0",
        name="fingertip",
        pos="0 0 0",
        rgba="0.0 0.8 0.6 1",
        size=".01",
        type="sphere",
    )
    fingertip.add_children([
        fingertip_1,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('reacher_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()