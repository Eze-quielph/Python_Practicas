#interaccion
#Verificar que usuario inserte un numero, de no haberlo hecho, hacer que lo ingrese
#Si lo ingreso, pedirle que te pase el simbolo de operacion
#ingrese segundo numero
#Mandamos resultado
print("Bienvenido")
print("Si escibres cancelar se cancela el programa")
print("Seleccione la operacion: suma, resta, division, multiplicacion: ")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese un numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese un numero: ")
    if resultado.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    
    elif op.lower() == "resta":
        resultado -= n2
    
    elif op.lower() == "division":
        resultado /= n2
    
    elif op.lower() == "multiplicacion":
        resultado *= n2

    print(f"resultado es: {resultado}")