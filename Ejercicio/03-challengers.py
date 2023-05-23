#  Fizz Buzz
"""
imprimimos numeros del 1 al 100
Si el numero es multiplo de 3 imprimimos fizz
Si el numero es multiplo de 5 imprimimos buzz
si el numero es multiplo de ambos imprimimos fizz buzz
"""


def multiplos(num):
    multiplo = num
    if num % 3 == 0 and num % 5 == 0:
        multiplo = "fizz buzz"
    elif num % 3 == 0:
        multiplo = "fizz"
    elif num % 5 == 0:
        multiplo = "buzz"
    return multiplo


def fizz_buzz():
    for i in range(1, 101):
        print(multiplos(i))


# fizz_buzz()

# Palabra Anagrama

"""
Escribe una funcion que reciba 2 palabras y retorne veradero o falso segun sean o no anagramas.
Una Anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial.
No hace falta comprobar que ambas palabras existan
Dos palabras exactamenre iguales no son anagrama
"""

palabra1 = input("Ingrese tu primer palabra: ")
palabra2 = input("Ingrese tu segunda palabra: ")


def anagrama():
    if len(palabra1) != len(palabra2):
        return False

    contador_letras = {}

    for letra in palabra1:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1

    for letra in palabra2:
        if letra in contador_letras:
            contador_letras[letra] -= 1
        else:
            return False

    for contador in contador_letras.values():
        if contador != 0:
            return False

    return True


anagrama = anagrama()
print(anagrama)
