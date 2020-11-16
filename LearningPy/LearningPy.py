import math
import sys
import bbutils as bb
import distutils
import distutils.util as dutil 
import pprint

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
line2=""
index2=0
lotsofstr="y="
modlst=["x="]
#pop=int(sys.builtin_module_names.count())
pop6=len(sys.builtin_module_names)
mlindex=0
while mlindex < pop6:
    shorty.append(f"    {str(sys.builtin_module_names[mlindex])}    ")
    #print(sys.builtin_module_names[mlindex])
    modlst.append(f"    {str(sys.builtin_module_names[mlindex])}    ")
    mlindex += 1
for x in [modlst]:
    shorty.append(f"x={x}")
shorty.append(f"str00={modlst[0]},\t{modlst[1]},\t{modlst[2]},\t{modlst[3]},\t{modlst[4]}.")
shorty.append(f"str05={modlst[5]},\t{modlst[6]},\t{modlst[7]},\t{modlst[8]},\t{modlst[9]}.")#print(str01)
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
pp2.pprint(shorty)


#bbutils.show_acceptable_modules()import pickle, pickletools#serialize/deserialize objects/streams pickle. +=