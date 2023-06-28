import os
os.system("cls")

listacod = []
listanom = []
listacatg = []
listapre = []
listastock = []

menu = """
1. Registro de Productos
2. Busqueda de Productos
3. Listar Productos
4. Salir
"""
while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1:
            while True:
                try:
                    cod = (input("Ingrese Codigo: "))
                    if len(cod) == 6:
                        listacod.append(cod)
                        break
                    else:
                        ("Error en el Codigo")
                except:
                    print("Error de Ingreso, Reintente")
            while True:
                try:
                    nom = (input("Ingrese Nombre: "))
                    if len(nom) > 2:
                        listanom.append(nom)
                        break
                    else:
                        print("Error de Ingreso, Reintente")
                except:
                    print("Ocurrio una Excepcion")
            while True:
                try:
                    catg = input("Ingrese Categoria: ")
                    if len(catg) > 0:
                        listacatg.append(catg)
                        break
                    else:
                        print("Error de Ingreso, Reintente")
                except:
                    print("Ocurrio una Excepcion")
            while True:
                try:
                    pre = (input("Ingrese Precio: "))
                    if len(pre) > 0:
                        listapre.append(pre)
                        break
                    else:
                        print("Error de Ingreso, Reintente")
                except:
                    print("Ocurrio una Excepcion")
            while True:
                try:
                    stock = (input("Ingrese Stock: "))
                    if len(stock) > 1:
                        listastock.append(stock)
                        break
                    else:
                        print("Error de Ingreso, Reintente")
                except:
                    print("Ocurrio Una Excepcion")
    except:
     print("Ocurrio Una excepcion")