
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        return f"{self.nombre}: ${self.precio}"


class Camisa(Producto):
    def __init__(self, precio, talla):
        super().__init__("Camisa", precio)
        self.__talla = talla  

    def mostrar_informacion(self):  
        return f"{self.nombre} - Talla: {self.__talla} - Precio: ${self.precio}"

class Pantalon(Producto):
    def __init__(self, precio, talla):
        super().__init__("Pantalón", precio)
        self.__talla = talla  

    def mostrar_informacion(self):  
        return f"{self.nombre} - Talla: {self.__talla} - Precio: ${self.precio}"

class Zapato(Producto):
    def __init__(self, precio, talla):
        super().__init__("Zapato", precio)
        self.__talla = talla  

    def mostrar_informacion(self):  
        return f"{self.nombre} - Talla: {self.__talla} - Precio: ${self.precio}"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def procesar_compra(self):
        total = sum(producto.precio for producto in self.productos)
        print(f"\nTotal de la compra: ${total}")


def realizar_compra():
    tienda = Tienda()
    
    while True:
        print("\nSeleccione un producto para agregar:")
        print("1. Camisa")
        print("2. Pantalón")
        print("3. Zapato")
        print("4. Finalizar compra")
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            precio = float(input("Ingrese el precio de la camisa: "))
            talla = input("Ingrese la talla de la camisa: ")
            tienda.agregar_producto(Camisa(precio, talla))
        
        elif opcion == "2":
            precio = float(input("Ingrese el precio del pantalón: "))
            talla = input("Ingrese la talla del pantalón: ")
            tienda.agregar_producto(Pantalon(precio, talla))
        
        elif opcion == "3":
            precio = float(input("Ingrese el precio del zapato: "))
            talla = input("Ingrese la talla del zapato: ")
            tienda.agregar_producto(Zapato(precio, talla))
        
        elif opcion == "4":
            print("\nProductos en tu carrito:")
            tienda.mostrar_productos()
            tienda.procesar_compra()
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


realizar_compra()
