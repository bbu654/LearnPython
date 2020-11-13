import math, sys, bbutils, distutils, distutils.util as dutil
class Patient:
    def __init__(self1, name, age, is_new):
        self1.name = name
        self1.age = age
        self1.is_new = is_new

    def printpatient(self1):
        if self1.is_new:
            notlit = ""
        else: #ifelse is_hot:
            notlit = "not "
        print("{} is {}a new patient. He is {}.".format(self1.name, notlit, self1.age))

iname = "Brice" #input("Name: ")
iage = 42 #int(input("Age: "))
some_string = "false"#input("True or False: RUANewPatient? ")
iisnew = bool(dutil.strtobool(some_string))
bb=bbutils
shorty=[]
shorty.append(bb.printit())
class LoanEligibility:
    def __init__(self2, loan_amount, has_high_income, has_good_credit, is_criminal):
            self2.loan_amount = loan_amount
            self2.has_high_income = has_high_income
            self2.has_good_credit = has_good_credit
            self2.is_criminal = is_criminal
    def print_eligible(self2):
        incomelit="You don't have a High Income, "
        creditlit="and don't have Good Credit, "
        criminalit="and you do NOT have a criminal record. "
        eligiblelit="SORRY! You are not ELIGIBLE for a Loan! "
        line1=f"{(eligiblelit if self2.is_criminal else eligiblelit.replace('SORRY! You are not','Congratulations! You are'))}{incomelit}{creditlit}{criminalit}"
        if not self2.is_criminal:
            if self2.hasgoodcredit:
                if self2.has_high_income:
                    print(f"Congratulations! You are ELIGIBLE for a Loan! You have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.1}.")
                else:
                    print(f"Congratulations! You are ELIGIBLE for a Loan! You don't have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}.")
            else:
                print(f"Congratulations! You are ELIGIBLE for a Loan! You don't have a High Income, and don't have Good Credit, and you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}.")

        else:
            if self2.hasgoodcredit:
                if self2.has_high_income:
                    print(f"SORRY! You are not ELIGIBLE for a Loan! You have a High Income, and Good Credit, and you do have a criminal record.")
                else:
                    print(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income, and Good Credit, and you do have a criminal record.")
            else:
                print(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income, and don't have Good Credit, and you do have a criminal record. ")



p1 = Patient(iname, iage, iisnew)
p1.printpatient()
price = 1000000
hashighincome=True
hasgoodcredit=True
iscriminal=True
if hasgoodcredit:
    print(f"Down payment is ${price * 0.1}")
else:
    print(f"Down payment is ${price * 0.2}")
print(f"Down payment is ${(price * 0.1 if hasgoodcredit else price * 0.2)}")