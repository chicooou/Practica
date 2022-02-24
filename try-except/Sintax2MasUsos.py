"""calculadora que suma y si se ingresan str en lugar de int cambiar a 
mal e imprimir con un if"""

n1 = input('ingresa el primer numero: ') #se pide el numero en str
n2 = input('ingresa el segundo numero: ')

try:
    n1 = int(n1) #se intenta convertir a int
    n2 = int(n2)
    print('la suma es: ',n1 + n2) # si se logra se imprime
except: #se crea la excepcion
    n1 = 'malo' # si no se logra convertir que sea igual a malo
    n2 = 'malo' 

'''aca podriamos imprimir y evitar el inf, pero con fines de comprender que se
se puede combinar lo hacemos de esta forma'''

if n1 == str(n1): # condicionamos si n1 es str se imprima
    print(n1)
if n2 == str(n2):
    print(n2)
