usuarios = [{"nombreusuario":"Juan","contraseña":"123", "tipo" : "admin"},
            {"nombreusuario":"Carla","contraseña":"123", "tipo" : "user"},
            {"nombreusuario":"Marco","contraseña":"123", "tipo" : "analista"}]



def inicio_Sesión(user,contraseña):
    encontrado = False
    for usuario in usuarios:
        if usuario["nombreusuario"] == user and usuario["contraseña"] == contraseña:
            return usuario["tipo"]
    if encontrado == False:
        print("--------------DATOS ERRONEOS -------------- \n")


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
        menu = int(input(menuPrincipal()))
        if menu == 1:
            usuario = input("Digite su usuario: ")
            contra = input("Digite su contraseña: ")
            tipo = inicio_Sesión(usuario,contra)
            if tipo == "admin":
                opcion = int(input(menuAdmin()))
                if opcion == 1:
                    break
            elif tipo == "user":
                opcion = int(input(menuUser()))
                if opcion == 1:
                    break
            elif tipo == "analista":
                opcion = int(input(menuAnalista()))
                if opcion == 1:
                    break


main()
