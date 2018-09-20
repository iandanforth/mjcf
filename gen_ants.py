from mjcf import elements as e


def get_ant(name="ant1", location=[0, 0, 0.75]):

    torso = e.Body(
        name="torso_"+name,
        pos=location,
    )

    # Torso
    camera = e.Camera(
        name="track_"+name,
        mode="trackcom",
        pos=[0, -3, 0.3],
        xyaxes=[1, 0, 0, 0, 0, 1]
    )
    torso_geom = e.Geom(
        name="torso_geom_"+name,
        pos=[0, 0, 0],
        size=0.25,
        type="sphere",
        rgba=None
    )
    joint = e.Joint(
        armature=0,
        damping=0,
        limited=False,
        margin=0.01,
        name="root_"+name,
        pos=[0, 0, 0],
        type="free"
    )
    front_right_leg, fr_hip, fr_ankle = get_leg(
        "front_right_leg_"+name
    )
    front_left_leg, fl_hip, fl_ankle = get_leg(
        "front_left_leg_"+name,
        hip_angle=90,
    )
    back_left_leg, bl_hip, bl_ankle = get_leg(
        "back_left_leg_"+name,
        hip_angle=180,
    )
    back_right_leg, br_hip, br_ankle = get_leg(
        "back_right_leg_"+name,
        hip_angle=270,
    )
    torso.add_children([
        camera,
        torso_geom,
        joint,
        front_right_leg,
        front_left_leg,
        back_left_leg,
        back_right_leg
    ])

    actuators = [
        fr_hip,
        fr_ankle,
        fl_hip,
        fl_ankle,
        bl_hip,
        bl_ankle,
        br_hip,
        br_ankle
    ]

    return torso, actuators

def get_leg(
    name,
    hip_distance=0.2,
    hip_angle=0.0,
    leg_length=0.4,
    foot_length=0.6
):
    leg = e.Body(
        name=name,
        pos=[0, 0, 0],
        euler=[0, 0, hip_angle]
    )

    aux_geom = e.Geom(
        fromto=[0, 0, 0, hip_distance, 0, 0],
        name="aux_geom_"+name,
        size=0.08,
        type="capsule"
    )
    aux_body = e.Body(
        name="aux_body_"+name,
        pos=[hip_distance, 0, 0]
    )
    leg.add_children([
        aux_geom,
        aux_body
    ])

    # Body
    hip_joint = e.Joint(
        axis=[0, 0, 1],
        name="hip_joint_"+name,
        pos=[0.0, 0.0, 0.0],
        range=[-30, 30],
        type="hinge"
    )
    leg_geom = e.Geom(
        fromto=[0.0, 0.0, 0.0, leg_length, 0.0, 0.0],
        name="leg_geom_"+name,
        size=0.08,
        type="capsule"
    )
    ankle_body = e.Body(
        name="ankle_body_"+name,
        pos=[leg_length, 0.0, 0]
    )
    aux_body.add_children([
        hip_joint,
        leg_geom,
        ankle_body
    ])

    # Body
    ankle_joint = e.Joint(
        axis=[0, 1, 0],
        name="ankle_joint_"+name,
        pos=[0.0, 0.0, 0.0],
        range=[30, 70],
        type="hinge"
    )
    ankle_geom = e.Geom(
        fromto=[0.0, 0.0, 0.0, foot_length, 0.0, 0.0],
        name="ankle_geom_"+name,
        size=0.08,
        type="capsule"
    )
    ankle_body.add_children([ankle_joint, ankle_geom])

    # Actuators
    hip = e.Motor(
        ctrllimited="true",
        ctrlrange=[-1.0, 1.0],
        joint=hip_joint.name,
        gear=150
    )
    ankle = e.Motor(
        ctrllimited=True,
        ctrlrange=[-1.0, 1.0],
        joint=ankle_joint.name,
        gear=150
    )

    return leg, hip, ankle


def main():
    #########################
    # Level 1
    mujoco = e.Mujoco(
        model="ant"
    )

    #########################
    # Level 2
    compiler = e.Compiler(
        angle="degree",
        coordinate="local",
        inertiafromgeom=True
    )
    option = e.Option(
        integrator="RK4",
        timestep=0.01
    )
    size = e.Size(
        njmax=1000,
        nconmax=500,
    )
    custom = e.Custom()
    default = e.Default()
    asset = e.Asset()
    worldbody = e.Worldbody()
    actuator = e.Actuator()

    mujoco.add_children([
        compiler,
        option,
        size,
        custom,
        default,
        asset,
        worldbody,
        actuator
    ])

    ######################
    # Level 3

    # Custom
    numeric = e.Numeric(
        name="init_qpos",
        data="0.0 0.0 0.55 1.0 0.0 0.0 0.0 0.0 1.0 0.0 -1.0 0.0 -1.0 0.0 1.0",
    )
    custom.add_child(numeric)

    # Default
    d_joint = e.Joint(
        armature=1,
        damping=1,
        limited=True
    )
    d_geom = e.Geom(
        conaffinity=0,
        condim=3,
        density=5.0,
        friction=[1, 0.5, 0.5],
        margin=0.01,
        rgba=[0.8, 0.6, 0.4, 1]
    )
    default.add_children([d_joint, d_geom])

    # Asset
    tex1 = e.Texture(
        builtin="gradient",
        height=100,
        rgb1=[1, 1, 1],
        rgb2=[0, 0, 0],
        type="skybox",
        width=100
    )
    tex2 = e.Texture(
        builtin="flat",
        height=1278,
        mark="cross",
        markrgb=[1, 1, 1],
        name="texgeom",
        random=0.01,
        rgb1=[0.8, 0.6, 0.4],
        rgb2=[0.8, 0.6, 0.4],
        type="cube",
        width=127
    )
    tex3 = e.Texture(
        builtin="checker",
        height=[100],
        name="texplane",
        rgb1=[0, 0, 0],
        rgb2=[0.8, 0.8, 0.8],
        type="2d",
        width=100
    )
    mat1 = e.Material(
        name="MatPlane",
        reflectance=0.5,
        shininess=1,
        specular=1,
        texrepeat=[60, 60],
        texture="texplane"
    )
    mat2 = e.Material(
        name="geom",
        texture="texgeom",
        texuniform=True
    )
    asset.add_children([
        tex1,
        tex2,
        tex3,
        mat1,
        mat2,
    ])

    # Worldbody
    light = e.Light(
        cutoff=100,
        diffuse=[1, 1, 1],
        dir=[-0, 0, -1.3],
        directional=True,
        exponent=1,
        pos=[0, 0, 1.3],
        specular=[.1, .1, .1]
    )
    floor_geom = e.Geom(
        conaffinity=1,
        condim=3,
        material="MatPlane",
        name="floor",
        pos=[0, 0, 0],
        rgba=[0.8, 0.9, 0.8, 1],
        size=[40, 40, 40],
        type="plane"
    )

    ant1, ant1_actuators = get_ant()
    ant2, ant2_actuators = get_ant(name="ant2", location=[0.0, 2.0, 0.75])
    worldbody.add_children([
        light,
        floor_geom
    ])

    ant_bodies = []
    ant_actuators = []
    for i in range(7):
        for j in range(7):
            name = "ant_{}_{}".format(i, j)
            y_offset = 2.0 * i
            x_offset = 2.0 * j
            body, actuators = get_ant(name=name, location=[x_offset, y_offset, 0.75])
            ant_bodies.append(body)
            ant_actuators.extend(actuators)

    worldbody.add_children(ant_bodies)

    # Actuator
    actuator.add_children(ant_actuators)

    model_xml = mujoco.xml()

    # Output
    with open('ants-gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()
