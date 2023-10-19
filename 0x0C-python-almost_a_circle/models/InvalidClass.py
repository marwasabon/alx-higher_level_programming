#!/usr/bin/python3
'''
This is a Python script that defines
a InvalidClass class that inherits from the Base class.
'''


from models.base import Base


class InvalidClass(Base):
  '''
  This is a Python script that defines
  a InvalidClass class that inherits from the Base class.
  '''
  def __init__(self, width, height):
    super().__init__(width, height)

  def area(self):
    return self.width * self.height
