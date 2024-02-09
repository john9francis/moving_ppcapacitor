# Edges at V=0
# plate 1 at V = +1
# plate 2 at V = -1

import numpy as np
from matplotlib import pyplot as plt
from plate import Plate
from capacitor import Capacitor

world = Capacitor(100, 100)

p1 = Plate(1, 60, 20, 20, -1)
p2 = Plate(1, 60, 20, 80, 1)


world.add_plate(p1)
world.add_plate(p2)


world.relax()

world.plot_voltage()
world.plot_electric_field()
