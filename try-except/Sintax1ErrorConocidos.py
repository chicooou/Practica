"""programa que ingrese un numero, divida. con solucion de errores para: 
1. division entre 0
2. errores tipicos ValueError, TypeError, IndexError
"""
import sys #nos sirve para imprimir el tipo de error

n1 = input('ingresa el primer numero: ') #declaramos las variables fuera del try
n2 = input('ingresa el segundo numero: ') #esta es una buena practica para que ingresen como srt

try:
    n1 = int(n1) # intentamos convertir las variables por defecto str a int
    n2 = int(n2)
    resultado = n1/n2
    print('El resultado es: ', resultado) #si se logran convertir imprimimos
except (ZeroDivisionError): # Si existe este error python hara lo siguiente
    print('dividiste entre cero') #imprimir esto
except (TypeError, ValueError, IndexError): # mas errores, tambien se puede en un solo except
    print('has tenido un error al ingresar los numeros: ')
    print('el error fue": ', sys.exc_info()[0]) # y con sys hacer que se imprima que error fue.
