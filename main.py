# Edges at V=0
# plate 1 at V = +1
# plate 2 at V = -1

import numpy as np

world = np.zeros([10, 10])

plate1_width = 1
plate1_height = 6
plate1_pos_row = 2
plate1_pos_col = 2

plate2_width = 1
plate2_height = 6
plate2_pos_row = 2
plate2_pos_col = 7

world[range(plate1_pos_row, plate1_pos_row + plate1_height), range(plate1_pos_col, plate1_pos_col + plate1_width)] = -1
world[range(plate2_pos_row, plate2_pos_row + plate2_height), range(plate2_pos_col, plate2_pos_col + plate2_width)] = 1
print(world)