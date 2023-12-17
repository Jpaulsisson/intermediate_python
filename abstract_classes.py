from abc import ABC, abstractmethod

# ABC stands for abstract base class
# It's kind of like a typescript type definition for classes
# so below we are saying that any class that inherits from "AbstractEmployee" MUST contain a say_id method.
# note: it doesn't matter what that method does...it just has to exist
class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
      return print(self.id)

e1 = Employee()
e1.say_id()