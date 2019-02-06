from mjcf import elements as e


def main():

    mujoco = e.Mujoco(
        model="cheetah",
    )
    compiler = e.Compiler(
        angle="radian",
        coordinate="local",
        inertiafromgeom="true",
        settotalmass="14",
    )
    default = e.Default(
    )
    size = e.Size(
        nstack="300000",
        nuser_geom="1",
    )
    option = e.Option(
        gravity="0 0 -9.81",
        timestep="0.01",
    )
    asset = e.Asset(
    )
    worldbody = e.Worldbody(
    )
    actuator = e.Actuator(
    )
    mujoco.add_children([
        compiler,
        default,
        size,
        option,
        asset,
        worldbody,
        actuator,
    ])
    joint = e.Joint(
        armature=".1",
        damping=".01",
        limited="true",
        solimplimit="0 .8 .03",
        solreflimit=".02 1",
        stiffness="8",
    )
    geom = e.Geom(
        conaffinity="0",
        condim="3",
        contype="1",
        friction=".4 .1 .1",
        rgba="0.8 0.6 .4 1",
        solimp="0.0 0.8 0.01",
        solref="0.02 1",
    )
    motor = e.Motor(
        ctrllimited="true",
        ctrlrange="-1 1",
    )
    default.add_children([
        joint,
        geom,
        motor,
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
        pos="0 0 .7",
    )
    worldbody.add_children([
        light,
        floor,
        torso,
    ])
    bthigh = e.Motor(
        gear="120",
        joint="bthigh",
        name="bthigh",
    )
    bshin = e.Motor(
        gear="90",
        joint="bshin",
        name="bshin",
    )
    bfoot = e.Motor(
        gear="60",
        joint="bfoot",
        name="bfoot",
    )
    fthigh = e.Motor(
        gear="120",
        joint="fthigh",
        name="fthigh",
    )
    fshin = e.Motor(
        gear="60",
        joint="fshin",
        name="fshin",
    )
    ffoot = e.Motor(
        gear="30",
        joint="ffoot",
        name="ffoot",
    )
    actuator.add_children([
        bthigh,
        bshin,
        bfoot,
        fthigh,
        fshin,
        ffoot,
    ])
    track = e.Camera(
        name="track",
        mode="trackcom",
        pos="0 -3 0.3",
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
        stiffness="0",
        type="slide",
    )
    rooty = e.Joint(
        armature="0",
        axis="0 1 0",
        damping="0",
        limited="false",
        name="rooty",
        pos="0 0 0",
        stiffness="0",
        type="hinge",
    )
    torso_1 = e.Geom(
        fromto="-.5 0 0 .5 0 0",
        name="torso",
        size="0.046",
        type="capsule",
    )
    head = e.Geom(
        axisangle="0 1 0 .87",
        name="head",
        pos=".6 0 .1",
        size="0.046 .15",
        type="capsule",
    )
    bthigh_1 = e.Body(
        name="bthigh",
        pos="-.5 0 0",
    )
    fthigh_1 = e.Body(
        name="fthigh",
        pos=".5 0 0",
    )
    torso.add_children([
        track,
        rootx,
        rootz,
        rooty,
        torso_1,
        head,
        bthigh_1,
        fthigh_1,
    ])
    bthigh_2 = e.Joint(
        axis="0 1 0",
        damping="6",
        name="bthigh",
        pos="0 0 0",
        range="-.52 1.05",
        stiffness="240",
        type="hinge",
    )
    bthigh_3 = e.Geom(
        axisangle="0 1 0 -3.8",
        name="bthigh",
        pos=".1 0 -.13",
        size="0.046 .145",
        type="capsule",
    )
    bshin_1 = e.Body(
        name="bshin",
        pos=".16 0 -.25",
    )
    bthigh_1.add_children([
        bthigh_2,
        bthigh_3,
        bshin_1,
    ])
    fthigh_2 = e.Joint(
        axis="0 1 0",
        damping="4.5",
        name="fthigh",
        pos="0 0 0",
        range="-1 .7",
        stiffness="180",
        type="hinge",
    )
    fthigh_3 = e.Geom(
        axisangle="0 1 0 .52",
        name="fthigh",
        pos="-.07 0 -.12",
        size="0.046 .133",
        type="capsule",
    )
    fshin_1 = e.Body(
        name="fshin",
        pos="-.14 0 -.24",
    )
    fthigh_1.add_children([
        fthigh_2,
        fthigh_3,
        fshin_1,
    ])
    bshin_2 = e.Joint(
        axis="0 1 0",
        damping="4.5",
        name="bshin",
        pos="0 0 0",
        range="-.785 .785",
        stiffness="180",
        type="hinge",
    )
    bshin_3 = e.Geom(
        axisangle="0 1 0 -2.03",
        name="bshin",
        pos="-.14 0 -.07",
        rgba="0.9 0.6 0.6 1",
        size="0.046 .15",
        type="capsule",
    )
    bfoot_1 = e.Body(
        name="bfoot",
        pos="-.28 0 -.14",
    )
    bshin_1.add_children([
        bshin_2,
        bshin_3,
        bfoot_1,
    ])
    fshin_2 = e.Joint(
        axis="0 1 0",
        damping="3",
        name="fshin",
        pos="0 0 0",
        range="-1.2 .87",
        stiffness="120",
        type="hinge",
    )
    fshin_3 = e.Geom(
        axisangle="0 1 0 -.6",
        name="fshin",
        pos=".065 0 -.09",
        rgba="0.9 0.6 0.6 1",
        size="0.046 .106",
        type="capsule",
    )
    ffoot_1 = e.Body(
        name="ffoot",
        pos=".13 0 -.18",
    )
    fshin_1.add_children([
        fshin_2,
        fshin_3,
        ffoot_1,
    ])
    bfoot_2 = e.Joint(
        axis="0 1 0",
        damping="3",
        name="bfoot",
        pos="0 0 0",
        range="-.4 .785",
        stiffness="120",
        type="hinge",
    )
    bfoot_3 = e.Geom(
        axisangle="0 1 0 -.27",
        name="bfoot",
        pos=".03 0 -.097",
        rgba="0.9 0.6 0.6 1",
        size="0.046 .094",
        type="capsule",
    )
    bfoot_1.add_children([
        bfoot_2,
        bfoot_3,
    ])
    ffoot_2 = e.Joint(
        axis="0 1 0",
        damping="1.5",
        name="ffoot",
        pos="0 0 0",
        range="-.5 .5",
        stiffness="60",
        type="hinge",
    )
    ffoot_3 = e.Geom(
        axisangle="0 1 0 -.6",
        name="ffoot",
        pos=".045 0 -.07",
        rgba="0.9 0.6 0.6 1",
        size="0.046 .07",
        type="capsule",
    )
    ffoot_1.add_children([
        ffoot_2,
        ffoot_3,
    ])

    model_xml = mujoco.xml()

    # Output
    with open('half_cheetah_gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()