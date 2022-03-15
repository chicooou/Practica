'''Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
'''
even = 0
odd = 0
serie = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in serie:
    if x%2 == 0:
        even += 1
    elif x%2 != 0:
        odd += 1
print('Numbers of even numbers: ',even)
print('Numbers of odd numbers: ',odd)
