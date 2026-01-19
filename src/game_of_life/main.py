from sim import Sim
from render import Renderer

while(1):
    Renderer.draw(Sim.step())
