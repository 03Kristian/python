texto = ["Hola ola hey que"]

text = input("ingrese una frase: ")

space = []
for i in texto:
    for j in i:
        space.append(i.find(texto[j]))
        if text == i:
            print("si")
    print(space)
