from functools import reduce
# *args, basically the spread operator, so far at least
# the main thing I can pull from my early knowledge is these arguments will be called positionally
def print_stuff(*stuff):
  for thing in stuff:
    print(thing)
    
    
# print_stuff(1,2,3,4,5,'askldh', 'aiksdhjgals', False,'', '^^empty string^^', {})
# print_stuff()
# print_stuff(2)

# **kwargs on the other hand, will be called with keywords
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
# print(tables)

def assign_food_items(**order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)
  print(order_items)

# assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

# These are combinable with all other parameter types
# The correct order for using multiple types is (positional_args, *args, keyword_args, **kwargs) or any version thereof
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)
  
  single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', scoop1='Vanilla, Cookies and Cream', scoop2='Chocolate')
  
# Some cool ways to use this
a, *b, c = [3, 6, 9, 12, 15]
# print(['a:', a], ['b:', b], ['c:', c])
# above: in javascript this would be called destructuring and a, *b, c would look like {a, ...b, c} basically. This is cool and I'm not actually sure whether the spread operator would work in this way.
# update: it does not have this capability that I've been able to find in JS

my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
# print(merged_tuple)



####### Namespaces ########
# Built-in namespace
# print(dir(__builtins__))
# above: this prints a list of all the built-ins in Python. (It's 152 items)

# Global namespace (aka this module)
# print(globals())
# above: built-in method "globals()" lists the entire global namespace object

# Lambda functions, kinda like ternary in JS
def add_stuff(sentence):
  return sentence + 'stuff' 
# print(add_stuff("Hey that's my "))

add_mine = lambda sentence: sentence + 'mine'

# print(add_mine("Hey that's "))

shut_up = lambda sentence: sentence if len(sentence) <= 30 else sentence[:30]

# print(shut_up('this, that, the other, and their friends, and yo mama'))


# Functions as params
def functioner(func_1, func_2, func_3, x):
  return [func_1(x), func_2(x), func_3(x)]

add = lambda x: x + 2
multiply = lambda x: x * 2
divide = lambda x: x / 2

# print(functioner(add, multiply, divide, 2))

shout = str.upper
louder = shout('this is loud now')
# print(louder)

grade_list = [3.5, 3.7, 2.6, 95, 87]

grades = map(lambda grade: grade if type(grade) == int else grade * 25 , grade_list)

# print(list(grades))

# note for the above lambda function:
# if you are using type() the result is NOT A STRING. It returns a class name which is built in.
# So... grades = map(lambda grade: grade if type(grade) == -----> "int" <----- else grade * 25 , grade_list)
# this won't work correctly.

books = [["Burgess", 1985], ["Orwell", "Nineteen Eighty-four"], ["Murakami", "1985"], ["Orwell", 1984], ["Burgess", "Nineteen Eighty-five"], ["Murakami", 1985]]


string_titles = filter(lambda book: type(book[1]) == str, books)
# print(list(string_titles))

letters = ['r', 'e', 'd', 'u', 'c', 'e']
word = reduce(lambda x, y: x + y, letters)
# print(word)

class CustomIterator1:
  def __init__(self, some_list, second_list):
    self.some_list = some_list
    self.second_list = second_list
    
  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    list_1_len = len(self.some_list)
    list_2_len = len(self.second_list)
    total_len = list_1_len + list_2_len
    
    if self.index < list_1_len:
      result = self.some_list[self.index]
      self.index += 1
      return result
    elif self.index >= list_1_len and self.index < total_len:
      result = self.second_list[self.index - list_1_len]
      self.index += 1
      return result
    else:
      print('end of loop')
      raise StopIteration
    
to_ten_and_back = CustomIterator1([x for x in range(1, 11)], [y for y in range(9, 0, -1)])

for item in to_ten_and_back:
  print(item)