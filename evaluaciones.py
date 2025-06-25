from pizza import Pizza

# a. Mostrar atributos de clase
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_masa)
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.formato)

# b. Validar "salsa de tomate" en la lista
print("\n¿'salsa de tomate' está en ['salsa de tomate', 'salsa bbq']?:", 
      Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear instancia y realizar pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar detalles del pedido
print("\n--- Detalles del pedido ---")
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Es una pizza válida?:", mi_pizza.valida)

# e. Mostrar si la clase Pizza es válida (debe dar error)
print(Pizza.valida)  # Esto generará un error ya que 'valida' es de instancia
