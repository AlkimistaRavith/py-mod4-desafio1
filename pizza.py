from ingredientes import Ingredientes

#1. clase para crear pizza, con sus atributos de clase.
class Pizza:
    precio = 10000
    formato = "familiar"
    ingredientes_proteicos = Ingredientes.proteicos
    ingredientes_vegetales = Ingredientes.vegetales
    tipos_masa = Ingredientes.masa
    lista_salsas = Ingredientes.salsas

    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_masa = None
        self.valida = False

    #2. Método estático para validar un elemento en una lista
    @staticmethod
    def validar_elemento(elemento, lista_valores):
        return elemento in lista_valores

    #3. Método para realizar un pedido
    def realizar_pedido(self):
        print("--Realiza tu pedido de pizza--")
        #Muestra opciones y pide ingrediente proteico
        print("Ingredientes proteicos disponibles: ", Pizza.ingredientes_proteicos)
        self.ingrediente_proteico = input("Ingresa un ingrediente proteico: ").lower()
        #Muestra opciones y pide ingredientes vegetales
        print("Ingredientes vegetales disponibles: ", Pizza.ingredientes_vegetales)
        vegetal_1 = input("Ingresa el primer ingrediente vegetal: ").lower()
        vegetal_2 = input("Ingresa el segundo ingrediente vegetal: ").lower()
        #Agrega vegetales a una lista.
        self.ingredientes_vegetales = [vegetal_1, vegetal_2]
        #Muestra opciones y pide seleccionar tipo de masa.
        print("Tipos de masa disponibles: ", Pizza.tipos_masa)
        self.tipo_masa = input("Ingresa el tipo de masa (tradicional o delgada): ").lower()

    #4. Validación de la pizza:
        #Validaciones de los ingredientes
        validacion_proteica = Pizza.validar_elemento(self.ingrediente_proteico, Pizza.ingredientes_proteicos)
        validacion_vegetal_1 = Pizza.validar_elemento(vegetal_1, Pizza.ingredientes_vegetales)
        validacion_vegetal_2 = Pizza.validar_elemento(vegetal_2, Pizza.ingredientes_vegetales)
        validacion_masa = Pizza.validar_elemento(self.tipo_masa, Pizza.tipos_masa)
        
        #Si todos(all) los elementos son True, valida es True (pizza valida).
        self.valida = all([validacion_proteica, validacion_vegetal_1, validacion_vegetal_2, validacion_masa])

