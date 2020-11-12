import sys, math, abc, distutils, distutils.util as dutil, bbuclassy
bbuclassy.pebbu()
shorty=[""]
iname = "Brice" #input("Name: ")
iage = 42 #int(input("Age: "))
some_string = "false"#input("True or False: RUANewPatient? ")
iisnew = bool(dutil.strtobool(some_string))
price = 1000000
hashighincome = True
hasgoodcredit=True
iscriminal=False

p1=bbuclassy.Patient(iname, iage, iisnew)
shorty.append( p1.printpatient())    

if hasgoodcredit:
    downpayment =price * 0.1
else:
    downpayment =price * 0.2
shorty.append(f"Down payment is ${downpayment}")
shorty.append(f"Down payment is ${(price * 0.1 if hasgoodcredit else price * 0.2)}")
eligibility = bbuclassy.LoanEligibility(price,hashighincome,hasgoodcredit,iscriminal)
shorty.append(eligibility.return_eligible())    
shorty.append(f"""{('Congratulations' if hasgoodcredit and not iscriminal else 'SORRY')}! You are {('' if hasgoodcredit and not iscriminal else 'not ')}ELIGIBLE for a Loan! You do{('' if hashighincome else ' not')} have a High Income And do{('' if hasgoodcredit else ' not')} have Good Credit And you do{(' NOT' if not iscriminal else '')} have a criminal record. {('Your Down Payment is $' if hasgoodcredit and not iscriminal else '')}{(downpayment if hasgoodcredit and not iscriminal else '')}""")

from termcolor import colored as cp
shorty.append(cp('hello', 'red'))
shorty.append(cp('world', 'green'))
#TGREEN =  '\033[32m' # Green Text\
#ENDC = '\033[m' # reset to the defaults
#print (TGREEN + "Das ist es!" , ENDC)
#print (TGREEN + "This is some green text!")
guesslist=[6,8,9]
sg= bbuclassy.secretgame(9,3)
shorty.append(sg.secretguess(guesslist))
guesslist2=[6,8,5]
shorty.append(sg.secretguess(guesslist2))
print(sys.builtin_module_names)
#sg.secretquess(1,9,8,7)
rp=bbuclassy.mspy("WW84","WW84")
shorty.append(rp.returnpop())
# Try to decode the word "terra"
shorty.append(f"Shifting terra by 13 gives: {rp.lassoWord( 'terra', 13 )}" )
print()
shorty.append(f"pi * 3= {math.pi*3}")
print(shorty)


    