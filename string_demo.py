print(2-1)
# print('2'-'1') does not work typeerror
# print('EU'-'Great Britain' does not work)

first_name = 'John'
last_name = 'Lennon'
name = first_name +' ' + last_name
print(name)

print('Naah, na na nanana naah, nanana naah, hey Jude. \n' * 10)
#print ten times

name = 'world'
print(f'Hello, {name}')

actor = 'Joaquin Phoenix'
year = 2020
movie = 'Joker'
print(f'{actor} wins Best Actor for {movie} at Golden Globes {year}.')

pi = 3.1415926
print(f'Pi equals {pi}')
print(f'Pi equals {pi:.4f}.')
print(f'Pi equals {pi:8.5f}.')
print(f'Pi equals {pi:8.2f}.')

a = 2020

# binary
print(f'{a:b}')

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')

a=123
type(123)

import math
print(math.pi)
print(math.sqrt(85))

import random
print(random.random())

random.choice([1, 2, 3, 4])

age=20
if age >= 21:
    print('Yes, you can.')
else:
    print('Sorry.')

True and True
not True
True and False
False and False
not False
5>3 and 3>1
True or True
True or False
False or False

#define a function
def print_twice(whatever):
    print(whatever)
    print(whatever)

#call a function

print_twice('Thanks for Columbia Offer!')

def my_abs(number):
    """
    returns absolute value of any number.
    number:an int.
    """
    #the above is called docstring.
    if number <0:
        return 0-number
    else:
        return number

b=-42
abs_b = my_abs(b)
print(abs_b)

