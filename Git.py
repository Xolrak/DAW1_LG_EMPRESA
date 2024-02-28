import time
import os
import platform

## funcion para comprobar el sistema
plataforma = platform.system()
def user():
    if plataforma == "Windows":
        ruta_perfil_usuario = os.getenv("USERPROFILE")
        nombre_carpeta = os.path.basename(ruta_perfil_usuario)
        return nombre_carpeta
    elif plataforma == "Linux":
        nombre_usuario = os.getenv("USER")
        return nombre_usuario
nick_usuario = user()

## funcion para posicionarse en la carpeta
def ubicacion_lg():
    os.chdir("C:\\Users\\" + nick_usuario + "\\Desktop\\Repositorios Git\\DAW1_EMPRESA")

## funciones de carga y descarga
def descarga_repositorios():
    os.system("git pull")
    print("\033[32mDescarga finalizada\033[0m")
    time.sleep(3)
    print("")
def carga_repositorios():
    os.system("git add --all")
    os.system("git commit -m \"Actualizacion de repositorio\"")
    os.system("git push")
    print("\033[32mCarga finalizada\033[0m")
    time.sleep(3)
    print("")

## CODIGO PRINCIPAL ##
while(True):
    print(" ------------------------------------ ")
    print("|                                    |")
    print("| 1 Descarga de repositorio a GitLab |")
    print("| 2 Carga de repositorio a GitLab    |")
    print("|                                    |")
    print(" ------------------------------------ ")
    eleccion = input("Seleccione una opcion: ")
    if eleccion == "1":
        ubicacion_lg()
        descarga_repositorios()
        exit()
    elif eleccion == "2":
        ubicacion_lg()
        carga_repositorios()
        exit()
    else:
        print("Opcion no valida. Escribe una correcta")