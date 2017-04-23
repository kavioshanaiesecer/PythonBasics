#Open aa File
fo = open('text.txt','w')

#Get Some info
print('Name: ',fo.name)

#Closed or Not
print('Is Closed: ',fo.closed)

#Checking the mode
print('Opening Mode: ',fo.mode)

#Wrting to a File
fo.write('I Love Python ')
fo.write('& Java Script')
fo.close()

#Using APPEND MODE
fo = open('text.txt','a')
fo.write(' I also Like PHP')
fo.close()

#Reading Files
fo = open('text.txt','r+')
text = fo.read()
print(text)
fo.close()

#Create a file from Sccript
fo = open('text2.txt','w+')
fo.write('This is my new file')
fo.close()















