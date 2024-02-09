# file to house a function
import numpy as np
from matplotlib import pyplot as plt
from plate import Plate
from capacitor import Capacitor


def plot_fringe_vs_separation():
  '''
  Plots the fringe field strength vs. the distance
  between plates
  '''

  fringe_field_relative = []
  fringe_field_absolute = []
  distance = []
  distance_above_plates = 5

  for length in range(2, 10):
    world = Capacitor(60, 60)

    top_position = 10

    p1 = Plate(1, 40, top_position, 25, -1)
    p2 = Plate(1, 40, top_position, 35, 1)

    p1.set_position_from_middle(world.get_width(), length, True)
    p2.set_position_from_middle(world.get_width(), length, False)

    world.add_plate(p1)
    world.add_plate(p2)

    world.relax()


    # now, calculate the fringe divided by total 
    x_middle = world.get_width() // 2
    y_middle = world.get_height() // 2

    print(f"x: {x_middle}, y: {y_middle}")
    strong_field_y = world.get_field_array()[0][y_middle, x_middle]
    strong_field_x = world.get_field_array()[1][y_middle, x_middle]

    fringe_field_y = world.get_field_array()[0][top_position - distance_above_plates, x_middle]
    fringe_field_x = world.get_field_array()[1][top_position - distance_above_plates, x_middle]

    strong_field_mag = np.linalg.norm([strong_field_x, strong_field_y])
    fringe_field_mag = np.linalg.norm([fringe_field_x, fringe_field_y])

    fringe_field_relative.append(fringe_field_mag/strong_field_mag)
    fringe_field_absolute.append(fringe_field_mag)
    distance.append(length * 2)



  # plot
  fig = plt.figure(figsize=(10,4))

  ax1 = fig.add_subplot(1, 2, 1)
  ax1.set_title("Absolute fringe field magnitude")
  ax1.set_xlabel("distance")
  ax1.set_ylabel("field strength")
  ax1.plot(distance, fringe_field_absolute)

  ax2 = fig.add_subplot(1, 2, 2)
  ax2.set_title("Relative fringe field magnitude")
  ax2.set_xlabel("distance")
  ax2.set_ylabel("field strength / total field strength")
  ax2.plot(distance, fringe_field_relative)
  plt.show()



if __name__ == "__main__":
  plot_fringe_vs_separation()