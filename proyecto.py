import random

usuarios = [{"nombreusuario":"Juan","contraseña":"123", "tipo" : "admin"},
            {"nombreusuario":"Carla","contraseña":"123", "tipo" : "user"},
            {"nombreusuario":"Marco","contraseña":"123", "tipo" : "analista"}]

personas = []


def inicio_Sesión(user,contraseña):
    encontrado = False
    for usuario in usuarios:
        if usuario["nombreusuario"] == user and usuario["contraseña"] == contraseña:
            return usuario["tipo"]
    if encontrado == False:
        print("-------Datos inválidos.Vuelva a intentarlo-------- \n")

def generarCedulas():
    cedula = random.randrange(1000) + 1
    return  cedula

def generarEdad():
    edades = random.randrange(0, 100)
    return edades

def formaRostro():
    rostro =["Redondo", "Alargado","Corazón","Cuadrado","Ovalado","Rectangular"]
    return rostro

def emociones():
    emocion = ["Enfado","Desprecio", "Disgusto", "Miedo", "Sorpresa", "Alegría", "Neutral","Tristeza"]
    return emocion


def colorPiel():
    piel = ["Negra","Marrón", "Morena", "Clara","Blanca"]
    return piel

def generos():
    genero = ['Masculino', 'Femenino']
    return genero

def grupoEtario(edad):
    if edad > 0 and edad <10:
        return "Niño"
    elif edad > 10 and edad <=19:
        return "Adolescente"
    elif edad >=20 and edad< 59:
        return "Adulto"
    elif edad >=59:
        return "Adulto Mayor"

def accesorios():
    accesorio = ["Lentes", "Aretes", "Percing"," "]
    return accesorio

def cabellos():
    cabellos = {}
    cabellos["color"] = ["Negro", "Rubio", "Café", "Castaño", "Gris", "Invisible"]
    cabellos["densidad"] = ["Escaso", "Moderado", "Abundante"]
    cabellos["textura"] = ["Lacio","Ondulado","Rizado"]
    return cabellos

def ojos():
    ojos = {}
    ojos["forma"] = ["Almendrados", "Separados", "Redondos", "Caídos", "Saltones", "Juntos", "Profundos","Asiático"]
    ojos["color"] = ["Negro", "Castaño", "Ámbar", "Avellana", "Verde", "Azul", "Gris"]
    return ojos

def ojosForma(ojos):
    forma = random.choice(ojos["forma"])
    return forma

def ojosColor(ojos):
    color = random.choice(ojos["color"])
    return color

def colorPelo(cabello):
        pelo = random.choice(cabello["color"])
        return pelo


def densidadCabello(cabello):
    pelo = random.choice(cabello["densidad"])
    return pelo

def texturaCabello(cabello):
        pelo = random.choice(cabello["textura"])
        return pelo

def provincias():
    provincia = ["San José","Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
    return  provincia

def crearPersona():
    diccionario = {}
    cedula = generarCedulas()
    edad = generarEdad()
    rostro = random.choice(formaRostro())
    idRostro = formaRostro().index(rostro)
    piel = random.choice(colorPiel())
    idPiel = colorPiel().index(piel)
    grupo = grupoEtario(edad)
    idGrupo = grupoEtario(edad).index(grupo)
    genero = random.choice(generos())
    idGenero = generos().index(genero)
    emocion = random.choice(emociones())
    idEmocion = emociones().index(emocion)
    accesorio = random.choice(accesorios())
    idAccesorio = accesorios().index(accesorio)
    provincia = random.choice(provincias())
    idProvincia = provincias().index(provincia)
    cabelloColor = colorPelo(cabellos())
    idCabelloColor = colorPelo(cabellos()).index(cabelloColor)
    cabelloDensidad = densidadCabello(cabellos())
    #idCabelloDensidad = densidadCabello(cabellos()).index(cabelloDensidad)
    cabelloTextura = texturaCabello(cabellos())
    #idCabelloTextura = texturaCabello(cabellos()).index(cabelloTextura)
    formaOjos = ojosForma(ojos())
    #idFormaOjos = ojosForma(ojos()).index(formaOjos)
    colorOjos = ojosColor(ojos())
    #idColorOjos = ojosColor(ojos()).index(colorOjos)
    diccionario = {"Cedula:":cedula,"Edad:": edad,"Rostro":idRostro,"Color Piel:":idPiel,"Grupo Etario:":idGrupo,"Genero:":idGenero,
                   "Emocion: ":idEmocion,"Accesorios:":idAccesorio,"Color Cabello:":idCabelloColor,"Densidad Cabello:":cabelloDensidad,
                   "Textura cabello:":cabelloTextura,"Forma ojos:":formaOjos,"Color ojos:":colorOjos,"Provincia:":idProvincia}
    personas.append(diccionario)
    return personas


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
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuAdmin()))
                if opcion == 1:
                    print(crearPersona())
                else:
                    break
            elif tipo == "user":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuUser()))
                if opcion == 1:
                    break
            elif tipo == "analista":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuAnalista()))
                if opcion == 1:
                    break


main()
