class Plate:
  '''
  Basically holds information about a plate like
  width, height, and position so that the capacitor 
  class can know how to set voltage in it's grid.
  '''

  def __init__(self, width=1, height=5, pos_row=2, pos_col=2, charge=1) -> None:
    '''
    Default plate with width 1, height 5, as position 2,2 and charge 1
    '''
    self.width = width
    self.height = height
    self.pos_row = pos_row
    self.pos_col = pos_col
    self.charge = charge
    pass

  
  # Functions to set the plate position relative to the capacitor

  def set_position_from_middle(self, capacitor_width, distance_from_middle, to_the_left=True):
    '''
    Takes in capacitor width, desired plate distance from middle, and if we want
    the plate to the left or right of the middle. Then sets the plate's
    position accordingly.
    '''
    if to_the_left:
      self.pos_col = round(capacitor_width / 2 - distance_from_middle)
    else:
      self.pos_col = round(capacitor_width / 2 + distance_from_middle)
    pass