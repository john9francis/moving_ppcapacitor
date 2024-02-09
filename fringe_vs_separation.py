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

  fringe_field = []
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

    fringe_field.append(fringe_field_mag/strong_field_mag)
    distance.append(length * 2)

    print(f"finished plotting distance: {distance[-1]}, field strength: {fringe_field[-1]}")
    #world.plot_electric_field()


  # plot
  plt.plot(distance, fringe_field)
  plt.show()



if __name__ == "__main__":
  plot_fringe_vs_separation()