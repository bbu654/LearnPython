pop: str = f"Brice"
print(f"Eat your veggies, {pop}\nThank you, {pop}, very much!")
x = ["apple", "banana", "cherry"]
x.append("orange")
x.append("blueberry")
x.append("pear")
for o, p in enumerate(x, 1):
    print(f"{o}: {p}", end=",  ")
else:
    print()
y = enumerate(x)
# print(list(y))    #return [f"{name['first']} {name['last']}" for name in lst]
r = [f"{q}" for q in y]
print(f"{r[0]} {r[1]} {r[2]} {r[3]} {r[4]} {r[5]}")
print(r)
# How to merge two dictionaries
# in Python 3.5+

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
# z = dict(x, **y)
# print(z)
# {'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {"a": 4, "b": 3, "c": 2, "d": 1}

sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print("passed")

if 1 in (x, y, z):
    print("passed")

# These only test for truthiness:
if x or y or z:
    print("passed")

if any((x, y, z)):
    print("passed")
