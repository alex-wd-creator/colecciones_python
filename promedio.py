print(" *** Promedio de calificaciones ***")

total_calificaciones = int(input("proporciona el numero de calificaciones a evaluar: "))
calificaciones = []

# iteramos las calificaciones
for indice in range(total_calificaciones):
    calificacion = int(input(f"calificacion[{indice}] = "))
    calificaciones.append(calificacion) # Agregamos la calificacion a la lista

# imprimimos las calificaciones proporcionadas
print(f"\n las calificaciones proporcionadas son: {calificaciones}")

# calculamos el promedio de las calificaciones
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones/ total_calificaciones
print(f"\n Promedio de las calificaciones: {promedio}")