usu = {"fer": "12345", "raul": "169905"}

def iniciar_sesion(usuario, contra):
    if usuario in usu:
        if usu[usuario] == contra:
            return (True, "___Bienvenido___")
        else:
            return (False, "___Datos invalidos, intente nuevamente___")
    else:
        return (False, "Datos invalidos, intente nuevamente")

def Inicio_Sesión():
    print("___Abrir Expediente Existente___ ")
    nombreusuario= input("Ingrese el nombre de usuario") 
    for usuario in listausuarios:
        if usuario["nombreusuario"] == nombreusuario and usuario["cedula"] == cedula:
            print("Bienvenido al expediente digital")
            return
    print ("nombre de mascota y nombre de dueño incorrectos, intente de nuevo")
Inicio_Sesión()


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

usuario1 = {"nombreusuario": "Juan","cedula": "#la cedula aleatoria",  "edad": "dd/mm/aa","rostro": "#FORMA ROSTRO ","COLOR PIEL": "### ","EMOCIONES": "### ","GÉNERO": "### "}
usuario2 = {"nombreusuario": "Carla","cedula": "#la cedula aleatoria", "edad": "dd/mm/aa","rostro": "#FORMA ROSTRO ","COLOR PIEL": "### ","EMOCIONES": "### ","GÉNERO": "### "}
listausuarios = [usuario, usuario2]
def menuinicio():
    print("___Menu inicio___")
    print("1) Ingrese 1 si desea registrar un nuevo usuario\n"
          "2) Ingrese 2 si desea abrir un expediente existente\n"
          "3) Ingrese 3 si desea salir del menu principal")
    opcion = input("¿Que acción desea realizar?")

    if opcion == "1":
         registrar()

    elif opcion == "2":
        abrirexpediente()

    elif opcion == "3":
        return
    else:
        print ("ingrese un número del menu ")
menuinicio()
def registrar():
    nombremascota = input("Ingrese el nombre de la mascota: ")
    raza = input("Ingrese la raza de la  mascota: ")
    nombredueno = input("Nombre del dueño: ")
    celular = input("Numero celular: ")
    nuevamascota ={"nombremascota": nombremascota," raza": raza, "nombredueno": nombredueno, "numero celular": celular }
    listamascotas.append(nuevamascota)
    print(nombremascota, "Registrado con éxito")
    menuinicio()


def abrirexpediente():
    print("___Abrir Expediente Existente___ ")
    nombremascota= input("Ingrese el nombre de su mascota")
    nombredueno= input("Ingrese el nombre del dueño")
    for mascota in listamascotas:
        if mascota["nombremascota"] == nombremascota and mascota["nombredueno"] == nombredueno:
            print("Bienvenido al expediente digital")
            return
    print ("nombre de mascota y nombre de dueño incorrectos, intente de nuevo")
    abrirexpediente()
    menuinicio()


registrar()