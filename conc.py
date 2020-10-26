import numpy as np
import pandas as pd

li = [1, 'Colorado', 4.7]
li

li[0]

arr = np.array([1,2,3,4])
arr

arr/3

## Append

li = li.append(5)

arr = np.append(arr,4)
arr

## Dictionaries
# keys must be unique

dic = {'MA': 3, 'BC': 1}
dic['MA']

dic['SE'] = 2
print(dic)

# SECTION 2
# Functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def suma(x,y):
    out = x + y
    return out

print(suma(56,98))

def maxi(lst):
    """maximum 
    Args:
        lst is a list or float

    Returns:
        the highes element of list
    """
    cm = lst[0]
    for i in lst[1:]:
        if i > cm:
            cm = i
    return cm

maxi(np.append(arr,4))
maxi([5,849,149,4895,4562])

## LambDA
lambda arguments: expression

(lambda x,y: x*y)(9,8)

q = lambda x: x / 2
q(894)

f = lambda x: np.cos(x)
x = np.linspace(-np.pi, np.pi, 100)
y = [f(i) for i in x]
plt.plot(x,y)
plt.show()

## EXERCISES LAB
def get_element(lst):
  new_lst = []
  for i in lst:
    new_lst.append(i**2)
    return lst[1]

lst = [1, 7, 3, 5]
get_element([1, 7, 3, 5])


my_dict = {'peaches':'cream', 'cat':'dog', 'this one':'that one'}
my_dict['this one']

my_dict = {'peaches':'cream', 'cat':'dog', 'this one':'that one'}
my_dict['this one']