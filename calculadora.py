#Inicializacion

def peticion_usuario():
    print("Bienvenido a la calculadora")
    print("Ingrese el primer numero")
    num1 = float(input())
    print("Ingrese el segundo numero")
    num2 = float(input())
    return num1, num2

def opciones():
    print("Seleccione la operacion a realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")    
    opcion = int(input())
    return opcion

def suma(num1, num2):
    return num1 + num2


num1, num2 = peticion_usuario()
opcion = opciones()
if opcion == 1:
    resultado = suma(num1, num2)
    print("El resultado de la suma es: ", resultado)