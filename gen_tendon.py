import os
from mjcf import elements as e


def main():
    #########################
    # Level 1
    mujoco = e.Mujoco(
        model="tendon"
    )

    #########################
    # Level 2
    compiler = e.Compiler(
        coordinate="global",
    )
    default = e.Default()
    visual = e.Visual()
    worldbody = e.Worldbody()
    tendon = e.Tendon()

    mujoco.add_children([
        compiler,
        default,
        visual,
        worldbody,
        tendon
    ])

    ######################
    # Level 3

    # Default
    d_geom = e.Geom(
        rgba=[0.9, 0.7, 0.1, 1],
        size=0.01
    )
    d_site = e.Site(
        type="sphere",
        rgba=[0.9, 0.9, 0.9, 1],
        size=0.005
    )
    d_joint = e.Joint(
        type="hinge",
        axis=[0, 1, 0],
        limited=True,
        range=[0, 60],
        solimplimit=[0.95, 0.95, 0.1]
    )

    default.add_children([
        d_geom,
        d_site,
        d_joint
    ])

    # Visual
    headlight = e.visual.Headlight(
        diffuse=[0.7, 0.7, 0.7]
    )
    visual.add_child(headlight)

    # Worldbody
    b1 = e.Body()
    s2 = e.Site(
        name="s2",
        pos=[-0.03, 0, 0.32]
    )
    b2 = e.Body()
    worldbody.add_children([
        b1,
        s2,
        b2
    ])

    # Tendon
    spatial_tendon = e.Spatial(
        width=0.002,
        rgba=[.95, .3, .3, 1],
        limited=True,
        range=[0, 0.33]
    )
    tendon.add_child(spatial_tendon)

    ######################
    # Level 4

    # b1
    b1_geom = e.Geom(
        type="cylinder",
        fromto=[-0.03, 0, 0.2, -0.03, 0, 0.15],
        size=0.03,
        rgba=[.2, .2, .5, 1],
        density=5000
    )
    b1_joint = e.Joint(
        type="slide",
        pos=[-0.03, 0, 0.2],
        axis=[0, 0, 1],
        limited=False,
    )
    s1 = e.Site(
        name="s1",
        pos=[-0.03, 0, 0.2]
    )
    b1.add_children([
        b1_geom,
        b1_joint,
        s1
    ])

    # b2

    b2_geom_1 = e.Geom(
        type="capsule",
        fromto=[0, 0, 0.3, 0.1, 0, 0.3]
    )
    g1 = e.Geom(
        name="g1",
        type="cylinder",
        fromto=[0.0, 0.015, 0.3, 0.0, -0.015, 0.3],
        size=0.02,
        rgba=[.3, .9, .3, .4]
    )
    b2_joint = e.Joint(
        pos=[0, 0, 0.3]
    )
    s3 = e.Site(
        name="s3",
        pos=[0.02, 0, 0.32],
        size=None
    )
    b3 = e.Body()
    b2.add_children([
        b2_geom_1,
        g1,
        b2_joint,
        s3,
        b3
    ])

    # spatial_tendon
    ss1 = e.spatial.Site(site="s1")
    ss2 = e.spatial.Site(site="s2")
    sg1 = e.spatial.Geom(geom="g1")
    ss3 = e.spatial.Site(site="s3")
    sp1 = e.spatial.Pulley(divisor=2)
    sg2 = e.spatial.Geom(geom="g2", sidesite="side2")
    ss4 = e.spatial.Site(site="s4")
    sp2 = e.spatial.Pulley(divisor=2)
    ss5 = e.spatial.Site(site="s5")
    sg3 = e.spatial.Geom(geom="g3", sidesite="side3")
    ss6 = e.spatial.Site(site="s6")

    spatial_tendon.add_children([
        ss1,
        ss2,
        sg1,
        ss3,
        sp1,
        ss3,
        sg2,
        ss4,
        sp2,
        ss3,
        sg2,
        ss5,
        sg3,
        ss6
    ])

    ######################
    # Level 5

    # b3

    b3_geom_1 = e.Geom(
        type="capsule",
        fromto=[0.1, 0, 0.3, 0.2, 0, 0.3]
    )
    g2 = e.Geom(
        name="g2",
        type="cylinder",
        fromto=[0.1, 0.015, 0.3, 0.1, -0.015, 0.3],
        size=0.02,
        rgba=[.3, .9, .3, .4]
    )
    b3_joint = e.Joint(
        pos=[0.1, 0, 0.3]
    )
    s4 = e.Site(
        name="s4",
        pos=[0.13, 0, 0.31],
        size=None
    )
    s5 = e.Site(
        name="s5",
        pos=[0.15, 0, 0.32]
    )
    side2 = e.Site(
        name="side2",
        pos=[0.1, 0, 0.33]
    )
    b4 = e.Body()

    b3.add_children([
        b3_geom_1,
        g2,
        b3_joint,
        s4,
        s5,
        side2,
        b4
    ])

    ######################
    # Level 6

    # b4

    b4_geom_1 = e.Geom(
        type="capsule",
        fromto=[0.2, 0, 0.3, 0.27, 0, 0.3]
    )
    g3 = e.Geom(
        name="g3",
        type="cylinder",
        fromto=[0.2, 0.015, 0.3, 0.2, -0.015, 0.3],
        size=0.02,
        rgba=[.3, .9, .3, .4]
    )
    b4_joint = e.Joint(
        pos=[0.2, 0, 0.3]
    )
    s6 = e.Site(
        name="s6",
        pos=[0.23, 0, 0.31]
    )
    side3 = e.Site(
        name="side3",
        pos=[0.2, 0, 0.33]
    )

    b4.add_children([
        b4_geom_1,
        g3,
        b4_joint,
        s6,
        side3
    ])
    model_xml = mujoco.xml()

    # Output
    outpath = os.path.join('tendon-gen.xml')
    with open(outpath, 'w') as fh:
        fh.write(model_xml)


if __name__ == '__main__':
    main()
