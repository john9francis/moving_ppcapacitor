import numpy as np
from matplotlib import pyplot as plt

# my own classes
from plate import Plate

class Capacitor:

  def __init__(self, size_x: float, size_y: float) -> None:
    self.world = np.zeros([size_x,size_y])

    # initialize stuff
    # note: plate list must be a list of Plate objects
    self.plate_list = []


  def add_plate(self, p:Plate):
    self.plate_list.append(p)

    self.add_plate_to_world(p)



  def create_and_add_plate(self, width, height, pos_row, pos_col, charge):
    p = Plate(width, height, pos_row, pos_col, charge)
    self.plate_list.append(p)

    self.add_plate_to_world(p)



  def add_plate_to_world(self, p:Plate):
    self.world[range(p.pos_row, p.pos_row + p.height), range(p.pos_col, p.pos_col + p.width)] = p.charge



  def plot_capacitor(self):
    plt.imshow(self.world, cmap='viridis')
    plt.colorbar()
    plt.show()
    pass


  def relax(self):
    # relaxation method:
    rows, columns =self.world.shape
    difference = 1
    running = True

    # add a safety feature incase it runs forever
    timeout_loops = 1000
    counter = 0

    while running:
      # we assume that it's accurate enough, and check later
      running = False

      for i in range(rows):
        for j in range(columns):

          # otherwise, calculate the avg here
          try:
            avg = .25 * (self.world[i-1,j] +self.world[i+1,j] +self.world[i,j-1] +self.world[i,j+1])
          except IndexError:
            pass
          # difference of the old vs. new value
          difference = abs(avg -self.world[i,j])

          # if ANY of the differences are too big,
          # we are going to keep running.
          if difference > 1e-4:
            running = True


          # reassign this entry to the average.
          self.world[i,j] = avg

          # reassign our edges and plates

          # plates
          for p in self.plate_list:
            self.world[range(p.pos_row, p.pos_row + p.height), range(p.pos_col, p.pos_col + p.width)] = p.charge

          # edges
          self.world[0, :] = 0
          self.world[rows-1, :] = 0
          self.world[:, 0] = 0
          self.world[:, columns-1] = 0


      # for safety, break if it's running too long
      counter += 1
      if counter > timeout_loops:
        print(f"timed out. The minimum difference was {difference}. ")
        break
      
      