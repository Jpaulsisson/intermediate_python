from collections import *
import random
# collections is basically specialized versions of containers
# so special lists, dictionaries, etc. with special methods

# --------------------------------
# Let's start with deque() -- (I'm pronouncing this "deck", but who knows if that's right)
# -- This is a list that's optimized for appending and popping from the front or back but not so much for accessing the stuff in the middle
# --------------------------------
a_big_list = [x for x in range(1, 123)]

a_big_deque = deque()
for i in a_big_list:
  if i % 2 == 0:
    a_big_deque.appendleft(i)
  else:
    a_big_deque.append(i)
# above: adding even numbers to the "left", or front of the list, and adding odd numbers to the end
# print(a_big_deque)

a_small_deque = deque([1, 2, 3])
a_small_deque.popleft()
# above: pops the zero index
# print(a_small_deque)
# deque([2, 3])

# --------------------------------
# Next up: namedtuple()
# -- This is kind of like a labeled tuple generator class
# -- The layout is namedtuple(nameOfTuple, [list of tuple element labels], optional args...(rename, defaults, module...))
# --------------------------------
Jedi = namedtuple('Jedi', ['name', 'mastery_level', 'lightsaber_color'])
# Now let's make a few
yoda = Jedi('Yoda', 'Grand Master', 'Green')
mace_windu = Jedi('Mace Windu', 'Master', 'Purple')

# print(yoda.mastery_level)
# Grand Master
# print(mace_windu.lightsaber_color)
# Purple

# --------------------------------
# Next: defaultdict()
# -- This is basically a way to add default values to keys in a dictionary when a key is called that doesn't exist
# -- I'm sure there are some fantastic use cases for this but man it seems incredibly niche to my newbie brain
# --------------------------------
letters_of_the_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
websters = {
  "a": "a words",
  "b": "b words",
  "c": "c words",
}
websters_defaults = defaultdict(lambda: '<- + words')
websters_defaults.update(websters)
# print(websters_defaults)
# defaultdict(<function <lambda> at 0x1025ca3e0>, {'a': 'a words', 'b': 'b words', 'c': 'c words'})
for letter in letters_of_the_alphabet:
  websters[letter] = websters_defaults[letter]
# print(websters)
# {'a': 'a words', 'b': 'b words', 'c': 'c words', 'd': '<- + words', 'e': '<- + words', 'f': '<- + words', 'g': '<- + words', 'h': '<- + words', 'i': '<- + words', 'j': '<- + words', 'k': '<- + words', 'l': '<- + words', 'm': '<- + words', 'n': '<- + words', 'o': '<- + words', 'p': '<- + words', 'q': '<- + words', 'r': '<- + words', 's': '<- + words', 't': '<- + words', 'u': '<- + words', 'v': '<- + words', 'w': '<- + words', 'x': '<- + words', 'y': '<- + words', 'z': '<- + words'}

# --------------------------------
# Next: OrderedDict()
# -- Not fully understanding the point of this special class other than optimization and some easy-to-use extra methods
# -- I'm sure it's great in some way I'm not seeing though
# --------------------------------
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

orders = OrderedDict(order_data)
to_move = [x[0] for x in order_data if x[-1] == 'returned']
# grab all returned values
to_remove = [x[0] for x in order_data if x[-1] == 'canceled']
# grab all canceled values
for item in to_move:
  orders.move_to_end(item)
# move all returned orders to the end
for item in to_remove:
  orders.pop(item)
# remove all canceled orders

# for order, status in dict(orders).items():
#   print(order, status)
# Order: 1 purchased
# Order: 2 purchased
# Order: 3 purchased
# Order: 5 purchased
# Order: 8 purchased
# Order: 11 purchased
# Order: 13 purchased
# Order: 15 purchased
# Order: 4 returned
# Order: 7 returned
# Order: 9 returned
# Order: 12 returned


profits = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

profits_the_sequel = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# --------------------------
# Next: ChainMap()
# -- This lets you chain dictionaries together to create one giant dictionary
# -- You can also add more dictionaries to the original giant one using the new_child() method
# --------------------------
profit_map = ChainMap(*profits)

def get_profits(profit_data):
  total_standard_profits = 0.0
  total_holiday_profits = 0.0
  for key in profit_data.keys():
    if 'holiday' not in key:
      total_standard_profits += profit_data[key]
    else:
      total_holiday_profits += profit_data[key]
  return total_standard_profits, total_holiday_profits

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)
# print(last_year_standard_profit, last_year_holiday_profit)
# 180796.27999999997 28608.55
for item in profits_the_sequel:
  profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)
# print(current_year_standard_profit, current_year_holiday_profit)
# 184631.15 32035.64
year_standard_so_far = current_year_standard_profit - last_year_standard_profit
year_holiday_so_far = current_year_holiday_profit - last_year_holiday_profit
# print(year_standard_so_far, year_holiday_so_far)
# 3834.8700000000244 3427.09

# --------------------------
# Next: Counter()
# -- This does basically what you'd assume it does with a little extra functionality that's cool.
# -- This might actually be my favorite of the collections module so far
# --------------------------
a_list_of_numbers = [1,2,3,2,1,5,6,2,3,6,7,5,7,9,6,5,8,0,5,6,8,7,9,4,5,1,3,6,8,2,6,9,8,4,5,6,6,2,3,6,5,5,9,5]
another_list_of_numbers = [2,5,4,8,7,9,6,5,4,8,2,1,5,3,4,7,5,1,2,3,6,5,4,7,8,2,2,4,8,6,2,1,7,5,6,2,3,1,4,8,6]
counted_numbers = Counter(a_list_of_numbers)
more_counted_numbers = Counter(another_list_of_numbers)
# print(counted_numbers)
# Counter({5: 9, 6: 9, 2: 5, 3: 4, 9: 4, 8: 4, 1: 3, 7: 3, 4: 2, 0: 1})
# print(more_counted_numbers)
# Counter({2: 7, 5: 6, 4: 6, 8: 5, 6: 5, 7: 4, 1: 4, 3: 3, 9: 1})

# some cool methods for this class
added_numbers = counted_numbers + more_counted_numbers
# print(added_numbers)
# Counter({5: 15, 6: 14, 2: 12, 8: 9, 4: 8, 1: 7, 3: 7, 7: 7, 9: 5, 0: 1})

minus_numbers = counted_numbers - more_counted_numbers
# print(minus_numbers)
# Counter({6: 4, 5: 3, 9: 3, 3: 1, 0: 1}) <-- this removes negative values and zeroed out values

# print(counted_numbers)
# Counter({5: 9, 6: 9, 2: 5, 3: 4, 9: 4, 8: 4, 1: 3, 7: 3, 4: 2, 0: 1})
counted_numbers.subtract(more_counted_numbers)
# print(counted_numbers)
# Counter({6: 4, 5: 3, 9: 3, 3: 1, 0: 1, 1: -1, 7: -1, 8: -1, 2: -2, 4: -4})


# --------------------------
# Next: UserDict()
# -- This allows us to create a dictionary with our own defined methods on it.
# -- I really like the idea of being able to do this
# --------------------------
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

class OrderProcessingDict(UserDict):
  
  def clean_orders(self):
    to_be_deleted = []
    for key, value in self.items():
      if value['order_status'] == 'complete':
        to_be_deleted.append(key)
    for item in to_be_deleted:
      del self[item]

dict_orders = OrderProcessingDict(data)

# for item in dict_orders:
#   print(item)

# print('-------------------------')
# print('updating... updating... all completed orders removed!')
# print('-------------------------')
dict_orders.clean_orders()

# for item in dict_orders:
#   print(item)

# --------------------------
# Next: UserList()
# -- This allows us to create a list with our own defined methods on it.
# -- Again, I really like the idea of being able to do this
# --------------------------

unshuffled = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

class PaulsList(UserList):
  def shuffle(self):
    start = 0
    stop = len(self) - 1
    for index in range(0, len(self)):
      random_index = random.randrange(start, stop)
      temp = self[index]
      self[index] = self[random_index]
      self[random_index] = temp
    
  # it should be noted that built-in methods can be overwritten and can be used like so:
  def append(self, new_value):
    print(f'I just appended {new_value} to this list!')
    super().append(new_value)
      
      
bout_to_be_shuffled = PaulsList(unshuffled)
# print(bout_to_be_shuffled)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
bout_to_be_shuffled.shuffle()
# our custom method is called on a perfectly sequential list and...
# print(bout_to_be_shuffled)
# [11, 15, 19, 3, 10, 9, 18, 6, 2, 12, 5, 1, 17, 4, 13, 8, 7, 20, 16, 14]... boom goes the dynamite
# bout_to_be_shuffled.append(21)
# print(bout_to_be_shuffled)
# I just appended 21 to this list!
# [5, 6, 8, 7, 4, 16, 18, 19, 1, 13, 10, 11, 9, 12, 17, 14, 20, 3, 15, 2, 21] <-- it was reshuffled because it ran again

# --------------------------
# Next: UserString()
# -- This allows us to create a string with our own defined methods on it.
# -- Yet again, I really like the idea of being able to do this
# -- One special note about this class: it has a "data" attribute built-in for easier use
# --------------------------

class BetterString(UserString):
  # This shows what the data attribute does
  def printData(self):
    print(self.data)

  def scream(self):
    screamed = self.data.upper() + '!'
    print(screamed)
    
  # we can also overwrite operators like so:  (<-- this changes the "-" operator)
  def __sub__(self, substring):
    # below: this doubles the input value within the string, just to prove we are really changing the functionality of this operator, heavily
    new = super().replace(substring, f'{substring}{substring}') 
    print(new)
    
better_string = BetterString('better string here')
better_string.printData()
# better string here
better_string.scream()
# BETTER STRING HERE!
better_string - 'here'
# better string herehere