from Dominio.Pelicula import Pelicula
from Servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    print('OPCIONES'.center(50,'*'))
    print('1. Agregar Pelicula')
    print('2. Listar Peliculas')
    print('3. Eliminar Catalogo de peliculas')
    print('4. Salir')
    opcion = int(input('Escribe tu Opción (1-4): '))

    if opcion == 1:
        pelicula = input('Digite el nombre de la pelicula: ')
        pelicula = Pelicula(pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == 2:
        CatalogoPeliculas.listar_peliculas()
    elif opcion == 3:
        CatalogoPeliculas.eliminar_peliculas()
    elif opcion == 4:
        print('Salimos del programa...')
    else:
        print('Digita una opción valida'.center(50, '/'))

