#Functions in Python

#Create a function 
def sayHello(name = 'Kaveendra'):
    print('Hello', name)
    
sayHello('Brad')

#Return a Value
def getSum(num1,num2):
    total = num1 + num2
    return total

numSum = getSum(1, 2)
print(numSum)

#Immutable Data - Cannot be override (Strings, Int)
#Mutable Data - Can Override (LIST, Dictionaries)

#IMMUTABLE
def addOneToNum(num):
    num = num + 1
    print('Value inside function: ',num)
    return

num = 5
addOneToNum(num)
print('Value outside the function: ',num)

#MUTABLE
def addOneToList(myList):
    myList.append(4)
    print('Value inside function: ',myList)
    return

myList = [1,2,3]
addOneToList(myList)
print('Value outside function: ',myList)




