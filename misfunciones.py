diccionaro_peliculas = {}
def agregar_pelicula():
    codigo     = input("Ingrese codigo de la pelicula: ")
    nombre     = input("Ingrese nombre de la pelicula: ")
    anio       = input("Ingrese año de la pelicula: ")
    categoria  = input("Ingrese la categoria de la pelicula: ")
    actores    = input("Ingrese los actores (separados por coma): ").split(",")
    directores = input("Ingrese el nombre del director de la pelicula: ")

    diccionaro_peliculas[codigo] ={
        "codigo"   :codigo,
        "nombre"   :nombre,
        "anio"     :anio,
        "categoria":categoria,
        "actores"  :actores,
        "director" :directores,
    }
    print("pelicula agregada correctamente. \n")
    
def listar_peliculas():
    if diccionaro_peliculas:
        print("listado de peliculas: ")
        for codigo, i in  diccionaro_peliculas.items():
            print(F"codigo    : {codigo}")
            print(f"nombre    : {i["nombre"]}")
            print(f"anio      : {i["anio"]}")
            print(f"categoria : {i["categoria"]}")
            print(f"actores   : {",".join(i["actores"])}")
            print(f"director  : {i["director"]}")
            print("*************************************")
    else:
        print("no hay peliculas registradas.\n")

def mostrar_menu():

    print("        MENU USUARIO:          ")
    print("*******************************")
    print("     1. agregar pelicula       ")
    print("     2. listar peliculas       ")
    print("     3. buscar peliculas       ")
    print("     4. salir y guardar        ")

    while True:
        try:
            print("")
            opcion = int(input("     seleccione una opcion: "))
            if opcion >=1 and opcion <= 4:
                return opcion
            else:
                print("opcion invalida. intente nuevamente.")
        except ValueError:
            print("Error: ingrese un numero valido en la opcion. ")

def buscar_pelicula():
    codigo = input("Ingrese el codigo de la pelicula: ")
    if codigo in diccionaro_peliculas:
        pelicula = diccionaro_peliculas[codigo]
        print("informacion de la pelicula encontrada: ")
        print(f"codigo        :{pelicula['codigo']} ")
        print(f"nombre        :{pelicula['nombre']}")
        print(f"anio          :{pelicula['anio']}")
        print(f"categoria     :{pelicula['categoria']}")
        print(f"actores       :{pelicula['actores']}")
        print(f"director      :{pelicula['director']}")

    else:
        print("UPS!! no se encuentran peliculas para este codigo")

def salir_y_guardar():
    print("Hasta pronto !!")
 
