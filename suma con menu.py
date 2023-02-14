# En estas primeras tres lineas se especifican las variables que se utilizaran
opciones = 0
num1 = ""
num2 = ""
# En esta linea se comienza el ciclo while para el primer numero
while isinstance(num1, float) != True:
# En esta linea se le solicita al usuario el primer numero
    try:
        num1 = float(input("Escribe el primer numero: "))
        print(num1)
# En esta linea se repite el ciclo si el usuario ingreso un valor incorrecto
    except:
        print("El valos es incorrecto, ingresar de nuevo ...")
# En esta linea se inicia el ciclo while para el segundo numero
while isinstance(num2, float) != True:
# En esta linea se pide al usuario el segundo numero
    try:
        num2 = float(input("Escribe el segundo numero: "))
# En esta linea se repite el ciclo si el usuario ingreso un valor incorrecto
    except:
        print("El valos es incorrecto, ingresar de nuevo ...")
# En esta linea se muestra al usuario el resultado de la suma de los dos numero que ingreso
print("La suma es", (num1 + num2))
# En esta linea se inicia el ciclo de las opciones
while opciones != 2:
# En estas dos lienas se le muestra al usuario las opciones que tiene
    print("1. Deseas realizar otra suma")
    print("2. Deseas salir del programa")
# En esta linea se le pide al usuraio que escriba la opcion que desea realizar
    opciones = int(input("Ingrese las opcion deseada: "))
# En esta linea se muestra el condicional si el usuario desea realizar otra suma
    if opciones == 1:
# En estas dos lineas se le pide al usuario los dos numeros
        num1 = float(input("Escribe el primer numero: "))
        num2 = float(input("Escribe el segundo numero: "))
# En esta linea se le muestra al usuario el resultado de la suma de los dos numeros que ingreso
        print("La suma es", (num1 + num2))
# Esta linea muestra un mensaje final si el usuario sale del programa
print("Adios")

