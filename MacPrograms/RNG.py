#! /usr/bin/env python3
import random
b=0
print('How many numbers do you want?')
a=input()
print('Do you want your numbers to be a certain length?')
numlength=input()
if numlength=='Yes':
    print('How long should they be?')
    b=input()
elif numlength=='yes':
    print('How long should they be?')
    b=input()
else:
    print('Here are your numbers:')
print('Here are your numbers:')
for i in range(int(a)):
    if int(b)==0:
        b=random.randint(1, 6)
    c=1
    number=0
    for i in range(int(b)):
        number=number+(random.randint(0, 9)*c)
        c=c*10
    print(number)
