class class_ex:
  salary=1200000#class attribute
  def __init__(self, name):# Constructor && dunder method->the method in python which starts with "__"
    self.name=name #object or instance attribute
  def greet(self): # self means sending instance itself
    print(f"Good Morining!!, {self.name}")
  @staticmethod # we should use this for not using self
  def bye():
    print("Thank You!!")

dimpu = class_ex("Goutham")
dimpu.greet() 
# it converts to class_ex.greet(dimpu) so we should use self in function defination in class or we should declare @staticmethod
print(f"Your Salary is {dimpu.salary}")
dimpu.bye()