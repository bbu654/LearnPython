def printit():
    print("String usage:             \t\t'...' in Strng - => bool  ")
    print("len(String)    - CharCount\t\tString.find()  - => index \t\tString.replace() -   ")
    print("String.upper() - UPPERCASE\t\tString.lower() - lowercase\t\tString.title()  - CamelCase  ")
    print("    ")
    print("    ")
    print("Arithmetic operators")
    print("10//3          => int     \t\tx += 3,+,-,*,             \t\t/ => floating point")
    print("operator precedance first to last: (),**,/,*,//,%,+,- \t\t\t\tround() abs() import math math.ceil\n")
    #return("hello from bbutils")

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




