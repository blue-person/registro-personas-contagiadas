#	Sistema de Información para el manejo de personas contagiadas con COVID-19
#
import os, shelve  # Importa las librerias necesarias para el correcto funcionamiento
from menu import *  # Importa todas las funciones del modulo que contiene el diseño del menu

archivo = shelve.open(
    "Datos"
)  # Crea el archivo "Datos" donde se guardara toda la informacion de las personas que se ingresen en el sistema
listaPersonas, listaCiudades, listaCantidad, diccCiudades, diccInverso, diccOrdenado = [], [], [], {}, {}, {}


class Persona:
    def __init__(self, nombre, tarjetaIdentidad, genero, edad, peso, estatura,
                 enfermedades, ciudad, departamento):
        self.nombre = nombre
        self.tarjetaIdentidad = tarjetaIdentidad
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.enfermedades = enfermedades
        self.ciudad = ciudad
        self.departamento = departamento


def limpiezaArreglos(
):  # Funcion que se encarga de limpiar todos los datos en los diferentes arreglos y tuplas del programa.
    listaCiudades.clear(
    )  #   Se uso para evitar posibles errores en las ultimas opciones del programa
    listaCantidad.clear()
    diccInverso.clear()
    tupla, tuplaOrdenada = (), ()
    diccOrdenado.clear()
    diccCiudades.clear()
    enterContinuar()


while True:
    try:
        menu()
        usuario = input("╚═─[Ingrese una opcion]→ ")
        limpieza()

        if usuario == "a":
            numeroArchivo = 0
            menuArchivo()

            for listaArchivos in (
                    list(archivo.keys())
            ):  # Enseña al usuario las llaves ya existentes en el archivo "Datos"
                numeroArchivo += 1
                print(f"╠═──────[{numeroArchivo}] » {listaArchivos} ")
            opcionArchivo = input("╚═─[Ingrese una opcion]→ ")

            numeroArchivo = 0
            menuArchivo()
            for listaArchivos in (list(archivo.keys())):
                numeroArchivo += 1
                print(f"╠═──────[{numeroArchivo}] » {listaArchivos} ")

            if opcionArchivo == "n":
                nombreArchivo = input(
                    "╠═─[Ingrese el nombre del archivo que desea crear]→ ")

            elif opcionArchivo == "a":
                nombreArchivo = input(
                    "╠═─[Ingrese el nombre del archivo que desea abrir]→ ")

            elif opcionArchivo == "d":
                nombreArchivo = input(
                    "╠═─[Ingrese el nombre del archivo que desea eliminar]→ ")
                try:
                    del archivo[
                        nombreArchivo]  # Elimina la llave que corresponda al nombre ingresado por el usuario
                except:  #   Si este nombre no existe, se notifica el error y se regresa al menu principal
                    menuArchivo_ErrorBorrar()

            else:
                menuArchivo_Invalido()
                print("╠═─[Opcion invalida]»")

            try:
                listaPersonas = archivo[
                    nombreArchivo]  # Se intenta abrir y leer la llave que corresponda al nombre ingresado por el usuario
                archivo.close(
                )  #   Si esta no existe, se ignora el error y el usuario es regresado al menu de inicio
            except (
                    KeyError, NameError
            ):  #   Una vez que el usuario haya guardado informacion en la llave correspondiente, este
                archivo.close()  #   error no deberia volver a aparecer
            enterContinuar()

        elif usuario == "g":
            try:
                limpieza()
                archivo = shelve.open("Datos")
                archivo[
                    nombreArchivo] = listaPersonas  # Se guarda la informacion que se tenga almacenada en las variables correspondientes
                listaPersonas = archivo[
                    nombreArchivo]  # Se lee la informacion que se tenga almacenada en la llave correspondiente
                archivo.close()
            except NameError:
                menuArchivo_ErrorGuardado()

        elif usuario == "s":
            limpieza(
            )  # El programa limpia todos los caracteres de la consola, despues de esto rompe el
            break  #   el bucle While inicial

        elif usuario == "1":  # Ingreso de los datos de un contagiado de COVID-19
            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [1]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )
            persona = Persona(
                input("╠═─[Ingrese el nombre de la persona]→ "),  #Nombre
                input("╠═─[Ingrese la tarjeta de identidad de la persona]→ "
                      ),  #Tarjeta de Identidad
                input(
                    "╠═─[Ingrese el genero de la persona (m) Masculino o (f) Femenino]→ "
                ),  #Genero
                int(input("╠═─[Ingrese la edad de la persona]→ ")),  #Edad
                float(input("╠═─[Ingrese el peso de la persona]→ ")),  #Peso
                float(input(
                    "╠═─[Ingrese la estatura de la persona]→ ")),  #Estatura
                input(
                    "╠═─[Ingrese las enfermedades que tenia la persona previo al contagio de COVID-19]→ "
                ),  #Enfermedades
                input("╠═─[Ingrese la ciudad donde reside la persona]→ "
                      ),  #ciudad
                input("╠═─[Ingrese el departamento donde reside la persona]→ "
                      )  #Departamento
            )
            listaPersonas.append(persona)
            enterContinuar()

        elif usuario == "2":  # Clasificacion de los datos en base a la ciudad donde se encuentren los contagiados
            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [2]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )
            localidadClasificacion = input(
                "╠═─[Ingrese la ciudad con la que desea clasificar los datos]→ "
            )

            for n in range(len(listaPersonas)):
                if listaPersonas[n].ciudad == localidadClasificacion:
                    print("║")
                    print(
                        f"╠═─[Nombre] » {listaPersonas[n].nombre}\n╠═─[Tarjeta de Identidad] » {listaPersonas[n].tarjetaIdentidad}\n╠═─[Genero] » {listaPersonas[n].genero}\n╠═─[Edad] » {listaPersonas[n].edad}\n╠═─[peso] » {listaPersonas[n].peso}\n╠═─[Estatura] » {listaPersonas[n].estatura}\n╠═─[Enfermedades] » {listaPersonas[n].enfermedades}\n╠═─[Ciudad] » {listaPersonas[n].ciudad}\n╠═─[Departamento] » {listaPersonas[n].departamento}"
                    )
            enterContinuar()

        elif usuario == "3":  # Clasificacion de los datos en base a la localidad con mas contagiados
            for n in range(len(listaPersonas)):
                listaCiudades.append(listaPersonas[n].ciudad)
                if listaCiudades[n] == listaPersonas[n].ciudad:
                    diccCiudades[
                        listaPersonas[n].ciudad] = listaCiudades.count(
                            listaPersonas[n].ciudad)

            for ciudad, repeticiones in diccCiudades.items():
                listaCantidad.append(repeticiones)
                if max(listaCantidad) == diccCiudades[ciudad]:
                    ciudadMaximo = ciudad

            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [3]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )

            for n in range(len(listaPersonas)):
                if ciudadMaximo == listaPersonas[n].ciudad:
                    print("║")
                    print(
                        f"╠═─[Nombre] » {listaPersonas[n].nombre}\n╠═─[Tarjeta de Identidad] » {listaPersonas[n].tarjetaIdentidad}\n╠═─[Genero] » {listaPersonas[n].genero}\n╠═─[Edad] » {listaPersonas[n].edad}\n╠═─[peso] » {listaPersonas[n].peso}\n╠═─[Estatura] » {listaPersonas[n].estatura}\n╠═─[Enfermedades] » {listaPersonas[n].enfermedades}\n╠═─[Ciudad] » {listaPersonas[n].ciudad}\n╠═─[Departamento] » {listaPersonas[n].departamento}"
                    )
            limpiezaArreglos()

        elif usuario == "4":  # Clasificacion de los datos en base a la localidad con menos contagiados
            for n in range(len(listaPersonas)):
                listaCiudades.append(listaPersonas[n].ciudad)
                if listaCiudades[n] == listaPersonas[n].ciudad:
                    diccCiudades[
                        listaPersonas[n].ciudad] = listaCiudades.count(
                            listaPersonas[n].ciudad)

            for ciudad, repeticiones in diccCiudades.items():
                listaCantidad.append(repeticiones)
                if min(listaCantidad) == diccCiudades[ciudad]:
                    ciudadMinimo = ciudad

            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [4]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )

            for n in range(len(listaPersonas)):
                if ciudadMinimo == listaPersonas[n].ciudad:
                    print("║")
                    print(
                        f"╠═─[Nombre] » {listaPersonas[n].nombre}\n╠═─[Tarjeta de Identidad] » {listaPersonas[n].tarjetaIdentidad}\n╠═─[Genero] » {listaPersonas[n].genero}\n╠═─[Edad] » {listaPersonas[n].edad}\n╠═─[peso] » {listaPersonas[n].peso}\n╠═─[Estatura] » {listaPersonas[n].estatura}\n╠═─[Enfermedades] » {listaPersonas[n].enfermedades}\n╠═─[Ciudad] » {listaPersonas[n].ciudad}\n╠═─[Departamento] » {listaPersonas[n].departamento}"
                    )
            limpiezaArreglos()

        elif usuario == "5":  # Mostrar en orden descendiente las localidades con personas contagiadas
            for n in range(len(listaPersonas)):
                listaCiudades.append(listaPersonas[n].ciudad)
                if listaCiudades[n] == listaPersonas[n].ciudad:
                    diccCiudades[
                        listaPersonas[n].ciudad] = listaCiudades.count(
                            listaPersonas[n].ciudad)

            for ciudad, repeticiones in diccCiudades.items():
                diccInverso[repeticiones] = ciudad

            tupla = diccInverso.items()
            tuplaOrdenada = sorted(tupla, reverse=True)
            diccOrdenado = dict(tuplaOrdenada)

            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [5]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )

            for repeticiones, ciudad in diccOrdenado.items():
                print(f"║ » {ciudad}")
            limpiezaArreglos()

        elif usuario == "6":  # Mostrar en orden ascendiente las localidades con personas contagiadas
            for n in range(len(listaPersonas)):
                listaCiudades.append(listaPersonas[n].ciudad)
                if listaCiudades[n] == listaPersonas[n].ciudad:
                    diccCiudades[
                        listaPersonas[n].ciudad] = listaCiudades.count(
                            listaPersonas[n].ciudad)

            for ciudad, repeticiones in diccCiudades.items():
                diccInverso[repeticiones] = ciudad

            tupla = diccInverso.items()
            tuplaOrdenada = sorted(tupla)
            diccOrdenado = dict(tuplaOrdenada)

            print(
                "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
            )
            print(
                "║                                            [6]                                             ║"
            )
            print(
                "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
            )

            for repeticiones, ciudad in diccOrdenado.items():
                print(f"║ » {ciudad}")
            limpiezaArreglos()

    except KeyboardInterrupt:  # Si el usuario usa Ctrl + C para salir del programa, se limpian todos los datos, se cierra el archivo
        limpieza()  #   "Datos" y finalmente se rompe el bucle While inicial
        archivo.close()
        break

    except Exception as error:  # Si ocurre algun error inesperado, el programa le enseña al usuario un breve mensaje sobre el error,
        limpieza(
        )  #   una vez haya leido el mensaje, solo debe presionar Enter para salir del programa
        print(
            "╔════════════════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            "║                                           Error                                            ║"
        )
        print(
            "╠════════════════════════════════════════════════════════════════════════════════════════════╝"
        )
        print(f"╠═─[Ocurrio un error inesperado]→ {error}")
        print(
            "╠════════════════════════════════════════════════════════════════════════════════════════════╗"
        )
        print(
            "║ Presione Enter para salir del programa                                                     ║"
        )
        input(
            "╚════════════════════════════════════════════════════════════════════════════════════════════╝"
        )
        limpieza()
        archivo.close()
        break
