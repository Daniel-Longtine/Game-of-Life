from random import randint
import config as cg

class Sim:
    def __init__(self, grid, step):
        self.grid = [randint(0,1) for _ in range(cg.height * cg.width * cg.depth)]
    
    def step(self, ):
        new_grid = []
        for cell in range(self.grid.size()):
            ...

    