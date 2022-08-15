import os

def limpieza():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def menu():
    limpieza()
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║               (a) Archivo               (g) Guardar                (s) Salir               ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
    print("║ [1] Registrar datos de una persona con COVID-19.                                           ║")
    print("║ [2] Listar los datos de las personas positivas de COVID-19 de una localidad.               ║")
    print("║ [3] Listar las personas de la localidad con la mayor cantidad de positivos con COVID-19.   ║")
    print("║ [4] Listar las personas de la localidad con la menor cantidad de personas con COVID-19.    ║")
    print("║ [5] Listar los municipios de mayor a menor dependiendo de los positivos de COVID-19.       ║")
    print("║ [6] Listar los municipios de menor a mayor dependiendo de los positivos de COVID-19.       ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╝")

def menuArchivo():
    limpieza()
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║      (n) Crear archivo nuevo          (a) Abrir archivo          (d) Eliminar archivo      ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("║ » Archivos:")

def menuArchivo_Invalido():
    limpieza()
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║      (n) Crear archivo nuevo          (a) Abrir archivo          (d) Eliminar archivo      ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╝")

def enterContinuar():
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ » Presione Enter para continuar                                                            ║")
    input("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

def menuArchivo_ErrorGuardado():
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                         Guardando...                                       ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
    print("║ No se esta trabajando en ningun archivo » Presione Enter para volver al menu de inicio     ║")
    input("╚════════════════════════════════════════════════════════════════════════════════════════════╝")

def menuArchivo_ErrorBorrar():
    limpieza()
    print("╔════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                                        Eliminando...                                       ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════════════╣")
    print("╠═─[Ocurrio un error]→ El archivo que se intenta eliminar no existe")
