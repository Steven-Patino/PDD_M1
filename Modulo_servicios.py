from datetime import date

#function that allows you to check if a book exists in the store
def buscar_libro(inventario, name):
    for p in inventario:
        if p["Título"] == name:
            return p
    return None

#function that checks if the author is in the inventory
def buscar_autor(inventario, name):
    for p in inventario:
        if p["Autor"] == name:
            return p
    return None

#function that requests all the information about a product and adds it to the inventory as a dictionary.
def agregar_producto(inventario):
    name=input("Ingresa el Titulo del libro: ").title().strip()
    autor=input("Ingresa el nombre del autor del libro antes mencionado: ").title().strip()
    category=input("Ingresar la categoría a la que pertenece el libro: ").capitalize().strip()
#validates that the data is an float
    while True:
        price=input("Ingresa el precio de venta del libro: ").strip()
        try:
            price=float(price)
            if price<0:
                print("El precio no puede ser negativo, intenta de nuevo.")
            break
        except:
            print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
            continue
#validates that the data is an integer
    while True:
        quantity=input("Ingresa el número de unidades a ingresar: ").strip()
        try:
            quantity=int(quantity)
            if quantity<0:
                print("La cantidad de unidades no puede ser negativo, intenta de nuevo.")
                continue
            break
        except:
            print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
            continue
    
    producto={"Título":name, "Autor":autor,"Categoría":category ,"Precio":price, "Cantidad":quantity}
    inventario.append(producto)
    return inventario


#This function records a sale, validating if the sale is possible based on stock availability, and updates the stock when it is made.
def registrar_venta(inventario):    
    print("Se procedera a hacer registro de la venta, ingrese los datos solicitados:")
    name=input("Ingrese el nombre del cliente: ").title().strip()
    book=input("Ingrese el título del libro a comprar: ").title().strip()
    existencia=buscar_libro(inventario,book)
    if existencia!=None:
        if existencia["Cantidad"]==0:
            print("El libro buscado no esta disponible debido a que esta agotado actualmente.")
            return None
        else:
            print(f"El libro buscado esta disponible en la tienda, tiene {existencia["Cantidad"]} unidades habilitados para la venta. \n")
    else:
        print("El libro que estas buscando, actualmente no existe esta disponible la tienda.") 
#validates that the data is an float
    while True:
        units=input("Ingrese el número de unidades que se van a comprar de este ejemplar. \n" \
        "Tenga en cuenta que por una compra mayor a 3 unidades se obtiene un 15% de descuento: ").strip()
        try:
            units=int(units)
            if units<0:
                print("La cantidad de unidades no puede ser negativo, intenta de nuevo.")
                continue            
            elif units>existencia["Cantidad"]:
                print("La cantidad en stock no es suficiente para satisfacer la cantidad solicitada, intenta con monto menor.")
                continue
            existencia["Cantidad"]-=units
            break
        except:
            print("El dato ingresado no es congruente con la información solicitada, intenta de nuevo.")
            continue
#Calculate the sales value and apply a discount if more than 3 units are sold.
    subtotal=existencia["Precio"]*units
    if units>3:
        subtotal_descuento=subtotal*(1-15/100)
        nota="Se aplico descuento"
    else:
        subtotal_descuento=subtotal
        nota="No se aplico descuento"

    print("\nLa venta ha sido registrada de forma existosa, a continuación se mostrará la información general de esta:")
    print(f"Cliente: {name}")
    print(f"Producto vendido: {book}")
    print(f"Unidades vendidas: {units}")
    print(f"Día de la venta: {date.today()}")
    print(f"Precio de la venta: {subtotal_descuento}, {nota}")
    
    venta={"Autor":existencia["Autor"],"Producto_vendido": book, "Unidades_vendidas":units, "Subtotal":subtotal, "Con_descuento":subtotal_descuento}
    
    return venta

#function that displays the best-selling items, as well as sales by author and total sales with and without discounts.
def solicitar_reporte(inventario, ventas):
    ganancia_bruta=0
    ganancia_neta=0

    rank=sorted(ventas, key=lambda productos: productos["Unidades_vendidas"])
    print("-----Los 3 productos más vendidos son:-----")
    if len(ventas)==0:
        print("No se han realizado aún ventas.")
    elif len(ventas)==1:
        print(f"1. {rank[len(ventas)-1]["Producto_vendido"]}")
    elif len(ventas)==2:
        print(f"1. {rank[len(ventas)-1]["Producto_vendido"]}")
        print(f"2. {rank[len(ventas)-2]["Producto_vendido"]}")
    else:
        print(f"1. {rank[len(ventas)-1]["Producto_vendido"]}")
        print(f"2. {rank[len(ventas)-2]["Producto_vendido"]}")
        print(f"3. {rank[len(ventas)-3]["Producto_vendido"]}")
    print()

    print("----------Ganancias por Autor----------")
    for i in inventario:
        ventas_autor=sum(p["Con_descuento"] for p in ventas if i["Autor"]==p["Autor"])
        print(f"Los libros del autor {i["Autor"]} han generado {ventas_autor} COP en ventas.")
    print()

    ganancia_bruta=sum(objeto["Subtotal"] for objeto in ventas)
    ganancia_neta=sum(objeto["Con_descuento"] for objeto in ventas)
    print("----------Ganancias totales----------")
    print(f"Ganancias totales sin tener en cuenta descuentos (Bruto): {ganancia_bruta}")
    print(f"Ganancias totales teniendo en cuenta descuentos (Neta): {ganancia_neta}")


#function that removes an item from the inventory based on the book title
def eliminar_producto(inventario, nombre):
    producto = buscar_libro(inventario, nombre)
    if not producto:
        return False

    inventario.remove(producto)
    return True

#function searches for a book and allows you to update its price and stock quantity.
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_libro(inventario, nombre)
    if not producto:
        return False

    if nuevo_precio != None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad != None:
        producto["cantidad"] = nueva_cantidad

    return True