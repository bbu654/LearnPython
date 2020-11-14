import math, sys, bbutils, distutils, distutils.util as dutil, pprint

iname = "Brice" #input("Name: ")
iage = 42 #int(input("Age: "))
some_string = "false"#input("True or False: RUANewPatient? ")
iisnew = bool(dutil.strtobool(some_string))
bb=bbutils
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
print(elgibilty.return_eligible())
#for x in [shorty]:
#    print(x)bimnames[str]=sys.builtin_module_names
#print('Count built-in modules: %d' %len(sys.builtin_module_names)); 
line2=""
index2=0
lotsofstr="y="
modlst=["x="]
#pop=int(sys.builtin_module_names.count())
str00=""
str01=""
str02=""
str03=""
str04=""
str05=""
str06=""
str07=""
str08=""
str09=""

pop6=len(sys.builtin_module_names)
mlindex=0
while mlindex < pop6:
    if mlindex ==0:
        str00=str(sys.builtin_module_names[mlindex])
    if mlindex == 1:
        str01=str(sys.builtin_module_names[mlindex])
    if mlindex ==2:
        str02=str(sys.builtin_module_names[mlindex])
    if mlindex ==3:
        str03=str(sys.builtin_module_names[mlindex])
    if mlindex ==4:
        str04=str(sys.builtin_module_names[mlindex])
    if mlindex ==5:
        str05=str(sys.builtin_module_names[mlindex])
    if mlindex ==6:
        str06=str(sys.builtin_module_names[mlindex])
    if mlindex ==7:
        str07=str(sys.builtin_module_names[mlindex])
    if mlindex ==8:
        str08=str(sys.builtin_module_names[mlindex])
    if mlindex ==9:
        str09=str(sys.builtin_module_names[mlindex])
    shorty.append(f"    {str(sys.builtin_module_names[mlindex])}    ")
    print(sys.builtin_module_names[mlindex])
    modlst.append(f"    {str(sys.builtin_module_names[mlindex])}    ")
    mlindex += 1
for x in [modlst]:
    print(f"x={x}")
print(f"str00={str00},\t{str01},\t{str02},\t{str03},\t{str04}.")
print(f"str05={str05},\t{str06},\t{str07},\t{str08},\t{str09}.")#print(str01)
#for x in [sys.builtin_module_names]:            #sys.builtin_module_names A tuple of strings print for loop each
#    print(f"tuple{index2}={x}\t")
#    index2 += 1
    #index3 = 0
    #for y in [x]:
    #    print(f"string{index3}={y}")
    #    index3 += 1
    #line2 += x.__name__
    #if index2 % 6 == 0:
    #    line2+="\n"
    #index2+=1
fargo1 = 'I think '
chucky=bb.mspy(fargo1)
shorty.append(chucky.returnpop())#blockofgold=bbutils.mspy.returnpop(4,fargo1)
pp2=pprint.PrettyPrinter(indent=2,width=104,stream=None,compact=True)
#pp2.pprint(sys.builtin_module_names)
#print(line2)
year=1984
print(f"the year is {year}")
year +=36
print(f"the year is now {year}")
if year==1984:
    print("answering machine msg")
if year == 2020:
    print("voice mail")
activity= input("spend an evening? A) Read a book or B) Party! ")
print(f"You chose: {activity}")
if activity=='A':
    print("Nice choice")
elif activity=='B':
    print("Better choice")
else:
    print('You should have entered "A" or "B" Lets just say you like to read')
    activity="A"

 # ask the candidate a second question
job = input( "What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n" )
if job == "A":
    print( "Curator, Nice choice!" )
elif job =="B":
    print( "Running a business? Sounds fun!" )
else:
    print("You must type A or B, let's just say you want to be a curator at the Smithsonian")
    job = "A"
 # ask the candidate a third question
value = input( "What's more important?\n(A) Money\n(B) Love\n" )
if value == "A":
    print( "Money, Nice choice!" )
elif value =="B":
    print( "Love? Sounds fun!" )
else:
    print("You must type A or B, let's just say money is more important to you.")
    value = "A"

# ask the candidate a fourth question
decade = input( "What's your favorite decade?\n(A) 1910s\n(B) 1980s\n" )
if decade == "A":
    print( "1910s, Nice choice!" )
elif decade =="B":
    print( "1980s? Sounds fun!" )
else:
    print("You must type A or B, let's just say the 1910s is your favorite decade.")
    decade = "A"

# ask the candidate a fifth question
travel = input( "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n" )
if travel == "A":
    print( "Driving, Nice choice!" )
elif travel =="B":
    print( "Flying? Sound fun!" )
else:
    print("You must type A or B, let's just say your favorite way to travel is by driving")
    travel = "A"

# print out their choices
print( f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")   

# create some variables for scoring
diana_like = 0
steve_like = 0
max_like = 0
barbara_like = 0

# update scoring variables based on the weapon choice
if activity == "A":
    diana_like = diana_like + 1
    barbara_like = barbara_like + 1
else:
    max_like = max_like + 1
    steve_like = steve_like + 1

# update scoring variables based on the job choice
if job == "A":
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
    steve_like = steve_like - 1
else:
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diana_like = diana_like - 1
    max_like = max_like + 2
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 2
    barbara_like = barbara_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    steve_like = steve_like + 2
    diana_like = diana_like + 1
else:
    max_like = max_like + 1
    barbara_like = barbara_like + 2

# update scoring variables based on the travel choice
if travel == "A":
    max_like = max_like + 2
    barbara_like = barbara_like - 1
else:
    diana_like = diana_like + 1
    steve_like = steve_like + 1

# print the results depending on the score
if diana_like >= 6:
    print( "You're most like Wonder Woman!" )
elif steve_like >= 6:
    print( "You're most like Steve Trevor!" )
elif barbara_like >= 6:
    print( "You're most like Barbara Minerva!")
else:
    print( "You're most like Max Lord!")
shorty.append(chucky.chant())
chucky.uselasso()
shorty.append( "Shifting WHY by 13 gives: \n" + chucky.lassoWord( "WHY", 13 ) )
shorty.append( "Shifting oskza by -18 gives: \n" + chucky.lassoWord( "oskza", -18 ) )
shorty.append( "Shifting ohupo by -1 gives: \n" + chucky.lassoWord( "ohupo", -1 ) )
shorty.append( "Shifting ED by 25 gives: \n" + chucky.lassoWord( "ED", 25 ) )
shorty.append(chucky.lassoWord("terra",13))
pp2.pprint(shorty)


#bbutils.show_acceptable_modules()import pickle, pickletools#serialize/deserialize objects/streams pickle.