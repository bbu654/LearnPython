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

