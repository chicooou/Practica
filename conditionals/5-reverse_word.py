'''Write a Python program that accepts a word from the user and reverse it.'''
#my code
# word = list(input('write a word: '))
# word.reverse()
# #word = str(word)
# print(word)
# print(''.join(word))

#The solution
word = input('input a word to reverse: ') 

for char in range(len(word) -1, -1, -1): #the iterator is saved on char, and find the last char with the -1 -1 -1
    print(word[char], end='')#the word[char], is like find the character on the word, from the up lane. end is to omit the jump line.
print('\n') # this is a jump line
