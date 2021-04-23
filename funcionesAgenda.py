import os

registro = {
    "Nombre" : None,
    "Apellido_P" : None,
    "Apellido_M" : None,
    "Teléfono_Móvil" : None,
    "Teléfono_Casa" : None,
    "Teléfono_Trabajo" :None
}

contactos=[]

def menu():
    while True:
        try:
            print("1)Registrar contacto","2)Listar contacto","3)Buscar contacto",
            "4)Modificar contacto","5)Eliminar contacto","6)Salir",sep="\n",end="\n")
            op=int(input("Seleccione la opción deseada->"))
            if op <= 0 or op > 6 :
                borrarPantalla()
                print("**Ésta opción NO existe, intenta de nuevo***",end="\n\n")
            else:
                return op
                break
                borrarPantalla()
                
        except ValueError as error:
            borrarPantalla()
            print("***El valor ingresado no es valido:***",error,"\nIntente de nuevo",sep="\n",end="\n\n")
        
def registrar_contacto(nombre,tel_c=None, tel_m=None, tel_t=None):
    if len(nombre) == 1:
        contactos.append({"Nombre":nombre[0],
                    "Apellido_P": "",
                    "Apellido_M":"",
                    "Teléfono_Móvil":tel_m,
                    "Teléfono_Casa":tel_c,
                    "Teléfono_Trabajo": tel_t})
    elif len(nombre) == 2:
        contactos.append({"Nombre":nombre[0],
                    "Apellido_P":nombre[1],
                    "Apellido_M":"",
                    "Teléfono_Móvil":tel_m,
                    "Teléfono_Casa":tel_c,
                    "Teléfono_Trabajo": tel_t})
    elif len(nombre) == 3:
        contactos.append({"Nombre":nombre[0],
                    "Apellido_P":nombre[1],
                    "Apellido_M":nombre[2],
                    "Teléfono_Móvil":tel_m,
                    "Teléfono_Casa":tel_c,
                    "Teléfono_Trabajo": tel_t})

def listar_contacto():
    borrarPantalla()
    if len(contactos) == 0:
        print("***No hay contactos registrados***",end="\n\n")
    else:
        for i in contactos:
            print("Nombre:",i["Nombre"])
            print("Apellido_P:",i["Apellido_P"])
            print("Apellido_M:",i["Apellido_M"])
            print("Teléfono_Móvil:",i["Teléfono_Móvil"])
            print("Teléfono_Casa:",i["Teléfono_Casa"])
            print("Teléfono_Trabajo:",i["Teléfono_Trabajo"])
            print("\n\n")

def buscar_contacto():
    while True:
        try:
            buscar=int(input("Ingrese el Nombre-->"))
        except ValueError as Error:
                print("Valor invalido", error)
        else:
            if buscar not in ids:
                print("ESTE CONTACTO NO EXISTE")
            else:
                for i in contactos:
                    if buscar == i["Nombre"]:
                        print("Nombre:", i["Nombre"])
                        print("Apellido_P:", i["Apellido_P"])
                        print("Apellido_M:",i["Apellido_M"])
                        print("Teléfono_Móvil:",i["Teléfono_Móvil"])
                        print("Teléfono_Casa:",i["Teléfono_Casa"])
                        print("Teléfono_Trabajo:",i["Teléfono_Trabajo"])
                        print("\n\n")
                        break
            break

def modificar_contacto():
    pass

def eliminar_contacto():
    pass

def salir():
    pass

def validar(nom):
	nom=nom.split()
	nom="".join(nom)
	if nom != nom.isalpha() == False:
		return 0
	else:
		return 1

def registrar_nombre():
    borrarPantalla()
    while True:
        print("Formato de entrada: fernando sanchez plascencia")
        nombre = input("Ingrese su nombre->")
        validacion = validar(nombre)
        if validacion == 1:
            nombre=nombre.split()
            return nombre
            break
        else:
            borrarPantalla()
            print("Los datos ingresados no son válidos o no pueden ir vacios")

def registrar_tel():
    tel_cas=None
    tel_m=None
    tel_t=None
    while True:
        print("1)Teléfono de casa","2)Teléfono móvil","3)Teléfono de trabajo","4)Menú anterior",sep="\n",end="\n\n")
        try:
            sel_num = int(input("¿Qué número desea registrar?->"))
        except ValueError as error:
            borrarPantalla()
            print("***Seleccion invalida***",error,sep="\n",end="\n\n")
        else:
            if sel_num == 1:
                borrarPantalla()
                while True:
                    try:
                        tel_cas = int(input("Ingrese el telefono de casa->"))
                        tel_cas=str(tel_cas)
                    except ValueError as error:
                        borrarPantalla()
                        print("***El valor ingresado es invalido***",error,sep="\n",end="\n\n")
                    else:
                        if len(tel_cas) > 10 or len(tel_cas) < 10:
                            borrarPantalla()
                            print("***El número debe tener diez digitos***",end="\n\n")
                        else:
                            print("***El número {} ha sido registrado con exito***".format(tel_cas), end="\n\n")                                    
                            break
            elif sel_num == 2:
                borrarPantalla()
                while True:
                    try:
                        tel_m = int(input("Ingrese el teléfono móvil->"))
                        tel_m =str(tel_m)
                    except ValueError as error:
                        borrarPantalla()
                        print("***El valor ingresado es invalido***",error,sep="\n",end="\n\n")
                    else:
                        if len(tel_m) > 10 or len(tel_m) < 10:
                            borrarPantalla()
                            print("***El número debe tener diez digitos***",end="\n\n")
                        else:
                            print("***El número {} ha sido registrado con exito***".format(tel_m), end="\n\n")                                    
                            break
            elif sel_num == 3:
                borrarPantalla()
                while True:
                    try:
                        tel_t = int(input("Ingrese el teléfono del trabajo->"))
                        tel_t=str(tel_t)
                    except ValueError as error:
                        borrarPantalla()
                        print("***El valor ingresado es invalido***",error,sep="\n",end="\n\n")
                    else:
                        if len(tel_t) > 10 or len(tel_t) < 10:
                            borrarPantalla()
                            print("***El número debe tener diez digitos***",end="\n\n")
                        else:
                            print("***El número {} ha sido registrado con exito***".format(tel_t), end="\n\n")                                    
                            break
            elif sel_num == 4:
                borrarPantalla()
                break
            else:
                borrarPantalla()
                print("***Ésta opción no es válida***",end="\n\n")  
    return tel_cas,tel_m,tel_t

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix": #sistemas Unix y GNU/Linux
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos": #Sistemas Windows
        os.system ("cls")
