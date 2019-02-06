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
    worldbody = e.Worldbody(
    )
    mujoco.add_children([
        compiler,
        default,
        worldbody,
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
    worldbody.add_children([
        light,
        floor,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('minimal_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()