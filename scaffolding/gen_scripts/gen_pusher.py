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
        gravity="0 0 0",
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
        armature="0.04",
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
    table = e.Geom(
        name="table",
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
    object = e.Body(
        name="object",
        pos="0.45 -0.05 -0.275",
    )
    goal = e.Body(
        name="goal",
        pos="0.45 -0.05 -0.3230",
    )
    worldbody.add_children([
        light,
        table,
        r_shoulder_pan_link,
        object,
        goal,
    ])
    motor = e.Motor(
        joint="r_shoulder_pan_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_1 = e.Motor(
        joint="r_shoulder_lift_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_2 = e.Motor(
        joint="r_upper_arm_roll_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_3 = e.Motor(
        joint="r_elbow_flex_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_4 = e.Motor(
        joint="r_forearm_roll_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_5 = e.Motor(
        joint="r_wrist_flex_joint",
        ctrlrange="-2.0 2.0",
        ctrllimited="true",
    )
    motor_6 = e.Motor(
        joint="r_wrist_roll_joint",
        ctrlrange="-2.0 2.0",
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
    )
    e2 = e.Geom(
        name="e2",
        type="sphere",
        rgba="0.6 0.6 0.6 1",
        pos=" 0.06 0.05 0.2",
        size="0.05",
    )
    e1p = e.Geom(
        name="e1p",
        type="sphere",
        rgba="0.1 0.1 0.1 1",
        pos="-0.06 0.09 0.2",
        size="0.03",
    )
    e2p = e.Geom(
        name="e2p",
        type="sphere",
        rgba="0.1 0.1 0.1 1",
        pos=" 0.06 0.09 0.2",
        size="0.03",
    )
    sp = e.Geom(
        name="sp",
        type="capsule",
        fromto="0 0 -0.4 0 0 0.2",
        size="0.1",
    )
    r_shoulder_pan_joint = e.Joint(
        name="r_shoulder_pan_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 0 1",
        range="-2.2854 1.714602",
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
    geom_1 = e.Geom(
        rgba="1 1 1 0",
        type="sphere",
        size="0.05 0.05 0.05",
        density="0.00001",
        conaffinity="0",
    )
    geom_2 = e.Geom(
        rgba="1 1 1 1",
        type="cylinder",
        size="0.05 0.05 0.05",
        density="0.00001",
        contype="1",
        conaffinity="0",
    )
    obj_slidey = e.Joint(
        name="obj_slidey",
        type="slide",
        pos="0 0 0",
        axis="0 1 0",
        range="-10.3213 10.3",
        damping="0.5",
    )
    obj_slidex = e.Joint(
        name="obj_slidex",
        type="slide",
        pos="0 0 0",
        axis="1 0 0",
        range="-10.3213 10.3",
        damping="0.5",
    )
    object.add_children([
        geom_1,
        geom_2,
        obj_slidey,
        obj_slidex,
    ])
    geom_3 = e.Geom(
        rgba="1 0 0 1",
        type="cylinder",
        size="0.08 0.001 0.1",
        density="0.00001",
        contype="0",
        conaffinity="0",
    )
    goal_slidey = e.Joint(
        name="goal_slidey",
        type="slide",
        pos="0 0 0",
        axis="0 1 0",
        range="-10.3213 10.3",
        damping="0.5",
    )
    goal_slidex = e.Joint(
        name="goal_slidex",
        type="slide",
        pos="0 0 0",
        axis="1 0 0",
        range="-10.3213 10.3",
        damping="0.5",
    )
    goal.add_children([
        geom_3,
        goal_slidey,
        goal_slidex,
    ])
    sl = e.Geom(
        name="sl",
        type="capsule",
        fromto="0 -0.1 0 0 0.1 0",
        size="0.1",
    )
    r_shoulder_lift_joint = e.Joint(
        name="r_shoulder_lift_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 1 0",
        range="-0.5236 1.3963",
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
    )
    r_upper_arm_roll_joint = e.Joint(
        name="r_upper_arm_roll_joint",
        type="hinge",
        pos="0 0 0",
        axis="1 0 0",
        range="-1.5 1.7",
        damping="0.1",
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
    )
    r_elbow_flex_joint = e.Joint(
        name="r_elbow_flex_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 1 0",
        range="-2.3213 0",
        damping="0.1",
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
    )
    r_forearm_roll_joint = e.Joint(
        name="r_forearm_roll_joint",
        type="hinge",
        limited="true",
        pos="0 0 0",
        axis="1 0 0",
        damping=".1",
        range="-1.5 1.5",
    )
    r_forearm_link = e.Body(
        name="r_forearm_link",
        pos="0 0 0",
    )
    r_forearm_roll_link.add_children([
        fr,
        r_forearm_roll_joint,
        r_forearm_link,
    ])
    fa = e.Geom(
        name="fa",
        type="capsule",
        fromto="0 0 0 0.291 0 0",
        size="0.05",
    )
    r_wrist_flex_link = e.Body(
        name="r_wrist_flex_link",
        pos="0.321 0 0",
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
    )
    r_wrist_flex_joint = e.Joint(
        name="r_wrist_flex_joint",
        type="hinge",
        pos="0 0 0",
        axis="0 1 0",
        range="-1.094 0",
        damping=".1",
    )
    r_wrist_roll_link = e.Body(
        name="r_wrist_roll_link",
        pos="0 0 0",
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
        axis="1 0 0",
        damping="0.1",
        range="-1.5 1.5",
    )
    tips_arm = e.Body(
        name="tips_arm",
        pos="0 0 0",
    )
    geom_4 = e.Geom(
        type="capsule",
        fromto="0 -0.1 0. 0.0 +0.1 0",
        size="0.02",
        contype="1",
        conaffinity="1",
    )
    geom_5 = e.Geom(
        type="capsule",
        fromto="0 -0.1 0. 0.1 -0.1 0",
        size="0.02",
        contype="1",
        conaffinity="1",
    )
    geom_6 = e.Geom(
        type="capsule",
        fromto="0 +0.1 0. 0.1 +0.1 0.",
        size="0.02",
        contype="1",
        conaffinity="1",
    )
    r_wrist_roll_link.add_children([
        r_wrist_roll_joint,
        tips_arm,
        geom_4,
        geom_5,
        geom_6,
    ])
    tip_arml = e.Geom(
        name="tip_arml",
        type="sphere",
        pos="0.1 -0.1 0.",
        size="0.01",
    )
    tip_armr = e.Geom(
        name="tip_armr",
        type="sphere",
        pos="0.1 0.1 0.",
        size="0.01",
    )
    tips_arm.add_children([
        tip_arml,
        tip_armr,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('pusher_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()