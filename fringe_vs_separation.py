# This file simply houses our plot fringe vs. separation function

import numpy as np
from matplotlib import pyplot as plt
from plate import Plate
from capacitor import Capacitor


def plot_fringe_vs_separation():
  '''
  Plots the fringe field strength vs. the distance
  between plates. 2 plots are generated: 
  1. The absolute fringe field energy
  2. The fringe field energy relative to the energy
     directly between the 2 plates

  note: The fringe field energy is calculated at 5 grid spaces
  above the tops of the plates. 
  '''

  fringe_field_relative = []
  fringe_field_absolute = []
  distances = []
  distance_above_plates = 5

  # iterate over distances between plates
  for distance_i in range(2, 10):

    # create a new capacitor
    cap = Capacitor(60, 60)

    # set a variable for the top position grid space
    top_position = 10

    # create 2 plates
    # note: used the keyword arguments so it was clear what these numbers are setting
    p1 = Plate(width=1, height=40, pos_row=top_position, pos_col=25, charge=-1)
    p2 = Plate(width=1, height=40, pos_row=top_position, pos_col=35, charge=1)

    # set these plates' distance from middle using our iterator
    p1.set_position_from_middle(cap.get_width(), distance_i, True)
    p2.set_position_from_middle(cap.get_width(), distance_i, False)

    # add plates to capacitor
    cap.add_plate(p1)
    cap.add_plate(p2)

    # run the relaxation method
    cap.relax()


    # Calculating the absolute and relative fringe field strengths
    # ____________________________________________________________

    # get the x and y middle grid spaces for our field between the plates
    x_middle = cap.get_width() // 2
    y_middle = cap.get_height() // 2

    # get our "strong field" strength, aka field directly between plates
    strong_field_y = cap.get_field_array()[0][y_middle, x_middle]
    strong_field_x = cap.get_field_array()[1][y_middle, x_middle]

    # get the fringe field strength, using the position above the plates
    fringe_field_y = cap.get_field_array()[0][top_position - distance_above_plates, x_middle]
    fringe_field_x = cap.get_field_array()[1][top_position - distance_above_plates, x_middle]

    # Since the cap.get_field_array function returns a vector (the field is a vector)
    # we need to normalize it to get the magnitude of the field
    strong_field_mag = np.linalg.norm([strong_field_x, strong_field_y])
    fringe_field_mag = np.linalg.norm([fringe_field_x, fringe_field_y])

    # append to our lists so we can graph later
    fringe_field_relative.append(fringe_field_mag/strong_field_mag)
    fringe_field_absolute.append(fringe_field_mag)

    # note: multiply by 2 because this distance is for each capacitor
    # from the middle, but we want to save distance between capacitors
    distances.append(distance_i * 2)



  # plot
  fig = plt.figure(figsize=(10,4))

  # absolute fringe field strength plot
  ax1 = fig.add_subplot(1, 2, 1)
  ax1.set_title("Absolute fringe field magnitude")
  ax1.set_xlabel("distance")
  ax1.set_ylabel("field strength")
  ax1.plot(distances, fringe_field_absolute)

  # relative fringe field strength plot
  ax2 = fig.add_subplot(1, 2, 2)
  ax2.set_title("Relative fringe field magnitude")
  ax2.set_xlabel("distance")
  ax2.set_ylabel("field strength / total field strength")
  ax2.plot(distances, fringe_field_relative)
  plt.show()



if __name__ == "__main__":
  plot_fringe_vs_separation()