from fringe_vs_separation import plot_fringe_vs_separation
from capacitor import Capacitor
from plate import Plate


def main():
  '''
  Shows off what the capacitor class can do
  '''
  cap = Capacitor(60, 60)

  p1 = Plate(1, 40, 10, 25, -1)
  p2 = Plate(1, 40, 10, 35, 1)

  cap.add_plate(p1)
  cap.add_plate(p2)

  cap.relax()
  cap.plot_voltage()
  cap.plot_voltage3D()
  cap.plot_electric_field()


  plot_fringe_vs_separation()



if __name__ == "__main__":
  main()