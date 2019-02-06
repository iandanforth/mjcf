# mjcf
Python Library for MuJoCo Format model xml

Have you ever wanted to generate MuJoCo format
xml files from Python classes? Of course you have! That's why this library
exists. 

For every mjcf element there is now a Python class for you to play with.

## Usage

The following is the contents of `gen_empty.py` which will (re)generate
`empty-gen.xml`. This is an empty checkerboard world, ripe for populating with
creations of your devising!

You can then run that world with

```
python model-viewer.py empty-gen.xml
```

```python
from mjcf import elements as e


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

    mujoco.add_children([
        option,
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

    model_xml = mujoco.xml()

    # Output
    with open('empty-gen.xml', 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()
```

## What is this insanity?

*So these are thin Python class wrapers for XML elements?*

Yup!

*Why?*

Python all the things!

*Ok*

Shutup!
