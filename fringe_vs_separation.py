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
    x_middle = round(world.get_width() / 2)
    y_middle = round(world.get_height() / 2)

    field_at_strongest = world.get_field_array()[y_middle, x_middle]

    field_at_fringe = world.get_field_array()[top_position - 2, x_middle]

    fringe_field.append(field_at_fringe/field_at_strongest)
    distance.append(length * 2)

    print(f"finished plotting distance: {distance[-1]}, field strength: {fringe_field[-1]}")


  # plot
  plt.plot(distance, fringe_field)
  plt.show()

