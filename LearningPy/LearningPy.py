import math, sys, bbutils, distutils, distutils.util as dutil, pprint




iname = "Brice" #input("Name: ")
iage = 42 #int(input("Age: "))
some_string = "false"#input("True or False: RUANewPatient? ")
iisnew = bool(dutil.strtobool(some_string))
bb=bbutils
shorty=[]
bb.printit()

p1 = bb.Patient(iname, iage, iisnew)
shorty.append( p1.returnpatient())
price = 1000000
hashighincome=True
hasgoodcredit=True
iscriminal=False
if not iscriminal:
    shorty.append(f"Down payment is ${(price * 0.1 if hasgoodcredit and hashighincome else price * 0.2)}")
    if hasgoodcredit and hashighincome:
        shorty.append(f"Down payment is ${price * 0.1}")
    else:
        shorty.append(f"Down payment is ${price * 0.20}")
    
elgibilty = bb.LoanEligibility( loan_amount=price, has_high_income=hashighincome, has_good_credit=hasgoodcredit, is_criminal=iscriminal)
print(elgibilty.return_eligible())
#for x in [shorty]:
#    print(x)
bimnames=sys.builtin_module_names           #sys.builtin_module_names A tuple of strings print for loop each
line2=""
index2=0
for x in [sys.builtin_module_names]:
    print(f"tuple{index2}={x}\t")
    index2 += 1
    #index3 = 0
    #for y in [x]:
    #    print(f"string{index3}={y}")
    #    index3 += 1
    #line2 += x.__name__
    #if index2 % 6 == 0:
    #    line2+="\n"
    #index2+=1
pp2=pprint.PrettyPrinter(indent=2,width=104,stream=None,compact=True)
pp2.pprint(sys.builtin_module_names)
#print(line2)
pp2.pprint(shorty)
import shutil
import pkgutil

def show_acceptable_modules():
    line = '-' * 100
    print('{}\n{:^30}|{:^20}\n{}'.format(line, 'Module', 'Location', line))
    for entry in pkgutil.iter_modules():
        print('{:30}| {}'.format(entry[1], entry[0].path))

#show_acceptable_modules()
import pickle, pickletools
#pickle.