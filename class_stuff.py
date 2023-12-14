# Working with classes beyond just defining them
# "self" is the Python version of JavaScript's "this"
# When referencing a defined class variable such as "new_id" below, 
# it's referenced by the class name
# When the "init" variables are referenced, it's with "self"
class Employee:
  new_id = 1
  def __init__(self, name="unknown"):
    self.id = Employee.new_id
    self.name = name
    Employee.new_id += 1
  
  def say_id(self):
    print("My id is " + str(self.id) + ".")
    
  def retinal_scan(self): 
    if self.name != "unknown":
      print("scanning... scanning... scanning... " + self.name + "! Confirmed.")
    else: print("scanning... scanning... scanning... Can not confirm name of employee. Please update file or get them out of here.")

e1 = Employee()
e2 = Employee("Scarlet")

# e1.say_id()
# e2.say_id()
# prints "My id is 1", "My id is 2"

# Inheritance from a parent class.
# This Admin class will inherit all the attributes and properties of Employee plus it's own
class Admin(Employee):
  pass

e3 = Admin()

# e3.say_id()
# prints "My id is 3"

# Overriding inheritance
class ThatGuy(Employee):
  def say_id(self):
    print("I am an Admin and my id is " + str(self.id))

e4 = ThatGuy("Chaz")
# e4.say_id()
# prints "I am an Admin and my id is 4"
# OR
# you could also use the super method to reference the parent class like so
class ThisGuy(Employee):
  def say_id(self):
    print("I promise I work here.") 
    super().say_id()
    
me = ThisGuy("Paul")
# me.say_id()
# prints "I promise I work here. My id is 5"

# Inheriting multiple classes at once
class Manager(ThisGuy):
  def say_title(self):
    super().say_id()
    print("I'm actually a manager.")
    
e5 = Manager("Chelsie")
# e5.say_title()
# prints "I promise I work here. My id is 6. I'm actually a manager."

# e1.retinal_scan()
# e2.retinal_scan()
# e3.retinal_scan()
# e4.retinal_scan()
# e5.retinal_scan()