def pebbu():
    #print("Hello from bbuclassy")
    #print("    ")
    #print("    ")
    print("String usage:             \t\t'...' in Strng - => bool  ")
    print("len(String)    - CharCount\t\tString.find()  - => index \t\tString.replace() -   ")
    print("String.upper() - UPPERCASE\t\tString.lower() - lowercase\t\tString.title()  - CamelCase  ")
    #print("    ")
    print("    ")
    print("Arithmetic operators")
    print("10//3          => int     \t\tx += 3,+,-,*,             \t\t/ => floating point")
    print("operator precedance first to last: (),**,/,*,//,%,+,- \t\t\t\tround() abs() import math math.ceil")          
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
    def __init__(self, name, age, is_new):
        self.name = name
        self.age = age
        self.is_new = is_new
        #
    def printpatient(self):
        if self.is_new:
            notlit = ""
        else: #ifelse is_hot:
            notlit = "not "
        return f"{self.name} is {notlit}a new patient. He is {self.age}."



class secretgame:
    def __init__(self3, secretnumber=9, guesslimit=3):
        self3.secretnumber=secretnumber
        self3.guesslimit=guesslimit        
        
    def secretguess(self3, listguess=[0]):
        self3.listguess=list(listguess)
        guesscount=0
        is_console = False
        while guesscount < self3.guesslimit:
#        for x in self3.listguess:
            if len(self3.listguess) != self3.guesslimit:
                is_console=True
            if is_console:
                x = int(input(f"{self3.guesslimit-guesscount} Guess's(1,2,3) left: ")) #     x=singleguess
            else:
                x=self3.listguess[guesscount]
            guesscount += 1
            if x==self3.secretnumber:
                return("You won!")    #                break
        else:
            return("Sorry you didnt guess correctly")



            
class LoanEligibility:
    def __init__(self2, loan_amount, has_high_income, has_good_credit, is_criminal):
            self2.loan_amount = loan_amount
            self2.has_high_income = has_high_income
            self2.has_good_credit = has_good_credit
            self2.is_criminal = is_criminal
    def return_eligible(self2):
        if not self2.is_criminal:
            if self2.has_good_credit:
                if self2.has_high_income:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.1}")
                else:
                    return(f"Congratulations! You are ELIGIBLE for a Loan! You don't have a High Income And Good Credit And you do NOT have a criminal record. Your Down Payment is {self2.loan_amount * 0.2}")
            else:
                return(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And don't have Good Credit And you do NOT have a criminal record. ")
        else:
            if self2.has_good_credit:
                if self2.has_high_income:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You have a High Income And have Good Credit And you do have a criminal record. ")
                else:
                    return(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And have Good Credit And you do have a criminal record. ")
            else:
                return(f"SORRY! You are not ELIGIBLE for a Loan! You don't have a High Income And don't have Good Credit And you do have a criminal record. ")
class mspy:
    def __init__(self4, args, pop):
        self4.args = args
        self4.pop = pop
    def returnpop(self4):
         # Associate the variable diana with the value "WONDER WOMAN 1984"
         diana = "WONDER WOMAN 1984"
         # Print a message with the true identity of Diana
         self4.pop += (f"I believe Diana is actually {diana}!    ")
         self4.pop += (f"I believe Diana is actually {diana}!    ")
         self4.pop += (f"I believe Diana is actually {diana}!    ")
         # This is a comment that won't be interpreted as a command.
         return(f"Hello, Themyscira! {self4.pop}")          
    def lassoWord(self4, word, shiftAmount ):
        decodedWord = ""    
        for letter in word:
            decodedLetter = mspy.lassoLetter(self4, letter, shiftAmount)
            decodedWord = decodedWord + decodedLetter
        return decodedWord
    # Define a function to find the truth by shifting the letter by the specified amount
    def lassoLetter( self4, letter, shiftAmount ):
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
    