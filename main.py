# Edges at V=0
# plate 1 at V = +1
# plate 2 at V = -1

import numpy as np
from matplotlib import pyplot as plt
from plate import Plate
from capacitor import Capacitor

world = Capacitor(10, 10)

p1 = Plate(1, 6, 2, 2, -1)
p2 = Plate(1, 6, 2, 7, 1)


world.add_plate(p1)
world.add_plate(p2)

world.plot_capacitor3D()

world.relax()

world.plot_capacitor3D()
