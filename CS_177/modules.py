'''
Modules
A single File containing preexisting Python code
Used to organize code logically and reuse it
called using import keyword
Types of Modules:
User-defined: any .py file created by me
Buildt-In: part of Python Standard Library. Already compiled and stored.

Inside python, 
code is compiled to bytecode by interpreter and stored as .pyc file in __pychace__ folder.
Next time you import the module:
->Python loads from .pyc ->faster performance, avoid recompiling


Libraries: Collection of Packages or Modules
Standard: Built-in Modules, Pre-installed.
maintained by python core team.
Third-Party Lib:Created by Communities and org.
Installed using pip.
Hosted by PyPI(Python Package Index)
Ex: Numpy, Pandas, Mathplotlib

Ways to Import modules:
1. import 'module' #import entire module. Access = func.module()
2. import 'module' as 'alias' #import entire module and give it a name you want. Access= func/variable.func()
3. from 'module' import 'funct/variable' #import only a sppecific func/variable. Access= func/variable
4. from module import * #import everything variables, functions, classes, etc. 

#Random: used to generate random numbers and make random selections

import random
a=random.randint(a,b)#generates random int from a to b (inclusive)
b=random.random()#generate random no. from 0.0 to 1.0
c=random.choice(x)#pick random value from x. x can a sequence(list,tupple,string)
d=random.shuffle(x)#randomly rearrange a list. x is a list

#collections: Provides specialized DataStructures. 
#nametuple (tuple)= tuple with named fields
#deque (list)=Double-ended queue
#Counter, ChainMap (dict): Count items or combine multiple dictionaries
#Counter: specialized dictionary for counting items in dict
#   ->keys=items being counted
#   ->Values=number of occurrences

import collections
w=[1,1,1,2,2,3,4,3,4]
c=collections.Counter(w)
print(c)#c=Counter({1:3,2:2,3:2,4:2}), Higest Value(the most number of occuring item first) first

#ChainMap: Groups Multiple dictionaries together.
#   ->searches from first dict to last
#   ->ex: d1={'A':1,'B':2}, d2={'C':3,'D':4}
#   ->d=collections.ChainMap(d1,d2)

d1={'A':1,'B':2}
d2={'C':3,'D':4}
d=collections.ChainMap(d1,d2)#d=ChainMap({'A': 1, 'B': 2}, {'C': 3, 'D': 4})
d3={'E':5}
d=d.new_child(d3)#adds to the front of d 
d=d.parents#removes the dict present at the front
print(d.map)#will print the list of dictionaries in d: [{'A': 1, 'B': 2}, {'C': 3, 'D': 4}]

#namedtuple: Tuple with names field(positional indices have names)
#   ->immutable like regular tuple


T=c=collections.namedtuple('tupleT',['greet','age','score'])#define a named tuple T with a set layout
c1=T('arvind',12,45.86)
c2=T('kejriwal',13,98.78)
print(c1['greet'])#arvind

#Queue(FIFO)
#Stack(LIFO)
#Deque: double-ended queue
#   ->can add and remove from both ends of a list

d=collections.deque(['a','b','c','d'])
d.append('e')#adds e to the right end
d.appendleft('f')#adds f to the left end
d.pop()#removes rightmost (last) value
d.popleft()#removes the first(leftmost) value
'''

import CS177 as cs
l=[99,58,39,23,58,47,12]
print(cs.appendleft(l,100))
print(cs.popleft(l))