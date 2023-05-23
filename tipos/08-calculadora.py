n1 = input("Ingresa primer numero")
n2 = input("Ingresa segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

resultado = """
 para los numeros {n1} y {n2},
 su suma es {suma} y su resta {resta}
 su multiplicacion es {multi} y su division es {div}
"""

print(resultado)