import csv
import os
from Email import email
from Menu import menu
def test():
    va=input("Desea realizar el test\n 1-Si\t 2-No\n")
    nuevotest=email()
    if (va=="1"):
        print ("------Test--------\n Datos correctos:corderocccc@gmail.com, informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com\n")
        print ("1°")
        nuevotest.crearCuenta('corderocccc@gmail.com','Juan','Alfredo')
        print (nuevotest.retornaEmail())
        print("2°")
        nuevotest.crearCuenta('informatica.fcefn@gmail.com','Pepe','Godzila')
        print (nuevotest.retornaEmail())
        print ("3°")
        nuevotest.crearCuenta('juanLiendro1957@yahoo.com','Arnoldo','Dracula')
        print(nuevotest.retornaEmail())
        os.system("pause")
        os.system("cls")
        print ("Datos Erroneos: ahgikuahgkia , fkahih@gfjak, fhakhfuujs.com\n")
        print ("1°\n")
        nuevotest.crearCuenta("ahgikuahgkia","afa","Roberto")
        print (nuevotest.retornaEmail())
        print ("2°\n")
        nuevotest.crearCuenta("fkahih@gfjak","afa","Roberto")
        print (nuevotest.retornaEmail())
        print ("3°\n")
        nuevotest.crearCuenta("fhakhfuujs.com","afa","Roberto")
        print (nuevotest.retornaEmail())
        os.system("pause")
        os.system("cls")


    elif(va=="2"):
        return
    else:
        print ("Dato no valido\n ")
        test()


if __name__== "__main__":
    test()
    pan=menu()
    op=int(input("Seleccione la opcion deseada\n 1-Ingresar el nombre y email de un usuario\n 2-Modificar contraseña\n 3-Leer archivo\n 4-Salir\n"))
    while (op<5 or op>0):
        pan.manejador(op)
        op=int(input("Seleccione la opcion deseada\n 1-Ingresar el nombre y email de un usuario\n 2-Modificar contraseña\n 3-Leer archivo\n 4-Salir\n"))

        if(op>5 or op<=0):
            print ("Valor invalido")
            op=int(input("Seleccione la opcion deseada\n 1-Ingresar el nombre y email de un usuario\n 2-Modificar contraseña\n 3-Leer archivo\n 4-Salir\n"))
            pan.manejador(op)
        elif (op==5)
            os.
            print ("Sayonara")



