from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="ant",
    )
    compiler = e.Compiler(
        angle="degree",
        coordinate="local",
        inertiafromgeom="true",
    )
    option = e.Option(
        integrator="RK4",
        timestep="0.01",
    )
    custom = e.Custom(
    )
    default = e.Default(
    )
    asset = e.Asset(
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        option,
        custom,
        default,
        asset,
        worldbody,
        actuator,
    ])
    init_qpos = e.Numeric(
        data="0.0 0.0 0.55 1.0 0.0 0.0 0.0 0.0 1.0 0.0 -1.0 0.0 -1.0 0.0 1.0",
        name="init_qpos",
    )
    custom.add_children([
        init_qpos,
    ])
    joint = e.Joint(
        armature="1",
        damping="1",
        limited="true",
    )
    geom = e.Geom(
        conaffinity="0",
        condim="3",
        density="5.0",
        friction="1 0.5 0.5",
        margin="0.01",
        rgba="0.8 0.6 0.4 1",
    )
    default.add_children([
        joint,
        geom,
    ])
    texture = e.Texture(
        builtin="gradient",
        height="100",
        rgb1="1 1 1",
        rgb2="0 0 0",
        type="skybox",
        width="100",
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
        material="MatPlane",
        name="floor",
        pos="0 0 0",
        rgba="0.8 0.9 0.8 1",
        size="40 40 40",
        type="plane",
    )
    torso = e.Body(
        name="torso",
        pos="0 0 0.75",
    )
    worldbody.add_children([
        light,
        floor,
        torso,
    ])
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="hip_4",
        gear="150",
    )
    motor_1 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="ankle_4",
        gear="150",
    )
    motor_2 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="hip_1",
        gear="150",
    )
    motor_3 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="ankle_1",
        gear="150",
    )
    motor_4 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="hip_2",
        gear="150",
    )
    motor_5 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="ankle_2",
        gear="150",
    )
    motor_6 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="hip_3",
        gear="150",
    )
    motor_7 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint="ankle_3",
        gear="150",
    )
    actuator.add_children([
        motor,
        motor_1,
        motor_2,
        motor_3,
        motor_4,
        motor_5,
        motor_6,
        motor_7,
    ])
    track = e.Camera(
        name="track",
        mode="trackcom",
        pos="0 -3 0.3",
        xyaxes="1 0 0 0 0 1",
    )
    torso_geom = e.Geom(
        name="torso_geom",
        pos="0 0 0",
        size="0.25",
        type="sphere",
    )
    root = e.Joint(
        armature="0",
        damping="0",
        limited="false",
        margin="0.01",
        name="root",
        pos="0 0 0",
        type="free",
    )
    front_left_leg = e.Body(
        name="front_left_leg",
        pos="0 0 0",
    )
    front_right_leg = e.Body(
        name="front_right_leg",
        pos="0 0 0",
    )
    back_leg = e.Body(
        name="back_leg",
        pos="0 0 0",
    )
    right_back_leg = e.Body(
        name="right_back_leg",
        pos="0 0 0",
    )
    torso.add_children([
        track,
        torso_geom,
        root,
        front_left_leg,
        front_right_leg,
        back_leg,
        right_back_leg,
    ])
    aux_1_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.2 0.2 0.0",
        name="aux_1_geom",
        size="0.08",
        type="capsule",
    )
    aux_1 = e.Body(
        name="aux_1",
        pos="0.2 0.2 0",
    )
    front_left_leg.add_children([
        aux_1_geom,
        aux_1,
    ])
    aux_2_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.2 0.2 0.0",
        name="aux_2_geom",
        size="0.08",
        type="capsule",
    )
    aux_2 = e.Body(
        name="aux_2",
        pos="-0.2 0.2 0",
    )
    front_right_leg.add_children([
        aux_2_geom,
        aux_2,
    ])
    aux_3_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.2 -0.2 0.0",
        name="aux_3_geom",
        size="0.08",
        type="capsule",
    )
    aux_3 = e.Body(
        name="aux_3",
        pos="-0.2 -0.2 0",
    )
    back_leg.add_children([
        aux_3_geom,
        aux_3,
    ])
    aux_4_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.2 -0.2 0.0",
        name="aux_4_geom",
        size="0.08",
        type="capsule",
    )
    aux_4 = e.Body(
        name="aux_4",
        pos="0.2 -0.2 0",
    )
    right_back_leg.add_children([
        aux_4_geom,
        aux_4,
    ])
    hip_1 = e.Joint(
        axis="0 0 1",
        name="hip_1",
        pos="0.0 0.0 0.0",
        range="-30 30",
        type="hinge",
    )
    left_leg_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.2 0.2 0.0",
        name="left_leg_geom",
        size="0.08",
        type="capsule",
    )
    body = e.Body(
        pos="0.2 0.2 0",
    )
    aux_1.add_children([
        hip_1,
        left_leg_geom,
        body,
    ])
    hip_2 = e.Joint(
        axis="0 0 1",
        name="hip_2",
        pos="0.0 0.0 0.0",
        range="-30 30",
        type="hinge",
    )
    right_leg_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.2 0.2 0.0",
        name="right_leg_geom",
        size="0.08",
        type="capsule",
    )
    body_1 = e.Body(
        pos="-0.2 0.2 0",
    )
    aux_2.add_children([
        hip_2,
        right_leg_geom,
        body_1,
    ])
    hip_3 = e.Joint(
        axis="0 0 1",
        name="hip_3",
        pos="0.0 0.0 0.0",
        range="-30 30",
        type="hinge",
    )
    back_leg_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.2 -0.2 0.0",
        name="back_leg_geom",
        size="0.08",
        type="capsule",
    )
    body_2 = e.Body(
        pos="-0.2 -0.2 0",
    )
    aux_3.add_children([
        hip_3,
        back_leg_geom,
        body_2,
    ])
    hip_4 = e.Joint(
        axis="0 0 1",
        name="hip_4",
        pos="0.0 0.0 0.0",
        range="-30 30",
        type="hinge",
    )
    rightback_leg_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.2 -0.2 0.0",
        name="rightback_leg_geom",
        size="0.08",
        type="capsule",
    )
    body_3 = e.Body(
        pos="0.2 -0.2 0",
    )
    aux_4.add_children([
        hip_4,
        rightback_leg_geom,
        body_3,
    ])
    ankle_1 = e.Joint(
        axis="-1 1 0",
        name="ankle_1",
        pos="0.0 0.0 0.0",
        range="30 70",
        type="hinge",
    )
    left_ankle_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.4 0.4 0.0",
        name="left_ankle_geom",
        size="0.08",
        type="capsule",
    )
    body.add_children([
        ankle_1,
        left_ankle_geom,
    ])
    ankle_2 = e.Joint(
        axis="1 1 0",
        name="ankle_2",
        pos="0.0 0.0 0.0",
        range="-70 -30",
        type="hinge",
    )
    right_ankle_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.4 0.4 0.0",
        name="right_ankle_geom",
        size="0.08",
        type="capsule",
    )
    body_1.add_children([
        ankle_2,
        right_ankle_geom,
    ])
    ankle_3 = e.Joint(
        axis="-1 1 0",
        name="ankle_3",
        pos="0.0 0.0 0.0",
        range="-70 -30",
        type="hinge",
    )
    third_ankle_geom = e.Geom(
        fromto="0.0 0.0 0.0 -0.4 -0.4 0.0",
        name="third_ankle_geom",
        size="0.08",
        type="capsule",
    )
    body_2.add_children([
        ankle_3,
        third_ankle_geom,
    ])
    ankle_4 = e.Joint(
        axis="1 1 0",
        name="ankle_4",
        pos="0.0 0.0 0.0",
        range="30 70",
        type="hinge",
    )
    fourth_ankle_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.4 -0.4 0.0",
        name="fourth_ankle_geom",
        size="0.08",
        type="capsule",
    )
    body_3.add_children([
        ankle_4,
        fourth_ankle_geom,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('ant_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()