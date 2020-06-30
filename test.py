print('hello world')

# Remember that indent is 4 spacings
print('test conditionals')
x = 5
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')
print('finish')

print('repeated steps')

n = 5
while n > 0:
    print(n)
    n = n - 1
print('done')

# using remainder, which tells you about the remainder when dividing numbers
a = 23
b = a % 5
print(b)
# 23 divided by 5 is 4, with a remainder of 3 left


# power is by using two multiplications
c = 2
d = c ** 3
print(d)

eee = 'hello ' + 'there'
print(eee)

type(eee)
type('hello')
type(1)

print('done')

print(float(99))

print(10 / 2)
print(9 / 2)

sval = '123'
ival = int(sval)
print(ival + 1)

name = input('Who are you? ')
print('Welcome ', name)

# Converting elevator floor
inp = input('Europe floor? ')
# Converting inp to an integer using int
usf = int(inp) + 1
print('US floor', usf)

# Comparison operators
# most of them are the same as matlab
# >= bigger or equal to
# <= smaller or equal to
# != means not equal to

x = 5
if x >= 4:
    print('bigger than 4')
if x != 7:
    print('not equal to 7')
if x == 5:
    print('equal to 5')
    print('not equal to 3')
print('after equality check')
# all the prints that are indented are part of the if statement, while when it is no longer indented it is no
# longer part of the if statement

print('Two way conditional statements')
x = 4
if x > 2:
    print('Bigger')
elif x == 2:
    print('Equal to 2')
else:
    print('Smaller')

# The try / except structure
astr = 'Hello'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)


# Functions
def thing():
    print('Hello')
    print('Howdy')


thing()
print('Zip')
thing()

big = max('Hello world')
print(big)
tiny = min("Hello world")
print(tiny)


# Return values
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('fr'), 'Sally')

# For loops
for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
print('Done')

n = 5
while n > 0:
    print(n)
    n = n-1
print(n)
print('donee')

while True:
    line = input('> ')
    if line[0] == '#':
        continue   # this goes back to start of the loop
    if line == 'Done':
        break     # this will exit the loop
    print(line)
print('Done!')

for i in [5, 4, 3, 2, 1]:
    print(i)
print('finite')

largest_so_far = None
print('Before',largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far,the_num)
print('After',largest_so_far)

# Use "is" for true, false and none, otherwise use ==


count = 0
sum = 0
print('Before',sum, count)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)


# Boolean value
found = False
print('Before',found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)


# course test
hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter rate: ')
r = float(rate)

totalpay = 0
for i in range(int(h)):
    if i < 40:
        pay = r
    elif i >= 40:
        pay = 1.5*r
    totalpay = pay + totalpay

print(totalpay)