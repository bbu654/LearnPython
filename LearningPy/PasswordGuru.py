from collections import namedtuple, Counter
import itertools
import json, collections
from os import X_OK
from typing import Collection

from pygame import key

"""     https://realpython.com/documenting-python-code/
    
    
    Additionally, you should use the following four essential 
    RULES as suggested by Jeff Atwood (aka Coding Horror 
        {Code tells you how; Comments tell you why.}):

Keep comments as close to the code being described as possible. 
    Comments that aren’t near their describing code 
    are frustrating to the reader 
    and easily missed when updates are made.

Don’t use complex formatting (such as tables or ASCII figures). 
    Complex formatting leads to distracting content 
    and can be difficult to maintain over time.

Don’t include redundant information. 
    Assume the reader of the code has a basic understanding 
    of programming principles and language syntax.

Design your code to comment itself. 
    The easiest way to understand code is by reading it. 
    When you design your code using clear, easy-to-understand concepts, 
    the reader will be able to quickly conceptualize your intent.

Class docstrings should contain the following information:
    A brief summary of its purpose and behavior
    Any public methods, along with a brief description
    Any class properties (attributes)
    Anything related to the interface for subclassers, 
        if the class is intended to be subclassed
The class constructor parameters should be documented 
    within the __init__ class method docstring. 
    Individual methods should be documented using their individual docstrings. 
    Class method docstrings should contain the following:
        A brief description of what the method is and what it’s used for
        Any arguments (both required and optional) 
            that are passed including keyword arguments
        Label any arguments that are considered optional 
            or have a default value
        Any side effects that occur when executing the method
        Any exceptions that are raised
        Any restrictions on when the method can be called
Let’s take a simple example of a data class that represents an Animal. 
    This class will contain a few class properties, 
    instance properties, a __init__, and a single instance method:
"""
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
        #reStructured Text Example
        """Gets and prints the spreadsheet's header columns

        :param file_loc: The file location of the spreadsheet
        :type file_loc: str
        :param print_cols: A flag used to print the columns to the console
            (default is False)
        :type print_cols: bool
        :returns: a list of strings representing the header columns
        :rtype: list
        """
class rest1:
    
    def test_multiple_flags_at_once():    # Different ways to test multiple # flags at once in Python
        x, y, z = 0, 1, 0

        if x == 1 or y == 1 or z == 1:
            print('passed')

        if 1 in (x, y, z):
            print('passed')
        # These only test for truthiness:
        if x or y or z:
            print('passed')

        if any((x, y, z)):
            print('passed')
    def Merging_two_dicts():
        """🐍PyTricks]: Merging two dicts in Python 3.5+ with a single expression      bbu654      Dan at Real Python <info@realpython.com>    Sat, Mar 20 at 9:53 AM"""
        # How to merge two dictionaries in Python 3.5+

        x = {'a': 1, 'b': 2}
        y = {'b': 3, 'c': 4}
        z = {**x, **y}
        print(z)
        #{'c': 4, 'a': 1, 'b': 3}

        # In Python 2.x you could
        # use this:
        z = dict(x, **y)
        print(z)
        #{'a': 1, 'c': 4, 'b': 3}

        # In these examples, Python merges dictionary keys in the order listed in the expression, overwriting 
        # duplicates from left to right.
        #
        # See: https://www.youtube.com/watch?v=Duexw08KaC8

        # The get() method on dicts and its "default" argument

name_for_userid = {
            382: "Alice",
            590: "Bob",
            951: "Dilbert",
            }

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
#"Hi Alice!"

print(greeting(333333))
#"Hi there!"
"""
    When "get()" is called it checks if the given key exists in the dict.
    If it does exist, the value for that key is returned.
    If it does not exist then the value of the default argument is returned instead.
    — Dan Bader (realpython.com)"""

def useNamedTuples():    # Why Python is Great: Namedtuples
    # Using namedtuple is way shorter than# defining a class manually:
    Car = namedtuple('Car', 'color mileage')

    # Our new "Car" class works as expected:
    my_car = Car('red', 3812.4)
    my_car.color            #'red'
    my_car.mileage          #3812.4
    print(my_car)                  # We get a nice string repr for free:
        #Car(color='red' , mileage=3812.4)
        # Like tuples, namedtuples are immutable:
    my_car.color = 'blue'   #AttributeError: "can't set attribute"
def ZenOfPython():
    """
    If you open a Python interpreter, and type "import this", as you know, it prints:
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than right now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    In the python source(Lib/this.py) this text is generated by a curious piece of code:
    """
    xs = """Gur Mra bs Clguba, ol Gvz Crgref
    Ornhgvshy vf orggre guna htyl.
    Rkcyvpvg vf orggre guna vzcyvpvg.
    Fvzcyr vf orggre guna pbzcyrk.
    Pbzcyrk vf orggre guna pbzcyvpngrq.
    Syng vf orggre guna arfgrq.
    Fcnefr vf orggre guna qrafr.
    Ernqnovyvgl pbhagf.
    Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
    Nygubhtu cenpgvpnyvgl orngf chevgl.
    Reebef fubhyq arire cnff fvyragyl.
    Hayrff rkcyvpvgyl fvyraprq.
    Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
    Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
    Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
    Abj vf orggre guna arire.
    Nygubhtu arire vf bsgra orggre guna *evtug* abj.
    Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
    Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
    Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    print( "".join([d.get(c, c) for c in xs]))
    #(as an alternative to the "pprint" module)

    # The standard string repr for dicts is hard to read:
    my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
    print(my_mapping)
    #{'b': 42, 'c': 12648430. 'a': 23}  # 😞
    # The "json" module can do a much better job:
    print(json.dumps(my_mapping, indent=4, sort_keys=True))
    #{
    #    "a": 23,
    #    "b": 42,
    #    "c": 12648430
    #}
    # Note this only works with dicts containing
    # primitive types (check out the "pprint" module):
    json.dumps({all: 'yup'})    #TypeError: keys must be a string
    #In most cases I'd stick to the built-in "pprint" module though :-)

        #— Dan
        #! -------------------------------------------------------------!
        # Why Python Is Great:
        # Function argument unpacking
def myfunc(x, y, z):
    print(x, y, z)
tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}
myfunc(*tuple_vec)
#1, 0, 1
myfunc(**dict_vec)
#1, 0, 1
#////////////////***********Stop Writing Classes************\\\\\\\\\\\\\\\\\\\
Talk1 = {"Title":"Stop Writing Classes","Author":"Jack Diederich","Link":"https://www.youtube.com/watch?v=o9pEzgHorH0","Summary":"Classes are great but they are also overused.  This talk will describe examples of class overuse taken from real world code and refactor the unnecessary classes, exceptions, and modules out of them."}
#Wrong:
import urllib#, urllib3, Requests
class API:
    def __init__(self,key):
        self.header = dict(apikey=key)

    def call(self,method,params):       #        requust = urllib.
        request = urllib.request(self.url + method[0] + '/'+method[1], urllib.urlencode(params),self.header)
        try:
            response = json.loads(urllib.urlopen(request).read())
            return response
        except urllib.HTTPError as error:
            return dict(Error=str(error))
MuffinAPI=API(key='SECRET-API-KEY')
MuffinAPI.API(key='SECRET-API-KEY').call(('mailings','stats'),{'id':1})
#Can be aliased like this:
MuffinAPI.request = API(key='SECRET-API-KEY').call
# and used in  a function like this:
MuffinAPI.request(('mailings','stats'),{'id':1})

MUFFIN_API= url='https://api.webservice.com/%s/%s'
MUFFIN_API_KEY = 'SECRET-API-KEY'
class newAPI:
    def request(noun,verb,**params):
        try:        #get_article()
            headers = {'apikey':MUFFIN_API_KEY}
            request = urllib.Request((MUFFIN_API % (noun,verb)), urllib.urlencode(params), headers)
            raise LookupError()
            return json.loads(urllib.urlopen(request).read())
            #services.crawler.crawlerexceptions.ArticleNotFoundException
        except SyntaxError:#ArticleNotFound
            pass
import heapq
class Heap(object):
    def __init__(self,data=None,key=lambda x:None):
        self.heap = data or []
        heapq.heapify(self.heap)
        self.key = key

    def pushleft(self,item):
        if self.key:
            item=(self.key(item),item)
        heapq.heappush(self.heap,item)
    def popleft(self):
        return heapq.heappop(self.heap)[1]
#OAuth2 Implementation: http://code.google.com/p/google-api-python-client/source/browse
#10k SLOC, 115 Modules, 207 Classes
class Flow(object):
    pass
class Storage(object):
    def put(self,data): 
        _abstract()
    def get(self): 
        _abstract()
def _abstract(): 
    pass

    #rewrite to OAuth2 only:
link2=f"http://github.com/jackdied/python-foauth2"    #132 SLOC, 3 Classes
class Cell(object):
    def __init__(self,x,y,alive=True):
        self.x = x
        self.y = y
        self.alive=alive
        self.next=None
    def neighbors(self):
        yield (self.x + 1, self.y)
        yield (self.x + 1, self.y + 1)
        #yield (self.x, self.y + 1)
        yield (self.x + 1, self.y)
class Board(object):
    def __init__(self):
        self.cells = {}    #{ x, y : Cell() }
    def Advance(self):
        for (x,y), cell in self.cells.items():
            if len( cell.neighbors)> 3:
                cell.next = False
class GameOfLife():
    #////////////////////******************Connors game of life implementaion
    def neighbors(point):
        x , y = point
        yield x + 1, y    
        yield x - 1, y    
        yield x, y + 1
        yield x, y - 1
        yield x + 1, y + 1
        yield x + 1, y - 1
        yield x - 1, y + 1
        yield x - 1, y - 1
    def advance(board):
        #pointa= 
        #neighbors1 = neighbors(pointa)
        newstate = set()
        recalc = board | set(itertools.chain(*map(GameOfLife.neighbors, board)))    
        for point in recalc:
            count = sum((neigh in board) for neigh in GameOfLife.neighbors(point))
            if count == 3 or (count==2 and point in GameOfLife.neighbors):
                newstate.add(point)
        return newstate
    glider = set([(0 , 0), (1 , 0), (2 , 0), (0 , 1), (1 , 2)])
    for i in range(1000):
        glider = advance(glider)
    print(glider)
        
import timeit
class ThetimeitmoduleA:
    def Thetimeitmodule():
        strTimeit=f" The 'timeit' module lets you measure the execution time of small bits of Python code."
        timeit.timeit('"-".join(str(n) for n in range(100))',   number=10000)
                    #0.3412662749997253
        timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
                    #0.2996307989997149
        timeit.timeit('"-".join(map(str, range(100)))',         number=10000)
                    #0.24581470699922647
    def Inplacevalueswapping():
        # Why Python Is Great:    # In-place value swapping
        # Let's say we want to swap the values of a and b...
        a = 23
        b = 42
        # The "classic" way to do it with a temporary variable:
        tmp = a
        a = b
        b = tmp
        # Python also lets us use this short-hand:
        a, b = b, a

        # "is" vs "=="

        a = [1, 2, 3]
        b = a
        a is b          #    True
        a == b          #    True
        c = list(a)
        a == c          #    True
        a is c          #    False

    # • "is" expressions evaluate to True if two #   variables point to the same object

    # • "==" evaluates to True if the objects #   referred to by the variables are equal
import contextlib

def myfunc(a: int, b:int) -> int:
    return a + b

def dispatch_if(operator: str, x: int, y: int) -> int:
    if   operator == 'add':  return x + y
    elif operator == 'sub':  return x - y
    elif operator == 'mul':  return x * y
    elif operator == 'div':  return x / y
    else:                    return None

def my_add(a: int, b: int) -> int:
    return a + b

def check(list1, val):
    return(all(x > val for x in list1))

def dispatch_dict(operator: str, x: int, y: int) -> int:
    return {
            'add': lambda: x + y,
            'sub': lambda: x - y,
            'mul': lambda: x * y,
            'div': lambda: x / y,
            }.get(operator, lambda: None)()


@contextlib.contextmanager
def file_hanlder(file_name,file_mode):
    file = open(file_name,file_mode)
    yield file
    file.close()

if __name__ == "__main__":

   with file_hanlder("test.txt","w") as f:
       f.write("Test")

   print(f.closed)

# Functions are first-class citizens in Python:# They can be passed as arguments to other functions,# returned as values from other functions, and# assigned to variables and stored in data structures.
if __name__ == "__main__":
    funcs = [myfunc]
    funcs[0]
    #<function myfunc at 0x107012230>
    funcs[0](2, 3)
    #5
    age = 15
    print((lambda: 'kid', 'lambda: adult')[age > 20]())    #kid
    # Python's list comprehensions are awesome.
         # Example:
    even_squares = [x * x for x in range(10) if not x % 2]
    print(even_squares)        #[0, 4, 16, 36, 64]
    value=0;x=0
    expression=x * x
    collection=range(10)
    condition=not x % 2
    vals = [expression         for value in collection         if condition]
    # This is equivalent to:
    vals = []
    for value in collection:
        if condition:            vals.append(expression)
    # Python has a HTTP server built into the standard library. 
    # #This is super handy for previewing websites.
    # Python 3.x   $ python3 -m http.server    # Python 2.x    $ python -m SimpleHTTPServer 8000
    # (This will serve the current directory at http://localhost:8000)
    # Because Python has first-class functions they can
    # be used to emulate switch/case statements
    dispatch_if('mul', 2, 8)        #16
    dispatch_dict('mul', 2, 8)      #16
    dispatch_if('unknown', 2, 8)    #None
    dispatch_dict('unknown', 2, 8)  #None
    
    # python program to check if all  values in the list are greater than val using all() function
    # driver code 
    list1 =[10, 20, 30, 40, 50, 60]
    val = 5
    if(check(list1, val)):
        print("Yes")
    else:
        print("No")
    
    val = 20 
    if (check(list1, val)):
        print("Yes")
    else:
        print("No")
    # Python 3.5+ supports 'type annotations' that can be
    # used with tools like Mypy to write statically typed Python:
    # collections.Counter lets you find the most common elements in an iterable:
    c = collections.Counter('helloworld')
    print(c)                    #Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
    print(c.most_common(3))     #[('l', 3), ('o', 2), ('e', 1)]
