import itertools
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


# Multi class
class Bread:
  yummy = True
  def __init__(self, leavened, make_time, color='brown'):
    self.leavened = leavened
    self.color = color
    self.make_time = make_time
  
  def addToDish(self, *args): 
    return [args, "Bread"]
  
class Sauce:
  tasty = True
  def __init__(self, base, make_time, color):
    self.base = base0
    self.make_time = make_time
    self.color = color

  def addToDish(self, *args):
    return [args, "{} sauce".format(self.base)]
  

class Pizza(Bread, Sauce):
  best_food = True
  def __init__(self, thiccness, *toppings):
    self.thiccness = thiccness
    self.toppings = [toppings]
    
class Pasta(Sauce, Bread):
  best_food = True
  def __init__(self, base, noods, sauce):
    self.noods = noods
    self.sauce = sauce
    self.base = base

classic = Pizza('thin', 'parmigiano', 'basil', 'mozzarella', 'prosciutto')
classico = Pasta('cream', 'penne', 'carbonara')

# print(vars(classic))
# print([classic.best_food, classic.tasty, classic.yummy])

# print(classic.addToDish('stuff'))
# print(classico.addToDish('any'))
# The important difference to note here is that if there are properties with the same name in both inherited classes then the one listed first takes priority. So when Pizza calls addToDish it prints the Bread version, and when Pasta calls the addToDish method it prints the Sauce version. I'm fully aware that this example fell apart by the end but the things I needed to make clear still stand. 

# another cool little diddy here is that you can do this...
class ThisClass:
  def the_thing_this_class_does(self):
    print('this is the thing THIS class does')

class ThatClass:
  def the_thing_this_class_does(self):
    print('this is the thing THAT class does')
  

this = ThisClass()
that = ThatClass()

these = [this, that]

for the_thing in these:
  the_thing.the_thing_this_class_does()
# prints:
# this is the thing THIS class does
# this is the thing THAT class does

first_list = [1, 2, 3]
second_list = ['a', 'b', 'c', 'd']
third_list = [True, False, True]

a_set = {1, 2, 3}
a_dict = {1: 'a', 2: 'b', 3: 'c'}

triple_list = [*first_list, *second_list, *third_list]
chained_list = itertools.chain(first_list, second_list, third_list)
combo_w_set = [*first_list, *a_set]
chain_combo_w_set = itertools.chain(first_list, a_set)
combo_w_dict = [*first_list, *a_dict]
chain_combo_w_dict = itertools.chain(first_list, a_dict)

# for item in triple_list:
#   print("triple: ", item)

#  ^^^ vvv these print the same thing 

# for item in chained_list:
#   print("chain: ", item)

# for item in combo_w_set:
#   print("set combo: ", item)

#  ^^^ vvv these print the same thing

# for item in chain_combo_w_set:
#   print("set chain combo: ", item)

# for item in combo_w_dict:
#   print("dict combo: ", item)

# ^^^ vvv these print the same thing

# for item in chain_combo_w_dict:
#   print("dict chain combo: ", item)

# Now THIS is powerful
all_combos = list(itertools.combinations(second_list, 3))
# prints [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
# That's freaking cool.

# Python's count built-in is really cool too
string_of_random_letters = "aiosupdhygaiksjdnbfgaiopsdgjuaisdghoasdioghasasdjkghaisipdugthasdjgbnaisdghasiodghjasodighuiasduh"

# prints 13
print(string_of_random_letters.count('a'))
# prints 11
print(string_of_random_letters.count('g'))
# prints 3
print(string_of_random_letters.count('p'))
# prints 2
print(string_of_random_letters.count('n'))
# prints 13
print(string_of_random_letters.count('s'))





