from mujoco_py import load_model_from_path, MjSim, MjViewer
import sys

model_path = sys.argv[1]
model = load_model_from_path(model_path)
sim = MjSim(model)
viewer = MjViewer(sim)

for i in range(15000):
    sim.step()
    viewer.render()
