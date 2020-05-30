class Cars:
  def __init__(self, num_of_wheels, color, make, model):
    self.num_of_wheels = num_of_wheels
    self.color = color
    self.make = make
    self.model = model

  def move(self):
      print("moving at 50mph")

  def Break(self):
      print("stoping ... stopped")


  def accelerate(self):
      print("increasing speed.... vroom , vroom ")
