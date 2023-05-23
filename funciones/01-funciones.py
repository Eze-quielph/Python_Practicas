def hola():
    print("Hola")


hola()


def saludo(params, params2="Benitez"):
    print(f"hola {params} {params2}")


nombre = input("Ingresa tu nombre")

nombre2 = input("Ingresa tu segundo nombre")

saludo(nombre)
saludo(nombre, nombre2)
