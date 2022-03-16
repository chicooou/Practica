'''Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5'''
numbers = [0, 1, 2, 3, 4, 5, 6]
for x in numbers:
    if x == 3:
        continue
    if x == 6:
        continue
    print(x, end='') # end = '' is used to omit the jump line