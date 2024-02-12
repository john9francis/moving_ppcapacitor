import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# my own classes
from plate import Plate

class Capacitor:
  '''
  Creates a grid to measure voltages and electric fields.
  Plate objects with their own voltages can be added.
  Calculates voltage over capacitor using relaxation method
  and the "relax()" function. 
  '''
  def __init__(self, size_x: float, size_y: float) -> None:
    # initialize voltage and electric field arrays of the correct size
    self.voltage_array = np.zeros([size_x,size_y])
    self.field_array = np.zeros([size_x,size_y])

    # a list for the plates. These will not be relaxed during the 
    # relaxation method.
    self.plate_list = []


  def get_width(self):
    rows, columns = self.voltage_array.shape
    return columns

  def get_height(self):
    rows, columns = self.voltage_array.shape
    return rows

  def add_plate(self, p:Plate):
    self.plate_list.append(p)
    self.__add_plate_to_world(p)


  def get_field_array(self):
    return self.field_array


  def create_and_add_plate(self, width, height, pos_row, pos_col, charge):
    '''
    Create a plate object with it's width, height, position and charge
    and add it to capacitor
    '''
    p = Plate(width, height, pos_row, pos_col, charge)
    self.plate_list.append(p)

    self.__add_plate_to_world(p)



  def __add_plate_to_world(self, p:Plate):
    '''
    Private function that takes the plate object and set's the correct
    grid spaces in the capacitor to the voltages of the plate
    '''
    self.voltage_array[range(p.pos_row, p.pos_row + p.height), range(p.pos_col, p.pos_col + p.width)] = p.charge


  def clear_plates(self):
    self.plate_list.clear()


  def reset(self):
    self.voltage_array = np.zeros_like(self.voltage_array)
    self.field_array = np.zeros_like(self.field_array)
    self.plate_list = []



  def plot_voltage(self):
    '''
    Plots the capacitor's voltage as a 2D heatmap
    '''
    plt.imshow(self.voltage_array, cmap='viridis')
    plt.colorbar()
    plt.show()
    pass


  def plot_voltage3D(self):
    '''
    Plots capacitor's voltage in a 3D representation
    '''
    x, y = np.meshgrid(np.arange(self.voltage_array.shape[1]), np.arange(self.voltage_array.shape[0]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_surface(x, y, self.voltage_array, cmap=cm.coolwarm)
    ax.view_init(elev = 40, azim = 70)
    ax.set_axis_off()
    plt.show()
    pass

  def plot_electric_field(self):
    '''Plots a vector plot of the electric field'''

    # Get a basic surface of the correct size to plot
    x, y = np.meshgrid(np.arange(self.voltage_array.shape[1]), np.arange(self.voltage_array.shape[0]))
    
    # Get the electric field at each point from the field_array
    dx, dy = self.field_array

    # quiver plot
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.quiver(x, y, dx, dy)
    plt.show()




  def relax(self):
    # relaxation method:
    rows, columns = self.voltage_array.shape
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


    # finally, create electric field from the new voltage stuff
    self.create_electric_field()



  def create_electric_field(self):
    '''
    Calculates the electric field based on the voltage.
    the electric field is the negative gradient of the voltage.
    saves this data to the self.field array.
    '''
    # note: the np.gradient function returns the y gradient before
    # the x one. For my field array I switched them so x is first. 
    
    dy, dx = np.gradient(self.voltage_array)
    self.field_array = -dx, -dy
