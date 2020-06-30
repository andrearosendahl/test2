num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print('All done')
print(tot, num, tot/num)


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        int(num)
    except:
        print('Invalid input')
        continue
    print(largest)
    print(num)
    if largest is None:
        largest = num
    elif num >= largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(largest)
    print(smallest)


print("Maximum is", largest)
print('Minimum is', smallest)