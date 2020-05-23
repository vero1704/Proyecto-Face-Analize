usu = {"fer": "12345", "raul": "169905"}

def iniciar_sesion(usuario, contra):
    if usuario in usu:
        if usu[usuario] == contra:
            return (True, "___Bienvenido___")
        else:
            return (False, "___Datos invalidos, intente nuevamente___")
    else:
        return (False, "Datos invalidos, intente nuevamente")


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
            log, msj = iniciar_sesion(usuario, contra)
            print(msj)
            while log:
                op = int(input(menuAdmin()))
                if op == 7:
                    log = False
        else:
            break


main()