# pizza.py

class Pizza:
    # Atributos de clase
    ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]
    precio = 10000
    tamanio = "familiar"

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

    # Método para realizar el pedido
    def realizar_pedido(self):
        print("Realiza tu pedido de pizza:\n")

        self.ingrediente_proteico = input("Ingresa un ingrediente proteico: ").lower()
        vegetal_1 = input("Ingresa el primer ingrediente vegetal: ").lower()
        vegetal_2 = input("Ingresa el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingresa el tipo de masa (tradicional o delgada): ").lower()

        self.ingredientes_vegetales = [vegetal_1, vegetal_2]

        # Validaciones
        es_valido_proteico = Pizza.validar_elemento(self.ingrediente_proteico, Pizza.ingredientes_proteicos)
        es_valido_vegetal_1 = Pizza.validar_elemento(vegetal_1, Pizza.ingredientes_vegetales)
        es_valido_vegetal_2 = Pizza.validar_elemento(vegetal_2, Pizza.ingredientes_vegetales)
        es_valido_masa = Pizza.validar_elemento(self.tipo_masa, Pizza.tipos_masa)

        self.valida = all([es_valido_proteico, es_valido_vegetal_1, es_valido_vegetal_2, es_valido_masa])
