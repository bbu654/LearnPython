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
        print(f"{popp}{'@' * i}{'@' * i}")#    print(pop)
        i+=1
    else:
        print("     @@\n")#    print("     @@")


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
    def __init__(self4, secretnumber=9, guesslimit=3):
        self4.secretnumber=secretnumber
        self4.guesslimit=guesslimit        
        
    def secretguess(self4, listguess=[0]):
        self4.listguess=list(listguess)
        guesscount=0
        is_console = False
        while guesscount < self4.guesslimit:
#        for x in self4.listguess:
            if len(self4.listguess) != self4.guesslimit:
                is_console=True
            if is_console:
                x = int(input(f"{self4.guesslimit-guesscount} Guess's(1,2,3) left: ")) #     x=singleguess
            else:
                x=self4.listguess[guesscount]
            guesscount += 1
            if x==self4.secretnumber:
                return("You won!")    #                break
        else:
            return("Sorry you didnt guess correctly")




import shutil
import pkgutil

def show_acceptable_modules():# modules = {         module        for _, module, package in list(pkgutil.iter_modules())}#        if package is False    }
    line2 = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line2, 'Module', 'Location', line2))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))
import sys

def listmodules():
    line2=""
    index2=0
    strs=[]
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
    if not True:
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
            for y in range(yin):
                shorty5.append(f"{chr(x+aascii)},{y}    ")
            shorty5.append('                                                                 ')
        matrix = [   [1,2,3],[4,5,6],[7,8,9]]
        for row in matrix:
            for item in row:
                shorty5.append(f"{item}    ")
            shorty5.append(f"                                                                       ")
        numbersz=[5,2,1,9,3,5]
        shorty5.append(f"before pop={numbersz}")
        numbersz.pop()
        shorty5.append(f"after  pop={numbersz}")
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
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

#prCyan("Hello World, ") 
#prYellow("It's") 
#prGreen("Geeks") 
#prRed("For") 
#prGreen("Geeks") 
# Python program to print 
# colored text and background 
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

 