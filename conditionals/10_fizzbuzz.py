'''Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead 
of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and
five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz'''

count = 0
while count < 50:
    count += 1
    if count % 3 == 0 and count % 5 == 0:
        print('Fizz' + 'Buzz')
        continue
    elif count % 3 == 0:
        print('Fizz')
        continue
    elif count % 5 == 0:
        print('Buzz')
        continue
    
    print(count)
