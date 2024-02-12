# Get the function I wrote to plot fringe field strength vs. separation distance
from fringe_vs_separation import plot_fringe_vs_separation

# Get my classes from their respective files
from capacitor import Capacitor
from plate import Plate


def main():
  '''
  Shows off what the capacitor class can do
  '''
  # initialize a capacitor with grid size 60 by 60
  cap = Capacitor(60, 60)

  # initialize 2 plate classes. Their parameters are:
  # Plate(width, height, position_y, position_x, charge)
  p1 = Plate(1, 40, 10, 25, -1)
  p2 = Plate(1, 40, 10, 35, 1)

  # add both plates to our capacitor
  cap.add_plate(p1)
  cap.add_plate(p2)

  # run the relaxation method to calculate voltage through the capacitor
  cap.relax()

  # plot voltage heatmaps and electric field vector plot
  cap.plot_voltage()
  cap.plot_voltage3D()
  cap.plot_electric_field()

  # plot the fringe field strength vs. separation
  plot_fringe_vs_separation()


# run main function
if __name__ == "__main__":
  main()