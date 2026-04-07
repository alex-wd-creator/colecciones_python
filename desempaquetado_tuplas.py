print("*** Desempaquetado de tuplas ***")

producto = ("P001", "Camisa", 20.00)

# Desempaquetamos cada valor en variables independientes
id, descripcion, precio = producto

print(f"tupla completa: {producto}")
# Valores independientes ya desempaquetados
print(f"producto: id = {id}, descripcion = {descripcion}, precio = {precio}")