from random import randint
import config as cg

class Sim:
    def __init__(self, grid, step):
        self.grid = [randint(0,1) for _ in range(cg.height * cg.width * cg.depth)]
    
    def step(self, ):
        grid_num_neighbors = [0 for _ in range(cg.height * cg.width * cg.depth)]
        grid_deltas = [ # this is just a list of each surrounding cell's math for the 1D grid array
            -1, 1, -cg.width, cg.width, 
            -cg.width - 1, -cg.width + 1, cg.width - 1, cg.width + 1, # 8 directly surrounding in the current slice
            -cg.height*cg.height, -cg.height*cg.height - 1, -cg.height*cg.height +1,
            -cg.height*cg.height + cg.width, -cg.height*cg.height + cg.width - 1, -cg.height*cg.height + cg.width + 1,
            -cg.height*cg.height - cg.width, -cg.height*cg.height - cg.width - 1, -cg.height*cg.height - cg.width + 1,
            cg.height*cg.height, cg.height*cg.height - 1, cg.height*cg.height +1,
            cg.height*cg.height + cg.width, cg.height*cg.height + cg.width - 1, cg.height*cg.height + cg.width + 1,
            cg.height*cg.height - cg.width, cg.height*cg.height - cg.width - 1, cg.height*cg.height - cg.width + 1, 
        ]
        for cell in range(self.grid.size()):
            if self.grid[cell] != 0:
                for delta in grid_deltas:
                    self.grid[cell + delta] += 1
        
        next_grid = [0] * self.grid.size()
        for cell in range(self.grid.size()):
            if self.grid[cell] == 0 and grid_num_neighbors[cell] >= cg.birth:
                next_grid[cell] = 1
            elif self.grid[cell] == 1 and grid_num_neighbors[cell] >= cg.survive:
                next_grid[cell] = 1
            else: 
                next_grid[cell] = 0
        
        self.grid = next_grid
        return self.grid