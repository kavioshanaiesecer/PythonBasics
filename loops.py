#Loops

#FOR LOOPS
people = ['John','Kaveendra','Sara','Tim','Ellie']
for person in people:
    print('Current Person: ',person)
    
#Iterate by Sequence
for i in range(len(people)):
    print('Current Person: ',people[i])
    
for i in range(1,10):
    print(i)
    
#WHILE LOOP
count = 0
while count <= 10:
    print('Count: ',count)
    if count == 5:
        break
    count = count + 1
    
