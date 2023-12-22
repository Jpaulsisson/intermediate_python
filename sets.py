# Sets... like lists but different
# as far as I can tell these are almost identical to JS sets
a_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 7, 9, 10]

# make sets with the set built-in
a_set = set(a_list)
# OR by placing the values in brackets
b_set = {1, 2, 3, 4, 6, 7, 1, 2, 3, 7, 9, 10}
# We could also do this
c_set = {*a_list}
# print(a_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}
# print(b_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}
# print(c_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}

# adding items to a set happens one of two ways..
# 1.
a_set.add(15)
# print(a_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15}
# 2.
b_set.update([15])
# print(b_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15}
# the difference is update() takes an iterable and can add multiple values, whereas add() is a singular item
# 3. (for clarity and completeness)
c_set.update([15, 16, 29])
# print(c_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 29}

# removing items is not terribly different than adding them. There are two methodsL:
# 1. If you use remove() and the element doesn't exist in the set, an error will be raised. Obviously, if it does exist, it's removed from the set.
a_set.remove(1)
# print(a_set)
# {2, 3, 4, 5, 6, 7, 9, 10, 15}
# 2. contrary to remove(), if discard() is asked to remove an element that doesn't exist, no error is thrown. Basically nothing happens at all.
b_set.discard(1)
# print(b_set)
# {2, 3, 4, 5, 6, 7, 9, 10, 15}
# If the below code was called with remove() instead of discard(), an error would be raised
c_set.discard(11)
# print(c_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 29}


# A frozenset can't be added to or deleted from. End.
frozen = frozenset(['Elsa', 'Anna', 'Sven', 'Kristoff', 'Olaf'])
# print(frozen)

# The thing about sets is that they're completely unordered. You can't access them by the index at all. BUT we can do this.
# print('Olaf' in frozen)
# True
# print('Shrek' in frozen)
# False


dictionary_of_sets = {
  # union() combines all elements of multiple sets and removes duplicates
  "union sets 1": a_set.union({0, 20}, c_set),
  # the pipe character is a union operator in Python( NOT OR like JS)
  # so far as I can tell, the union operator only works on sets
  "union sets 2": a_set | {0, 20} | c_set,
  # intersection() only gives the elements that are shared
  "intersected sets 1": a_set.intersection(c_set),
  # the ampersand operator works on sets for intersection()
  "intersected sets 2": a_set & c_set,
  # difference() gives the values that are in the first set but are NOT in the second set
  "set difference 1": a_set.difference(b_set),
  # the minus or hyphen is the operator for difference()
  "set difference 2": a_set - b_set,
  # and finally the last is symmetric_difference() and it returns the unique values not shared by the sets
  "symmetric diff 1": a_set.symmetric_difference(c_set),
  # the operator for this is the hat ^ (i now it isn't a hat, it's like carot or caret or carrot or something)
  "symmetric diff 2": a_set ^ c_set,
}

# print(dictionary_of_sets['union sets 1'])
# print(dictionary_of_sets['union sets 2'])
# both: {0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 20, 29}
# print(dictionary_of_sets['intersected sets 1'])
# print(dictionary_of_sets['intersected sets 2'])
# both: {2, 3, 4, 5, 6, 7, 9, 10, 15}
# print(dictionary_of_sets['set difference 1'])
# print(dictionary_of_sets['set difference 2'])
# both: {5}
# print(dictionary_of_sets['symmetric diff 1'])
# print(dictionary_of_sets['symmetric diff 2'])
# both: {1, 16, 29}




my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

print(my_tags)




































