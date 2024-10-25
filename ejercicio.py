class Producto:
    # Atributos de clase
    __impuesto = 0.15  # 15% de impuesto

    # Constructor
    def __init__(self, nombre, precio, cantidad):
        # Atributos de instancia
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Método de instancia
    def MostrarDetalles(self):
        return f"Nombre: {self.get_nombre()}, Precio: {self.get_precio()}, Cantidad: {self.get_cantidad()}"
        # Método de clase
    @classmethod  # Decorador
    def CrearDesdeDiccionario(cls, data):
        return cls(data['nombre'], data['precio'], data['cantidad'])

    # Método estático
    @staticmethod  # Decorador
    def CalcularImpuesto(precio):
        return precio * Producto.__impuesto


# Clase hija "ProductoElectrónico" de clase padre "Producto"
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        # Atributo de instancia adicional
        self.__garantia = garantia

    def MostrarDetalles(self):
        # Sobrescribiendo el método de instancia "MostrarDetalles"
        return f"Nombre: {self.get_nombre()}, Precio: {self.get_precio()}, Cantidad: {self.get_cantidad()}, Garantia: {self.__garantia} años"


# Clase hija "ProductoRopa" de clase padre "Producto"
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, cantidad, tamano, color):
        super().__init__(nombre, precio, cantidad)
        # Atributos de instancia adicionales
        self.__tamano = tamano
        self.__color = color

    def MostrarDetalles(self):
        # Sobrescribiendo el método de instancia "MostrarDetalles"
        return f"Nombre: {self.get_nombre()}, Precio: {self.get_precio()}, Cantidad: {self.get_cantidad()}, Tamaño: {self.__tamano}, Color: {self.__color}"


# Creación de objetos de clases hijas
producto1 = ProductoElectronico("Laptop", 1000, 5, 2)
producto2 = ProductoRopa("Camisa", 50, 10, "M", "Rojo")

print(producto1.MostrarDetalles())
print(producto2.MostrarDetalles())
print(f"Impuesto sobre Laptop: {Producto.CalcularImpuesto(producto1.get_precio())}")