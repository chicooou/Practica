#Write a Python program to convert temperatures to and from celsius, fahrenheit.
#celsius formula: (F - 32) x 0.5556 = C
# Fahrenheit formula: (C x 1.8) + 32 = F


#my code
'''
a = input('ingresa F si quieres convertir F a C, o C si quieres convertir C a F: ')
val = input('ingresa el valor a convertir: ')
try:
    val = int(val)
except(TypeError, ValueError):
    print('error al ingresar el valor')
    exit()
if a == 'F':
    C = (int(val) - 32)*0.556
    print(val, 'Fahrenheit is ',round(C),' in Celsius' )
elif a == 'C':
    F = (int(val) * 1.8)+32
    print(val, 'Celsius is ',round(F),' in Fahrenheit' )
else:
    print('has ingresado un dato mal, try it again')  '''
    

#the answer
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ") 
degree = int(temp[:-1]) # : create a new list, and -1 omit the last index, in this case the character
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


