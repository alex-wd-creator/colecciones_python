print("*** Comvinacion listas y tuplas ***")

# Definir una lista que almacena tuplas de producto
productos = [
    ("p001", "camiseta", 20.00),
    ("p002", "jeans", 30.00),
    ("p003", "sudadera", 40.00)
]

# imprimimos la informacion de cada producto
# y calculamos el precio total
precio_total = 0

print(f"informacion de los productos: ")
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto # unpacking
    print(f"Producto: id = {id}, descripcion = {descripcion}, precio= {precio}")
    precio_total += precio # producto[2] para obtener el precio

print(f"precio total d elos productos: {precio_total}")