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
    Parameters
    ---------------
    
    returns
    ---------------
    
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list): #funciona, pasa el pytest no modificar
    """ Carga los contactos iniciales de la agenda desde un fichero
    Parameters
    ---------------
        param contactos: list
        esta es nuestra lista principal, declarada en el main
    returns
    ---------------
        no retorna nada por que las lista no es necesario retorna debido a que no es necesario retorna la lista
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...
    datos=('nombre','apellido','email','telefonos')
    tlfn=list()
    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            linea=linea[0:(len(linea))]
            linea=linea.split(";")
            diccionario_clientes={}
            for i in range(len(linea)):
                if i <3:
                    if "\n" in linea[i]:
                        dato=(linea[i][0:(len(linea[i])-1)])
                        diccionario_clientes[datos[i]]=dato
                    else:
                        diccionario_clientes[datos[i]]=linea[i]
                if i>=3:
                    numero=linea[i]
                    if "\n" in numero:
                        tlfn.append(numero[0:(len(numero)-1)])
                    else:
                        tlfn.append(numero)
            diccionario_clientes[datos[3]]=tlfn.copy()
            if diccionario_clientes not in contactos:
                contactos.append(diccionario_clientes.copy())
            tlfn.clear()
            diccionario_clientes.clear()

def buscar_contacto(contactos: list,email:str):#funciona , pytest funciona, no modificar
    """
    se recorre la lista contacto para que devuelva la posicion en donde esta el email del contacto

    internamente tenemos una lista con elementos en diccionario
    contactos[{'nombre':nico,'apellido':aprobado,'email':XXXX@gmail.com,'telefono':[123123123,+34132123321]},{'nombre':paco,'apellido':garcia,'email':XXXX@hotmail.com,'telefono':[123129123,+34137123321]}]
                                                        ---------------                                                                               ----------------
              ------------------------------------si encuentra este correo la posicion es igual a 0--------- ------------------------------------si encuentra este correo la posicion es igual a 1---------
    Parameters
    ---------------
        param contactos: list
        esta es nuestra lista principal, declarada en el main
        param email: str
        es el email a buscar, que el usuario introduce
    returns
    ---------------
    posicion: int
        retorna la posicion, donde esta el email dentro de la lista
        en caso de que no lo encuentre no retorna nada, por defecto la funcion daria el valor: None
    """
# esto lo que ase es que tu tienes la lista te la recorre si hay un valor que esta dentro de email te retorna pos quees la posicion de la lista intermanete tengo[d,d1,d2,d3,d4] donde d3 esta en la pos 3, al no poner nada por defecto las funciones retornan none
    posicion=0
    for clientes in contactos:
        if clientes['email'] == email:
            return posicion
        posicion+=1

def eliminar_contacto(email,contactos: list):#funciona
    """ Elimina un contacto de la agenda
        elimina al contacto de la agenda pero solo te imprime por pantalla no retorna nada 
    Parameters
    ---------------
        param email:str
        es el email que el usuario introduce
        param contactos: list
        esta es nuestra lista principal, declarada en el main
    returns
    ---------------

    """
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        borrar_consola()
        pos = buscar_contacto(contactos,email)
        numeros=""
        if pos != None:
            dato=contactos[pos]
            for i in range(len(dato['telefonos'])):
                numeros+= f" {dato['telefonos'][i]}"    
            print(f"se elimino el contacto {dato['nombre']} {dato['apellido']} con email: {dato['email']}\n los telefono/s son:{numeros}")
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")

def mostrar_menu():#funciona
    """ muestra las opciones que hay en el programa al usuario
    Parameters
    ---------------
    
    returns
    ---------------

    """
    print("1. Nuevo contacto\n2. Modificar contacto\n3. Eliminar contacto\n4. Vaciar agenda\n5. Cargar agenda inicial\n6. Mostrar contactos por criterio\n7. Mostrar la agenda completa\n8. Salir")

def pedir_opcion():#funciona pytest, no modificar
    """ pide el inputs numero al usuario 
    Parameters
    ---------------
    
    returns
    ---------------
    numero:int
    devuelve el numero que ha tecleado el usuario, en caso de que el usuario introduzca una letra el == -1
    """
    numero= input(">> Seleccione una opción:")
    numero=diferencia_simetrica_sino_diego_no_aprueba(numero)
    return numero

def diferencia_simetrica_sino_diego_no_aprueba(opcion:str): #pasa el py test funciona
    """ comprueba si opcion esta dentro del conjunto OPCIONES_MENU

    Parameters
    opcion:str

    ---------------
    opcion: 
    returns
    ---------------
    opcion: int
    es la opcion que ha tecleado el usuario
    -1: int
    en caso de que el usuario haya añadido alguna letra o numero que no este en OPCIONES_MENU, te retorna -1 debido a que seria como que el usuario a tecleado una opcion invalida
    """
    try:
        opcion=int(opcion)
        conjunto_a={opcion}
        conjunto_b=set(OPCIONES_MENU)
        conjunto_c=conjunto_a ^ conjunto_b
        conjunto_d=conjunto_c ^ conjunto_b
        if conjunto_d <= OPCIONES_MENU:
            return opcion
        else:
            print(f"la opcion no es una opcion valida")
            return -1
    except ValueError as e:
        print(f"la opcion no es una opcion valida")
        return -1

def modificar_contacto(contactos:list):
    """
    modifica la informacion del diccionario que esta dentro de la lista contacto 
    imprime en pantalla, si la operacion ha salido bien o mal 
    Parameters
    ---------------
    contactos: list
        es la lista declarada en el main, donde esta todo los contactos
    returns
    ---------------
    
    """
    
    borrar_consola()
    print
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos,input("dame el email del cliente a modificar: "))
        if pos != None:
            print("que quieres modificar\nnombre\napellido\nemail\ntelefono")
            clave=input("¿que quieres modificar?")
            valor=input("dime el nuevo valor del dato")
            dicionario=contactos[pos]
            dicionario[clave]=[valor]
            contactos[pos]=dicionario
            print(f"Se modifico el contacto")
        else:
            print("No se encontró el contacto para modificar")
            pulse_tecla_para_continuar()
    except Exception as e:
        print(f"**Error** {e}")
        print("No se modifico ningún contacto")

def vaciar_agenda(contactos: list):
    """
    elimina todos los contactos de la lista contactos
    imprime por pantalla si la operacion salio bien o mal
    Parameters
    ---------------
    contactos: list
        es la lista contactos, donde estan todos los contactos guardados
    returns
    ---------------
    
    """
    borrar_consola()
    print("se va a eliminar la agenda ENTERA")
    confirmacion=input("¿esta seguro de eliminar la agenda?(si/NO)").upper()
    borrar_consola()
    if confirmacion=="SI":
        contactos.clear()
        print("se elimino la agenda")
    else:
        print("no se elimino la agenda")

def recargar_contactos(contactos):
    """ inserta los contactos del archivo contactos.csv a la lista contactos
    Parameters
    ---------------
    contactos: list
        es la lista contactos, donde estan todos los contactos guardados
    returns
    ---------------
    
    """
    borrar_consola()
    cargar_contactos(contactos)
    print(f"se cargaron contactos {len(contactos)} a la agenda")

def ordenar_agenda(contactos):
    """ te muestra los contactos que tenga el mismo nombre,apellido,telefono,email
    para ello el ususario teclea el valor ordenar, que es la clave, y el valor valor que es para comprobar si esta alguien en la agenda
    Parameters
    ---------------
    contactos: list
        es la lista contactos, donde estan todos los contactos guardados
    returns
    ---------------
    
    """
    diccionario={}
    lista_telefonos=[]
    ordenar=input("como quieres ordenar la lista(nombre/apellido/email/telefonos): ")
    valor=input("cual es el valor a buscar: ")
    if "nombre"==ordenar or "apellido"==ordenar or "email"==ordenar:
        for elementos in contactos:
            diccionario[elementos[ordenar]]=elementos
        diccionario_ord = dict(sorted(diccionario.items()))
        lista=lista_ordenada(diccionario_ord)
        lista_solo_valor=[]
        for i in lista:
            if i[ordenar] ==valor:
                lista_solo_valor.append(i)
        borrar_consola()
        mostrar_contactos(lista_solo_valor)
    elif "telefonos" ==ordenar:
        for elementos in contactos:
            lista=elementos['telefonos']
            for j in range (len(lista)):
                if lista[j]== valor:
                    lista_telefonos.append(elementos)
        borrar_consola()
        mostrar_contactos(lista_telefonos)
    if 0 == len(lista_telefonos) or 0 == len(lista_solo_valor):
        print(f"no se encontro ningun contacto con la informacion {valor}")
            
    else:
        "***ERROR*** --has introducido los parametros mal"

def lista_ordenada(diccionario_ord:dict):#PD: esta funcion la cree por que me creias que querias que ordenaras la agenda por nombre pero todos los nombres alfabeticamente, pero no era asi 
    """ esta funcion lo que hace, pasar de esto
    ejemplo de ordenar por nombre
    diccionario_ord{ ana:{'nombre':ana,'apellido':vela,'email':XXXX@gmail.com,'telefono':[123123123,+34132123321]},paco:{'nombre':paco,'apellido':garcia,'email':XXXX@hotmail.com,'telefono':[123129123,+34137123321]},nico:{'nombre':nico,'apellido':aprobado,'email':XXXX@gmail.com,'telefono':[123123123,+34132123321]},{'nombre':paco,'apellido':garcia,'email':XXXX@hotmail.com,'telefono':[123129123,+34137123321]}}
    pasaria a esto
    lista[{'nombre':ana,'apellido':vela,'email':XXXX@gmail.com,'telefono':[123123123,+34132123321]},{'nombre':paco,'apellido':garcia,'email':XXXX@hotmail.com,'telefono':[123129123,+34137123321]},nico:{'nombre':nico,'apellido':aprobado,'email':XXXX@gmail.com,'telefono':[123123123,+34132123321]},{'nombre':paco,'apellido':garcia,'email':XXXX@hotmail.com,'telefono':[123129123,+34137123321]}]
    Parameters
    ---------------
    diccionario_ord: dict
        es la lista contactos, donde estan todos los contactos guardados
    returns
    ---------------
    lista : list
        es la lista creada con todos los valores  creados

    """
    lista=[]
    for elementos in diccionario_ord:
        lista.append(diccionario_ord[elementos])
    return lista

def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion=0
    while opcion != 8:
        borrar_consola()
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if int(opcion) in OPCIONES_MENU:
            if opcion == 1:# 1. Nuevo contacto
                agregar_contacto(contactos)
            elif opcion == 2:# 2. Modificar contacto
                modificar_contacto(contactos)
            elif opcion == 3:# 3. Eliminar contacto
                borrar_consola()
                eliminar_contacto(input("dame el email del cliente a eliminar: "),contactos)
                pulse_tecla_para_continuar()
            elif opcion == 4:# 4. Vaciar agenda
                vaciar_agenda(contactos)
                pulse_tecla_para_continuar()
            elif opcion == 5:# 5. Cargar agenda inicial
                recargar_contactos(contactos)
                pulse_tecla_para_continuar()
            elif opcion == 6:# 6. Mostrar contactos por criterio
                ordenar_agenda(contactos)
                pulse_tecla_para_continuar()
            elif opcion == 7:# 7. Mostrar la agenda completa
                mostrar_contactos(contactos)
                pulse_tecla_para_continuar()

def pulse_tecla_para_continuar(): #funciona
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")

def validar_email(email:str,contactos): #funciona pasa pytest no modificar
    if email =="" or email == " ":
            raise ValueError("el email no puede ser una cadena vacía")
    elif "@" not in email:
        raise ValueError("el email no es un correo válido")
    else:
        for elementos in contactos:
            elementos=str(elementos['email'])
            if email.upper == elementos.upper:
                raise ValueError("el email ya existe en la agenda")

def pedir_email(contactos): #funciona, pasa pytest
        email=input("dame el email del cliente:\n")
        validar_email(email,contactos)
        if email =="" or email == " ":
            raise ValueError("el email no puede ser una cadena vacía")
        elif "@" not in email:
            raise ValueError("el email no es un correo válido")
        else:
            for elementos in contactos:
                elementos=str(elementos['email'])
                if email.upper == elementos.upper:
                    raise ValueError("el email ya existe en la agenda")
        return email

def pedir_nombre(): #funciona
    print("dime el nombre del cliente:")
    nombre=input().title()
    while nombre =="" or nombre == " ":
        nombre=input("***ERROR***, el nombre no puede estar vacio\n dime el nombre del cliente")
    return nombre

def pedir_apellido(): #funciona
    print("dime el apellido del cliente:")
    apellidos=input().title()
    while apellidos =="" or apellidos == " ":
        apellidos=input("***ERROR***, el apellido no puede estar vacio\n dime el nombre del cliente")
    return apellidos

def validar_telefono(tlfn): #funciona, pasa pytest no modificar
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
        numero=1
        telefonos=[]
        while tlfn!= "":
            tlfn=input(f"dame el numero de telefono {numero} del cliente:\n")
            tlfn=tlfn.replace(" ","")
            validar=validar_telefono(tlfn)
            while validar!=True and tlfn!= "":
                tlfn=input("dame el numero de telefono del cliente(de manera correcta):\n")
                tlfn=tlfn.replace(" ","")
                validar=validar_telefono(tlfn)
            if validar==True and tlfn != "":
                telefonos.append(tlfn)
                numero+=1
    except ValueError:
        print("el numero de telefono se introducio mal")
        pedir_telefono(contactos)
    else:
        return telefonos

def pedir_datos(contactos): #funciona
    diccionario_datos_cliente={}
    datos=('nombre','apellido', 'email','telefonos')
    borrar_consola()
    dato=pedir_nombre()
    diccionario_datos_cliente[datos[0]]=dato
    borrar_consola()
    dato=pedir_apellido()
    diccionario_datos_cliente[datos[1]]=dato
    try:
        borrar_consola()
        dato=pedir_email(contactos)
    except ValueError as e:
        print(e)
        print("el cliente no se añadio, empieza de nuevo")
        pedir_datos(contactos)
    else:
        diccionario_datos_cliente[datos[2]]=dato
        borrar_consola()
        dato=pedir_telefono(contactos)
        borrar_consola()
        diccionario_datos_cliente[datos[3]]=dato
        return diccionario_datos_cliente

def agregar_contacto(contactos:list): #funciona
    verificar=input("¿quieres agregar un nuevo cliente?(SI/no): ").upper()
    if verificar=="" or verificar=="SI":
        borrar_consola()
        dato=pedir_datos(contactos)
        numeros=""
        for i in range(len(dato['telefonos'])):
            numeros+= f" {dato['telefonos'][i]}"
        print(f"se agrego el contacto {dato['nombre']} {dato['apellido']} con email: {dato['email']}\n  los telefono/s son:{numeros}")
        contactos.append(dato)
    else:
        print("\nno se añadio ningun contacto nuevo, volviendo al menu")

def mostrar_contactos(contactos):
    print("AGENDA\n------")
    for contacto in contactos:
        nombre = str(contacto['nombre'])
        nombre=nombre.replace("[","").replace("]","").replace("'","")
        apellidos = str(contacto['apellido'])
        apellidos=apellidos.replace("[","").replace("]","").replace("'","")
        email = str(contacto['email'])
        email=email.replace("[","").replace("]","").replace("'","")
        print(f"Nombre: {nombre} {apellidos} ({email})")
        if len(contacto['telefonos'])==0:
            print(f"Teléfonos: ninguno")
        else:
            texto="Teléfonos: "
            for i in range (len(contacto['telefonos'])):
                telefonos= contacto['telefonos']
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
    eliminar_contacto("rciruelo@gmail.com",contactos)

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