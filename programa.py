from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ").lower()
    
    if tipo_tienda == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda inválido. Inténtelo nuevamente.")
        return crear_tienda()

def ingresar_producto(tienda):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    producto = Producto(nombre, precio, stock)
    tienda.ingresar_producto(producto)
    print("Producto ingresado correctamente.")

def listar_productos(tienda):
    print("Productos existentes:")
    print(tienda.listar_productos())

def realizar_venta(tienda):
    nombre_producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    resultado_venta = tienda.realizar_venta(nombre_producto, cantidad)
    print(resultado_venta)

if __name__ == "__main__":
    tienda = crear_tienda()

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Ingresar Productos")
        print("2. Listar productos existentes")
        print("3. Realizar una venta")
        print("4. Salir del programa")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            ingresar_producto(tienda)
        elif opcion =="2":
            listar_productos(tienda)
        elif opcion == "3":
            realizar_venta(tienda)
        elif opcion == "4":
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")
