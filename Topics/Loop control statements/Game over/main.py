scores = input().split()
c, i = 0, 0
for answer in scores:
    if answer == 'C':
        c += 1
    elif answer == 'I':
        i += 1
        if i == 3:
            break
    else:
        print('Invalid Input!')
        quit()
print('You won' if i < 3 else 'Game over')
print(c)
