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





