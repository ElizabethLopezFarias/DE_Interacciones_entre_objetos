from abc import ABC, abstractmethod
# Definimos la Clase Tienda
class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__productos = []
        self.__costo_delivery = costo_delivery

    @abstractmethod
    def ingresar_producto(self, producto):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

# Importación Producto
from producto import Producto

# Definimos objetos y especificamos funciones

class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod += producto.obtener_stock()  # Sumar el stock del nuevo ingreso al producto existente
                return
        # Si el producto no existe, agregarlo a la lista de productos
        self.__productos.append(producto)

    def listar_productos(self):
        return "No hay productos disponibles en el restaurante"

    def realizar_venta(self, nombre_producto, cantidad):
        # No se realiza ninguna validación ni modificación de stock en un restaurante
        return f"Venta realizada: {cantidad} unidades de {nombre_producto}"

class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        self.__productos = []

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod += producto.obtener_stock()  # Sumar el stock del nuevo ingreso al producto existente
                return
        # Si el producto no existe, agregarlo a la lista de productos
        self.__productos.append(producto)

    def listar_productos(self):
        if not self.__productos:
            return "No hay productos disponibles en el supermercado."
        
        lista_productos = ""
        for producto in self.__productos:
            if producto.obtener_stock() < 10:
                lista_productos += f"{producto} - Pocos productos disponibles\n"
            else:
                lista_productos += f"{producto}\n"
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.obtener_nombre() == nombre_producto:
                if cantidad > producto.obtener_stock():  # Validar cantidad disponible
                    cantidad_vendida = producto.obtener_stock()
                    producto.actualizar_stock(0)
                    return f"Venta parcial realizada: {cantidad_vendida} unidades de {nombre_producto}"
                else:
                    producto -= cantidad
                    return f"Venta realizada: {cantidad} unidades de {nombre_producto}"
        return "Producto no encontrado en el supermercado"


class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        self.__productos = []  

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod += producto.obtener_stock()  # Sumar el stock del nuevo ingreso al producto existente
                return
        # Si el producto no existe, agregarlo a la lista de productos
        self.__productos.append(producto)

    def listar_productos(self):
        if not self.__productos:
            return "No hay productos disponibles en la farmacia."
        
        lista_productos = ""
        for producto in self.__productos:
            if producto.obtener_precio() > 15000:
                lista_productos += f"{producto} - Envío gratis al solicitar este producto\n"
            else:
                lista_productos += f"{producto}\n"
        return lista_productos

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.obtener_nombre() == nombre_producto:
                if cantidad > 3:  # Validar cantidad máxima en Farmacia
                    print("No se puede vender más de 3 unidades por producto en la farmacia.")
                    return
                if cantidad <= producto.obtener_stock():
                    producto -= cantidad
                    return f"Venta realizada: {cantidad} unidades de {nombre_producto}"
                else:
                    cantidad_vendida = producto.obtener_stock()
                    producto.actualizar_stock(0)
                    return f"Venta parcial realizada: {cantidad_vendida} unidades de {nombre_producto}"
        return "Producto no encontrado en la farmacia"
