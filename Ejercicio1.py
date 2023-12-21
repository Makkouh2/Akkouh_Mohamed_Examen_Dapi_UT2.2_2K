Lista=["LibroCuentas.txt"]
def LeerDocumento():
    """"La primera función solo lee lo que hay en el fichero

        -parametros: lo guardamos en una lista y cada dato de la lista es una linea

        -salida: devuelve lo que hay en la lista 
    """
    with open("LibroCuentas.txt","r") as file:
        lineas = file.read()
        print(lineas)
    
LeerDocumento()       
        
def IdentificarPagado():
    for linea in Lista:
    