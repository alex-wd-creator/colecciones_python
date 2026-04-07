print("*** Playlist ***")

# Aqui se define la lista
lista_reproduccion= []
numero_canciones = int(input("cuantas canciones desea agregar: "))

# itineramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f"proporciona la cancion {indice + 1}: ")
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico
# lista_reproduccion.sort(reverse=True) #orden descendente
lista_reproduccion.sort()

# mostrar la lista de canicones 
print(f"\n Lista de reproduccion en orden alfabético: ")
for cancion in lista_reproduccion:
    print(f"- {cancion}")