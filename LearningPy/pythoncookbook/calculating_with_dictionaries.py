# example.py
#
# Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
zipofdicts = zip(prices.values(), prices.keys()) # Tuples];; This didnt work minprice = min(zipofdicts) maxprice = max(zipofdicts)

minprice = (0,"")
maxprice = (0,"")

for x in zipofdicts:
   if x[0] < minprice[0] or minprice[0]==0:
      minprice = x
   if x[0] > maxprice[0]:
      maxprice = x
   print(f'{x}', end='    ')
else:
   print()
# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price: ', min_price, '    max price: ', max_price, '    minzip: ', minprice, '    maxzip: ', maxprice)

print('sortprice:',end='    ')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print(name, price, sep=', ', end='    ')
else:
    print()


###Python zip()
#The zip() function takes iterables (can be zero or more), 
#          aggregates them in a tuple, and return it.
#The syntax of the zip() function is:
  #zip(*iterables)
      #zip() Parameters
      #Parameter	Description
      #iterables	can be built-in iterables (like: list, string, dict), 
      #           or user-defined iterables
  #Recommended Reading: Python Iterators, __iter__ and __next__

#Return Value from zip()
# The zip()function returns an iterator of tuples based on the iterable objects.
# If we do not pass any parameter, zip() returns an empty iterator
# If a single iterable is passed, 
#    zip() returns an iterator of tuples with each tuple having only one element.
# If multiple iterables are passed, 
#    zip() returns an iterator of tuples with each tuple having elements from all the iterables.

#Example 1: Python zip()
#Suppose, two iterables are passed to zip(); 
#one iterable containing three and other containing five elements. 
#Then, the returned iterator will contain three tuples. 
#It's because iterator stops when the shortest iterable is exhausted.
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)
#Output
#
#[]
#{(2, 'two'), (3, 'three'), (1, 'one')}

##Example 2: Different number of iterable elements
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(f'EX2.1:setofresult(zip({numbersList},{numbers_tuple})):{result_set}')

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(f'EX2.2:setofresult(zip({numbersList},{str_list},{numbers_tuple})):{result_set}')
#Output
#
#{(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
#{(2, 'two', 'TWO'), (1, 'one', 'ONE')}

##Example 3: Unzipping the Value Using zip()
##The * operator can be used in conjunction with zip() to unzip the list.
##zip(*zippedList)
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(f'EX3:cord:{coordinate}, valu:{value}listofzip:{result_list}', end='   zip(*loz): ')

c, v =  zip(*result_list)
print('coord:', c, end='   ')
print('value:', v)
#Output:
#
#[('x', 3), ('y', 4), ('z', 5)]
#c = ('x', 'y', 'z')
#v = (3, 4, 5)

longstr = ["Four score and seven years ago blah bleh blau"]
lst = ["Geeks For geeks"]
strzip = lst.extend(longstr)
#strlist= list(strzip)
#w1, w2, w3, w4, w5, w6, w7, w8, w9=zip(*longstr)
#print(w1, w2,w3,w4,w5,w6,w7,w8,w9)
# Python3 program to Convert single 
# indexed list into multiple indexed list 

def convert(lst): 
	return ' '.join(lst).split()#return (lst[0].split()) 

# Driver code 
 
print( convert(lst)) 
