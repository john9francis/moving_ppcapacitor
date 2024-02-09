class Plate:
  def __init__(self, width=1, height=5, pos_row=2, pos_col=2, charge=1) -> None:
    self.width = width
    self.height = height
    self.pos_row = pos_row
    self.pos_col = pos_col
    self.charge = charge
    pass


  # to do: 
  # add different constructors to calculate position in different ways
  # e.g. distance from center

  def set_position_from_middle(self, width, distance_from_middle, to_the_left=True):
    if to_the_left:
      self.pos_col = round(width / 2 - distance_from_middle)
    else:
      self.pos_col = round(width / 2 + distance_from_middle)
    pass