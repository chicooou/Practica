'''Write a Python program to find those numbers
which are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included)

in = 1500 and 2700



'''
#this is my answer
'''divisibles = 1499
multiples = 1499
while divisibles >= 1499:
    if divisibles%7 == 0:
        print(str(divisibles) + ' is divisible of 7')
    divisibles += 1 
    if divisibles == 2701:
        break
input()
while multiples >= 1499:
    factor = multiples * 5
    print('from: ', multiples, str( factor) + ' is multiple of 5')
    multiples += 1
    if multiples == 2701:
        break'''

#this is the valid answer
nl=[] #create a list, it allows to save the data divisibles and multiples
for x in range(1500, 2701):#a bucle in range to 1500 to 2700
    if (x%7==0) and (x%5==0):#the condition to find the divisibles and multiples
        nl.append(str(x))#here we add the value to the list
print (','.join(nl))#print the list, join is to add the comma