fruit = 'banana'
letter = fruit[1]
print(letter)

print('hi')

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
#for line in something
#    if not line.startswith('something')
#        continue
#    print(line)

# lists
print([5, 7, 3, 4])
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

# can add elements using append function
stuff = ()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')

# >>9 in t (in python console)
t.sort()

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
for w in stuff:
    print(w)

# double split pattern
line = 'From an email@email.com saturday'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# Dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 5
print(purse)  # order of the dictionary is unsorted, random

jjj = {'letter' : 3, 'number' : 3, 'word' : 1}
list(jjj)
jjj.keys()
jjj.values()
jjj.items()
for aaa, bbb in jjj.items():
    print(aaa, bbb)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

counts = dict()
line = input('')
words = line.split()
for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email,0) + 1

biggestemail = None
biggestcount = None
for email,count in counts.items():
    if biggestcount is None or count > biggestcount:
        biggestcount = count
        biggestemail = email

print(biggestemail, biggestcount)

(x, y) = (4, 'fred')
print(y)

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
tups = d.items()
print(tups)

# sorting by keys
d = {'a' : 2, 'b' : 3, 'c' : 1}
t = sorted(d.items())
print(t)

# sorting by values
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

print(sorted([(v, k) for k, v in d.items()]))