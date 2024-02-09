from fringe_vs_separation import plot_fringe_vs_separation
from capacitor import Capacitor
from plate import Plate

world = Capacitor(60, 60)

p1 = Plate(1, 40, 10, 25, -1)
p2 = Plate(1, 40, 10, 35, 1)

world.add_plate(p1)
world.add_plate(p2)

world.relax()
world.plot_voltage()
world.plot_voltage3D()
world.plot_electric_field()


plot_fringe_vs_separation()

