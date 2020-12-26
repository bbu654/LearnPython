import math
import sys
import bbutils as bb
import distutils
import distutils.util as dutil 
import pprint
import random as roll
import emoji
from itertools import islice
import bbutilities as bbut
iname = "Brice"         #input("Name: ")
iage = 42               #int(input("Age: "))
some_string = "false"   #input("True or False: RUANewPatient? ")
iisnew = bool(dutil.strtobool(some_string))

shorty=[]
bb.printit()

p1 = bb.Patient(iname, iage, iisnew)
shorty.append(p1.returnpatient())
loanamount = 1000000
hashighincome=True
hasgoodcredit=True
iscriminal=False
if not iscriminal:
    shorty.append(f"Down payment is ${(loanamount * 0.1 if hasgoodcredit and hashighincome else loanamount * 0.2)}")
    if hasgoodcredit and hashighincome:
        shorty.append(f"Down payment is ${loanamount * 0.1}")
    else:
        shorty.append(f"Down payment is ${loanamount * 0.20}")
    
elgibilty = bb.LoanEligibility( loan_amount=loanamount, has_high_income=hashighincome, has_good_credit=hasgoodcredit, is_criminal=iscriminal)
shorty.append(elgibilty.return_eligible())
#for x in [shorty]:    #    print(x)bimnames[str]=sys.builtin_module_names    #print('Count built-in modules: %d' %len(sys.builtin_module_names)); 
shorty.append(bb.listmodules())
#shorty.append(f"str00={modlst[0]},\t{modlst[1]},\t{modlst[2]},\t{modlst[3]},\t{modlst[4]}.")
#shorty.append(f"str05={modlst[5]},\t{modlst[6]},\t{modlst[7]},\t{modlst[8]},\t{modlst[9]}.")#print(str01)
#for x in [sys.builtin_module_names]:            #sys.builtin_module_names A tuple of strings print for loop each
#    print(f"tuple{index2}={x}\t")               #    index2 += 1    #index3 = 0    #for y in [x]:    #    print(f"string{index3}={y}")
    #    index3 += 1    #line2 += x.__name__     #if index2 % 6 == 0:    #    line2+="\n"    #index2+=1
fargo1 = 'I think '
chucky=bb.mspy(fargo1)  #shorty.append(chucky.returnpop())               #blockofgold=bbutils.mspy.returnpop(4,fargo1)
pp2=pprint.PrettyPrinter(indent=2,width=110,stream=None,compact=True)    #pp2.pprint(sys.builtin_module_names) #print(line2)
shorty.append(chucky.chant())
shorty.append(chucky.uselasso())
shorty.append(chucky.LikeWW())
shorty.append( "Shifting WHY by 13 gives:  "+ chucky.lassoWord( "WHY", 13 ) )
shorty.append( "Shifting oskza by -18 gives:  " + chucky.lassoWord( "oskza", -18 ) )
shorty.append( "Shifting ohupo by -1 gives:  " + chucky.lassoWord( "ohupo", -1 ) )
shorty.append( "Shifting ED by 25 gives:  " + chucky.lassoWord( "ED", 25 ) )

shorty.append(chucky.lassoWord("WHY",13).title())
shorty.append(chucky.lassoWord("oskza",-18).title() + chucky.lassoWord("ohupo",-1) )
shorty.append(chucky.lassoWord("ED",25).upper() )
shorty.append(chucky.lassoWord("terra",13))
whiley=bb.whileforloops(False)
commands=["start","start","stop","stop","quit"]
shorty.append(whiley.autohelp(commands))
shorty.append(whiley.userange(4,6))
if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    shorty.append(F'a={a};;;    ')
    shorty.append(f'list(dedupe(a)={list(bb.dedupe(a))}{bb.DeepDiveOnCollections}')
collection_list = []
print(collection_list,end='    ')
list123 = [1,2,3,4,5]
print(list123,end='    ')
listalpha = ['a','b','c','d','e']
print(listalpha,end='    ')
collection_list = list()
print(collection_list,end='    ')

collection_list = [1] * 10 # [1,1,1,1,1,1,1,1,1,1]
collection_list.extend(listalpha)
collection_list.extend(list123)
print(collection_list)
truepop=True
iNeedanum=0

"""for i,elm in islice(enumerate(some_list),7,40):
  print i,elm  """
for yearindex, yearobj in enumerate(bb.listyearsum2020):
    for nextindex, nextobj in islice(enumerate(bb.listyearsum2020),yearindex):#for element in l[1:]:
        for elveindex, elveobj in islice(enumerate(bb.listyearsum2020),nextindex):
            if yearobj+nextobj+elveobj == 2020:
                print(f'the sum of {yearobj}*{nextobj}*{elveobj}={yearobj*nextobj*elveobj}')

adventofcode1stday="Advent of Code *bbu654 4*  :year 2020  That's the right answer! You are one gold star closer to saving your vacation. You have completed Day 1 and Day 2!" 
print(f'adventofcode1stday={adventofcode1stday}')
pobbu = bb.day3AdventOfCode(1) * 44996864#bb.day3AdventOfCode(3) * bb.day3AdventOfCode(5) * bb.day3AdventOfCode(7)
shorty.append(f'day2AdventOfCode={bb.day2AdventOfCode()} and day3={pobbu}')


if False:
    day3rdlineAdventOfCode()
#while truepop:
#bb.listyearsum2020
recap=("""\nRecap
  Strings:
  Strip = Trim in C#
  You can define a literal string by using either a set of single-quote or double-quote symbols.
  You can add an escape sequence to use a special character inside your string, 
      such as a single-quote escape sequence (\'), double-quote escape sequence (\"), 
      a new line escape sequence (\n      ), or a tab escape sequence (\t).
  You can print the raw output of a string by prefixing it with the r character.
  You can define a multi-line verbatim string by using either a set of three single-quote characters 
      (''') or a set of three double-quote characters (\"\"\").
  The print() function can concatenate a variable number of strings 
  sent as arguments into the function. You can specify the character you want 
     to separate each argument, as well as the ending character.
  The format() function allows you to define a format string (essentially, a template). 
  The string contains a series of replacement fields 
  that are replaced with arguments you pass into the function.
  The new format string literal, or f-string, reduces the keystrokes of the format() method. 
  This allows you to use variables or expressions in the replacement fields.
  Format specifiers are a compact syntax that allows you 
  to format numbers, dates, and percentages, as well as alignment and spacing.
  Types:
  The type() function returns the data type of a specified value.
  The isinstance() function allows you to check to see whether 
  a value is an instance of a specified data type. The float data type is for numeric values 
  containing fractional values that are represented as numbers after the decimal point.
  Values have data types, and variables do not. 
  A variable is merely pointed to a value, and it can point to any value of any data type.
  A queue is a special term in programming 
  that refers to a list that stores items in the order in which they were added. 
  Recap
  Lists are data structures that are intended to collect related data in your programs. 
  The data can be of any type. But elements are usually of the same data type 
  because they serve a similar purpose in your programs.
  Create a list by using square brackets. Use a comma to separate each item.
  Access individual elements inside the list by using square brackets 
  and a zero-based index.   Access the first item in the list by using index 0. 
  Access the last item in the list by using index -1. 
  Access items relative to the end of the list 
  by using other negative numbers as indexes.  Create slices by using square brackets 
  and a colon.   The colon separates the beginning of the slice, on the left, 
  from the end of the slice, on the right. Use helper functions like 
  pop(), append(), remove(), extend(), and clear() to change the items in a list.
  Queues are useful when you need to do some calculation logic 
  on many items in a specific order. After you add items to the list, 
  you remove them for processing one by one.   A pop operation removes an item 
  from the queue for processing.  You can remove an item from the beginning of the list 
  ("first in, first out", or FIFO).   Or you can remove an item from 
  the end of the list ("last in, first out", or LIFO). The pop() helper function 
  allows you to select an item from the list by using its index. 
  The first item is 0, and the last item is -1.
  Recap
  Use the in and not in keywords as part of a Boolean expression 
  to test whether a value is part of a list. Use the for statement to iterate through 
  all items in a list. Also use the statement to execute a code block 
  that puts the current item in scope to be inspected in the logic of the code block.
  Use the continue statement to skip the remaining code block logic 
  and continue to the next list item that's assigned by the for statement.
  Use the break statement to break out of the for statement prematurely.
  Use the else statement to create a code block that executes 
  after you use the for statement to iterate through all items in the list.
  Nest for statements to create a list of every combination of two lists.
  Use the random module's choice() and choices() functions to select 
  one or many items from the list, respectively.
  """)
if False:
    shorty.append(bb.StringChallenge())
dice = roll.randint(1,10)
commandscalc=['c','2','bob','*','4']
print(f"roll={dice},    {commandscalc}={bb.Calculator(commandscalc,False)}{emoji.emojize('    Howdy :sun_with_face:')}")
comman=['Frank','Bob','q']
bb.gocurrent(comman,False)
print()
bb.dicerollMS(comman,False)
bb.threadsafePrint()
print()
shorty.append(bbut.dontknow())
#from PythonCookBook import get_top_n_items_from_list
##shorty.append(get_top_n_items_from_list.exampleBBU())#

if True:
    shorty.append(bbut.poppop())
    print()
    # bbut.backwardcounting(10000000)
    # bbut.backwardcounting(20000000)

#if True:
#    shorty.append(get_top_n_items_from_list.exampleBBU())
#    print(f'{get_top_n_items_from_list.exampleBBU()}')

    pp2.pprint(shorty) 
if False:
    print(recap)
    shorty.append(recap)
    bb.colortest()
    bb.mothodlog()
    bb.print_format_table()
    #bb.newguess()
#bbutils.show_acceptable_modules()import pickle, pickletools#serialize/deserialize objects/streams pickle. +=