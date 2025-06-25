from ingredientes import Ingredientes

#1. clase para crear pizza, con sus atributos de clase.
class Pizza:
    precio = 10000
    formato = "familiar"
    ingredientes_proteicos = Ingredientes.proteicos
    ingredientes_vegetales = Ingredientes.vegetales
    tipos_masa = Ingredientes.masa

    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_masa = None
        self.valida = False

    # Método estático para validar un elemento en una lista
    @staticmethod
    def validar_elemento(elemento, lista_valores):
        return elemento in lista_valores

    # Método para mostrar las opciones de ingredientes.
    def mostrar_opciones(self, opciones):
        for k, v in opciones.items():
            print(f"{k}. {v}")

    # Método para realizar el pedido
    def realizar_pedido(self):
        print("\nRealiza tu pedido de pizza:")

        print("\nSelecciona un ingrediente proteico:")
        self.mostrar_opciones(Pizza.ingredientes_proteicos)
        opcion_proteico = int(input("Ingrese el número de la opción: "))
        if self.validar_elemento(opcion_proteico, Pizza.ingredientes_proteicos):
            self.ingrediente_proteico = Pizza.ingredientes_proteicos[opcion_proteico]

        print("\nSelecciona el primer ingrediente vegetal:")
        self.mostrar_opciones(Pizza.ingredientes_vegetales)
        opcion_veg1 = int(input("Ingrese el número de la opción: "))
        print("\nSelecciona el segundo ingrediente vegetal:")
        self.mostrar_opciones(Pizza.ingredientes_vegetales)
        opcion_veg2 = int(input("Ingrese el número de la opción: "))

        if (self.validar_elemento(opcion_veg1, Pizza.ingredientes_vegetales) and
            self.validar_elemento(opcion_veg2, Pizza.ingredientes_vegetales)):
            self.ingredientes_vegetales = [
                Pizza.ingredientes_vegetales[opcion_veg1],
                Pizza.ingredientes_vegetales[opcion_veg2]
            ]

        print("\nSelecciona el tipo de masa:")
        self.mostrar_opciones(Pizza.tipos_masa)
        opcion_masa = int(input("Ingrese el número de la opción: "))
        if self.validar_elemento(opcion_masa, Pizza.tipos_masa):
            self.tipo_masa = Pizza.tipos_masa[opcion_masa]

        # Validación final
        self.valida = all([
            self.ingrediente_proteico is not None,
            len(self.ingredientes_vegetales) == 2,
            self.tipo_masa is not None
        ])