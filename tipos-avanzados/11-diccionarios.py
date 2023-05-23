punto = {
    "x": 10,
    "y": 20
}

print(punto["x"])

punto["z"] = 34

print(punto["z"])

print(punto.get("x", "por defecto si no existe"))

del punto["x"]
print(punto)
