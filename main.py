# Edges at V=0
# plate 1 at V = +1
# plate 2 at V = -1

import numpy as np
from matplotlib import pyplot as plt

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


#print(world)
# plot
plt.imshow(world, cmap='viridis')
plt.colorbar()
plt.show()


# relaxation method:
rows, columns = world.shape
difference = 1
running = True

#while running:
for i in range(10):
  # we assume that it's accurate enough, and check later
  running = False

  for i in range(rows):
    for j in range(columns):
        
      # otherwise, calculate the avg here
      try:
        avg = .25 * (world[i-1,j] + world[i+1,j] + world[i,j-1] + world[i,j+1])
      except IndexError:
        pass
      # difference of the old vs. new value
      difference = abs(avg - world[i,j])

      # if ANY of the differences are too big,
      # we are going to keep running.
      if difference > 1e-4:
        running = True


      # reassign this entry to the average.
      world[i,j] = avg

      # reassign our edges and capacitors
      
      # capacitors
      world[range(plate1_pos_row, plate1_pos_row + plate1_height), range(plate1_pos_col, plate1_pos_col + plate1_width)] = -1
      world[range(plate2_pos_row, plate2_pos_row + plate2_height), range(plate2_pos_col, plate2_pos_col + plate2_width)] = 1

      # edges
      world[0, :] = 0
      world[rows-1, :] = 0
      world[:, 0] = 0
      world[:, columns-1] = 0



#print(world)
# plot again
plt.imshow(world, cmap='viridis')
plt.colorbar()
plt.show()