import csv

from Email import email
import os
class menu:
    __va=int
    __Em=email()
    def __init__(self):
        self.__va=None
        self.__Em=email()
    def getopcion(self):
        return self.__init__()
    def manejador (self,op):
        if (op==1):
            self.opcion1()
        elif (op==2):
            self.opcion2 ()
        elif (op==3):
            self.opcion3 ()
    def opcion1(self):
        nomb=input ("Ingrese su nombre:\n")
        usuar=input("Ingrese su usario:\n")
        con=input ("Contrasena:\n")
        self.__Em.crearCuenta(usuar,con,nomb)
        #print ("Estimado señor",nomb,"le enviaremos un email a su cuenta",usuar)
    def opcion2 (self):
        vieja=input ("Por favor ingrese su contraseña anterior\n")
        self.__Em.comprobar(vieja)
        t=input ("Esta conforme con los cambios\n Pulse 1-Si 2-No")
        if (t==2):
            self.opcion2()
    def opcion3 (self):
        archivo=open("Lista.csv")
        reader=csv.reader(archivo,delimiter=';')
        bandera=False
        for Fila in reader:
            if bandera==False:
                bandera = True
            else:
                self.__Em=email(Fila[0], Fila[1], Fila[2], Fila[3])
                print(self.__Em.retornaEmail())







