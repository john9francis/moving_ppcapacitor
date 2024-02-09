import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# my own classes
from plate import Plate

class Capacitor:

  def __init__(self, size_x: float, size_y: float) -> None:
    self.voltage_array = np.zeros([size_x,size_y])
    self.field_array = np.zeros([size_x,size_y])

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
    self.voltage_array[range(p.pos_row, p.pos_row + p.height), range(p.pos_col, p.pos_col + p.width)] = p.charge

  def clear_plates(self):
    self.plate_list.clear()


  def plot_voltage(self):
    plt.imshow(self.voltage_array, cmap='viridis')
    plt.colorbar()
    plt.show()
    pass


  def plot_voltage3D(self):
    x, y = np.meshgrid(np.arange(self.voltage_array.shape[1]), np.arange(self.voltage_array.shape[0]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_surface(x, y, self.voltage_array, cmap=cm.coolwarm)
    ax.view_init(elev = 40, azim = 70)
    ax.set_axis_off()
    plt.show()
    pass

  def plot_electric_field(self):
    '''Plots a quiver plot'''

    # make sure the electric field data is here
    self.create_electric_field()

    x, y = np.meshgrid(np.arange(self.voltage_array.shape[1]), np.arange(self.voltage_array.shape[0]))
    dx, dy = self.field_array

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.quiver(x, y, dx, dy)
    plt.show()



  def relax(self):
    # relaxation method:
    rows, columns = self.voltage_array.shape
    difference = 1
    running = True

    # add a safety feature in case it runs forever
    timeout_loops = 1000
    counter = 0

    while running:
      # we assume that it's accurate enough, and check later
      running = False

      # Calculate averages using array slicing and avoid loops
      avg = 0.25 * (
        np.roll(self.voltage_array, 1, axis=0) +
        np.roll(self.voltage_array, -1, axis=0) +
        np.roll(self.voltage_array, 1, axis=1) +
        np.roll(self.voltage_array, -1, axis=1)
      )

      # Calculate the absolute differences in one go
      differences = np.abs(avg - self.voltage_array)

      # If ANY of the differences are too big, we are going to keep running.
      if np.any(differences > 1e-4):
        running = True

      # Reassign the entries to the average.
      self.voltage_array = avg

      # Reassign our edges and plates

      # Plates
      for p in self.plate_list:
        self.voltage_array[
          p.pos_row : p.pos_row + p.height, p.pos_col : p.pos_col + p.width
        ] = p.charge

      # Edges
      self.voltage_array[0, :] = 0
      self.voltage_array[rows - 1, :] = 0
      self.voltage_array[:, 0] = 0
      self.voltage_array[:, columns - 1] = 0

      # For safety, break if it's running too long
      counter += 1
      if counter > timeout_loops:
        print(f"Timed out. The minimum difference was {np.min(differences)}.")
        break



  def create_electric_field(self):
    '''
    takes the gradient of every point in the voltage data
    '''
    self.field_array = np.gradient(self.voltage_array)
