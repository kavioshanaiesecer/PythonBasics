#STRING FUNCTIONS

myStr = 'Hello Kaveendra World!'

#Capitalize
print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

#Get Length 
print(len(myStr))

#Replace
print(myStr.replace('World', 'Everyone'))

#Count
sub = 'H'
print(myStr.count(sub))

#Startswith
print(myStr.startswith('Hello'))

#Endswith
print(myStr.endswith('World!'))

#Split in to a list
print(myStr.split())

#find
print(myStr.find('e'))

#Index - throws an error
print(myStr.index('H'))

#Is all alpanumeric
print(myStr.isalnum())

#Alphabetic
print(myStr.isalpha())

#Is all Numeric
print(myStr.isnumeric())

