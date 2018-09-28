from mjcf import elements as e
from random import random, uniform
from colors import get_rgb, viridis


def get_cubes():
    square_count = 10
    colorscale = viridis
    colorscale.reverse()
    cubes = []
    for i in range(square_count):
        for j in range(square_count):
            x = i + random()
            y = j + random()
            min_side = 0.1
            max_side = 0.5
            side_range = max_side - min_side
            side = uniform(min_side, max_side)
            z = side * 2
            color_point = (side - min_side) / side_range
            rgb = get_rgb(colorscale, color_point)
            alpha = 1 - (color_point / 10)
            rgba = rgb + [alpha]
            cube = get_cube(x, y, z, side, rgba)
            cubes.append(cube)

    return cubes


def get_cube(x=0, y=0, z=1, size=0.2, rgba=[0.5, 0.5, 0.5, 1]):

    body = e.Body(
        pos=[x, y, z]
    )
    freejoint = e.Freejoint()
    geom = e.Geom(
        type="box",
        size=[size, size, size],
        rgba=rgba
    )

    body.add_children([
        freejoint,
        geom
    ])

    return body


def main():
    #########################
    # Level 1
    mujoco = e.Mujoco(
        model="empty"
    )

    #########################
    # Level 2
    option = e.Option(
        integrator="RK4",
        timestep=0.01
    )
    asset = e.Asset()
    worldbody = e.Worldbody()

    size = e.Size(
        njmax=4000,
        nconmax=4000,
    )

    mujoco.add_children([
        option,
        size,
        asset,
        worldbody
    ])

    ######################
    # Level 3

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

    worldbody.add_children([
        light,
        floor_geom,
    ])

    cubes = get_cubes()
    worldbody.add_children(cubes)

    model_xml = mujoco.xml()

    # Output
    with open('terrain-gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()
