numeros = [2, 4, 1, 45, 75, 22]

# Modifica la lista
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

# Devuelve una nueva list
num1 = sorted(numeros)
print(num1)


# Ordenar array de array
usuarios = [["lucas", 1], ["Tomi", 7], ["santi", 3]]


def ordena(element):
    return element[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
