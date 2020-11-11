class Patient:
    def __init__(self, name, age, is_new):
        self.name = name
        self.age = age
        self.is_new = is_new

    def printpatient(pat):
        print("{} is ('' if {} else 'not ')a new patient. he is {}.".format(name,is_new,age))
    