import Modulo_servicios as ms

#the initial inventory is loaded with 5 default products
inventario=[{"Título":"Metamorfosis","Autor":"Frank Kafka","Categoría":"Ficción","Precio": 27000, "Cantidad":30},
            {"Título":"El Perfume","Autor":"Patrick Süskind","Categoría":"Horror","Precio": 33200, "Cantidad":30},
        {"Título":"El Principito","Autor":"Antoine de Saint-Exupéry","Categoría":"Fábula","Precio": 30000, "Cantidad":30},
        {"Título":"Cien Años De Soledad","Autor":"Gabriel García Márquez","Categoría":"Novela","Precio": 50000, "Cantidad":30},
        {"Título":"El Quijote De La Mancha","Autor":"Miguel de Cervantes Saavedra","Categoría":"Novela","Precio": 61000, "Cantidad":30}]
ventas=[]

#Initialize the options menu; this will continue to function until the user selects the exit option.
while True:
    print("\n----------Bienvenido al Sistema Integral de Gestión de Inventario y Ventas----------")
    print("1. Registrar producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Estadísticas relevantes")
    print("7. Salir")
    opcion_menu=input("\nEscoge el número correspondiente a la opción escogida: ")
#validates that the data is an integer
    try:
        opcion_menu=int(opcion_menu)
    except ValueError:
        print("El elemento ingresado no corresponde con alguna de las opciones, observa bien el menú e intenta de nuevo.")
        continue

#Option 1 allows you to add a product to the inventory by calling the add product function.
    if opcion_menu==1:
        print("Has escogido la opción regitrar producto.\n" \
        "Se procedera a hacer registro del producto, ingrese los datos solicitados:")
        inventario=ms.agregar_producto(inventario)
        print("El producto ha sido ingresado de manera exitosa al sistema, seras redireccionado al menú principal\n")

#Option 2 allows you to search if a book is in the system; if the book exists in the system, it displays all its information.
    elif opcion_menu==2:
        a_buscar=input("Ingrese el título del libro que deseas consultar en el sistema: ").strip().title()
        respuesta=ms.buscar_libro(inventario,a_buscar)
        if respuesta!=None:
            print("\nA continuación se mostrara la información del objeto buscado:\n")
            print(f"Título:{respuesta["Título"]}\nAutor:{respuesta["Autor"]}\nCategoría:{respuesta["Categoría"]}\nPrecio:{respuesta["Precio"]}\nCantidad:{respuesta["Cantidad"]}")
        else:
            print("El elemento buscado no existe actualmente en el sistema, revisa bien e intenta nuevamente.")
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal\n")
    
#Option 3 allows you to search if a book is in the system. If the book exists in the system, 
#it requests the new price and the new quantity in stock to update the inventory.
    elif opcion_menu==3:
        a_buscar=input("Ingrese el título del libro que deseas actualizar su información en el sistema: ").strip().title()
        producto_encontrado=ms.buscar_libro(inventario, a_buscar)
        if producto_encontrado==None:
            print("\n"+f"El producto {a_buscar} no se encuentra actualmente en el inventario.")

        else:
            ##validates that the data is a float
            while True:
                nuevo_precio=input("Ingresa el nuevo precio de venta del libro: ").strip()
                try:
                    nuevo_precio=float(nuevo_precio)
                    if nuevo_precio<0:
                        print("El precio no puede ser negativo, intenta de nuevo.")
                    break
                except:
                    print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
                    continue
            ##validates that the data is an inter
            while True:
                nueva_cantidad=input("Ingresa el número actual de unidades del libro mencionado: ").strip()
                try:
                    nueva_cantidad=int(nueva_cantidad)
                    if nueva_cantidad<0:
                        print("La cantidad de unidades no puede ser negativo, intenta de nuevo.")
                        continue
                    break
                except:
                    print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
                    continue
            ms.actualizar_producto(inventario, a_buscar, nuevo_precio, nueva_cantidad)
            print("\n"+f"El producto {a_buscar} ha sido actualizado de manera exitosa en el sistema, seras redireccionado al menú principal")

#Option 4 allows you to search if a book is in the system; if the book exists in the system, it removes it from the inventory.
    elif opcion_menu==4:
        nombre_eliminar=input("Ingresa el nombre del producto a eliminar: ").strip().title()
        producto_encontrado=ms.buscar_libro(inventario, nombre_eliminar)
        if producto_encontrado==False:
            print("\n"+f"El producto {nombre_eliminar} no se a podido eliminar porque no existe en el inventario, Seras redireccionado al menú principal")
        else:
            inventario.remove(producto_encontrado)
            print("\n"+f"El producto {nombre_eliminar} ha sido eliminado de manera exitosa del sistema, seras redireccionado al menú principal")

#Option 5 requests all the information necessary to register a sale and saves it in a dictionary list.
    elif opcion_menu==5:
        venta=ms.registrar_venta(inventario)
        ventas.append(venta)
        print("La venta ha sido registrada de manera exitosa al sistema, seras redireccionado al menú principal\n")

#Option 6 allows you to request all general sales statistics, showing sales by author, total sales with and without discounts, as well as the 3 best-selling items
    elif opcion_menu==6:
        ms.solicitar_reporte(inventario,ventas)
        print("\n"+"Se ha terminado la acción seleccionada, Seras redirigido al menú principal\n")

#This option ends the menu loop and allows the user to terminate the program.
    elif opcion_menu==7:
        print("Haz salido correctamente del sistema, vuelva pronto.")
        break

#block of code that validates that the chosen option is between 1 and 9, otherwise, it requests the data again.
    else:
        print("El elemento ingresado no corresponde con alguna de las opciones, observa bien el menú e intenta de nuevo.")
        continue