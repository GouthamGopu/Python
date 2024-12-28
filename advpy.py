from typing import List, Tuple, Dict, Union


if((n:=5)>3):
  print("walrus operater[ := ]\n\t Assigns a variable in an expression\n")


# Type defination
print("Type defination using [:] and [->] operaters")
age: int = 18
def sum(a:int,b:int) -> int :
  return a+b
print(sum(5,10))
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier=123 # allowed


#match condition
print("\nmatch condition method same as switch case in cpp or c: \n")
def http_status(status):
  match status:
    case 200:
      return "OK"
    case 404:
      return "Not Found"
    case 500:
      return "Internal Server Error"
    case _:
      return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status

# New operators | and |= allow for merging and updating dictionaries
print("\nNew operators | and |= allow for merging and updating dictionaries\n")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
dict2 |= {'c':2, 'e':'5'}
print(merged) 
print(dict2)



# using "with" keyword for opening 2 files at once

print("\nusing \"with\" keyword for opening 2 files at once\n")
with (
  open("sample.txt") as s,
  open("write.txt") as w
):
  print(s.read())
  print(w.read())


# try and exception -> if the code in the try block code can will execute except block and go to next line of execution. so code never fails when we use try except in code
# print("\ntry and exception\n")


#if this fails code execution stops here itself but in try block it cntinues with the next step
# n=int(input("enter any number:"))

# try:
#   n=int(input("enter any number:"))
# except ValueError as v:
#   print(v)
# except Exception as e:
#   print(e)


#Raise a error using "raise" keyword

# print("\nRaise a error using \"raise\" keyword\n")

# a=int(input("enter any number:"))
# b=int(input("enter any number:"))

# if(b==0):
#   raise ZeroDivisionError("we cant divide with zero")
# else:
#   print(f"Division of {a} and {b} is {a/b}")

print("\n__name__ \n")
print(__name__)#when we ran this file it prints __main__ if we import this file into other file and run that file it prints the file name of this file so  we use the code only that should execute when ran on this file lyk this

if(__name__ == "__main__"):
  print("this outputs when only this file runs")




print("\nGlobal key word\n")
a=1

def fna():
  a=0
  print(a)
fna()
print(a)
b=1
def fnb():
  global b
  b=0
  print(b)

fnb()
print(b)

print("\nEnumerate KeyWord\n")

list=[1,2,3,4,5]

for index,item in enumerate(list):
  print(f"index {index} --> data {item}")

squareList=[i*i for i in list]

print(squareList)