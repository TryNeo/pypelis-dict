import os
import time

PELICULAS = dict()

def clear_pantalla():
    os.system('clear')             


def insertar_pelicula(num_pelicula,titulo,director,agno,cantidad):
    PELICULAS [num_pelicula] = {
        'Titulo' : titulo,
        'Director' : director,
        'Anio' : agno,
        'Cantidad':cantidad
    }


def mostrar_peliculas():
    if len(PELICULAS.keys()) > 0:
        print("Cod\t\tTitulo\t\tDirector\tAño\tCantidad")
        for x,y in PELICULAS.items():
            print(x,"\t\t"+y['Titulo'],"\t\t"+y['Director'],"\t\t"+y['Anio'],"\t"+y['Cantidad'])
            print("")
    else:
        print("Cod\t\tTitulo\t\tDirector\tAño\tCantidad")
        time.sleep(2)


def rentar_peliculas(num_pelicula):
    pelicula = PELICULAS.get(num_pelicula)
    if pelicula is None:
        print("La pelicula No existe")
        print("")
    else:
        confirmacion = input(f"La pelicula que desea rentar es{pelicula['Titulo']} dirigada por {pelicula['Director']} en el año {pelicula['Anio']}.?(S/N)").lower()
        if confirmacion == "s":
            if int(pelicula['Cantidad']) > 0:
                print("La pelicula ha sido Rentada")
                PELICULAS[num_pelicula]['Cantidad'] = str(int(pelicula['Cantidad']) - 1)
                print("")
            else:
                print("No hay Stock de la pelicula solicitada")
                print("")
        elif confirmacion == "n":
            print("No desea rentar pelicula")
            print("")
        else:
            print("Error eso no una opcion existente")
            print("")


def devolver_peliculas(num_pelicula):
    pelicula = PELICULAS.get(num_pelicula)
    if pelicula is None:
        print("La pelicula No existe")
        print("")
    else:
        confirmacion = input(f"La pelicula que desea devolver es{pelicula['Titulo']} dirigada por {pelicula['Director']} en el año {pelicula['Anio']}.?(S/N)").lower()
        if confirmacion == "s":
            print("La pelicula ha sido devuelta")
            PELICULAS[num_pelicula]['Cantidad'] = str(int(pelicula['Cantidad']) + 1)
            print("")
        elif confirmacion == "n":
            print("No desea devolver la  pelicula")
            print("")
        else:
            print("Error eso no una opcion existente")
            print("")


def eliminar_peliculas(num_pelicula):
    pelicula = PELICULAS.get(num_pelicula)
    if pelicula is None:
        print("La pelicula No existe")
        print("")
    else:
        confirmacion = input(f"La pelicula que desea eliminar es{pelicula['Titulo']} dirigada por {pelicula['Director']} en el año {pelicula['Anio']}.?(S/N)").lower()
        if confirmacion == "s":
            PELICULAS.pop(num_pelicula)
            print("La pelicula ha sido eliminada")
            print("")
        elif confirmacion == "n":
            print("No desea ha eliminado la  pelicula")
            print("")
        else:
            print("Error eso no una opcion existente")
            print("")

def menu():
    print(f"{len(PELICULAS)} pelicula registradas")
    print("""1. Ingresar nueva pelicula
2. Mostrar todas las peliculas
3. Rentar pelicula
4. Devoler pelicula
5. Eliminar una pelicula
6. Salir
    """)

def main():
    while True:
        menu()
        opcion = int(input("opcion:"))
        if opcion == 1:
            clear_pantalla()
            num_pelicula = int(input("ingrese el pelicula Nro."))
            titulo = input("Titulo:")
            director = input("Director:")
            agno = input("Año:")
            cantidad = input("Cantidad:")
            clear_pantalla()
            insertar_pelicula(num_pelicula,
                titulo,
                director,
                agno,
                cantidad)
        elif opcion == 2:
            clear_pantalla()
            mostrar_peliculas()
        elif opcion == 3:
            clear_pantalla()
            rentar = int(input("¿Que pelicula desea rentar?"))
            rentar_peliculas(num_pelicula = rentar)
        elif opcion == 4:
            clear_pantalla()
            devolver = int(input("¿Que Pelicula desea devolver?"))
            devolver_peliculas(num_pelicula = devolver)
        elif opcion == 5:
            clear_pantalla()
            eliminar = int(input("¿Que Pelicula desea eliminar?"))
            eliminar_peliculas(num_pelicula = eliminar)
        elif opcon == 6:
            print("Gracias por usar nuestro sistema")
            break

if __name__ == "__main__":
    main()