from Rectangle import Rectangle

class Surface:
  def __init__(self, Rectangle, x, y, height, width):
    self.rect = Rectangle(x ,y ,height ,width)
    #self.image = 

  def getRect(self):
    return self.rec