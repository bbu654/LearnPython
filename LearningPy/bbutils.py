import shutil
import pkgutil
import random
import logging                          #from thread_safe_print import thread_safe_print
import threading
from collections import defaultdict, namedtuple, deque
import binarytree
import debugpy
import prettyprint
import itertools
def printit():
    print("String usage:             \t\t'...' in Strng - => bool  ")
    print("len(String)    - CharCount\t\tString.find()  - => index \t\tString.replace() -   ")
    print("String.upper() - UPPERCASE\t\tString.lower() - lowercase\t\tString.title()  - CamelCase  ")
    print("    ")
    print("    ")
    print("Arithmetic operators")
    print("10//3          => int     \t\tx += 3,+,-,*,             \t\t/ => floating point")
    print("operator precedance first to last: (),**,/,*,//,%,+,- \t\t\t\tround() abs() import math math.ceil")
    #return("hello from bbutils")
    i=0
    while i <= 5:
        k=i
        popp=''
        while k<=5:
            popp=popp + ' ' 
            k+=1                #pooo='@' * i
        print(f"{popp}\033[92m{'#' * i}{'#' * i}") #    print(pop)def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
        i+=1
    else:
        print("     @@\033[00m\n")#    print("     @@")


class Patient:
    def __init__(self1, name, age, is_new):
        self1.name = name
        self1.age = age
        self1.is_new = is_new

    def returnpatient(self1):
        if self1.is_new:
            notlit = ""
        else: #ifelse is_hot:
            notlit = "not "
        return("{} is {}a new patient. He is {}.".format(self1.name, notlit, self1.age))


class LoanEligibility:
    def __init__(self2, loan_amount, has_high_income, has_good_credit, is_criminal):
            self2.loan_amount = loan_amount
            self2.has_high_income = has_high_income
            self2.has_good_credit = has_good_credit
            self2.is_criminal = is_criminal
    def return_eligible(self2):
        incomelit="You do not have a High Income, "
        creditlit="and do not have Good Credit, "
        criminalit="and you do NOT have a criminal record."
        eligiblelit="SORRY! You are not ELIGIBLE for a Loan! "
        downpayment=f" Your Down Payment is {(self2.loan_amount * 0.1 if self2.has_high_income and self2.has_good_credit else self2.loan_amount * 0.2)}."
        line1=f"{(eligiblelit if self2.is_criminal else eligiblelit.replace('SORRY! You are not','Congratulations! You are'))}{(incomelit.replace('not ','') if self2.has_high_income else incomelit)}{(creditlit.replace('not ','') if self2.has_good_credit else creditlit)}{(criminalit.replace('NOT ','') if self2.is_criminal else criminalit )}{('' if self2.is_criminal else downpayment)}"
        print(line1)
        if not self2.is_criminal:
            if self2.has_good_credit:
                if self2.has_high_income:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You do have a High Income, and do have Good Credit, and you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.1}.")
                else:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You do not have a High Income, and do have Good Credit, and you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}.")
            else:
                if self2.has_high_income:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You do have a High Income, and do not have Good Credit, and you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}.")
                else:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You do not have a High Income, and do not have Good Credit, and you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}.")

        else:
            if self2.has_good_credit:
                if self2.has_high_income:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You do have a High Income, and do have Good Credit, and you do have a criminal record.")
                else:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You do not have a High Income, and do have Good Credit, and you do have a criminal record.")
            else:
                if self2.has_high_income:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You do have a High Income, and do not have Good Credit, and you do have a criminal record. ")
                else:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You do not have a High Income, and do not have Good Credit, and you do have a criminal record. ")



class secretgame:
    def __init__(self, secretnumber=9, guesslimit=3):
        self.secretnumber=secretnumber
        self.guesslimit=guesslimit        
        
    def secretguess(self, listguess=[0]):
        self.listguess=list(listguess)
        guesscount=0
        is_console = False
        while guesscount < self.guesslimit:
#        for x in self4.listguess:
            if len(self.listguess) != self.guesslimit:
                is_console=True
            if is_console:
                x = int(input(f"{self.guesslimit-guesscount} Guess's(1,2,3) left: ")) #     x=singleguess
            else:
                x=self.listguess[guesscount]
            guesscount += 1
            if x==self.secretnumber:
                return("You won!")    #                break
        else:
            return("Sorry you didnt guess correctly")




def show_acceptable_modules():# modules = {         module        for _, module, package in list(pkgutil.iter_modules())}#        if package is False    }
    line2 = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line2, 'Module', 'Location', line2))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))
import sys

def listmodules():
    modlst=[]    #pop=int(sys.builtin_module_names.count())
    pop6=len(sys.builtin_module_names)
    mlindex=0
    modlen=13
    while mlindex < pop6:    #shorty.append(f"    {str(sys.builtin_module_names[mlindex])}    ")        #print(sys.builtin_module_names[mlindex])
        #if len(sys.builtin_module_names[mlindex]) > modlen:
        sbmn = str(sys.builtin_module_names[mlindex])[0:13].ljust(modlen,' ')
        modlst.append( f"{str(mlindex).zfill(2)}={sbmn}")
        mlindex += 1
    #for x in modlst:
    #    strs.append(f"{x}")
    modulelists=list(sys.builtin_module_names)
    if False:
        for y in modulelists:
             modlst.append(f"    {y}    ")
    return modlst

#Example 2 Project: autocomplete-python Source File: imports.py View license

def _get_module_names(self3, search_path=None):
    
    #Get the names of all modules in the search_path. This means file names and not names defined in the files.
    names = []
    # add builtin module names
    if search_path is None:
        names += [self3._generate_name(name) for name in sys.builtin_module_names]
 
    if search_path is None:
        search_path = self3.sys_path_with_modifications()
    for module_loader, name, is_pkg in pkgutil.iter_modules(search_path):
        names.append(self3._generate_name(name))
    return names
#namesbbu=_get_module_names(self3)
#for xyz in [namesbbu]:
#    print(xyz)
#

class mspy:
    def __init__(self5, fargo):
        #self5.args = args
        self5.fargo = fargo

    #    def returnpop(self5):
    def chant(self5):#Diana is {diana}!    WONDER WOMAN 1984
         # Associate the variable diana with the value "WONDER WOMAN 1984"
         diana = "WONDER WOMAN 1984"
         # Print a message with the true identity of Diana
         self5.fargo += (f"Diana is {diana}! ")
         fargo2=self5.fargo.replace("WONDER WOMAN 1984","WW84")
         # This is a comment that won't be interpreted as a command.
         return(f"Hello, Themyscira! Chant = {fargo2} {fargo2} {fargo2}")          

    def lassoWord(self5, word, shiftAmount ):
        decodedWord = ""    
        for letter in word:
            decodedLetter = mspy.lassoLetter(self5, letter, shiftAmount)
            decodedWord = decodedWord + decodedLetter
        return decodedWord

    # Define a function to find the truth by shifting the letter by the specified amount
    def lassoLetter( self5, letter, shiftAmount ):
        # Invoke the ord function to translate the letter to its ASCII code 
        # Save the code to the letterCode variable
        letterCode = ord(letter.lower())        
        # The ASCII number representation of lowercase letter 'a'
        aAscii = ord('a')    
        # The number of letters in the alphabet
        alphabetSize = 26    
        # The formula to calculate the ASCII number for the decoded letter
        # Take into account looping around the alphabet
        trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)    
        # Convert the ASCII number to the character or letter
        decodedLetter = chr(trueLetterCode)    
        # Send the decoded letter back
        return decodedLetter

    
    def uselasso(self5):
        return("ok")

    def question_activity(self5, likes, questions, is_console_input, activity):

        shorty3=[]
        if is_console_input:
            activity= input("{questions[0]}")
        else:
            print(f"{questions[0]}", end='\t')            #job='A'            #value='B'            #decade='A'            #travel='B'
            
        shorty3.append(f"You chose: {activity}")
        if activity=='A':                   # update scoring variables based on the activity choice
            print("Reading? Nice choice!")
            likes[0] = likes[0] + 1
            likes[1] = likes[1] + 1
        elif activity=='B':
            print("Partying? Sounds Fun!")
            likes[2] = likes[2] + 1
            likes[3] = likes[3] + 1        
        else:
            print('You should have entered "A" or "B" Lets just say you like to read')
            activity="A"
            likes[0] = likes[0] + 1
            likes[1] = likes[1] + 1        
        return likes                        #likes=[diana_like, barbara_like, steve_like, max_like]
    def question_job(self5, likes, questions, is_console_input, job):         
        if is_console_input:
            job = input(f"{questions[1]}")
        else:
            print(f"{questions[1]}", end='\t')
        if job == "A":                      # update scoring variables based on the job choice
            print( "Curator? Nice choice!" )
            likes[0] = likes[0] + 2
            likes[1] = likes[1] + 2
            likes[2] = likes[2] + 1            
        elif job =="B":
            print( "Biz Runner? Sounds fun!" )
            likes[3] = likes[3] + 2
        else:
            print("You must type A or B, let's just say you want to be a curator at the Smithsonian")
            job = "A"
            likes[0] = likes[0] + 2
            likes[1] = likes[1] + 2
            likes[2] = likes[2] + 1            
        return likes                        #likes=[diana_like, barbara_like, steve_like, max_like]
    def question_value(self5, likes, questions, is_console_input, value): # ask the candidate a third question
        if is_console_input:
            value = input(f"{questions[2]}")
        else:
            print(f"{questions[2]}", end='\t')
        if value == "A":                # update scoring variables based on the value choice
            print( "Money, Nice choice!" )
            likes[0] = likes[0] - 1
            likes[3] = likes[3] + 2
        elif value =="B":
            print( "Love?    Sounds fun!" )
            likes[0] = likes[0] + 1
            likes[2] = likes[2] + 2
            likes[1] = likes[1] + 1
        else:
            print("You must type A or B, let's just say money is more important to you.")
            value = "A"
            likes[0] = likes[0] - 1
            likes[3] = likes[3] + 2
        return likes                        #likes=[diana_like, barbara_like, steve_like, max_like]
    def question_decade(self5, likes, questions, is_console_input, decade):       
        if is_console_input:                # ask the candidate a fourth question
            decade = input(f"{questions[3]}")
        else:
            print(f"{questions[3]}", end='\t')
        
        if decade == "A":                   # update scoring variables based on the decade choice
            print( "1910s,   Nice choice!" )
            likes[2] = likes[2] + 2
            likes[0] = likes[0] + 1
        elif decade =="B":
            print( "1980s? Sounds fun!" )
            likes[3] = likes[3] + 1
            likes[1] = likes[1] + 2
        else:
            print("You must type A or B, let's just say the 1910s is your favorite decade.")
            decade = "A"
            likes[2] = likes[2] + 2
            likes[0] = likes[0] + 1
        return likes                            #likes=[diana_like, barbara_like, steve_like, max_like]
    def question_travel(self5, likes, questions, is_console_input, travel):         # ask the candidate a fifth question
        if is_console_input:
            travel = input(f"{questions[4]}")
        else:
            print(f"{questions[4]}", end='\t')
        if travel == "A":                       # update scoring variables based on the travel choice
            print( "Driving, Nice choice!" )
            likes[3] = likes[3] + 2             # Max
            likes[1] = likes[1] - 1             # Barbara
        elif travel =="B":
            print( "Flying?  Sound fun!" )
            likes[0] = likes[0] + 1             # Diana Prince WW84
            likes[2] = likes[2] + 1             # Steve Trevor
        else:
            print("You must type A or B, let's just say your favorite way to travel is by driving")
            travel = "A"
            likes[3] = likes[3] + 2             # Max
            likes[1] = likes[1] - 1             # Barbara
        return likes                            #likes=[diana_like, barbara_like, steve_like, max_like]
    def LikeWW(self5):                          # create some variables for scoring
        #diana2_likes = steve2_likes = max2_likes = barbara2_likes = 0    #        diana_like = 0        steve_like = 0        max_like = 0        barbara_like = 0        max2_likes += 1
        is_console_input = False
        year=1984
        shorty2 = []
        shorty2.append(f"the year is {year}")
        year = year + 36
        shorty2.append(f"the year is now {year}")
        if year==1984:
            shorty2.append("answering machine msg")
        if year == 2020:
            shorty2.append("voice mail")

        questions=["Which activity?           (A) Reading                       (B) Party!"]
        questions.append("What's your dream job?    (A) Curator at the Smithsonian    (B) BizRun")
        questions.append("What's more important?    (A) Money                         (B) Love  ")
        questions.append("What's your best decade?  (A) 1910s                         (B) 1980s ")
        questions.append("How do you travel best    (A) Driving                       (B) Flying")
            
        if not is_console_input:    #shorty2.append(f"{questions[0]}")       #        likes=[diana_like, barbara_like, steve_like, max_like]
            activity='A'
            job='A'
            value='B'
            decade='A'
            travel='B'
        likes=[0,0,0,0]
        likes=mspy.question_activity(self5, likes, questions, is_console_input, activity)
        likes=mspy.question_job(     self5, likes, questions, is_console_input, job)
        likes=mspy.question_value(   self5, likes, questions, is_console_input, value)
        likes=mspy.question_decade(  self5, likes, questions, is_console_input, decade)
        likes=mspy.question_travel(  self5, likes, questions, is_console_input, travel)

        # print out their choices
        shorty2.append( f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")   
        
        # print the results depending on the score
        if likes[0] >= 6:
            shorty2.append( f"You're most like Wonder Woman! {likes[0]} " )
        if likes[2] >= 6:
            shorty2.append( f"You're most like Steve Trevor! {likes[2]} " )
        if likes[1] >= 6:
            shorty2.append( f"You're most like Barbara Minerva! {likes[1]} ")
        if likes[3] >= 6:
            shorty2.append( f"You're most like Max Lord! {likes[3]} ")
        if likes[0] < 6 and likes[1] < 6 and likes[2] < 6 and likes[3] < 6:
            shorty2.append("You are not like anyone. ")
        return shorty2

class whileforloops:            
    def __init__(self6, is_console_input):        #self5.args = args
        self6.is_console_input = is_console_input

    def autohelp(self6, commands):
        command_index=0
        shorty4=[]
        if self6.is_console_input:
            command = input("> ").lower()
        else:
            command = commands[command_index]
        car_started=False            #car_started=False
        while True:
            if self6.is_console_input:
                command = input("> ").lower()
            else:
                command = commands[command_index]
            command_index+=1

            if command == "start":
                if car_started:
                    shorty4.append(f"Car already started")
                else:
                    shorty4.append(f"Car Started")
                    car_started=True                    #car_stopped=False
            elif command == "stop":
                if not car_started:
                    shorty4.append(f"Car already Stopped")
                else:
                    shorty4.append(f"Car Stopped")
                    car_started = False                    #car_stopped = True
            elif command == "quit":
                break
            elif command == "help":
                shorty4.append(f"""
                        start - to start the car
                        stop  - to stop  the car
                        quit  - to quit  the program
                        
                        """)
            else:
                shorty4.append("Sorry I didnt understand that")
        return shorty4
    def userange(self6, xin, yin):
        shorty5=[]
        aascii=ord('a')
        for x in range(xin):
            for y in range(1, yin):
                shorty5.append(f"{chr(x+aascii)}, {y}    ")
            shorty5.append('                                      ')
        matrix = [   [1,2,3],[4,5,6],[7,8,9]]
        for row in matrix:
            for item in row:
                shorty5.append(f"{item}    ")
            shorty5.append(f"                                                                       ")
        numbersz=[5,2,1,9,3,5]
        shorty5.append(f"b4 pop(2)={numbersz}")
        shorty5.append(numbersz.pop(2))
        shorty5.append(f"after pop={numbersz}")
        #shorty5.append(f"max={max(numbersz)}")
        maxofnums=numbersz[0]
        for z in numbersz:
            if z > maxofnums:
                maxofnums=z
        shorty5.append(f"max of numbers={maxofnums}")
        return shorty5
    
#  Message='>' not supported between instances of 'list' and 'int'
#  Source=C:\Users\bbbu6\Source\repos\LearningPy\LearningPy\LearningPy.py
#  StackTrace:
#  File "C:\Users\bbbu6\Source\repos\LearningPy\LearningPy\LearningPy.py", line 69, in <module>
#    shorty.append(whiley.userange(4,3))


# Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end=' ')
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end=' ')
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk), end=' ')
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk), end=' ')
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk), end=' ')
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk), end=' ') 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk), end=' ') 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk), end=' ') 
def colortest():
    prCyan("Hello World, ") 
    prYellow("It's") 
    prGreen("Geeks") 
    prRed("For") 
    prGreen("Geeks!") 
# Python program to print       # colored text and background 
def print_format_table(): 
	""" 
	prints table of formatted text format options 
	"""
	for style in range(8): 
		for fg in range(30, 38): 
			s1 = '' 
			for bg in range(40, 48): 
				format = ';'.join([str(style), str(fg), str(bg)]) 
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format) 
			print(s1) 
		print('\n') 

#print_format_table()
# 
#  
# dedupeSetEx.py <= example.py
#
# Remove duplicate entries from a sequence while keeping order
#Set
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    #print it thx
    #if __name__ == '__main__':
    #    a = [1, 5, 2, 1, 9, 1, 5, 10]
    #    print(F'a={a}')
    #    print(f'list(dedupe(a)={list(dedupe(a))}')
listyearsum2020=[1567,1223,1758,1842,1933,1898,1409,1058,1533,1417,1032,1634,1477,1394,1888,1972,1237,1390,1677,1546,1302,1070,1369,1455,1065,1924,1593,1131,1064,1346,1914,1129,1830,1450,1278,1740,1809,1176,1734,1102,1807,1982,1603,1736,2008,1980,1905,1633,1732,1350,1865,1988,1805,1998,1152,1046,1870,1557,1789,1766,1945,1359,1002,1126,1719,1497,1296,1560,1936,1929,1464,2005,1281,618,1257,1107,1632,1688,1964,1803,1360,1384,1889,1411,1328,1452,1868,1515,1586,1631,1618,1087,1710,1094,1774,1295,1700,1636,1230,1421,1910,1522,1366,1144,1757,1493,1316,1103,687,1371,1720,1155,1559,1900,989,1367,1999,1066,1773,1787,1402,1047,1806,1956,1219,1555,1307,1419,1706,1884,1109,1181,2010,1298,1730,1078,1848,1398,1687,2007,1550,1664,1225,1079,1698,350,1222,1377,1977,1510,1571,1630,1029,1379,1942,1949,1249,1829,1297,1530,1607,1324,1069,1476,928,1039,1855,1644,1454,1310,1172,547,1034,1878,1479,1457,1319,1810,1759,1439,1851,545,1470,2003,1908,1564,1491,1174,1301,1689,1276,1781,1392,1499,1962,1653,1823,1381,1827,1974]
DeepDiveOnCollections= """
    In this tutorial we will explore and master the most common and important data structures in Python 
    by performing a variety of operations with them. 
    A Collection is a container variable that is used to store some number of objects, 
    where objects can be of the same type or different.
    List
    List is an ordered set of elements that can be of different types. x=[] or list(x)
    You can also create a list of identical values ​​using multiplication.
    As said above, lists can contain variables of different type. 
    However, lists usually are used to store variables of same time to imitate behavior of arrays.
    To get the length of list, use the len() function. In Python, 
    you do not need to explicitly specify the size of a list while creating.
    Length is calculated in constant time.
    To access a specific list item or assign value to it, 
    we refer to the element by index where first element 
    has index of 0. To access an item from back, 
    use negative index [-1]:
    Accessing a nonexistent index results in an error:
    Error Index: list index out of range !
    Using the in operator, we can check if an object exists in the list. 
    Result of operation returns a bool value:
    You can also use slices to access a particular range of 
    values of given list:
    It is important to note that when using a slice, 
    a new list gets created:
    number_list[:] is number_list = false
    We can iterate over list items using the for loop. Often it is 
    necessary to get the index of the current element during 
    iteration. To do this, you can use the enumerate function, 
            which returns the index and the current element:
    As lists are a mutable data structures, we can add and remove 
    items. To add item to list, use .append() method:
    If you need to expand the list with another list, 
    you can use the .extend() method, which adds the 
    transferred list to the end of your list:
    
    You can use the del keyword to remove an item from the list:
    To find the minimum and maximum or calculate the sum of 
    all elements, we can use the built-in functions min, max, sum:
    It is often required to convert the list to a string, 
    for this you can use the str.join() method:
    Often we need to sort the list. There are two ways to sort 
    a list in Python.
    sorted()- the standard function, which returns the 
    new list obtained by sorting the original:
    .sort ()- the list method, which sorts list itself. 
    For sorting, the Timsort algorithm is used. O(n log n) 
    for worst case:
    If we need to sort in reverse order, pass reverse=True as argument:
    Dictionary
    Dictionary allows you to store data in key-value format. 
    Use the curly braces literal or just call dict() to define 
    a dictionary. If we want to add data to dictionary while 
    defining it, we write the key-value through a colon.
    Access to the value by key is carried out for constant time 
    and it does not depend on the size of the dictionary.
    If you access element by key that does not exist, 
    Python will throw a KeyError error, but it is often useful to try 
    to get the value from the dictionary, and if there is no key, 
    return some standard value. For such purposes we can use 
    a built-in get() method.
    Using the in operator, we can check if an object exists in the dictionary. 
    Result of operation returns a bool value:
    As dictionary is a mutable data structure, we can add and remove elements from it. 
    We can add item to dictionary simply using key access. 
    To remove the key and value from the dictionary, you can use the 
    del keyword as with lists:
    We can also add some key-value to the dictionary using can 
    the built-in update() method, which takes another dictionary 
    and extends our dictionary and also updates values of the original 
    dictionary in the case of identical keys.
    To remove the key-value from the dictionary and return the value 
    at the same time, we use the pop method:
    Sometimes it is required to check if a key exists in the dictionary, 
    and in case of failure add this new key-value pair. 
    For such situations we use setdefault() method:
    Using a for loop, we can iterate over dictionary keys:
    To iterate not by keys, but by keys and values ​​at once, 
    we can use the method items():
    The values() ​​method, which returns the values ​​logically:
    Set
    Set is an unordered collection of unique objects. 
    Sets are mutable and are most often used to remove duplicates 
    and all kinds of entry checks.
    You can use the set literal to declare an empty set or use curly braces 
    to declare the set and add some elements there at the time of declaration:
    To check whether an object is contained in a set, we use in keyword. 
    The check is performed in constant time. Each element of the structure 
    is hashed by analogy with dictionaries. Based on the key received 
    from the hash function, the object is searched.
    To add an element to the set we use the add() method. 
    The remove() method is used to remove a specific element:
    Sets in Python support standard set operations — such as union, 
    difference, intersection, and symmetric difference.
    NOTE: all mentioned collections and their methods, 
    functions are ones that are mostly used in practice. 
    There are more of them.
    Wrapping Up
    Want to learn more? Refer to this link:
    The Python Standard Library - Python 3.8.2 documentation
    While The Python Language Reference describes the exact syntax 
    and semantics of the Python language, this library…
    docs.python.org
    Kamoliddin Nabijonov
            """
           # print(f'DeepDiveOnCollections={DeepDiveOnCollections}')
        #output:
#a=[1, 5, 2, 1, 9, 1, 5, 10]
#list(dedupe(a)=[1, 5, 2, 9, 10]
def neighbours(ferry, row, col):
    occupied_seats = 0
    for i in range(max(row - 1, 0), min(len(ferry), row + 2)):
        for j in range(max(col - 1, 0), min(len(ferry[0]), col + 2)):
            if (i != row or j != col) and ferry[i][j] == '#':
                occupied_seats += 1
    return occupied_seats

def next_generation(ferry):
    next_ferry = []
    rows = len(ferry)
    cols = len(ferry[0])
    
    for row in range(rows):
        next_row = []
        for col in range(cols):
            if ferry[row][col] == '.':
                next_row.append('.')
            elif ferry[row][col] == 'L':
                next_row.append('#' if neighbours(ferry, row, col) == 0 else 'L')
            elif ferry[row][col] == '#':
                next_row.append('#' if neighbours(ferry, row, col) < 4 else 'L')
        next_ferry.append(''.join(next_row))
    return next_ferry
def day11seatchart():
    path = f'day11seatchart.txt'
    ferry=[]          #    tlines=[]
    rules = """All decisions are based on the number of occupied seats 
        adjacent to a given seat (one of the eight positions 
        immediately up, down, left, right, or diagonal from the seat). 
        The following rules are applied to every seat simultaneously:
        If a seat is empty (L) and there are no occupied seats adjacent 
        to it, the seat becomes occupied.  If a seat is occupied (#) 
        and four or more seats adjacent to it are also occupied, 
        the seat becomes empty.  Otherwise, the seat's state does not 
        change.  Floor (.) never changes; seats don't move, and nobody sits on the floor. """

    with open(path, 'r') as file11:
        line = file11.read()
            #for line in lines:
        lines=str(line)
        ferry=lines.strip().split('\n')        
            #    ferry = input.strip().split('\n')
    print(f'{ferry[0]}{ferry[1]}')
    iteration = 0
    print(f'{rules}')
    while True:
        next_ferry = next_generation(ferry)
        tpass=sum(row.count('#') for row in ferry)
        if ferry == next_ferry:
            return tpass
        ferry = next_ferry
        print(f'iteration={iteration},total passengers={tpass}')
        iteration += 1
        if iteration > 200:
            break
def fillseats(lines):
    mline=[]
    tlines=[]
    zero0=0
    intline=[]
    
    rows, cols = (99, 97) 
    intlines = [[0 for i in range(cols)] for j in range(rows)] 
    #print(arr) 
    #for init1 in range(99):
    #    for init2 in range(97):
    #        intlines[init1,init2]=0
    count=0
    for irow,line in enumerate(lines):
        kline=str(line)
        for icol in range(cols):
            if icol>0 and irow>0 and icol<cols and irow <rows:
                for x in range(-1,2):
                    for y in range(-1,2):
                        if lines[irow+x][icol+x] == '#':
                            bagtotal+=1
                        if lines[irow+x][icol+y] == '#':
                            bagtotal+=1
                        if lines[irow+y][icol+x] == '#':
                            bagtotal+=1
                        if lines[irow+y][icol+y] == '#':
                            bagtotal+=1
            #for j in range(len(i)):
            #need to copy like we are doingrules
            if irow == 0:#row=0
                #don't check -1
                lkd=0
                if icol ==0:
                    kld=0
                    
                    if kline[icol+1] == 'L':
                        if lines[irow][icol] == 'L':
                            if lines[irow+1][icol+1]=='L':
                                kld=0
                    #don't check -1
            if kline[icol]=='L':
                mline.append('M')
            
            else:
                #if count == 0:
                #    print(f'kline[i]={kline[i]}')
                if kline[icol] == "[" or kline[icol] == "'" or kline[icol] == "]":
                    kld=0
                else:
                    mline.append(kline[icol])
                    count+=1
        else:
            sline=str('')
            for x in mline: 
                sline += x 
            tlines.append(sline)
            count=0
    return tlines
def solve():
    path = f'day11seatchart.txt'
    day11seats=[]          # $
    tlines=[]
    rules = """All decisions are based on the number of occupied seats 
        adjacent to a given seat (one of the eight positions 
        immediately up, down, left, right, or diagonal from the seat). 
        The following rules are applied to every seat simultaneously:
        If a seat is empty (L) and there are no occupied seats adjacent 
        to it, the seat becomes occupied.  If a seat is occupied (#) 
        and four or more seats adjacent to it are also occupied, 
        the seat becomes empty.  Otherwise, the seat's state does not 
        change.  Floor (.) never changes; seats don't move, and nobody sits on the floor. """

    with open(path, 'r') as file11:
        for line in file11.readlines():
            day11seats.append(str(line).rsplit())
    tlines=fillseats(day11seats)
    for lidx, line in enumerate(tlines):
        if lidx % 5 == 0: 
            print(f'{str(line)[2:10]}', end='  ')
    print(rules)
    return 6969
def builditntheywillcome(numbers,num3,startnum,endnum):
    numbintwc=[]           #all possible between start and end
    changed=[]
    same=[]
    for jnum in range(startnum,endnum):
        if jnum == startnum or jnum == startnum+3 or jnum == startnum+6 or jnum == startnum+9:
            same.append(numbers[jnum])#dont change it ever
            changed.append(numbers[jnum])
        else:
            changed.append(0)#change 
            same.append(numbers[jnum])#same
def day10Joltprt2(numbers,num3,one1,three3):
    startnum=0
    endnum=0
    for jindx, jnum in enumerate(numbers):
        if jindx==0:
            startnum=jindx
        elif jnum-numbers[jindx-1]>1:    #Three!What about 2 threes in a row?
            endnum=jindx
            numbintwc=builditntheywillcome(numbers,num3,startnum,endnum)
        """ (((((((((((((((((((((2 ^ 7) * 4) * 16) * 16) * 4) * 4) * 4) * 16) * 16) * 4) * 16) * 4) * 16) * 16) * 4) * 8) * 4) * 8) * 16) * 4) * 2) * 
        18446744073709551645
        16295147905179352830000 
        2024782584832"""
    return one1*three3,((one1**3)-one1)*((three3**3)-three3)
def day10Joltages():
    path = f'day10Joltages.txt'
    numbers=[0]
    with open(path, 'r') as input:
        for line in input.readlines():
            numbers.append(int(line.rstrip()))#=input.readlines().splitlines()    #numbers = [int(n) for n in day10]
    numbers.sort()
    num3=[]
    #print(numbers)
    one1=0
    three3=0
    for i in range(1,len(numbers)):             #        print(f'{(numbers[i] if i%4==0 else "")}',end='')        print(f'{(numbers[i] if i >88 else "")}',end='')
        if numbers[i] - numbers[i-1] == 1:
            one1+=1
        else:
            three3+=1
            num3.append(numbers[i])
    else:
        onem=one1-1
        return one1*(three3+1),(((2**onem)+(three3+1)))  #day10Joltprt2(numbers,num3,one1,three3+1)        #[0, 1, 2, 3, 6, 7, 8, 9, 10, 13, 14, 17, 18, 19, 20, 21, 24, 27, 28, 29, 30, 31, 34, 35, 36, 39, 40, 41, 42, 43, 46, 49, 50, 51, 54, 57, 58, 59, 60, 61, 64, 65, 66, 67, 68, 71, 72, 73, 76, 77, 78, 79, 80, 83, 84, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 101, 104, 105, 108, 111, 112, 113, 114, 117, 118, 119, 122, 123, 124, 125, 128, 131, 132, 133, 134, 135, 138, 139, 142, 145, 146, 147, 148, 149, 153]
    lkd=0
    

def sumofsums(day9,cntlidx,psum,begin1):
    sumofs=0
    for oidx in range(begin1,cntlidx-1):
        sumofs+=day9[oidx]
        if sumofs > psum:
            return begin1,oidx,False
        elif sumofs == psum:
            return begin1,oidx,True 

def day9part2(day9,cntlidx,psum):
    sumsp=[]
    begin1=0
    for pidx in range(cntlidx):        #for oidx in range(pidx+1,cntlidx):
        sumsp.append(day9[pidx]+day9[pidx+1])
    sumequal= True
    #while sumequal:
    for pidx in range(begin1,cntlidx-1):
        begin1,end1,sumequal=sumofsums(day9,cntlidx,psum,pidx)
        if sumequal:     return min(day9[begin1:end1]) + max(day9[begin1:end1])    #    break
    #tmp1=day9[begin1] 55732936
    #tmp2=day9[begin1+1]
    #tmp3=day9[end1]
    #icntr=0
    #for oidx in range(begin1,end1):
    #    if day9[oidx] < day9[oidx+1]:
    #        if icntr<((end1 - begin1) / 2):
    #            begin1=oidx
    #        else:
    #            end1=oidx
    #            #break
    #    icntr+=1
    #    print(f'{day9[oidx]}',end='    ')
    #return day9[begin1]+day9[end1]
def foundsum(day9,asize,control,pbool):
    for pidx in range(asize):
        for oidx in range(pidx+1,asize): #this wont work    ap9=int(day9[pidx+cidx])    ao9=int(day9[oidx+cidx])    aa9=int(day9[cidx+asize])
            if pidx==oidx:
                lkd=0
            elif day9[pidx+control] + day9[oidx+control] == day9[asize+control]:
                pbool=True
                return pbool
            else:
                lkd=1
    #else:        if not pbool: return False        else: lkd=0
    #18527440    24097807    20804499    29896884    21250506    22674194    25441452    23472142    23804453    35735535    37205496    36695485    26983955    25254094    25584276    34697022 
    return pbool
def day9xmascipher():
    debugpy.debug_this_thread()
    path = 'day9xmascipher.txt'
    day9=[]
    asize=25            #de=deque([0]*asize,asize)
    with open(path, 'r') as file9:
        while line:=file9.readline().strip():
            day9.append(int(line))
        #day9 = file9.read().splitlines()            #for idx in range(asize):    #    de.appendleft(day9[idx])           
    upperrangA=len(day9)-(asize+1)    #    1000-26=974
    lastnumit=day9[999]
    pbool=False        #    firsttime=True#controller for 0+25 to len(day9) 1689 is too low
    for cidx in range(upperrangA):    #ans's[index] is 25-999 & cidx0-974
        if cidx == 145: 
            debugpy.breakpoint()
        #if cidx >0 and not pbool:
        #    print(f'day9^^^{cidx}^^^{day9[(cidx-1)+asize]}',end='    ')
        pbool=False
        if not foundsum(day9,asize,cidx,False):
            return cidx,day9[cidx+asize],day9part2(day9,cidx,day9[cidx+asize])
    return day9[upperrangA]
def day8infloopacc(nopcount,jmpcount,Limit):
    jmpycount=0
    nopycount=0
    accum=0
    linenum=0
    notunique=[]
    unicorn=[]
    FOUND=False
    path = f'day8infloopacc.txt'
    file8= open(path, 'r')
    lines = [line.strip() for line in file8.readlines() if line.strip()]
    file8.close()

    for pidx,pline in enumerate(lines): 
        pops= pline.split()[0]
        if pops  == 'jmp':
            jmpycount+=1
            if jmpycount == jmpcount:
                lines[pidx].replace('jmp','nop')
        elif pops == 'nop':
            nopycount+=1
            if nopycount == nopcount:
                lines[pidx].replace('nop','jmp')
        #if pline in unicorn:
        #    if pline.split()[0] == 'jmp':
        #        notunique.append(pline)
        #else:
        #    unicorn.append(pline)
    #print()
    notunique=[]
    unicorn=[]
    while True:        #for linenum,line in enumerate(lines):
        if accum > Limit: break
        ops,acc = lines[linenum].split(' ')
        if ops == 'acc':
            linenum+=1
            accum+= int(acc)
            #print(f'()={ops}{acc},accln={linenum},accum={accum}', end='    ')
        elif ops == 'jmp':
            linenum+=int(acc)
            #if linenum in unicorn:
            #    print(f'()={ops}{acc},jmpto={linenum},accum={accum}', end='***********************    ')
            #   # break
            #else:
            #    unicorn.append(linenum)
            #print(f'()={ops}{acc},jmpto={linenum},accum={accum}', end='    ')
            if linenum> len(lines) or linenum < 0: # or accum > 6000:
                break
            else:
                continue
        else:
            linenum+=1
            #print(f'()={ops}{acc},nopln={linenum},accum={accum}', end='    ')
    #if accum < 1000000:
    return accum
def day7bags():
    countline=0
    totalcommas=0
    largestline=0
    indexofMergeit=0
    countbags=0
    constChildLit='#'
    dedupe=[]
    mergeit=[]
    bagkvp=[]
    nextones=[]
    deadends=[]
    bloodys1=[]
    path = f'day7bagrules.txt'
    file1 = open(path, 'r')
    while True:
        line=file1.readline()
        line=line.strip()
        if line.__contains__('bags'):
            line=line.replace('bags','bag')
            line=line.replace('.','')
        countline += 1
        if not line:
            break
        if line.__contains__('contain'):
            root=line.split(' contain ')
            poproot=root[0]
            bagroot=root[1].split(', ')
            for bagchild in bagroot:                                                        #if str(bagchild).__contains__('bags'):                #    str(bagchild).replace('bags','bag')
                ptemp0=f'{constChildLit}{str(bagchild[2:])}'
                ptemp1=f'{ptemp0}'#' : {str(bagchild[0])}'
                dedupe.append(ptemp1)
                #if countline>42:                     breakpoint
                if len(mergeit) > 0:
                    #indexofMergeit= i
                    for i, j in enumerate(mergeit):
                        if j[:j.index('bag')+3] == ptemp0:
                            ptemp4=f'{str(mergeit[i])}, {poproot}'
                            mergeit[i]=ptemp4
                            break
                    else:
                        mergeit.append(f'{ptemp1} | {poproot}')   #if indexofMergeit == []:                        #    indexofMergeit = 0                        #if mergeit.__contains__(ptemp0):                        #if indexofMergeit == 0: # or indexofMergeit == []:                                    #else:                    #ptemp3=mergeit[i]
                        bagkvp.append(f'{ptemp0[1:]}')
                else:    
                    mergeit.append(f'{ptemp1} | {poproot}')
                    bagkvp.append(f'{ptemp0[1:]}')            
            if line.__contains__(','):
                countcommas=line.count(',') +1
            else:
                countcommas=1
            if countcommas > largestline:
                largestline=countcommas
            totalcommas+=countcommas            #bagchild = bagroot.split()            #Bag = namedtuple('Bag', dedupe)

    ntstr=  """
            # Basic example
            >>> Point = namedtuple('Point', ['x', 'y'])
            >>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
            >>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
            33
            >>> x, y = p                # unpack like a regular tuple
            >>> x, y
            (11, 22)
            >>> p.x + p.y               # fields also accessible by name
            33
            >>> p                       # readable __repr__ with a name=value style
            Point(x=11, y=22)"""
    #need to keep trak where we are at all get_top_n_items_from_list
    #When are we done
    WriteMergit(mergeit,bagkvp)
   
    usedbagsstr='shiny gold bag,'
    mergechild= 'shiny gold bag'
    masterliststr=str(mergeit[bagkvp.index(f'{mergechild}')])
    MASTERLIST=masterliststr.split('| ')[1].split(', ')
  # for tempaaaa in MASTERLIST: nextones.append(f'{constChildLit}{str(tempaaaa)}')
    for bagidx,bagval in enumerate(MASTERLIST):
        usedbagsstr,countbags,nextones,deadends=drilldownbags(bagval,usedbagsstr,countbags,bagkvp,mergeit,nextones,deadends,constChildLit)
    if len(nextones) > 0:
        for tempo in nextones:
            if usedbagsstr.__contains__(tempo):
                nextones.remove(tempo)
    if len(nextones) > 0:
        for nxtval in nextones:
            bloodys1.append(nxtval)
            nextones.remove(nxtval)
        for bldval in bloodys1:
            usedbagsstr,countbags,nextones,deadends=drilldownbags(bldval,usedbagsstr,countbags,bagkvp,mergeit,nextones,deadends,constChildLit)    
    return countline,largestline,totalcommas,countbags    
def WriteMergit(mergeit, bagkvp):
    file2=open('mergeit.txt','w')
    for ik in mergeit: file2.write(ik + '\n')
    else: file2.close()
    file3 =open('bagkvp.txt','w')
    for ji in bagkvp: file3.write(ji + '\n')
    else: file3.close()
def drilldownbags(mergechild, usedbagsstr,countbags,bagkvp,mergeit,nextones,deadends,constChildLit):
    #bagkvp=shiny gold bag,146#ABD 1 4 clear blue bag
    #use mergit to get all shiny gold bag
    if bagkvp.__contains__(mergechild):
        shinygoldindex= bagkvp.index(f'{mergechild}')#mergeit.index('#shiny gold bag : 146 | clear blue bag, bright coral bag, muted cyan bag, pale blue bag, dim maroon bag, light gray bag')
        usedbagsstr+=f'{mergechild}, '
        nextones.append(f'{mergechild}')
        countbags+=1
        sgb=str(mergeit[shinygoldindex])
        ss2=sgb.split('| ')[1].split(', ')
        for tempaaaa in ss2: nextones.append(f'{str(tempaaaa)}')
        ss3=[]
        ss4=[]
        for bagidx, bagdict in enumerate(ss2):
            ss3.append(f'{str(bagdict)}')    #        sn1= bagidx
            #nextones.append(f'{constChildLit}{str(st3)}')
        for childidx, childval in enumerate(ss3):#just get it from bagkvp
            #for mergidx,mergval in enumerate(mergeit): #need another subroutine
            if bagkvp.__contains__(childval):
                tempw=str(mergeit[bagkvp.index(f'{childval}')])
                nextones.append(str(childval))
                #for tmpidx,tmpval in enumerate(bagkvp):
                #if str(tmpval) == childval:
                #   tempw=str(mergeit[bagkvp.index(f'{childval}')])
                #me rgval has each single element of the mergeit
                #mergstr = str(mergval)
                mergstr3= tempw.split('| ')[1].split(', ')    #            mergstr2= str(mergstr1[1])            mergstr3=mergstr2.split(', ')
                for tempx in mergstr3:
                    if bagkvp.__contains__(f'{tempx}'):
                        if not usedbagsstr.__contains__(tempx):
                            countbags+=1
                            ss4.append(tempx)
                            usedbagsstr+=f'{tempx}, '
                            if nextones.__contains__(tempx): nextones.remove(tempx)
                        else:
                            countbags+=1
                            deadends.append(f'{tempx}, ')                    
                    else:
                        countbags+=1
                        deadends.append(f'{tempx}, ')
                        #nextones.remove(tempx)
    else:
        tempp=0#douhave the balls to recusivelly call this thing    
    return usedbagsstr,countbags,nextones,deadends
def day6answers():
    countline=0
    countanswers=0
    countgrouplines=0
    dup=0
    dedupe=[]
    mergeit=[]
    path = f'day6answers.txt'
    skiprestofgroup=False
    file1 = open(path, 'r')
    while True:
        line=file1.readline()
        countline += 1
        if not line:
            break
        if line == '\n':
            #if countgrouplines> 1:
            #    countanswers+=len(mer)
            countanswers+= len(dedupe)
            dedupe=[]
            mergeit=[]
            skiprestofgroup=False
            countgrouplines=0
        else:
            line=line.strip()
            countgrouplines+=1
            if skiprestofgroup:
                dup+=1
            else:
                if countgrouplines == 1:
                    for item in line:
                        dedupe.append(item)
                else:
                    for itema in line:
                        if dedupe.__contains__(itema):
                            mergeit.append(itema)
                        else:
                            dup+=1    
                    else:
                        if len(mergeit)>0:
                            dedupe.clear()
                            for ql in mergeit:
                                dedupe.append(ql)
                            else:
                                mergeit.clear()
                        else:
                            skiprestofgroup=True
                            dedupe.clear()
        
            #if len(line)>0:
            #    for item in line:
            #        if dedupe.__contains__(item):
            #            dup+=1
            #        else:
            #            dedupe.append(item)

        #linelen= len(line.strip())
        #if there are more than one line in a group=if countgrouplines> 1
        #countanswers += linelen
        #allseats.append(ishighest(line,largestseat))
        #countseats += 1
    countanswers+=len(dedupe)#else:
    #    print(seats)
    file1.close()
    #allseats.sort()
    return countanswers#l
def ishighest(line,largestseat):
    #if line[0] == "F":          #0-63
    #    if line[1] == "F":      #0-31
    #        if line[2] == "F":  #0-15
    #            if line[3] == "F":        #0-7
    #                if line[4] == "F":    #0-3
    #                    if line[5] == "F":#0-1
    #                        if line[6]  == "F":
    #                            seatdict = ["FFFFFFF" : 0]
    #                        else:           #0123456 
    #                            seatdict = ["FFFFFFB" : 1]
    #                    else:               #FBFBBFFRLR
    #                        if line[6] == "F":
    #                            seatdict = ["FFFFBBF" : 2]
    #                        else:           #0123456
    #                            seatdict = ["FFFFBBB" : 3]
    #                else:
    #                    if line[5] == "F": #4-7
    #                        if line[6]  == "F":
    #                            seatdict = ["FFFBFFF" : 4]
    #                        else:           #0123456
    #                            seatdict = ["FFFBFFB" : 5]
    #                    else:
    #                        if line[6] == "F"
    #                            seatdict = ["FFFBBFF" : 6]
    #                        else:           #0123456
    #                            seatdict = ["FFFBBBB" : 7]
    n = 7
    line=line.strip()
    row,seat = [line[i:i+n] for i in range(0, len(line), n)]
    brow= row.replace('F','0')
    crow= brow.replace('B','1')
    bseat= seat.replace('L' ,'0')
    cseat= bseat.replace('R','1')
    drow= int(crow,2)
    dseat=int(cseat,2)
    eseat=(drow*8)+dseat    #    print(f'line{line},row{crow},')
    if eseat > largestseat:
        largestseat=eseat
    #return largestseat
    return eseat
    SeatInfo = namedtuple('Seatinfo',[line,crow,cseat])
def day5SeatNumbers():
    countline=0
    countseats=0
    largestseat=0
    allseats=[]
    path = f'day5seatnumbers.txt'
    seats = binarytree.bst(height=6,is_perfect=True)
    file1 = open(path, 'r')
    while True:
        line=file1.readline()
        countline += 1
        if not line:
            break
        #largestseat= ishighest(line,largestseat)
        allseats.append(ishighest(line,largestseat))
        #countseats += 1
    #else:
    #    print(seats)
    file1.close()
    allseats.sort()
    return allseats#largestseat

def incrementstring(popopo):
    popopo.replace("['","")
    popopo.replace("']","")
    lot=0
    jot=''
    for tot in popopo:
        if str(tot).isdigit():
            jot= str(tot)
            lot= int(jot)
    lot += 1
    lot= int(popopo) + 1
    #uup+=1
    popopo=str(lot)
    return popopo

def ispassport(fieldsbbu):
    """  byr (Birth Year) - four digits; at least 1920 and at most 2002.
         iyr (Issue Year) - four digits; at least 2010 and at most 2020.
         eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
         hgt (Height) - a number followed by either cm or in:
         If cm, the number must be at least 150 and at most 193.
         If in, the number must be at least 59 and at most 76.
         hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
         ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
         pid (Passport ID) - a nine-digit number, including leading zeroes.
         cid (Country ID) - ignored, missing or not.       """
    byrpop=str(fieldsbbu.get('byr'))
    iyrpop=str(fieldsbbu.get('iyr'))
    eyrpop=str(fieldsbbu.get('eyr'))
    hgtpop=str(fieldsbbu.get('hgt'))
    hclpop=str(fieldsbbu.get('hcl'))
    eclpop=str(fieldsbbu.get('ecl'))
    pidpop=str(fieldsbbu.get('pid'))
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    if byrpop.isdigit() and byrpop > '1919' and byrpop < '2003':
        byr = True

    if iyrpop.isdigit() and iyrpop > '2009' and iyrpop < '2021':
        iyr = True 

    if eyrpop.isdigit() and eyrpop > '2019' and eyrpop < '2031':
        eyr = True 

    if hgtpop.__contains__('in'):
        if hgtpop > '58in' and hgtpop < '77in':
            hgt = True
    if not hgt:
        if hgtpop.__contains__('cm'):
            if hgtpop > '149cm' and hgtpop < '194cm':
                hgt = True            
    
    if (len(hclpop) == 7) and hclpop[0]== '#':
        for item in hclpop[1:]:
            if item < '0' or item.lower() > 'f':
                break
        else:
            hcl=True

    if eclpop == 'amb' or eclpop == 'blu' or eclpop == 'brn' or eclpop == 'gry' or eclpop == 'grn' or eclpop == 'hzl' or eclpop == 'oth':
        ecl = True
    
    if (len(pidpop) == 9) and pidpop.isdigit():
        pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        popopo = str(fieldsbbu.get("ppt"))
        fieldsbbu["ppt"]=incrementstring(popopo)
    else:
        popopo = str(fieldsbbu.get("fal"))
        fieldsbbu["fal"]=incrementstring(popopo)    #        print(f'falsedict={fieldsbbu}')        
    fieldsbbu={"byr":"", "iyr":"", "eyr":"", "hgt":"", "hcl":"", "ecl":"", "pid":"", "cid":"", "ppt": fieldsbbu.get("ppt"), "fal": fieldsbbu.get("fal")}        #return True     
    return fieldsbbu
def day4passports():
    countpassports = 0
    countline=0
    countfalse=0
    path = f'day4passports.txt'
    file1 = open(path, 'r')
   #passportdict=defaultdict(str)
    passportdict={"byr":"", "iyr":"", "eyr":"", "hgt":"", "hcl":"", "ecl":"", "pid":"", "cid":"", "ppt":'0', "fal":'0'}
    countppt=defaultdict(int)
    countppt["ppp"]=0
    countppt["faa"]=0
    print(countppt)
    #passportdict.update(countppt)
    while True:
        line = file1.readline()   # Get next line from file 
        countline +=1
        if not line: # if line is empty end of file is reached 
            break
        if line=='\n':
            passportdict = ispassport(passportdict)
        else:
            splitlinekvp = line.strip().split(' ')
            for ppkvp in splitlinekvp:
                ppkey, ppvalue= ppkvp.split(':',1)
                passportdict[ppkey]=str(ppvalue)
    #else:
    if ispassport(passportdict):
        countpassports+=1
        print(f'Lastdict={passportdict}')
    else:
        countfalse+=1
        print(f'LASTfalsedict={passportdict}')
        
    file1.close()
    print(f'countfalse={str(passportdict["fal"])}', end="    ")
    return str(passportdict["ppt"])
def passwordisvalid(line):
    #self.line = line
    lineparts = line.split(':',1)
    password=lineparts[1].strip()
    numberandchars = lineparts[0].split(' ',1)
    charactrinpassword= numberandchars[1].strip()
    numbersa = numberandchars[0].split(',')
    numbersb  = numbersa[0].split('-')
    numbersofcharmusthave = int(numbersb[0].strip())
    numberofcharmaxhave  = int(numbersb[1].strip())
    charcountpassword=0
    numberofcharmaxhave -=1
    numbersofcharmusthave -=1
    if password[numbersofcharmusthave] == charactrinpassword:
        charcountpassword +=1
    if password[numberofcharmaxhave] == charactrinpassword:
        charcountpassword +=1
    #countchar = password.count(charactrinpassword)
    #if numberofcharmaxhave >= countchar and numbersofcharmusthave <= countchar:
    if charcountpassword == 1:
        return True
    else:
        return False
def day2AdventOfCode():
    path = f'InputDay2Passwords.txt'
    # Python program to  demonstrate readline() 
    file1 = open(path, 'r') 
    count = 0
    while True: 
        line = file1.readline()   # Get next line from file 
        if not line: # if line is empty end of file is reached 
            break
        if (passwordisvalid(line)):
            count += 1
    file1.close()
    return count
def isitatree(line, column):
    if line[column] == '#':
        return True
    else:
        return False
def day3AdventOfCode(step):
    """
    read a line;add 3 to collumn ;check column>len(line)
    """
    path = f'InputDay3Trees.txt'
    #step = 3    
    column = 0
    count = 0    
    file1 = open(path, 'r') 
    line= file1.readline()
    linecnt = 1
    popo = len(line) -1    #line.strip() \n char
    while True:
        line= file1.readline()
        line= file1.readline()
        linecnt +=2
        if not line:
            break
        column +=step
        if column >= popo:   #not >= 31 because 31 is the last valid char
            print(f'col{column - popo}= col{column} - len(line){popo}', end="    ")
            column = column - popo    #(step - 1) - (column - popo)    #step-1= zero-based index
            
        if isitatree(line,column):
            count +=1
    file1.close()
    return count
def day3rdlineAdventOfCode():
    path = f'InputDay3Trees.txt'
    step = 3    
    file1 = open(path, 'r') 
    column = -1
    count = 0    #    while True:         # Print every second line.
    with open(path, 'r') as handle:
        for lineno, line in enumerate(handle):
            if lineno % step == 0:
                column +=3
                if column >= len(line):
                    column= len(line) - column
                    print(f'newcol={column}',end='    ')
                if (isitatree(line, column)):   # line = file1.readline()   # Get next line from file         if not line: # if line is empty end of file is reached             break           if (isitatree(line)):
                        count += 1
    handle.close()
    return count

def StringChallenge():
    shorty6=[]
    first_value = '  FIRST challenge         '
    second_value = '-  second challenge  -'
    third_value = 'tH IR D-C HALLE NGE'
    
    fourth_value = 'fourth'
    fifth_value = 'fifth'
    sixth_value = 'sixth'
    shorty6.append(f"b4={first_value}, {second_value}, {third_value}, {fourth_value}, {fifth_value}, {sixth_value}  ")
    # First challenge
    first_value = first_value.strip()
    first_value = first_value.lower()
    first_value = first_value.title()
    first_value = f'{first_value:^30}'
    
    # Second challenge
    second_value = second_value.replace('-', '')
    second_value = second_value.strip()
    second_value = second_value.capitalize()
    
    # Third challenge
    third_value = third_value.replace(' ', '')
    third_value = third_value.replace('-', ' ')
    third_value = third_value.swapcase()
    third_value = f'{third_value:>30}'
    
    shorty6.append(first_value)
    shorty6.append(second_value)
    shorty6.append(third_value)
    
    # Fourth challenge - use only the print() function (no f-strings)
    shorty6.append(f"{fourth_value}#{fifth_value}#{sixth_value}!")
    
    # Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
    #shorty6.append(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}', end='    ')
    shorty6.append(f"    {fourth_value}    ")
    shorty6.append(f"{fifth_value}    ")
    shorty6.append(f"{sixth_value}    ")
    sum=0    
    mixtup=['7']
    mixtup.append(7)
    mixtup.append(7.1)
    for x in mixtup:
        boolint=str(isinstance(x, int))[0]
        typeofx=str(type(x)).split()
        testtype=typeofx[1].replace('>','')
        if str(x).isnumeric():
            sum += int(x)
        elif str(x).isdecimal() or testtype.count('float')> 0:
            sum += float(x)
        else:
            print("problem Houston!", end='    ')
        print(f"type({x})={testtype},isinstance={boolint}", end='    ')
    else:
        print(f"sum={sum}", end='    ')
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']
        # print(f'0-based indexing into the list ... second item: {colors[1]}')
        # print(f'Last item of the list: {colors[-1]}')
        # print(f'Next to last item in the list: {colors[-2]}')
    shorty6.append(f"{colors}")
    shorty6.append(f'\nPrint a SLICE, colors[2:5], starting at index 2 and excluding 5: ')
    shorty6.append(f"{colors[2:5]}    ")
    
    shorty6.append(f'A slice, colors[:3], starting at index 0 to 3: ')
    shorty6.append(f'{colors[:3]}    ')

    shorty6.append('\nA slice, colors[4:], starting a index 4 to end: ')
    shorty6.append(f'{colors[4:]}    ')

    shorty6.append(f'A slice, colors[-4:-1], from the 4th from the (not the) end: ')
    shorty6.append(f'{colors[-4:-1]}    ')
    colors.reverse()
    shorty6.append(f'colors.reverse={colors}    ')
    colors.sort()
    shorty6.append(f'colors.sort={colors}    ')
    new_colors = ['lime', 'gray']
    colors.extend(new_colors)
    shorty6.append(f".extend(new_['lime', 'gray']={colors}")
    shorty6.append(r'r"print raw   \t\n\t\'\t    ')
    firststr = str.capitalize('conrad')
    secondstr = 'grant'.capitalize()
    thirdstr = 'bob'
    shorty6.append(f"{firststr} {secondstr}")
    shorty6.append(f"{firststr} {secondstr} {thirdstr.capitalize()}")
    shorty6.append(f"{firststr}-{secondstr}-{thirdstr}, sep='-',end=''")
    shorty6.append(f"{firststr}-{secondstr}-{thirdstr}")
    shorty6.append(f"{'Mississippi'.count('s')}")
    shorty6.append(f"{len('Mississippi')}")
    messagez = 'The quick brown fox jumps over the lazy dog'
    shorty6.append(f"{messagez.find('q')}")
    shorty6.append(f"{messagez.find('t')}")
    shorty6.append(f"{messagez.count('T')}")

    valuez = 'hi'
    print(f'{valuez:<5}', end='.    ')
    print(f'{valuez:>5}', end='.    ')
    print(f'{valuez:^5}', end='.   ')
    print(f"{valuez:-^5}", end='    ')
    return shorty6
 
def Calculator(commands=[0], is_console_read=True):
    commandindex = 0
    if len(commands) > 0 and is_console_read:
        exit(6969)
    first_nums = getNum(commandindex, commands, is_console_read)
    first_numeric= first_nums[0]
    commandindex = first_nums[1]
    operatorsxyz = getOperator(commandindex, commands, is_console_read)
    operator     = operatorsxyz[0]
    commandindex = operatorsxyz[1]
    secondnums = getNum(commandindex, commands, is_console_read)
    secondnumeric= secondnums[0]
    commandindex = secondnums[1]
    return getanswer(first_numeric, secondnumeric, operator)
def getNum(commandindex, commands=[0], is_console_read=True):
    while True:
        if is_console_read:
            first_operand = input("please enter a valid number: ")
        else:
            first_operand=commands[commandindex]
            commandindex += 1
        if str(first_operand).isnumeric():
            break
        else:
            print(f"Err#{first_operand}",end='!   ')
    numericx=[int(first_operand), commandindex] 
    return numericx
def getOperator(commandindex, commands=[0], is_console_read=True):
    opers=['+','-','*','/','%','**']
    lasto=''
    while True:
        if is_console_read:
            first_operand = input("please enter a Operator(+,-,*,/,%,**): ")
        else:
            first_operand=commands[commandindex]
            commandindex += 1
        fox=opers.count(first_operand)
        if fox > 0:
            lasto=first_operand
            break
        else:
            print(f"ErrO{first_operand}",end='!   ')
    numericy=[lasto, commandindex] 
    return numericy

def getanswer(first_operand, second_operand, operation):
    if operation == '+':
        return first_operand + second_operand
    if operation == '-':
        return first_operand - second_operand
    if operation == '*':
        return first_operand * second_operand
    if operation == '/':
        return first_operand / second_operand
    if operation == '%':
        return first_operand % second_operand
    if operation == '**':
        return first_operand ** second_operand
    
def gocurrent(comman=[0],is_console_input=True):
    commandindex = 0
    if len(comman) > 0 and is_console_input:
        exit(6969)
    count = 0
    pr1 = pr2 = 0
    if is_console_input:
        pl1= input("Player One, Tell me your name: ")
        pl2= input("Player Two, Tell me your name: ")
    else:
        pl1=comman[commandindex]
        commandindex+=1
        pl2=comman[commandindex]
        commandindex+=1
    while pr1 != 5 and pr2 !=5:
        pr1=random.randint(1,5)
        print(f"{pl1} rolls {pr1}",end=',    ')
        count += 1
        pr2 = random.randint(1,5)
        print(f"{pl2} rolls {pr2}",end=',    ')
        count += 1
    else:
        if pr1 == 5:
            print(f"wow {pl1}, it took {count} rolls for you two to roll a 5!",end=',    ')
        elif pr2 == 5:
            print(f"wow {pl2}, it took {count} rolls for you two to roll a 5!",end=',    ')
def dicerollMS(comman=[0],is_console_input=True):
    rollx = 0
    count = 0
    commandindex = 0
    print("First person to roll a 5 wins!",end=',    ')
    while rollx != 5:
        if is_console_input:
            name = input('Enter a name, or \'q\' to quit:  ' )
        else:
            name = comman[commandindex]
            commandindex += 1
       
        if name.strip() == '':
            continue

        if name.strip() == 'q':
            break
  
        count = count + 1
        rollx = random.randint(1, 5)
        print(f'{name} rolled {rollx}',end='    ')
    else:
        print(f'{name} Wins!!!',end='    ')

    print(f'You rolled the dice {count} times.', end='    ')
def newguess():
    import random

    value = random.randint(1, 10)
    count = 0
    guess = 0
    print('Guess a number between 1 and 10')

    while guess != value:
        count += 1
        guess = input(f'Enter guess #{count}: ')

        if guess.isnumeric():
            guess = int(guess)
        else:
            print('Numbers only, please!')
            continue

        if guess > value:
            print('Your guess is too high, try again!')
        elif guess < value:
            print('Your guess is too low, try again!')

    else:
        print(f'You guessed it in {count} tries!')
def mothodlog():
    logging.basicConfig(format='%(threadName)s %(message)s')
    logging.error('hello, from mothodlog')
        #MainThread hello
def threadsafePrint():
    thread_name = threading.current_thread().name       #threading.current_thread().name#   __name__()   # Thread.getName()
    for letter in 'ABC':        #threading.currentThread.n
        thread_safe_print(f'[{thread_name} {letter}]', end='    ')
        
lock = threading.Lock()

def thread_safe_print(*args, **kwargs):
    with lock:
        print(*args, **kwargs)