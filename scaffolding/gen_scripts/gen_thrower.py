from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="arm3d",
    )
    compiler = e.Compiler(
        inertiafromgeom="true",
        angle="radian",
        coordinate="local",
    )
    option = e.Option(
        timestep="0.01",
        gravity="0 0 -9.81",
        iterations="20",
        integrator="Euler",
    )
    default = e.Default(
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        option,
        default,
        worldbody,
        actuator,
    ])
    joint = e.Joint(
        armature="0.75",
        damping="1",
        limited="true",
    )
    geom = e.Geom(
        friction=".8 .1 .1",
        density="300",
        margin="0.002",
        condim="1",
        contype="0",
        conaffinity="0",
    )
    default.add_children([
        joint,
        geom,
    ])
    light = e.Light(
        diffuse=".5 .5 .5",
        pos="0 0 3",
        dir="0 0 -1",
    )
    geom_1 = e.Geom(
        type="plane",
        pos="0 0.5 -0.325",
        size="1 1 0.1",
        contype="1",
        conaffinity="1",
    )
    r_shoulder_pan_link = e.Body(
        name="r_shoulder_pan_link",
        pos="0 -0.6 0",
    )
    goal = e.Body(
        name="goal",
        pos="0.575 0.5 -0.328",
    )
    ball = e.Body(
        name="ball",
        pos="0.5 -0.8 0.275",
    )
    worldbody.add_children([
        light,
        geom_1,
        r_shoulder_pan_link,
        goal,
        ball,
    ])
    motor = e.Motor(
        joint="r_shoulder_pan_joint",
        ctrlrange="-10.0 10.0",
        ctrllimited="true",
    )
    motor_1 = e.Motor(
        joint="r_shoulder_lift_joint",
        ctrlrange="-10.0 10.0",
        ctrllimited="true",
    )
    motor_2 = e.Motor(
        joint="r_upper_arm_roll_joint",
        ctrlrange="-10.0 10.0",
        ctrllimited="true",
    )
    motor_3 = e.Motor(
        joint="r_elbow_flex_joint",
        ctrlrange="-10.0 10.0",
        ctrllimited="true",
    )
    motor_4 = e.Motor(
        joint="r_forearm_roll_joint",
        ctrlrange="-15.0 15.0",
        ctrllimited="true",
    )
    motor_5 = e.Motor(
        joint="r_wrist_flex_joint",
        ctrlrange="-15.0 15.0",
        ctrllimited="true",
    )
    motor_6 = e.Motor(
        joint="r_wrist_roll_joint",
        ctrlrange="-15.0 15.0",
        ctrllimited="true",
    )
    actuator.add_children([
        motor,
        motor_1,
        motor_2,
        motor_3,
        motor_4,
        motor_5,
        motor_6,
    ])
    e1 = e.Geom(
        name="e1",
        type="sphere",
        rgba="0.6 0.6 0.6 1",
        pos="-0.06 0.05 0.2",
        size="0.05",
        density="0.0001",
    )
    e2 = e.Geom(
        name="e2",
        type="sphere",
        rgba="0.6 0.6 0.6 1",
        pos=" 0.06 0.05 0.2",
        size="0.05",
        density="0.0001",
    )
    e1p = e.Geom(
        name="e1p",
        type="sphere",
        rgba="0.1 0.1 0.1 1",
        pos="-0.06 0.09 0.2",
        size="0.03",
        density="0.0001",
    )
    e2p = e.Geom(
        name="e2p",
        type="sphere",
        rgba="0.1 0.1 0.1 1",
        pos=" 0.06 0.09 0.2",
        size="0.03",
        density="0.0001",
    )
    sp = e.Geom(
        name="sp",
        type="capsule",
        fromto="0 0 -0.4 0 0 0.2",
        size="0.1",
        density="1",
    )
    r_shoulder_pan_joint = e.Joint(
        name="r_shoulder_pan_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 0 1",
        range="-0.4854 1.214602",
        damping="1.0",
    )
    r_shoulder_lift_link = e.Body(
        name="r_shoulder_lift_link",
        pos="0.1 0 0",
    )
    r_shoulder_pan_link.add_children([
        e1,
        e2,
        e1p,
        e2p,
        sp,
        r_shoulder_pan_joint,
        r_shoulder_lift_link,
    ])
    geom_2 = e.Geom(
        rgba="1 1 1 1",
        type="box",
        pos="0 0 0.005",
        size="0.075 0.075 0.001",
        contype="1",
        conaffinity="1",
        density="1000",
    )
    geom_3 = e.Geom(
        rgba="1 1 1 1",
        type="box",
        pos="0.0 0.075 0.034",
        size="0.075 0.001 0.03",
        contype="1",
        conaffinity="0",
    )
    geom_4 = e.Geom(
        rgba="1 1 1 1",
        type="box",
        pos="0.0 -0.075 0.034",
        size="0.075 0.001 0.03",
        contype="1",
        conaffinity="0",
    )
    geom_5 = e.Geom(
        rgba="1 1 1 1",
        type="box",
        pos="0.075 0 0.034",
        size="0.001 0.075 0.03",
        contype="1",
        conaffinity="0",
    )
    geom_6 = e.Geom(
        rgba="1 1 1 1",
        type="box",
        pos="-0.076 0 0.034",
        size="0.001 0.075 0.03",
        contype="1",
        conaffinity="0",
    )
    geom_7 = e.Geom(
        rgba="1 1 1 1",
        type="capsule",
        fromto="0.073 0.073 0.0075 0.073 0.073 0.06",
        size="0.005",
        contype="1",
        conaffinity="0",
    )
    geom_8 = e.Geom(
        rgba="1 1 1 1",
        type="capsule",
        fromto="0.073 -0.073 0.0075 0.073 -0.073 0.06",
        size="0.005",
        contype="1",
        conaffinity="0",
    )
    geom_9 = e.Geom(
        rgba="1 1 1 1",
        type="capsule",
        fromto="-0.073 0.073 0.0075 -0.073 0.073 0.06",
        size="0.005",
        contype="1",
        conaffinity="0",
    )
    geom_10 = e.Geom(
        rgba="1 1 1 1",
        type="capsule",
        fromto="-0.073 -0.073 0.0075 -0.073 -0.073 0.06",
        size="0.005",
        contype="1",
        conaffinity="0",
    )
    goal_slidey = e.Joint(
        name="goal_slidey",
        type="slide",
        pos="0 0 0",
        axis="0 1 0",
        range="-10.3213 10.3",
        damping="1.0",
    )
    goal_slidex = e.Joint(
        name="goal_slidex",
        type="slide",
        pos="0 0 0",
        axis="1 0 0",
        range="-10.3213 10.3",
        damping="1.0",
    )
    goal.add_children([
        geom_2,
        geom_3,
        geom_4,
        geom_5,
        geom_6,
        geom_7,
        geom_8,
        geom_9,
        geom_10,
        goal_slidey,
        goal_slidex,
    ])
    geom_11 = e.Geom(
        rgba="1. 1. 1. 1",
        type="sphere",
        size="0.03 0.03 0.1",
        density="25",
        contype="1",
        conaffinity="1",
    )
    ball_free = e.Joint(
        name="ball_free",
        type="free",
        armature="0",
        damping="0",
        limited="false",
    )
    ball.add_children([
        geom_11,
        ball_free,
    ])
    sl = e.Geom(
        name="sl",
        type="capsule",
        fromto="0 -0.1 0 0 0.1 0",
        size="0.1",
        density="0.0001",
    )
    r_shoulder_lift_joint = e.Joint(
        name="r_shoulder_lift_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 1 0",
        range="-0.5236 0.7963",
        damping="1.0",
    )
    r_upper_arm_roll_link = e.Body(
        name="r_upper_arm_roll_link",
        pos="0 0 0",
    )
    r_shoulder_lift_link.add_children([
        sl,
        r_shoulder_lift_joint,
        r_upper_arm_roll_link,
    ])
    uar = e.Geom(
        name="uar",
        type="capsule",
        fromto="-0.1 0 0 0.1 0 0",
        size="0.02",
        density="0.0001",
    )
    r_upper_arm_roll_joint = e.Joint(
        name="r_upper_arm_roll_joint",
        type="hinge",
        pos="0 0 0",
        axis="1 0 0",
        range="-1.5 1.7",
        damping="1.0",
    )
    r_upper_arm_link = e.Body(
        name="r_upper_arm_link",
        pos="0 0 0",
    )
    r_upper_arm_roll_link.add_children([
        uar,
        r_upper_arm_roll_joint,
        r_upper_arm_link,
    ])
    ua = e.Geom(
        name="ua",
        type="capsule",
        fromto="0 0 0 0.4 0 0",
        size="0.06",
        density="0.0001",
    )
    r_elbow_flex_link = e.Body(
        name="r_elbow_flex_link",
        pos="0.4 0 0",
    )
    r_upper_arm_link.add_children([
        ua,
        r_elbow_flex_link,
    ])
    ef = e.Geom(
        name="ef",
        type="capsule",
        fromto="0 -0.02 0 0.0 0.02 0",
        size="0.06",
        density="0.0001",
    )
    r_elbow_flex_joint = e.Joint(
        name="r_elbow_flex_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 1 0",
        range="-0.7 0.7",
        damping="1.0",
    )
    r_forearm_roll_link = e.Body(
        name="r_forearm_roll_link",
        pos="0 0 0",
    )
    r_elbow_flex_link.add_children([
        ef,
        r_elbow_flex_joint,
        r_forearm_roll_link,
    ])
    fr = e.Geom(
        name="fr",
        type="capsule",
        fromto="-0.1 0 0 0.1 0 0",
        size="0.02",
        density="0.0001",
    )
    r_forearm_roll_joint = e.Joint(
        name="r_forearm_roll_joint",
        type="hinge",
        limited="true",
        pos="0 0 0",
        axis="1 0 0",
        damping="1.0",
        range="-1.5 1.5",
    )
    r_forearm_link = e.Body(
        name="r_forearm_link",
        pos="0 0 0",
        axisangle="1 0 0 0.392",
    )
    r_forearm_roll_link.add_children([
        fr,
        r_forearm_roll_joint,
        r_forearm_link,
    ])
    fa = e.Geom(
        name="fa",
        type="capsule",
        fromto="0 0 0 0 0 0.291",
        size="0.05",
        density="0.0001",
    )
    r_wrist_flex_link = e.Body(
        name="r_wrist_flex_link",
        pos="0 0 0.321",
        axisangle="0 0 1 1.57",
    )
    r_forearm_link.add_children([
        fa,
        r_wrist_flex_link,
    ])
    wf = e.Geom(
        name="wf",
        type="capsule",
        fromto="0 -0.02 0 0 0.02 0",
        size="0.01",
        density="0.0001",
    )
    r_wrist_flex_joint = e.Joint(
        name="r_wrist_flex_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 0 1",
        range="-1.0 1.0",
        damping="1.0",
    )
    r_wrist_roll_link = e.Body(
        name="r_wrist_roll_link",
        pos="0 0 0",
        axisangle="0 1 0 -1.178",
    )
    r_wrist_flex_link.add_children([
        wf,
        r_wrist_flex_joint,
        r_wrist_roll_link,
    ])
    r_wrist_roll_joint = e.Joint(
        name="r_wrist_roll_joint",
        type="hinge",
        pos="0 0 0",
        limited="true",
        axis="0 1 0",
        damping="1.0",
        range="0 2.25",
    )
    geom_12 = e.Geom(
        type="capsule",
        fromto="0 -0.05 0 0 0.05 0",
        size="0.01",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 0.392",
    )
    body_1 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 1.57",
    )
    body_2 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 1.178",
    )
    body_3 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 0.785",
    )
    body_4 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 1.96",
    )
    body_5 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 2.355",
    )
    body_6 = e.Body(
        pos="0 0 0",
        axisangle="0 0 1 2.74",
    )
    r_wrist_roll_link.add_children([
        r_wrist_roll_joint,
        geom_12,
        body,
        body_1,
        body_2,
        body_3,
        body_4,
        body_5,
        body_6,
    ])
    geom_13 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_14 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density=".0001",
    )
    geom_15 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body.add_children([
        geom_13,
        geom_14,
        geom_15,
    ])
    geom_16 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_17 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_18 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_1.add_children([
        geom_16,
        geom_17,
        geom_18,
    ])
    geom_19 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_20 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_21 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_2.add_children([
        geom_19,
        geom_20,
        geom_21,
    ])
    geom_22 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_23 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_24 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_3.add_children([
        geom_22,
        geom_23,
        geom_24,
    ])
    geom_25 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_26 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_27 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_4.add_children([
        geom_25,
        geom_26,
        geom_27,
    ])
    geom_28 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_29 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_30 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_5.add_children([
        geom_28,
        geom_29,
        geom_30,
    ])
    geom_31 = e.Geom(
        type="capsule",
        fromto="0 0.025 0 0 0.075 0.075",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_32 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.075 0 0.075 0.15",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    geom_33 = e.Geom(
        type="capsule",
        fromto="0 0.075 0.15 0 0 0.225",
        size="0.005",
        contype="1",
        conaffinity="1",
        density="0.0001",
    )
    body_6.add_children([
        geom_31,
        geom_32,
        geom_33,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('thrower_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()