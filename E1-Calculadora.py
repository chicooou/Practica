"""calculadora que sume, reste, multiplique y divida, 2 numeros ingresados
por el usuario.
-Que determine si se ingreso un valor erroneo, envie un mensaje y 
finalice el programa si fue asi
- que el usuario ingrese el signo de la operacion.
- Depuracion de errores comunes con try except
"""
#Parte 1---------------------------------------------------------------


n1 = input('ingresa el primer numero: ') #ingreso del primer numero
n2 = 0 #declaro para validad signo
try: #try para validar ingreso del primer numero
    n1 = float(n1) #que lo convierta a float
except(TypeError, ValueError): #en caso no pueda, estos errores los imprima 
    print('Error al ingresar el primer numero')
    exit() # el exit cierra el script al tener algun error.

#Parte 2----------------------------------------------------------------
signo = input('ingresa la operacion: ')
if signo == '+': #condicional para determinar el nombre del operador
    operador = "Suma "#se asigna el nombre para usarlo en la impresion final
elif signo == '-':
    operador = "Resta "
elif signo == '*':
    operador = "Multiplicacion "
elif signo == '/':
    operador = "Division "
else:
    print('ingresaste un signo invalido') #tambien funciona como un except

#Parte 3------------------------------------------------------------------
n2 = input('ingresa el segundo numero: ') #la misma logica que con n1
try:
    n2 = float(n2)
except(TypeError, ValueError):
    print('Error al ingresar el segundo numero')
    exit()

#Parte 4-------------------------------------------------------------------
if signo == '+': #condicional para determinar que operacion ingreso
    Resultado = n1 + n2 # el valor se asigna a nuevaa variables
    print(operador, Resultado)
elif signo == '-':
    Resultado = n1 - n2
    print(operador, Resultado)
elif signo == '*':
    Resultado = n1 * n2
    print(operador, Resultado)
elif signo == '/':
    try:
        #Resultado = n1 / n2
        print(operador, n1/n2)
    except(ZeroDivisionError):
        print('Division por 0')