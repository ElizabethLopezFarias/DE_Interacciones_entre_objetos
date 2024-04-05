class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    # encapsulamiento
    def obtener_nombre(self):
        return self.__nombre
    # encapsulamiento
    def obtener_precio(self):
        return self.__precio
    # encapsulamiento
    def obtener_stock(self):
        return self.__stock
    
    # verificación y actualización de stock 
    def actualizar_stock(self, cantidad):
        if cantidad >= 0:
            self.__stock = cantidad
        else:
            self.__stock = 0

    # Sobrecarga del método __str__ para imprimir el producto de forma legible
    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio}, Stock: {self.__stock}"

    def __add__(self, cantidad):
        self.__stock += cantidad
        return self

    def __sub__(self, cantidad):
        if self.__stock >= cantidad:
            self.__stock -= cantidad
        else:
            print("No hay suficiente stock disponible")
        return self

    def __eq__(self, otro_producto):
        return self.__nombre == otro_producto.obtener_nombre()  # Comparar por el nombre del producto