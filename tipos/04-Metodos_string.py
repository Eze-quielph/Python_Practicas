animal = "chanchito"
animal2 = "  CHANCHITO  "

print(animal.upper())
print(animal2.lower())
print(animal.capitalize())
print(animal.title())
print(animal2.strip())
print(animal2.lstrip())
print(animal2.rstrip())
print(animal2.find('CH'))
print(animal2.replace('CH', 'C'))
print("nCH" in animal)
print("nCH" not in animal)