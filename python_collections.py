from collections import *
# collections is basically specialized versions of containers
# so special lists, dictionaries, etc. with special methods

# Let's start with deque  (I'm pronouncing this as "deck", but I'm not sure that's correct)
# -- This is a list that's optimized for appending and popping from the front or back but not so much for accessing the stuff in the middle
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
print(a_small_deque)
# deque([2, 3])




















