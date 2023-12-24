from collections import *
# collections is basically specialized versions of containers
# so special lists, dictionaries, etc. with special methods

# --------------------------------
# Let's start with deque() -- (I'm pronouncing this "deck", but I feel confident that's not correct)
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
websters_defaults = defaultdict(lambda: '<- that + words')
websters_defaults.update(websters)
# print(websters_defaults)
# defaultdict(<function <lambda> at 0x1025ca3e0>, {'a': 'a words', 'b': 'b words', 'c': 'c words'})
for letter in letters_of_the_alphabet:
  websters[letter] = websters_defaults[letter]
# print(websters)
# {'a': 'a words', 'b': 'b words', 'c': 'c words', 'd': '<- that + words', 'e': '<- that + words', 'f': '<- that + words', 'g': '<- that + words', 'h': '<- that + words', 'i': '<- that + words', 'j': '<- that + words', 'k': '<- that + words', 'l': '<- that + words', 'm': '<- that + words', 'n': '<- that + words', 'o': '<- that + words', 'p': '<- that + words', 'q': '<- that + words', 'r': '<- that + words', 's': '<- that + words', 't': '<- that + words', 'u': '<- that + words', 'v': '<- that + words', 'w': '<- that + words', 'x': '<- that + words', 'y': '<- that + words', 'z': '<- that + words'}

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





