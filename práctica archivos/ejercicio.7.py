def guardar_nombre():
    nombre = input("Ingrese su nombre: ")
    with open("nombres.txt", 'w') as archivo:
        archivo.write(nombre + '\n')
    print(f"Su nombre '{nombre}' ha sido guardado en 'nombres.txt'.")

# Ejemplo de como se usaria:
guardar_nombre()
