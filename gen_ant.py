import os
from mjcf.generated import elements as e
import math


def rotate(point, angle, origin=[0, 0]):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.

    Source: https://stackoverflow.com/a/34374437/1775741
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def gen_world():
    world = {
        "mujoco": {
            "worldbody": {
                "light": {
                    "@cutoff": "100",
                    "@diffuse": "1 1 1",
                    "@dir": "-0 0 -1.3",
                    "@directional": "true",
                    "@exponent": "1",
                    "@pos": "0 0 1.3",
                    "@specular": ".1 .1 .1"
                },
                "geom": {
                    "@conaffinity": "1",
                    "@condim": "3",
                    "@material": "MatPlane",
                    "@name": "floor",
                    "@pos": "0 0 0",
                    "@rgba": "0.8 0.9 0.8 1",
                    "@size": "20 20 .125",
                    "@type": "plane"
                },
                "body": {
                    "@name": "ball",
                    "@pos": "0.0 0.0 1.0",
                    "joint": [
                        {
                            "@name": "ball_joint",
                            "@pos": "0.0 0.0 0.2",
                            "@type": "ball",
                            "@damping": "2.0"
                        },
                        {
                            "@type": "slide",
                            "@axis": "0 0 1",
                            "@damping": "2.0"
                        },
                        {
                            "@type": "slide",
                            "@axis": "0 1 0",
                            "@damping": "2.0"
                        },
                        {
                            "@type": "slide",
                            "@axis": "1 0 0",
                            "@damping": "2.0"
                        }
                    ],
                    "geom": {
                        "@pos": "0.0 0.0 0.0",
                        "@size": "0.2",
                        "@type": "sphere"
                    }
                }
            },
            "asset": {
                "texture": [
                    {
                        "@builtin": "gradient",
                        "@height": "100",
                        "@rgb1": ".4 .5 .6",
                        "@rgb2": "0 0 0",
                        "@type": "skybox",
                        "@width": "100"
                    },
                    {
                        "@builtin": "checker",
                        "@height": "100",
                        "@name": "texplane",
                        "@rgb1": "0 0 0",
                        "@rgb2": "0.8 0.8 0.8",
                        "@type": "2d",
                        "@width": "100"
                    }
                ],
                "material": {
                    "@name": "MatPlane",
                    "@reflectance": "0.5",
                    "@shininess": "1",
                    "@specular": "1",
                    "@texrepeat": "60 60",
                    "@texture": "texplane"
                }
            }
        }
    }

    return world


def get_leg(
    name, 
    hip_distance=0.2,
    hip_angle=0.0,
    leg_length=0.2,
    foot_length=0.4):
    x_y_string = " ".join([str(_) for _ in hip_start_x_y])
    hip_from_to_template = "0.0 0.0 0.0 {}"
    pos_template = "{} 0".format(x_y_string)
    pos = pos_template.format(x_y_string)
    from_to = hip_from_to_template.format(pos)
    leg = e.Body(name=name, pos="0 0 0")

    aux_geom = e.Geom(
        fromto=from_to,
        name="aux_geom_"+name,
        size="0.08",
        type="capsule"
    )
    aux_body = e.Body(
        name="aux_body_"+name,
        pos=pos
    )
    leg.add_children([
        aux_geom,
        aux_body
    ])

    # Body
    hip_joint = e.Joint(
        axis="0 0 1",
        name="hip_joint_"+name,
        pos="0.0 0.0 0.0",
        range="-30 30",
        type="hinge"
    )
    leg_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.2 0.2 0.0",
        name="leg_geom_"+name,
        size="0.08",
        type="capsule"
    )
    ankle_body = e.Body(
        name="ankle_body_"+name,
        pos="0.2 0.2 0"
    )
    aux_body.add_children([
        hip_joint,
        leg_geom,
        ankle_body
    ])

    # Body
    ankle_joint = e.Joint(
        axis="-1 1 0",
        name="ankle_joint_"+name,
        pos="0.0 0.0 0.0",
        range="30 70",
        type="hinge"
    )
    ankle_geom = e.Geom(
        fromto="0.0 0.0 0.0 0.4 0.4 0.0",
        name="ankle_geom_"+name,
        size="0.08",
        type="capsule"
    )
    ankle_body.add_children([ankle_joint, ankle_geom])

    # Actuators
    hip = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint=hip_joint.name,
        gear="150"
    )
    ankle = e.Motor(
        ctrllimited="true",
        ctrlrange="-1.0 1.0",
        joint=ankle_joint.name,
        gear="150"
    )

    return leg, hip, ankle


def main():
    # filepath = os.path.join('assets', 'minimal.xml')
    # with open(filepath, 'r') as fh:
    #     raw = fh.read()
    # markup = parse(raw)
    # jason = json.dumps(markup, indent=4)

    # world_dict = gen_world()
    # world_markup = unparse(world_dict, pretty=True)

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
        inertiafromgeom="true"
    )
    option = e.Option(
        integrator="RK4",
        timestep="0.01"
    )
    custom = e.Custom()
    default = e.Default()
    asset = e.Asset()
    worldbody = e.Body() # TODO: Return to worldbody
    actuator = e.Actuator()

    mujoco.add_children([
        compiler,
        option,
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
        armature="1",
        damping="1",
        limited="true"
    )
    d_geom = e.Geom(
        conaffinity="0",
        condim="3",
        density="5.0",
        friction="1 0.5 0.5",
        margin="0.01",
        rgba="0.8 0.6 0.4 1"
    )
    default.add_children([d_joint, d_geom])

    # Asset
    tex1 = e.Texture(
        builtin="gradient",
        height="100",
        rgb1="1 1 1",
        rgb2="0 0 0",
        type="skybox",
        width="100"
    )
    tex2 = e.Texture(
        builtin="flat",
        height="1278",
        mark="cross",
        markrgb="1 1 1",
        name="texgeom",
        random="0.01",
        rgb1="0.8 0.6 0.4",
        rgb2="0.8 0.6 0.4",
        type="cube",
        width="127"
    )
    tex3 = e.Texture(
        builtin="checker",
        height="100",
        name="texplane",
        rgb1="0 0 0",
        rgb2="0.8 0.8 0.8",
        type="2d",
        width="100"
    )
    mat1 = e.Material(
        name="MatPlane",
        reflectance="0.5",
        shininess="1", specular="1",
        texrepeat="60 60",
        texture="texplane"
    )
    mat2 = e.Material(
        name="geom",
        texture="texgeom",
        texuniform="true"
    )
    asset.add_children([
        tex1,
        tex2,
        tex3,
        mat1,
        mat2,
    ])

    # # Worldbody
    # light = e.Light(
    #     cutoff="100",
    #     diffuse="1 1 1",
    #     dir="-0 0 -1.3",
    #     directional="true",
    #     exponent="1",
    #     pos="0 0 1.3",
    #     specular=".1 .1 .1"
    # )
    # floor_geom = e.Geom(
    #     conaffinity="1",
    #     condim="3",
    #     material="MatPlane",
    #     name="floor",
    #     pos="0 0 0",
    #     rgba="0.8 0.9 0.8 1",
    #     size="40 40 40",
    #     type="plane"
    # )
    # torso = e.Body(name="torso", pos="0 0 0.75")
    # worldbody.add_children([
    #     light,
    #     floor_geom,
    #     torso
    # ])


    # # Torso
    # camera = e.Camera(
    #     name="track",
    #     mode="trackcom",
    #     pos="0 -3 0.3",
    #     xyaxes="1 0 0 0 0 1"
    # )
    # torso_geom = e.Geom(
    #     name="torso_geom",
    #     pos="0 0 0",
    #     size="0.25",
    #     type="sphere"
    # )
    # joint = e.Joint(
    #     armature="0",
    #     damping="0",
    #     limited="false",
    #     margin="0.01",
    #     name="root",
    #     pos="0 0 0",
    #     type="free"
    # )
    # front_left_leg, fl_hip, fl_ankle = get_leg("front_left_leg", hip_start_x_y=[0.2, 0.2])
    # front_right_leg, fr_hip, fr_ankle = get_leg("front_right_leg", hip_start_x_y=[-0.2, 0.2])
    # # back_left_leg = get_leg("back_left_leg")
    # # back_right_leg = get_leg("back_right_leg")
    # torso.add_children([
    #     camera,
    #     torso_geom,
    #     joint,
    #     front_left_leg,
    #     front_right_leg,
    #     # back_left_leg,
    #     # back_right_leg
    # ])

    # # Actuator
    # actuator.add_children([
    #     fl_hip,
    #     fl_ankle,
    #     fr_hip,
    #     fr_ankle,
    #     # hip_3,
    #     # ankle_3,
    #     # hip_4,
    #     # ankle_4
    # ])

    model_xml = mujoco.xml()

    # Output
    outpath = os.path.join('ant-gen.xml')
    with open(outpath, 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()
