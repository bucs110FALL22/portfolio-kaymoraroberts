class Rectangle: 
    def __init__(self,x, y, height, width):
      if x < 0:
        self.x = 0 
      else:
        self.x = x
      print(self.x)
      
      if y < 0: 
        self.y = 0 
      else:
        self.y = y 
      print(self.y)
    
      if height < 0:
        self.height = 0
      else:
        self.height = height
      print(self.height)

      if width < 0:
        self.width = 0 
      else:
        self.width = width
      print(self.width)


    def __str__ (self):
      return 'Rectangle(x:' + str(self.x) + ',y:' + str(self.y) +')' + ',height:' + str(self.height) + ' width:' + str(self.width)


def main():
    myObject = Rectangle(1,2,10,10)
    print(myObject.__str__())

main()