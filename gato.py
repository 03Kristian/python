animal = ["gato","perro"]

for i in range(0, len(animal)):
    print( ",' ", end="" )
    for j in range(0, len(animal[i])):
        print(animal[i][j], end=", ")


palabras = ["gato","perro"]
space =[]
for i in palabras:
    for j in i:
        space.append(j)
print(space)

#extend()

for i in  palabras:
    for j in i:
        space.extend(j)
print(space)