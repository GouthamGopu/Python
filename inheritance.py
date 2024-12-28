print("\nTypes of inheritance:\n1.Simple\n2.Multiple\n3.Multilevel")
class a:
  pass
class b(a):#simple inheritance
  pass
class c(b):#multilevel inheritance
  pass
class d(b,a):#multiple inheritance
  pass

print("\n*********\n")
print("Constructors & Super Keyword\n")
class Company :
  company="Amazon"
  def __init__(self):
    print("iam constructor of Company")

class Employees(Company):
  def __init__(self):
    super().__init__()
    print("iam constructor of Employees")

e=Employees()

print("\n*********\n")

print("Class Method Demonstration\n")
class classMethoDemonstration :
  company="Amazon"
  @classmethod
  def name_classAttribute(cls):
    print(f"the company name is {cls.company}")

  def name_objAttribute(self):
    print(f"the company name is {self.company}")

clas=  classMethoDemonstration()
clas.company="Google"

clas.name_classAttribute()
clas.name_objAttribute()


print("\n*********\n")

print("Property And Getters & Setters\n")

class Employee: 
  @property 
  def name(self): 
    return self.ename 
  @name.setter 
  def name (self,value): 
    self.ename = value 


e= Employee()
e.name="goutham"
print(e.name)

print("\n*********\n")

print("Property Overloading:\n")

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return Number(self.n + num.n)
    def __sub__(self, num):
        return Number(self.n - num.n)
    def __str__(self):
        return f"Your Ans is {self.n}"

n = Number(3)
m = Number(2)

print(n + m)
print(n - m)

print("\n*********\n")