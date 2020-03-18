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