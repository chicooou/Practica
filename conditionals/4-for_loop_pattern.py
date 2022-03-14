'''4. Write a Python program to construct the 
following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
#My solution:
# pattern = ['*', '* *', '* * *', '* * * *', '* * * * *', '* * * *', '* * *', '* *', '*'] # a list with the dots
# for x in pattern: # the iterator run on the items from the list
#     print(x)

#the solution:
n=5; #the limit for the iterators
for i in range(n): # this is the 1st iterator, control the line jump from 1 to 5
    for j in range(i): # the 2nd iterator, this control the *
        print ('* ', end="")
    print('')

for i in range(n,0,-1): #this is the same top, but regressively, this with the parametter range -1 (is the step)
    for j in range(i):
        print('* ', end="")
    print('')