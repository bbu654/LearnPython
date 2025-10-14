from string.templatelib import Template    #interpolated string
from typing             import Callable
import urllib.parse, html
from string import Template as oldTemplt 

def make_template(tstr: Template,) -> str:
    values: list[str] = []
    for itr in tstr:
        if isinstance(itr, str):
            values.append(itr)
        else:
            values.append(itr.value)
    return ''.join(values)

def build_template(t_string: Template, processor: Callable[[str], str]):
    values: list[str] = []
    for itsastr in t_string:
        if isinstance(itsastr, str):
            values.append(itsastr)
        else:
            values.append(processor(str(itsastr.value)))
    return ''.join(values)

#ERRs dont use round; import copy.deepcopy
name1:     str = 'Brice'
age1:      str = '30'
message:   str = f'My name is {name1}, and my age is {age1}'
message1:  str = 'My name is {}, and my age is {}'.format(name1,age1)
template1: oldTemplt = oldTemplt('Hello, $name2! You are $age2 years old')
print(f'{template1.substitute(name2='Brice', age2=99)}')

templt: Template = t'Hello, {name1}, you are {age1}'
print(templt)
print(make_template(templt))

opo: str = 'This is a popper string.'
unescapedstt: Template = t'http://www.BriceSky.com/?q={opo}'
print(build_template(unescapedstt, urllib.parse.quote))

pop: str = '<script>alert("Danger")</script>'
unescapedstr: Template = t'Hello {pop}'
print(build_template(unescapedstr, html.escape))
food = 'cheeze'
tmplt: Template = t'Tasty {food!s:>8}!'
print(''.join([x if isinstance(x,str) else x.value for x in tmplt]))
#print(f'{''.join(lst)}')