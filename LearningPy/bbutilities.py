import colorama, time, functools, collections
from functools import wraps
from statistics import mean as avg
#@bbutilities.atimer

def atimer(func):    # a timer decorator from "Python Cookbook chapter 9.2"
    @wraps(func)
    def timerwrapper(*args, **kwargs):
        timerstart=time.time()
        funcresult=func(*args, **kwargs)
        timerend=time.time()
        print(f'{func.__name__}: {timerend-timerstart}',end='        ')
        return funcresult
    return timerwrapper

@atimer    
def dontknow():
    shorty=[] # 456789012
    name = 'Imtiaz Abedin'
    try:               # Write the suspicious block of code
       shorty.append(name[12])
    except AssertionError as assertE:  # Catch a single exception
       shorty.append(f'AssertionError={assertE}')# This block will be executed if exception A is caught
    except (EnvironmentError, SyntaxError, NameError) as ESNE:  # catch multiple exception
       shorty.append(f"Environment, Syntax, or NameError={ESNE}") # This block will be executed if any of the exception B, C or D is caught
    except Exception as exc:   # This block will be executed if any other exception other than A, B, C or D is caught
       shorty.append(f' Any Other Exception exc={exc}')               
    else:            # If no exception is caught, this block will be executed
       shorty.append(f"if no exception is caught, this will be executed")
    finally:
       shorty.append(f"This block will be executed FINALLY, and it is a must!")
    shorty.append('This will be printed, after the finally s.')
    journaldevRecap="""
        Here you can see that, we use except keyword in different style. 
        The first except keyword is used to catch only one exception that is AssertionError exception.
        However, the second except keyword is used to catch multiple exceptions, as you see.
        If you use except keyword without mentioning any specific exception, 
        it will catch any exception that is raised by the program.
        The else block will be executed if no exception is found. 
        Lastly, whether any exception is caught or not, the finally block will be executed.
        So, if you run the above code, we will get the output:
        python exception handling, python try except
        If you change ‘name[15]’ to ‘nameee[15]’ in the above code, 
        you will get the following output.
            python try except finally exception handling
        Python Exception Handling Important Points
        For undergoing a professional python project you need to be careful about exceptions. 
        A simple exception can ruin your code. 
        So, you need to handle those exceptions. 
        A few important points about handling exceptions are given below.
        It is better to surround the suspicious code with try-except.
        Using one try-except block for one line of suspicious code 
        is better than using one try-except block for a block of suspicious code.
        It is better to catch specific exception class. 
        Using generalized exception class is not that much useful for handling.
        Sort List natural order;;  use reverse=True, keytosort 
        Use functools module to create complex sorting logic based on multiple fields.
        """
    backwardcounting(20000)    
    if False:
        shorty.append(journaldevRecap)
        verify_age(23)  # won't raise exception
        verify_age(17)  # will raise exception
    #food=["apples", "bananas","cherries", "dates", "eclairs", "fruits"]
    persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 24, 'M'], ['Alexa', 22, 'F']]
    shorty.append(f"    persons.sort(key=functools.cmp_to_key(compare_function))                      {' '*13}")
    shorty.append(f"                                                                                  {' '*13}")        
    shorty.append(f"    def compare_function(person_a, person_b):                                     {' '*13}")    
    shorty.append(f"        if person_a[2] == person_b[2]:        # if their gender become same       {' '*13}")        
    shorty.append(f"            return person_a[1] - person_b[1]  # return True if person_a is younger{' '*13}")        
    shorty.append(f"        else:                                 # if their gender not the same      {' '*13}")        
    shorty.append(f"            if person_b[2] == \"F\":            # give person_b first priority if F {' '*13}")        
    shorty.append(f"                return 1                                                          {' '*13}")        
    shorty.append(f"            else:                             # else give person_a first priority {' '*13}")        
    shorty.append(f"                return -1                                                         {' '*13}")        
    shorty.append(f'Before sorting: {persons}')
    persons.sort(key=functools.cmp_to_key(compare_function))
    shorty.append(f'After  sorting: {persons}')    
   
    return shorty

class UnderAge(Exception):
   pass
def verify_age(age):
   if int(age) < 18:
       raise UnderAge
   else:
       print('Age: '+str(age))

def compare_function(person_a, person_b):
    if person_a[2] == person_b[2]:  # if their gender become same
        return person_a[1] - person_b[1]  # return True if person_a is younger
    else:  # if their gender not matched
        if person_b[2] == 'F':  # give person_b first priority if she is female
            return 1
        else:  # otherwise give person_a first priority
            return -1


class Employee:

    def __init__(self, n, a, gen):
        self.name = n
        self.age = a
        self.gender = gen

    def __str__(self):
        return f'Emp[{self.name}:{self.age}:{self.gender}]'
        
    # List uses __repr__, so overriding it to print useful information
    __repr__ = __str__
@atimer
def poppop():
    shorty1=[]
    e1 = Employee('Alice', 26, 'F')
    e2 = Employee('Trudy', 25, 'M')
    e3 = Employee('Bobby', 24, 'M')
    e4 = Employee('Alexa', 22, 'F')
    emp_list = [e1, e2, e3, e4]
    
    shorty1.append(f'def sort_by_age( emp):                              {" "*40}')        
    shorty1.append(f'        return emp.age                              {" "*40}')        
    shorty1.append(f'try:                                                {" "*40}')        
    shorty1.append(f'    emp_list.sort(key=sort_by_age)                  {" "*40}')        
    shorty1.append(f'except TypeError as te:                             {" "*40}')         
    shorty1.append(f'     print(te)                                      {" "*40}')        
    shorty1.append(f'Before Sorting By Age: {emp_list}')
    def sort_by_age( emp):
            return emp.age
    try:
        emp_list.sort(key=sort_by_age)
    except TypeError as te:
        shorty1.append(te)
    # sorting based on age
    
    shorty1.append(f'After  Sorting By Age: {emp_list}')
    
    #print()
    backwardcounting(10000)

    grades=[2,33,22,11,400,551,6,77,88,39,26,82,19,89]
    shorty1.append(f"avg={drop_first_last(grades)}")
    return shorty1


@atimer
def backwardcounting(n:int):
    while n > 0:
        n -= 1


def drop_first_last(grades):
    grades.pop(grades.index(min(grades)))
    grades.pop(grades.index(max(grades)))
    first, *middle, last = grades
    return avg(middle)#sum(middle)/len(middle)#    lad= Collection.avg()
    