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
    modulelists=list(sys.builtin_module_names)
    for y in [modulelists]:
        print(y)


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

    def returnpop(self5):
         # Associate the variable diana with the value "WONDER WOMAN 1984"
         diana = "WW84"
         # Print a message with the true identity of Diana
         self5.fargo += (f"Diana is {diana}!    ")
         self5.fargo += (f"Diana is {diana}!    ")
         self5.fargo += (f"Diana is {diana}!    ")
         # This is a comment that won't be interpreted as a command.
         return(f"Hello, Themyscira! {self5.fargo}")          

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

    def chant(self5):#Diana is {diana}!    Wonder Women 1984
        return("Chant= "+self5.fargo + self5.fargo + self5.fargo)

    def uselasso(self5):
        print("ok")