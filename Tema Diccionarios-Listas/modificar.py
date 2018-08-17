
listaProductos= [{"ID":"2","Nombre":"Bombillo","Cantidad": 5,"Descripcion":"generico","Precio":500}]


def imprimirProductos():
    for i in listaProductos:
        print("\n\n\n")
        print("ID: ",i["ID"],"\n"
              "Nombre: ",i["Nombre"],"\n"
              "Cantidad",i["Cantidad"],"\n"
              "Descripcion",i["Descripcion"],"\n"
              "Precio",i["Precio"])



def diccionarioModificar(identificador, valorCambiar, op):

    for i in listaProductos:

        if i["ID"]== identificador:
            if(valorCambiar == "Nombre"):
                if(i["Nombre"] != op):
                    i["Nombre"] = op

            elif(valorCambiar == "Cantidad"):
                if(i["Cantidad"] != op):
                    i["Cantidad"] = op

            elif(valorCambiar == "Descripcion"):
                if(i["Descripcion"] != op):
                    i["Descripcion"] = op

            else:
                if(i["Precio"] != op):
                    i["Precio"] = op

    print(listaProductos)




def menu():
    opcion= int(input("Bienvenido \n"
                      "1.imprimir productos \n"
                      "2.Modificar productos\n"
                      "Opcion: "))


    if(opcion==1):
       imprimirProductos()
       print("\n\n\n\n")
       menu()

    if(opcion ==2):
       identificador = input("digite el identificador")
       op = input( "1.Cambio nombre\n"
                   "2.Cambio de cantidad\n"
                   "3.Cambio de descripcionn\n"
                   "4.Cambio de precio \n")

       if(op == "1"):
           nombre = input("Ingrese el nombre nuevo")
           diccionarioModificar(identificador, "Nombre" ,nombre)
       if(op == "2"):
            cantidad = input("Ingrese la cantidad nueva")
            diccionarioModificar(identificador,  "Cantidad",cantidad)
       if(op == "3"):
            descripcion = input("Ingrese la descripción nueva")
            diccionarioModificar(identificador,  "Descripcion",descripcion)
       if(op == "4"):
            precio = input("Ingrese el precio nuevo")
            diccionarioModificar(identificador, "Precio",precio)

       print("\n\n\n\n")
       menu()



menu()