# 5.2.py
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

from ast import Num


largest = None
smalest = None
while True:
    num = input ('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('invalid input, please insert a integer number')
        continue

    if largest == None: 
        largest = num 
    elif largest < num:
        largest = num 

    if smalest == None:
        smalest = num          
    elif smalest > num:
        smalest = num
    
         
print ('Maximum number is ', largest)
print ('Minimum number is ', smalest) 





