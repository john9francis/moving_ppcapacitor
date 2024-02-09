# Edges at V=0
# plate 1 at V = +1
# plate 2 at V = -1

import numpy as np
from matplotlib import pyplot as plt
from plate import Plate
from capacitor import Capacitor

for length in range(0, 25, 10):
  world = Capacitor(60, 60)

  p1 = Plate(1, 40, 10, 25, -1)
  p2 = Plate(1, 40, 10, 35, 1)

  p1.set_position_from_middle(world.get_width(), length, True)
  p2.set_position_from_middle(world.get_width(), length, False)

  world.add_plate(p1)
  world.add_plate(p2)


  world.relax()

  world.plot_voltage3D()
  world.plot_electric_field()



# todo: 
# plot electric field fringe/middle vs. plate distance
