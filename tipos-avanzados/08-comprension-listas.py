usuarios = [
    ["Chanchito", 4],
    ["Feli", 3],
    ["ale", 1]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)


nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# Filtrar
nombres2 = [usuario for usuario in usuarios if usuario[1] > 4]
print(nombres2)


nombres3 = list(map(lambda usuario: usuario[0], usuarios))

print(nombres3)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
