from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
    )
    compiler = e.Compiler(
        angle="degree",
        coordinate="local",
        inertiafromgeom="true",
    )
    option = e.Option(
        integrator="RK4",
        timestep="0.02",
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
        default,
        asset,
        worldbody,
        actuator,
    ])
    joint = e.Joint(
        armature="0",
        damping="0",
        limited="false",
    )
    geom = e.Geom(
        conaffinity="0",
        condim="3",
        density="100",
        friction="1 0.5 0.5",
        margin="0",
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
        texrepeat="30 30",
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
        pos="0 0 0",
    )
    worldbody.add_children([
        light,
        floor,
        torso,
    ])
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-1 1",
        joint="ballx",
    )
    motor_1 = e.Motor(
        ctrllimited="true",
        ctrlrange="-0.25 0.25",
        joint="rot",
    )
    actuator.add_children([
        motor,
        motor_1,
    ])
    pointbody = e.Geom(
        name="pointbody",
        pos="0 0 0.5",
        size="0.5",
        type="sphere",
    )
    pointarrow = e.Geom(
        name="pointarrow",
        pos="0.6 0 0.5",
        size="0.5 0.1 0.1",
        type="box",
    )
    ballx = e.Joint(
        axis="1 0 0",
        name="ballx",
        pos="0 0 0",
        type="slide",
    )
    bally = e.Joint(
        axis="0 1 0",
        name="bally",
        pos="0 0 0",
        type="slide",
    )
    rot = e.Joint(
        axis="0 0 1",
        limited="false",
        name="rot",
        pos="0 0 0",
        type="hinge",
    )
    torso.add_children([
        pointbody,
        pointarrow,
        ballx,
        bally,
        rot,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('point_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()