import json
from typing import Iterator
print(f'{abs(33)=}; {abs(-33)=}; {abs(5+3j)=}; ')
print(f'{all([1,1,1,0,1])=}; {all([0,0,0,0,0])=}; {all([1,1,1,1,1])=}; ')
print(f'{any([1,1,1,0,1])=}; {any([0,0,0,0,0])=}; {any([1,1,1,1,1])=}; ')
print(f'{ascii('A')=}; {ascii('$')=}; {chr(5000)}={ascii(chr(5000))}; ')
print(f'{bin(7)=}; {bin(69)=}; {bin(5000)=}')
print(f'{bool('A')=}; {bool(120)}; {bool([])}')
print(f'{callable('A')=}; {callable(print)=}; {callable(5000)=}')
print(f'{chr(65)=}; {chr(99)=}; {chr(5000)=}')
print(f'{complex(5)=}; {complex('7+5j')=}; {complex(5, 1)=}')
print(f'{dict(a=1,b=2)=}; {dict(['a1','b2'])=}; {dict(['aY','bZ'])=}')
print(f'{dir()=}; {dir(json)=}; {dir(int)=}')
print(f'{divmod(7,4)=}; {divmod(2.5,1.5)=}; {divmod(5000,5)=}')     #divmod(7,4)=(1, 3); divmod(2.5,1.5)=(1.0, 1.0); divmod(5000,5)=(1000, 0)
print(f'{list(enumerate(['A','B','C']))=};')                        #list(enumerate(['A','B','C']))=[(0, 'A'), (1, 'B'), (2, 'C')];
print(f'{[str(iA) + x for iA, x in enumerate(['A','B','C'])]=}')    #[str(iA) + x for iA, x in enumerate(['A','B','C'])]=['0A', '1B', '2C']'''
print(f'{eval("(10+11)*2")=}')                                      #eval("(10+11)*2")=42
source:str = """
print(11+31)                                                       
for j in range(1,11):
    print(f'{j}',end=" ")                                          
        """
exec(source);names1:list[str] = ['James','John', 'Jam', 'Brice']                 
j_names: filter = filter(lambda s: s[0].lower() == 'j', names1);print(list(j_names))    #1 2 3 4 5 6 7 8 9 10 ['James', 'John', 'Jam']
print(float(eval("11+31")))                                          #42.0
fs: frozenset[int]= frozenset([1,2,3]);print(fs);print(hash(fs))     #frozenset({1, 2, 3})-272375401224217160
print(f'{globals()}; {locals()}; {id(source)}; {source is j_names}') #hash,help, open, *people, repl, reverse, set(unique)
print(f'{list(iter([1,2,3]))=}; {len(source)=}; {list('123')}')      #list(iter([1,2,3]))=[1, 2, 3]; len(source)=167; ['1', '2', '3']
print(f'{list(map(lambda s: s.upper(), ['Brice', 'Amy', 'Gary']))=}; {issubclass(bool,int)=}')    #list(map(lambda s: s.upper(), ['Brice', 'Amy', 'Gary']))=['BRICE', 'AMY', 'GARY']; issubclass(bool,int)=True
print(f'{max(names1,key=len)=}; {min(names1,key=len)=};')            #max(names1,key=len)='James'; min(names1,key=len)='Jam';
print(f'{ord('A')=}; {pow(2,5)=}; {list(range(10,0,-1))=}; {list(reversed([1,2,3,4,5]))=}')   #ord('A')=65; pow(2,5)=32; list(range(10,0,-1))=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]; list(reversed([1,2,3,4,5]))=[5, 4, 3, 2, 1]
print(f'{round(1.222222,3)=}; {[1,2,3,4,5][slice(None,None,-1)]=}')  #[::=1]    range(1,11)    round(1.222222,3)=1.222; [1,2,3,4,5][slice(None,None,-1)]=[5, 4, 3, 2, 1]
print(f'{sorted([1,6,3,2,7,8,4])=}; {sorted(names1,key=len)=}')      #sorted([1,6,3,2,7,8,4])=[1, 2, 3, 4, 6, 7, 8]; sorted(names1,key=len)=['Jam', 'John', 'James', 'Brice']
print(f'{sum([1,2,3,4,5,6,7,8])=}; {type('poi')}; {list(zip([1,2,3,4],['a','b','c'],[True,False,True]))=}')    #sum([1,2,3,4,5,6,7,8])=36; <class 'str'>; list(zip([1,2,3],['a','b','c'],[True,False,True]))=[(1, 'a', True), (2, 'b', False), (3, 'c', True)]
