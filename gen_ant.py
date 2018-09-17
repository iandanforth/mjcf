from mjcf.generated import elements as e


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


def get_leg(name):
    leg = e.Body(name=name)
    aux_geom = e.Geom()
    aux_body = e.Body()
    leg.add_children([
        aux_geom,
        aux_body
    ])

    hip_joint = e.Joint()
    leg_geom = e.Geom()
    ankle_body = e.Body()
    aux_body.add_children([
        hip_joint,
        leg_geom,
        ankle_body
    ])

    ankle_joint = e.Joint()
    ankle_geom = e.Geom()
    ankle_body.add_children([ankle_joint, ankle_geom])

    return leg

def main():
    # filepath = os.path.join('assets', 'minimal.xml')
    # with open(filepath, 'r') as fh:
    #     raw = fh.read()
    # markup = parse(raw)
    # jason = json.dumps(markup, indent=4)

    # world_dict = gen_world()
    # world_markup = unparse(world_dict, pretty=True)

    # # Output
    # outpath = os.path.join('minimal-gen.xml')
    # with open(outpath, 'w') as fh:
    #     fh.write(world_markup)

    #########################
    # Level 1
    mujoco = e.Mujoco()

    #########################
    # Level 2
    compiler = e.Compiler()
    option = e.Option()
    custom = e.Custom()
    default = e.Default()
    asset = e.Asset()
    worldbody = e.Worldbody()
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
    numeric = e.Numeric()
    custom.add_child(numeric)

    # Default
    d_joint = e.Joint()
    d_geom = e.Geom()
    default.add_children([d_joint, d_geom])

    # Asset
    tex1 = e.Texture()
    tex2 = e.Texture()
    tex3 = e.Texture()
    mat1 = e.Material()
    mat2 = e.Material()
    asset.add_children([
        tex1,
        tex2,
        tex3,
        mat1,
        mat2,
    ])

    # Worldbody
    light = e.Light()
    floor_geom = e.Geom()
    torso = e.Body()
    worldbody.add_children([
        light,
        floor_geom,
        torso
    ])

    # Actuator
    hip_1 = e.Motor()
    ankle_1 = e.Motor()
    hip_2 = e.Motor()
    ankle_2 = e.Motor()
    hip_3 = e.Motor()
    ankle_3 = e.Motor()
    hip_4 = e.Motor()
    ankle_4 = e.Motor()
    actuator.add_children([
        hip_1,
        ankle_1,
        hip_2,
        ankle_2,
        hip_3,
        ankle_3,
        hip_4,
        ankle_4
    ])

    ######################
    # Level 4

    # Torso
    camera = e.Camera()
    torso_geom = e.Geom()
    joint = e.Joint()
    front_left_leg = get_leg("front_left_leg")
    front_right_leg = get_leg("front_right_leg")
    back_left_leg = get_leg("back_left_leg")
    back_right_leg = get_leg("back_right_leg")
    torso.add_children([
        camera,
        torso_geom,
        joint,
        front_left_leg,
        front_right_leg,
        back_left_leg,
        back_right_leg
    ])

    model_xml = mujoco.xml()
    print(model_xml)


if __name__ == '__main__':
    main()
