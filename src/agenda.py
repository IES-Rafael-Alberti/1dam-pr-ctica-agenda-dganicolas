"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1,2,3,4,5,6,7,8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola(): #funciona
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list): #funciona
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...
    datos=('nombre','apellidos','email','telefono')
    tlfn=list()
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            linea=linea[0:(len(linea)-1)]
            linea=linea.split(";")
            diccionario_clientes={}
            for i in range(len(linea)):
                if i <3:
                    diccionario_clientes[datos[i]]=[linea[i]]
                if i>=3:
                    numero=linea[i]
                    if "+34" in numero:
                        numero = numero[0:3]+"-"+numero[3:]
                        tlfn.append(numero)
                    else:
                        tlfn.append(numero)
            diccionario_clientes[datos[3]]=tlfn.copy()
            contactos.append(diccionario_clientes.copy())
            tlfn.clear()
            diccionario_clientes.clear()

def pedir_email_eliminar():
    return input("dame el email del cliente: ")

def buscar_contacto(contactos: list):#funciona
# esto lo que ase es que tu tienes la lista te la recorre si hay un valor que esta dentro de email te retorna pos quees la posicion de la lista intermanete tengo[d,d1,d2,d3,d4] donde d3 esta en la pos 3, al no poner nada por defecto las funciones retornan none
    pos=0
    email=pedir_email_eliminar()
    for clientes in contactos:
        if clientes['email'] == email:
            return pos
        pos+=1

def eliminar_contacto(contactos: list):#funciona
    """ Elimina un contacto de la agenda
    ...
    """
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
            print(contactos)
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

def mostrar_menu():#funciona
    print("1. Nuevo contacto\n2. Modificar contacto\n3. Eliminar contacto\n4. Vaciar agenda\n5. Cargar agenda inicial\n6. Mostrar contactos por criterio\n7. Mostrar la agenda completa\n8. Salir")

def pedir_opcion():
    numero= int(input(">> Seleccione una opción:"))
    while numero > 8 or numero < 1:
        borrar_consola()
        mostrar_menu()
        numero= int(input(">> Seleccione una opción(1 al 8):"))
    return numero

def diferencia_simetrica_sino_diego_no_aprueba(opcion):
    conjunto_a={opcion}
    conjunto_b=set(OPCIONES_MENU)
    conjunto_c=conjunto_a ^ conjunto_b
    conjunto_d=conjunto_c ^ conjunto_b
    return conjunto_d

def modificar_contacto(contactos:list):
    borrar_consola()
    print
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos)
        if pos != None:
            
            print("que quieres modificar\nnombre\napellido\nemail\ntelefono")
            clave=input("¿que quieres modificar?")
            valor=input("dime el nuevo valor del dato")
            contactos[pos]=[clave][valor]
            print(f"Se modifico el contacto {contactos[pos]}")
            print(contactos)
        else:
            print("No se encontró el contacto para modificar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion=0
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if opcion in diferencia_simetrica_sino_diego_no_aprueba(opcion):
            if opcion == 1:
                agregar_contacto(contactos)
            elif opcion == 2:
                modificar_contacto(contactos)
            elif opcion == 3:
                input()
            elif opcion == 4:
                input()
            elif opcion == 5:
                input()
            elif opcion == 6:
                input()
            elif opcion == 7:
                input()



def pulse_tecla_para_continuar(): #funciona
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")

def validar_email(email:str,contactos): #funciona
    if email =="" or email == " ":
            raise ValueError("el email no puede ser una cadena vacía")
    elif "@" not in email:
        raise ValueError("el email no es un correo válido")
    else:
        for elementos in contactos:
            elementos=str(elementos['email'])
            if email.upper == elementos.upper:
                raise ValueError("el email ya existe en la agenda")

def pedir_email(contactos): #funciona
    verificar="S"
    while verificar=="S":
        try:
            verificar="N"
            print("dime el email del cliente")
            email=input()
            validar_email(email,contactos)

        except ValueError as e:
            print(e)
            verificar="S"
            pulse_tecla_para_continuar()
    return email

def pedir_nombre(): #funciona
    print("dime el nombre del cliente")
    nombre=input()
    while nombre =="" or nombre == " ":
        nombre=input("***ERROR***, el nombre no puede estar vacio\n dime el nombre del cliente")
    nombre=nombre.title()
    return nombre

def pedir_apellido(): #funciona
    print("dime el apellido del cliente")
    apellidos=input()
    while apellidos =="" or apellidos == " ":
        apellidos=input("***ERROR***, el apellido no puede estar vacio\n dime el nombre del cliente")
    return apellidos

def validar_telefono(tlfn): #funciona
    try:
        if (len(tlfn) == 12 or len(tlfn)==9) and ("+" in tlfn or "+" not in tlfn):
            if "+" in tlfn:
                if "+34" == tlfn[0:3]:
                    numero=int(tlfn[1:])
                    if type(numero)==int:
                        return True
                else:
                    return False
            else:
                numero=int(tlfn)
                if type(numero)==int:
                    return True
        else:
            return False
    except ValueError:
        print("el telefono se tecleo mal")


def pedir_telefono(contactos): #funciona
    try:
        tlfn=" "
        telefonos=[]
        while tlfn!= "":
            tlfn=input("dame el numero de telefono del cliente: ")
            tlfn=tlfn.replace(" ","")
            validar=validar_telefono(tlfn)
            while validar!=True and tlfn!= "":
                tlfn=input("dame el numero de telefono del cliente(de manera correcta): ")
                tlfn=tlfn.replace(" ","")
                validar=validar_telefono(tlfn)
            if "+34" in tlfn:
                tlfn=tlfn[0:3]+"-"+tlfn[3:]
            if tlfn != "":
                telefonos.append(tlfn)
    except ValueError as e:
        print("el numero de telefono se introducio mal")
        pedir_telefono(contactos)
    else:
        return telefonos

def pedir_datos(contactos): #funciona
    diccionario_datos_cliente={}
    datos=('nombre','apellidos', 'email','telefono')
    dato=pedir_nombre()
    diccionario_datos_cliente[datos[0]]=dato
    dato=pedir_apellido()
    diccionario_datos_cliente[datos[1]]=dato
    dato=pedir_email(contactos)
    diccionario_datos_cliente[datos[2]]=dato
    dato=pedir_telefono(contactos)
    diccionario_datos_cliente[datos[3]]=dato
    print(diccionario_datos_cliente)
    return diccionario_datos_cliente

def agregar_contacto(contactos:list): #funciona
    dato=pedir_datos(contactos)
    contactos.append(dato)

def mostrar_contactos(contactos):
    print("AGENDA\n------")
    for contacto in contactos:
        nombre = str(contacto['nombre'])
        nombre=nombre.replace("[","").replace("]","").replace("'","")
        apellidos = str(contacto['apellidos'])
        apellidos=apellidos.replace("[","").replace("]","").replace("'","")
        email = str(contacto['email'])
        email=email.replace("[","").replace("]","").replace("'","")
        print(f"Nombre: {nombre} {apellidos} ({email})")
        if len(contacto['telefono'])==0:
            print(f"Teléfonos: ninguno")
        else:
            texto="Teléfonos: "
            for i in range (len(contacto['telefono'])):
                telefonos= contacto['telefono']
                texto+= str(telefonos[i]) +" / "
            texto=texto[0:len(texto)-2]
            print(f"{texto}")
        print("......")


#TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)********************************************************
    # ------************************************************************
    # Nombre: Antonio Amargo (aamargo@gmail.com)************************
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.

def main():
    """ Función principal del programa
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(contactos)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos) -------------
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @. ---------------------
    
    
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. ---------------------------
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    
    
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(contactos)#tengo que mejorar esto

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda(contactos)


if __name__ == "__main__":
    main()