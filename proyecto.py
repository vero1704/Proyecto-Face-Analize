from datetime import datetime
from typing import KeysView

usu = dict({'fer':['fer','123','admin'],'vero':['vero','123','usuario']})

def iniciar_sesion(usuario,contra):
    usua= usu.keys()
    for i in usua:
        for j in usu:
            if usuario == i :
                return (True, "\n--------------BIENVENIDO -------------- ")
            else:
                    return (False, "\n------Datos invalidos, intente nuevamente-------------\n")


def menuPrincipal():
    menu = ("--------------FACE ANALIZE -------------- \n"
         "***************************************** \n"
         "1.Iniciar Sesion\n"
         "2.Salir\n"
         "\n"
         "Seleccione una opcion: ")
    return menu

def menuAdmin():
    menu = ("--------------FACE ANALIZE -------------- \n"
         "***************************************** \n"
         "\n1.Crear persona automaticamente \n"
         "2.Crear persona manualmente \n"
         "3.Salir\n"
         "\n"
         "Seleccione una opcion: ")
    return  menu

def menuUser():
    menu = ("--------------FACE ANALIZE -------------- \n"
         "***************************************** \n"
         "\n1.Modificar una persona\n"
         "2.Consultar personas \n"
         "3.Salir\n"
         "\n"
         "Seleccione una opcion: ")
    return  menu

def menuAnalista():
    menu = ("--------------FACE ANALIZE -------------- \n"
         "***************************************** \n"
         "\n1.Estadistica por provincia\n"
         "2.Estadistica de grupo etario \n"
         "3.Estadistica por emocióm"
         "4.Salir\n"
         "\n"
         "Seleccione una opcion: ")
    return  menu

def main():
    while True:
        opcion = int(input(menuPrincipal()))
        if opcion == 1:
            usuario = input("Usuario: ")
            contra = input("Contraseña: ")
            log, msj = iniciar_sesion(usuario,contra)
            print(msj)
            while log:
                  op = int(input(menuAdmin()))
                  if op == 3:
                     log = False
                     break

        else:
            break


main()