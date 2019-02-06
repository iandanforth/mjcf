from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="humanoid",
    )
    compiler = e.Compiler(
        angle="degree",
        inertiafromgeom="true",
    )
    default = e.Default(
    )
    option = e.Option(
        integrator="RK4",
        iterations="50",
        solver="PGS",
        timestep="0.003",
    )
    size = e.Size(
        nkey="5",
        nuser_geom="1",
    )
    visual = e.Visual(
    )
    asset = e.Asset(
    )
    worldbody = e.Worldbody(
    )
    tendon = e.Tendon(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        default,
        option,
        size,
        visual,
        asset,
        worldbody,
        tendon,
        actuator,
    ])
    joint = e.Joint(
        armature="1",
        damping="1",
        limited="true",
    )
    geom = e.Geom(
        conaffinity="1",
        condim="1",
        contype="1",
        margin="0.001",
        material="geom",
        rgba="0.8 0.6 .4 1",
    )
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-.4 .4",
    )
    default.add_children([
        joint,
        geom,
        motor,
    ])
    map = e.Map(
        fogend="5",
        fogstart="3",
    )
    visual.add_children([
        map,
    ])
    texture = e.Texture(
        builtin="gradient",
        height="100",
        rgb1=".4 .5 .6",
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
        condim="3",
        friction="1 .1 .1",
        material="MatPlane",
        name="floor",
        pos="0 0 0",
        rgba="0.8 0.9 0.8 1",
        size="20 20 0.125",
        type="plane",
    )
    torso = e.Body(
        name="torso",
        pos="0 0 1.4",
    )
    worldbody.add_children([
        light,
        floor,
        torso,
    ])
    left_hipknee = e.Fixed(
        name="left_hipknee",
    )
    right_hipknee = e.Fixed(
        name="right_hipknee",
    )
    tendon.add_children([
        left_hipknee,
        right_hipknee,
    ])
    abdomen_y = e.Motor(
        gear="100",
        joint="abdomen_y",
        name="abdomen_y",
    )
    abdomen_z = e.Motor(
        gear="100",
        joint="abdomen_z",
        name="abdomen_z",
    )
    abdomen_x = e.Motor(
        gear="100",
        joint="abdomen_x",
        name="abdomen_x",
    )
    right_hip_x = e.Motor(
        gear="100",
        joint="right_hip_x",
        name="right_hip_x",
    )
    right_hip_z = e.Motor(
        gear="100",
        joint="right_hip_z",
        name="right_hip_z",
    )
    right_hip_y = e.Motor(
        gear="300",
        joint="right_hip_y",
        name="right_hip_y",
    )
    right_knee = e.Motor(
        gear="200",
        joint="right_knee",
        name="right_knee",
    )
    left_hip_x = e.Motor(
        gear="100",
        joint="left_hip_x",
        name="left_hip_x",
    )
    left_hip_z = e.Motor(
        gear="100",
        joint="left_hip_z",
        name="left_hip_z",
    )
    left_hip_y = e.Motor(
        gear="300",
        joint="left_hip_y",
        name="left_hip_y",
    )
    left_knee = e.Motor(
        gear="200",
        joint="left_knee",
        name="left_knee",
    )
    right_shoulder1 = e.Motor(
        gear="25",
        joint="right_shoulder1",
        name="right_shoulder1",
    )
    right_shoulder2 = e.Motor(
        gear="25",
        joint="right_shoulder2",
        name="right_shoulder2",
    )
    right_elbow = e.Motor(
        gear="25",
        joint="right_elbow",
        name="right_elbow",
    )
    left_shoulder1 = e.Motor(
        gear="25",
        joint="left_shoulder1",
        name="left_shoulder1",
    )
    left_shoulder2 = e.Motor(
        gear="25",
        joint="left_shoulder2",
        name="left_shoulder2",
    )
    left_elbow = e.Motor(
        gear="25",
        joint="left_elbow",
        name="left_elbow",
    )
    actuator.add_children([
        abdomen_y,
        abdomen_z,
        abdomen_x,
        right_hip_x,
        right_hip_z,
        right_hip_y,
        right_knee,
        left_hip_x,
        left_hip_z,
        left_hip_y,
        left_knee,
        right_shoulder1,
        right_shoulder2,
        right_elbow,
        left_shoulder1,
        left_shoulder2,
        left_elbow,
    ])
    track = e.Camera(
        name="track",
        mode="trackcom",
        pos="0 -4 0",
        xyaxes="1 0 0 0 0 1",
    )
    root = e.Joint(
        armature="0",
        damping="0",
        limited="false",
        name="root",
        pos="0 0 0",
        stiffness="0",
        type="free",
    )
    torso1 = e.Geom(
        fromto="0 -.07 0 0 .07 0",
        name="torso1",
        size="0.07",
        type="capsule",
    )
    head = e.Geom(
        name="head",
        pos="0 0 .19",
        size=".09",
        type="sphere",
        user="258",
    )
    uwaist = e.Geom(
        fromto="-.01 -.06 -.12 -.01 .06 -.12",
        name="uwaist",
        size="0.06",
        type="capsule",
    )
    lwaist = e.Body(
        name="lwaist",
        pos="-.01 0 -0.260",
        quat="1.000 0 -0.002 0",
    )
    right_upper_arm = e.Body(
        name="right_upper_arm",
        pos="0 -0.17 0.06",
    )
    left_upper_arm = e.Body(
        name="left_upper_arm",
        pos="0 0.17 0.06",
    )
    torso.add_children([
        track,
        root,
        torso1,
        head,
        uwaist,
        lwaist,
        right_upper_arm,
        left_upper_arm,
    ])
    joint_1 = e.Joint(
        coef="-1",
        joint="left_hip_y",
    )
    joint_2 = e.Joint(
        coef="1",
        joint="left_knee",
    )
    left_hipknee.add_children([
        joint_1,
        joint_2,
    ])
    joint_3 = e.Joint(
        coef="-1",
        joint="right_hip_y",
    )
    joint_4 = e.Joint(
        coef="1",
        joint="right_knee",
    )
    right_hipknee.add_children([
        joint_3,
        joint_4,
    ])
    lwaist_1 = e.Geom(
        fromto="0 -.06 0 0 .06 0",
        name="lwaist",
        size="0.06",
        type="capsule",
    )
    abdomen_z_1 = e.Joint(
        armature="0.02",
        axis="0 0 1",
        damping="5",
        name="abdomen_z",
        pos="0 0 0.065",
        range="-45 45",
        stiffness="20",
        type="hinge",
    )
    abdomen_y_1 = e.Joint(
        armature="0.02",
        axis="0 1 0",
        damping="5",
        name="abdomen_y",
        pos="0 0 0.065",
        range="-75 30",
        stiffness="10",
        type="hinge",
    )
    pelvis = e.Body(
        name="pelvis",
        pos="0 0 -0.165",
        quat="1.000 0 -0.002 0",
    )
    lwaist.add_children([
        lwaist_1,
        abdomen_z_1,
        abdomen_y_1,
        pelvis,
    ])
    right_shoulder1_1 = e.Joint(
        armature="0.0068",
        axis="2 1 1",
        name="right_shoulder1",
        pos="0 0 0",
        range="-85 60",
        stiffness="1",
        type="hinge",
    )
    right_shoulder2_1 = e.Joint(
        armature="0.0051",
        axis="0 -1 1",
        name="right_shoulder2",
        pos="0 0 0",
        range="-85 60",
        stiffness="1",
        type="hinge",
    )
    right_uarm1 = e.Geom(
        fromto="0 0 0 .16 -.16 -.16",
        name="right_uarm1",
        size="0.04 0.16",
        type="capsule",
    )
    right_lower_arm = e.Body(
        name="right_lower_arm",
        pos=".18 -.18 -.18",
    )
    right_upper_arm.add_children([
        right_shoulder1_1,
        right_shoulder2_1,
        right_uarm1,
        right_lower_arm,
    ])
    left_shoulder1_1 = e.Joint(
        armature="0.0068",
        axis="2 -1 1",
        name="left_shoulder1",
        pos="0 0 0",
        range="-60 85",
        stiffness="1",
        type="hinge",
    )
    left_shoulder2_1 = e.Joint(
        armature="0.0051",
        axis="0 1 1",
        name="left_shoulder2",
        pos="0 0 0",
        range="-60 85",
        stiffness="1",
        type="hinge",
    )
    left_uarm1 = e.Geom(
        fromto="0 0 0 .16 .16 -.16",
        name="left_uarm1",
        size="0.04 0.16",
        type="capsule",
    )
    left_lower_arm = e.Body(
        name="left_lower_arm",
        pos=".18 .18 -.18",
    )
    left_upper_arm.add_children([
        left_shoulder1_1,
        left_shoulder2_1,
        left_uarm1,
        left_lower_arm,
    ])
    abdomen_x_1 = e.Joint(
        armature="0.02",
        axis="1 0 0",
        damping="5",
        name="abdomen_x",
        pos="0 0 0.1",
        range="-35 35",
        stiffness="10",
        type="hinge",
    )
    butt = e.Geom(
        fromto="-.02 -.07 0 -.02 .07 0",
        name="butt",
        size="0.09",
        type="capsule",
    )
    right_thigh = e.Body(
        name="right_thigh",
        pos="0 -0.1 -0.04",
    )
    left_thigh = e.Body(
        name="left_thigh",
        pos="0 0.1 -0.04",
    )
    pelvis.add_children([
        abdomen_x_1,
        butt,
        right_thigh,
        left_thigh,
    ])
    right_elbow_1 = e.Joint(
        armature="0.0028",
        axis="0 -1 1",
        name="right_elbow",
        pos="0 0 0",
        range="-90 50",
        stiffness="0",
        type="hinge",
    )
    right_larm = e.Geom(
        fromto="0.01 0.01 0.01 .17 .17 .17",
        name="right_larm",
        size="0.031",
        type="capsule",
    )
    right_hand = e.Geom(
        name="right_hand",
        pos=".18 .18 .18",
        size="0.04",
        type="sphere",
    )
    camera = e.Camera(
        pos="0 0 0",
    )
    right_lower_arm.add_children([
        right_elbow_1,
        right_larm,
        right_hand,
        camera,
    ])
    left_elbow_1 = e.Joint(
        armature="0.0028",
        axis="0 -1 -1",
        name="left_elbow",
        pos="0 0 0",
        range="-90 50",
        stiffness="0",
        type="hinge",
    )
    left_larm = e.Geom(
        fromto="0.01 -0.01 0.01 .17 -.17 .17",
        name="left_larm",
        size="0.031",
        type="capsule",
    )
    left_hand = e.Geom(
        name="left_hand",
        pos=".18 -.18 .18",
        size="0.04",
        type="sphere",
    )
    left_lower_arm.add_children([
        left_elbow_1,
        left_larm,
        left_hand,
    ])
    right_hip_x_1 = e.Joint(
        armature="0.01",
        axis="1 0 0",
        damping="5",
        name="right_hip_x",
        pos="0 0 0",
        range="-25 5",
        stiffness="10",
        type="hinge",
    )
    right_hip_z_1 = e.Joint(
        armature="0.01",
        axis="0 0 1",
        damping="5",
        name="right_hip_z",
        pos="0 0 0",
        range="-60 35",
        stiffness="10",
        type="hinge",
    )
    right_hip_y_1 = e.Joint(
        armature="0.0080",
        axis="0 1 0",
        damping="5",
        name="right_hip_y",
        pos="0 0 0",
        range="-110 20",
        stiffness="20",
        type="hinge",
    )
    right_thigh1 = e.Geom(
        fromto="0 0 0 0 0.01 -.34",
        name="right_thigh1",
        size="0.06",
        type="capsule",
    )
    right_shin = e.Body(
        name="right_shin",
        pos="0 0.01 -0.403",
    )
    right_thigh.add_children([
        right_hip_x_1,
        right_hip_z_1,
        right_hip_y_1,
        right_thigh1,
        right_shin,
    ])
    left_hip_x_1 = e.Joint(
        armature="0.01",
        axis="-1 0 0",
        damping="5",
        name="left_hip_x",
        pos="0 0 0",
        range="-25 5",
        stiffness="10",
        type="hinge",
    )
    left_hip_z_1 = e.Joint(
        armature="0.01",
        axis="0 0 -1",
        damping="5",
        name="left_hip_z",
        pos="0 0 0",
        range="-60 35",
        stiffness="10",
        type="hinge",
    )
    left_hip_y_1 = e.Joint(
        armature="0.01",
        axis="0 1 0",
        damping="5",
        name="left_hip_y",
        pos="0 0 0",
        range="-120 20",
        stiffness="20",
        type="hinge",
    )
    left_thigh1 = e.Geom(
        fromto="0 0 0 0 -0.01 -.34",
        name="left_thigh1",
        size="0.06",
        type="capsule",
    )
    left_shin = e.Body(
        name="left_shin",
        pos="0 -0.01 -0.403",
    )
    left_thigh.add_children([
        left_hip_x_1,
        left_hip_z_1,
        left_hip_y_1,
        left_thigh1,
        left_shin,
    ])
    right_knee_1 = e.Joint(
        armature="0.0060",
        axis="0 -1 0",
        name="right_knee",
        pos="0 0 .02",
        range="-160 -2",
        type="hinge",
    )
    right_shin1 = e.Geom(
        fromto="0 0 0 0 0 -.3",
        name="right_shin1",
        size="0.049",
        type="capsule",
    )
    right_foot = e.Body(
        name="right_foot",
        pos="0 0 -0.45",
    )
    right_shin.add_children([
        right_knee_1,
        right_shin1,
        right_foot,
    ])
    left_knee_1 = e.Joint(
        armature="0.0060",
        axis="0 -1 0",
        name="left_knee",
        pos="0 0 .02",
        range="-160 -2",
        stiffness="1",
        type="hinge",
    )
    left_shin1 = e.Geom(
        fromto="0 0 0 0 0 -.3",
        name="left_shin1",
        size="0.049",
        type="capsule",
    )
    left_foot = e.Body(
        name="left_foot",
        pos="0 0 -0.45",
    )
    left_shin.add_children([
        left_knee_1,
        left_shin1,
        left_foot,
    ])
    right_foot_1 = e.Geom(
        name="right_foot",
        pos="0 0 0.1",
        size="0.075",
        type="sphere",
        user="0",
    )
    right_foot.add_children([
        right_foot_1,
    ])
    left_foot_1 = e.Geom(
        name="left_foot",
        type="sphere",
        size="0.075",
        pos="0 0 0.1",
        user="0",
    )
    left_foot.add_children([
        left_foot_1,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('humanoid_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()