from misfunciones import agregar_pelicula ,listar_peliculas,mostrar_menu,buscar_pelicula

while True:
    opcion = mostrar_menu()

    if opcion ==    1:
        agregar_pelicula()
    elif opcion ==  2:
        listar_peliculas()
    elif opcion ==  3:
        buscar_pelicula()
    elif opcion == 4:
        print("ups vuelva pronto")
        break
    else:
        print("opcion no valida. intente nuevamente.\n")
