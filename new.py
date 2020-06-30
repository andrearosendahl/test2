fruit = 'banana'
letter = fruit[1]
print(letter)

print(fruit[0])
x = 3
w = fruit[x-1]
print(w)

# len is a function that counts the amount of letters
x = len(fruit)
print(x)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter, index)
    index = index + 1

for letter in fruit:
    print(letter)


s = 'Monty Python'
print(s[0:4])
print(s[6:11])
print(s[6:20])
print(s[5:])


#write in python console
if 'n' in fruit:
    print('spelled it correctly')
if 'm' in fruit:
    print('mispelled word')


greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print('Hi There'.lower())

type(greet)
dir(greet)

fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o','x')
print(nstr)

greet = '   Hi    '
print(greet.strip())

line = 'Have a nice day'
line.startswith('Have')
line.startswith('H')


data = 'many words in this line which makes this more difficult'
atpos = data.find('l')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos:sppos]
print(host)


# opening a file
# handle = open('filename','mode')


stuff = 'Hello\nworld'
print(stuff)


# file handle as a sequence
#xfile = open('something')
#for cheese in xfile:
#    print(cheese)

# to find out how many characters are in a text file, use .read
# to get rid of the extra "enter" (\n), use rstrip
#something = open('file')


# want to skip uninteresting lines
for line in something
    if not line.startswith('something')
        continue
    print(line)

# lists
print([1, 2, 3, 4])
print([1, [2, 3], 4]) # a list that includes another list
print([])
#lists are mutable, while strings are not
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28 #changes the third number from 26 to 28
print(lotto)
print(len(lotto))

#using a range function, turns a list
print(range(4))
print(range(len(lotto)))

for i in range(len(lotto)):
    number = lotto(i)
    print(number)

t = [9, 3, 4, 2, 49, 34]
t[1:3]
t[:4]
t[5:]

#can add elements using append function
stuff = lists()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')

#>>9 in t (in python console)
t.sort()

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
for w in stuff:
    print(w)

#double split pattern
line = 'From an email@email.com saturday'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
