   codigo = int(input("ingrese el codigo de pelicula: "))
    encontrado=False

    for i in range(int(codigo)):
        if codigo==codigo[i]["codigo"]:
            res = codigo[i]
            encontrado = True

    if encontrado:
        print("la pelicula fue encontrada")
    else:
        print("no se encontraron resultados para este codigo")