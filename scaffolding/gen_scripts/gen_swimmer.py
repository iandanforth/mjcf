from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="swimmer",
    )
    compiler = e.Compiler(
        angle="degree",
        coordinate="local",
        inertiafromgeom="true",
    )
    option = e.Option(
        collision="predefined",
        density="4000",
        integrator="RK4",
        timestep="0.01",
        viscosity="0.1",
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
    geom = e.Geom(
        conaffinity="1",
        condim="1",
        contype="1",
        material="geom",
        rgba="0.8 0.6 .4 1",
    )
    joint = e.Joint(
        armature="0.1",
    )
    default.add_children([
        geom,
        joint,
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
        pos="0 0 -0.1",
        rgba="0.8 0.9 0.8 1",
        size="40 40 0.1",
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
        gear="150.0",
        joint="rot2",
    )
    motor_1 = e.Motor(
        ctrllimited="true",
        ctrlrange="-1 1",
        gear="150.0",
        joint="rot3",
    )
    actuator.add_children([
        motor,
        motor_1,
    ])
    geom_2 = e.Geom(
        density="1000",
        fromto="1.5 0 0 0.5 0 0",
        size="0.1",
        type="capsule",
    )
    slider1 = e.Joint(
        axis="1 0 0",
        name="slider1",
        pos="0 0 0",
        type="slide",
    )
    slider2 = e.Joint(
        axis="0 1 0",
        name="slider2",
        pos="0 0 0",
        type="slide",
    )
    rot = e.Joint(
        axis="0 0 1",
        name="rot",
        pos="0 0 0",
        type="hinge",
    )
    mid = e.Body(
        name="mid",
        pos="0.5 0 0",
    )
    torso.add_children([
        geom_2,
        slider1,
        slider2,
        rot,
        mid,
    ])
    geom_3 = e.Geom(
        density="1000",
        fromto="0 0 0 -1 0 0",
        size="0.1",
        type="capsule",
    )
    rot2 = e.Joint(
        axis="0 0 1",
        limited="true",
        name="rot2",
        pos="0 0 0",
        range="-100 100",
        type="hinge",
    )
    back = e.Body(
        name="back",
        pos="-1 0 0",
    )
    mid.add_children([
        geom_3,
        rot2,
        back,
    ])
    geom_4 = e.Geom(
        density="1000",
        fromto="0 0 0 -1 0 0",
        size="0.1",
        type="capsule",
    )
    rot3 = e.Joint(
        axis="0 0 1",
        limited="true",
        name="rot3",
        pos="0 0 0",
        range="-100 100",
        type="hinge",
    )
    back.add_children([
        geom_4,
        rot3,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('swimmer_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()