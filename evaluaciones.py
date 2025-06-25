from pizza import Pizza
from ingredientes import Ingredientes
#5. Evaluaciones:
# a. Mostrar atributos de clase
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_masa)
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.formato)

# b. Validar "salsa de tomate" en la lista (la lista de salsas está en ingredientes.py)
print(f"\n¿'salsa de tomate' está en {Ingredientes.salsas}?: ", 
      "Sí se encuentra" if Pizza.validar_elemento("salsa de tomate", Ingredientes.salsas) else "No se encuentra")
print("\n")

# c. Crear instancia y realizar pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar detalles del pedido y validar la pizza.
print(f"""\n--- Detalles del pedido ---
Ingrediente proteico: {mi_pizza.ingrediente_proteico}
Ingredientes vegetales: {mi_pizza.ingredientes_vegetales}
Tipo de masa: {mi_pizza.tipo_masa}
¿Es una pizza válida?: {'Sí' if mi_pizza.valida else 'No'}
""")

# e. Mostrar si la clase Pizza es válida (debe dar error)
print(Pizza.valida)  # Esto genera un error ya que 'valida' es de instancia
