from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="walker2d",
    )
    compiler = e.Compiler(
        angle="degree",
        coordinate="global",
        inertiafromgeom="true",
    )
    default = e.Default(
    )
    option = e.Option(
        integrator="RK4",
        timestep="0.002",
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    asset = e.Asset(
    )
    mujoco.add_children([
        compiler,
        default,
        option,
        worldbody,
        actuator,
        asset,
    ])
    joint = e.Joint(
        armature="0.01",
        damping=".1",
        limited="true",
    )
    geom = e.Geom(
        conaffinity="0",
        condim="3",
        contype="1",
        density="1000",
        friction=".7 .1 .1",
        rgba="0.8 0.6 .4 1",
    )
    default.add_children([
        joint,
        geom,
    ])
    light = e.Light(
        cutoff="100",
        diffuse="1 1 1",
        dir="-0 0 -1.3",
        directional="true",
        exponent="1",
        pos="0 0 1.3",
        specular=".1 .1 .1",
    )
    floor = e.Geom(
        conaffinity="1",
        condim="3",
        name="floor",
        pos="0 0 0",
        rgba="0.8 0.9 0.8 1",
        size="40 40 40",
        type="plane",
        material="MatPlane",
    )
    torso = e.Body(
        name="torso",
        pos="0 0 1.25",
    )
    worldbody.add_children([
        light,
        floor,
        torso,
    ])
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="thigh_joint",
    )
    motor_1 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="leg_joint",
    )
    motor_2 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="foot_joint",
    )
    motor_3 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="thigh_left_joint",
    )
    motor_4 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="leg_left_joint",
    )
    motor_5 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        gear="100",
        joint="foot_left_joint",
    )
    actuator.add_children([
        motor,
        motor_1,
        motor_2,
        motor_3,
        motor_4,
        motor_5,
    ])
    texture = e.Texture(
        type="skybox",
        builtin="gradient",
        rgb1=".4 .5 .6",
        rgb2="0 0 0",
        width="100",
        height="100",
    )
    texgeom = e.Texture(
        builtin="flat",
        height="1278",
        mark="cross",
        markrgb="1 1 1",
        name="texgeom",
        random="0.01",
        rgb1="0.8 0.6 0.4",
        rgb2="0.8 0.6 0.4",
        type="cube",
        width="127",
    )
    texplane = e.Texture(
        builtin="checker",
        height="100",
        name="texplane",
        rgb1="0 0 0",
        rgb2="0.8 0.8 0.8",
        type="2d",
        width="100",
    )
    MatPlane = e.Material(
        name="MatPlane",
        reflectance="0.5",
        shininess="1",
        specular="1",
        texrepeat="60 60",
        texture="texplane",
    )
    geom_1 = e.Material(
        name="geom",
        texture="texgeom",
        texuniform="true",
    )
    asset.add_children([
        texture,
        texgeom,
        texplane,
        MatPlane,
        geom_1,
    ])
    track = e.Camera(
        name="track",
        mode="trackcom",
        pos="0 -3 1",
        xyaxes="1 0 0 0 0 1",
    )
    rootx = e.Joint(
        armature="0",
        axis="1 0 0",
        damping="0",
        limited="false",
        name="rootx",
        pos="0 0 0",
        stiffness="0",
        type="slide",
    )
    rootz = e.Joint(
        armature="0",
        axis="0 0 1",
        damping="0",
        limited="false",
        name="rootz",
        pos="0 0 0",
        ref="1.25",
        stiffness="0",
        type="slide",
    )
    rooty = e.Joint(
        armature="0",
        axis="0 1 0",
        damping="0",
        limited="false",
        name="rooty",
        pos="0 0 1.25",
        stiffness="0",
        type="hinge",
    )
    torso_geom = e.Geom(
        friction="0.9",
        fromto="0 0 1.45 0 0 1.05",
        name="torso_geom",
        size="0.05",
        type="capsule",
    )
    thigh = e.Body(
        name="thigh",
        pos="0 0 1.05",
    )
    thigh_left = e.Body(
        name="thigh_left",
        pos="0 0 1.05",
    )
    torso.add_children([
        track,
        rootx,
        rootz,
        rooty,
        torso_geom,
        thigh,
        thigh_left,
    ])
    thigh_joint = e.Joint(
        axis="0 -1 0",
        name="thigh_joint",
        pos="0 0 1.05",
        range="-150 0",
        type="hinge",
    )
    thigh_geom = e.Geom(
        friction="0.9",
        fromto="0 0 1.05 0 0 0.6",
        name="thigh_geom",
        size="0.05",
        type="capsule",
    )
    leg = e.Body(
        name="leg",
        pos="0 0 0.35",
    )
    thigh.add_children([
        thigh_joint,
        thigh_geom,
        leg,
    ])
    thigh_left_joint = e.Joint(
        axis="0 -1 0",
        name="thigh_left_joint",
        pos="0 0 1.05",
        range="-150 0",
        type="hinge",
    )
    thigh_left_geom = e.Geom(
        friction="0.9",
        fromto="0 0 1.05 0 0 0.6",
        name="thigh_left_geom",
        rgba=".7 .3 .6 1",
        size="0.05",
        type="capsule",
    )
    leg_left = e.Body(
        name="leg_left",
        pos="0 0 0.35",
    )
    thigh_left.add_children([
        thigh_left_joint,
        thigh_left_geom,
        leg_left,
    ])
    leg_joint = e.Joint(
        axis="0 -1 0",
        name="leg_joint",
        pos="0 0 0.6",
        range="-150 0",
        type="hinge",
    )
    leg_geom = e.Geom(
        friction="0.9",
        fromto="0 0 0.6 0 0 0.1",
        name="leg_geom",
        size="0.04",
        type="capsule",
    )
    foot = e.Body(
        name="foot",
        pos="0.2/2 0 0.1",
    )
    leg.add_children([
        leg_joint,
        leg_geom,
        foot,
    ])
    leg_left_joint = e.Joint(
        axis="0 -1 0",
        name="leg_left_joint",
        pos="0 0 0.6",
        range="-150 0",
        type="hinge",
    )
    leg_left_geom = e.Geom(
        friction="0.9",
        fromto="0 0 0.6 0 0 0.1",
        name="leg_left_geom",
        rgba=".7 .3 .6 1",
        size="0.04",
        type="capsule",
    )
    foot_left = e.Body(
        name="foot_left",
        pos="0.2/2 0 0.1",
    )
    leg_left.add_children([
        leg_left_joint,
        leg_left_geom,
        foot_left,
    ])
    foot_joint = e.Joint(
        axis="0 -1 0",
        name="foot_joint",
        pos="0 0 0.1",
        range="-45 45",
        type="hinge",
    )
    foot_geom = e.Geom(
        friction="0.9",
        fromto="-0.0 0 0.1 0.2 0 0.1",
        name="foot_geom",
        size="0.06",
        type="capsule",
    )
    foot.add_children([
        foot_joint,
        foot_geom,
    ])
    foot_left_joint = e.Joint(
        axis="0 -1 0",
        name="foot_left_joint",
        pos="0 0 0.1",
        range="-45 45",
        type="hinge",
    )
    foot_left_geom = e.Geom(
        friction="1.9",
        fromto="-0.0 0 0.1 0.2 0 0.1",
        name="foot_left_geom",
        rgba=".7 .3 .6 1",
        size="0.06",
        type="capsule",
    )
    foot_left.add_children([
        foot_left_joint,
        foot_left_geom,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('walker2d_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()