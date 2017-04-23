#Conditionals

x = 7

#Basic If
if x<6:
    print('This is True')
    
#If Else
if x < 6:
    print('This is True')

else:
    print("This is False")
    
#Elif
color = 'red'

if color == 'red':
    print("Color is Red")
elif color == 'blue':
    print('color is blue')
else:
    print('color is not blue')
    
#Nested If
if color == 'red':
    if x < 10:
        print('Color is RED and X is GREATER THAN 10')
 
#Logical Operators
if color == 'red' and x < 10:
    print('Color is Read and X is Less than 10')   
    