# Sets... like lists but different
# as far as I can tell these are almost identical to JS sets
a_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 7, 9, 10]

# make sets with the set built-in
a_set = set(a_list)
# OR by placing the values in brackets
b_set = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 7, 9, 10}
# We could also do this
c_set = {*a_list}
print(a_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}
print(b_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}
print(c_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10}

# adding items to a set happens one of two ways..
# 1.
a_set.add(15)
print(a_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15}
# 2.
b_set.update([15])
print(b_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15}
# the difference is update() takes an iterable and can add multiple values, whereas add() is a singular item
# 3. (for clarity and completeness)
c_set.update([15, 16, 29])
print(c_set)
# {1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 29}



























































