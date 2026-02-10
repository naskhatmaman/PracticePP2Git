#1
class MyClass:
    x = 5

obj = MyClass()
print(obj.x)

#2 Class with multiple attributes
class Car:
    brand = "Toyota"
    year = 2020

c = Car()
print(c.brand, c.year)

#3 Class with no attributes (empty blueprint)
class Empty:
    pass

e = Empty()
print(type(e))

#4 Class with attribute referencing another class
class Engine:
    power = "150 HP"

class Vehicle:
    engine = Engine()

v = Vehicle()
print(v.engine.power)

#5 Class with attribute that is a list
class StudentGroup:
    students = ["Bekzat", "Aruzhan", "Dias"]

sg = StudentGroup()
print(sg.students)