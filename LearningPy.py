import distutils
import distutils.util
class Patient:
    def __init__(self, name, age, is_new):
        self.name = name
        self.age = age
        self.is_new = is_new

    def printpatient(self):
        if self.is_new:
            notlit = ""
        else: #ifelse is_hot:
            notlit = "not "
        print(f"{self.name} is {notlit}a new patient. He is {self.age}.")

iname = "Brice" #input("Name: ")
iage = 42 #int(input("Age: "))
some_string = "false"#input("True or False: RUANewPatient? ")
iisnew = bool(distutils.util.strtobool(some_string))

class LoanEligibility:
    def __init__(self2, loan_amount, has_high_income, has_good_credit, is_criminal):
            self2.loan_amount = loan_amount
            self2.has_high_income = has_high_income
            self2.has_good_credit = has_good_credit
            self2.is_criminal = is_criminal
    def print_eligible(self2):
        if not self2.is_criminal:
            if self2.has_good_credit:
                if self2.has_high_income:
                    print(f"Congratulations! You are ELIGIBLE for a Loan! You have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.1}")
                else:
                    print(f"Congratulations! You are ELIGIBLE for a Loan! You don't have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}")
            else:
                print(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And don't have Good Credit And you do NOT have a criminal record. ")
        else:
            if self2.has_good_credit:
                if self2.has_high_income:
                    print(f"SORRY! You are not ELIGIBLE for a Loan! You have a High Income And have Good Credit And you do have a criminal record. ")
                else:
                    print(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And have Good Credit And you do have a criminal record. ")
            else:
                print(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And don't have Good Credit And you do have a criminal record. ")
price = 1000000
hashighincome = True
hasgoodcredit=True
iscriminal=False
p1 = Patient(iname, iage, iisnew)
p1.printpatient()
print("String usage:             \t\t'...' in Strng - => bool  ")
print("len(String)    - CharCount\t\tString.find()  - => index \t\tString.replace() -   ")
print("String.upper() - UPPERCASE\t\tString.lower() - lowercase\t\tString.title()  - CamelCase  ")
print("    ")
print("    ")
print("Arithmetic operators")
print("10//3          => int     \t\tx += 3,+,-,*,             \t\t/ => floating point")
print("operator precedance first to last: (),**,/,*,//,%,+,- \t\t\t\tround() abs() import math math.ceil")          

if hasgoodcredit:
    downpayment =price * 0.1
else:
    downpayment =price * 0.2
print(f"Down payment is ${downpayment}")
print(f"Down payment is ${(price * 0.1 if hasgoodcredit else price * 0.2)}")
eligibility = LoanEligibility(price,hashighincome,hasgoodcredit,iscriminal)
eligibility.print_eligible()    
print(f"""{('Congratulations' if hasgoodcredit and not iscriminal else 'SORRY')}! 
You are {('' if hasgoodcredit and not iscriminal else 'not ')}ELIGIBLE for a Loan! 
You do{('' if hashighincome else ' not')} have a High Income 
And do{('' if hasgoodcredit else ' not')} have Good Credit 
And you do{(' NOT' if not iscriminal else '')} have a criminal record.
{('Your Down Payment is $' if hasgoodcredit and not iscriminal else '')}{(downpayment if hasgoodcredit and not iscriminal else '')}
""")

i=1
while i <= 5:
    k=i
    popp=''
    while k<=5:
        popp=popp + ' ' 
        k+=1
    #pooo='@' * i
    print(f"{popp}{'@' * i}{'@' * i}")
#    print(pop)
    i+=1
else:
    print("     @@")
#    print("     @@")
#from termcolor import colored
#print(colored('hello', 'red'), colored('world', 'green'))

#TGREEN =  '\033[32m' # Green Text
#ENDC = '\033[m' # reset to the defaults

#print (TGREEN + "Das ist es!" , ENDC)
#print (TGREEN + "This is some green text!")

class secretgame:
    def __init__(self3, secretnumber=9, guesslimit=3):
        self3.secretnumber=secretnumber
        self3.guesslimit=guesslimit        
        
    def secretguess(self3, listguess=[0]):
        self3.listguess=list(listguess)
        guesscount=1
#        while guesscount < self3.guesslimit:
        for x in self3.listguess:
            if self3.listguess == 0:
                self3.listguess1 = int(input("Guess(1,2,3): "))
#            guesscount += 1
            if x==self3.secretnumber:
                print("You won!")
                break
        else:
            print("Sorry you didnt guess correctly")
guesslist=[6,8,9]
sg=secretgame(9,3)
sg.secretguess(guesslist)
guesslist2=[6,8,5]
sg.secretguess(guesslist2)
#sg.secretquess(1,9,8,7)



    