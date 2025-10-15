from datetime import datetime

class Text:
    def __init__(self,text: str) -> None:
        self.text = text
    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'upper':
                return self.text.upper()
            case 'lower':
                return self.text.lower()
            case 'count':
                return str(len(self.text))
            case _:
                raise ValueError(f'Format specifier "{format_spec}" doesnt exist!')


decimal1: float = 1234.5678  
percent1: float = .5678
print(f'{decimal1=:.2f}, {percent1=:.2%}') #decimal1=1234.57, percent1=56.78%

big_number: int = 1_000_000.9876
print(f'{big_number:,.1f}')    #1,000,001.0

now: datetime = datetime.now()    
print(f'{now:%x}, {now:%c}, {now=:%H:%M:%S}')    #10/15/25, Wed Oct 15 03:46:28 2025, now=03:46:28

user : str = 'BriceSky'
txt  : str = fr'\User\{user}\Documents\bkjsj\tsldjksld'
print(f'{txt=},{user=}')    #txt='\\User\\BriceSky\\Documents\\bkjsj\\tsldjksld',user='BriceSky'

print(f'{1 + 1} {f'{2+2} {f'{3+3}'}'}')    #2 4 6
var: int = 20
print(f'{user:_>20}: {user:_^20}: {user:_<{var}}')    
#____________BriceSky: ______BriceSky______: BriceSky____________ 
my_text: Text = Text('BriceSky')

mydik: dict[int, str] = {0: 'Brice', 1: 'Amy', 2: 'Gary'}
mydik.setdefault(4, 'NotFound')
print(f'{mydik.get(2)=}, {mydik.get(4)=}')    #mydik.get(2)='Gary'
print(f'{my_text:upper}: {my_text:lower}: {my_text:count}')    #BRICESKY: bricesky: 8
print('got here')    #got here

name1: str = 'Brice'
age1:  int = 69

print('Name: ' + 'Brice, ' + 'Age: ' + str(age1)) #Name: Brice, Age: 69
print(f'Name: {name1} (Age {age1=})') #Name: Brice (Age age1=69)

