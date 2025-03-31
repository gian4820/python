class Person:
  def __init__(self, age):
    self.age = int(age)
  
@property
def isAdult(self):
    if self.age > 18:
      return True
    else:
      return False
  
age=int(input())


print(Person.isAdult(age))