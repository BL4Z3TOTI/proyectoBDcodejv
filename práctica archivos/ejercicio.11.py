def calcular_costo_telegrama(mensaje):
    costo = 0
    for caracter in mensaje:
        if 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z':
            costo += 10
        elif caracter.isdigit():
            costo += 20
        elif caracter != ' ':
            costo += 30  # Consideramos las letras acentuadas y la ñ como caracteres especiales
    return costo

# Ejemplo de como se usaría:
mensaje1 = "Hola profe Carlos carden como estas?"
costo1 = calcular_costo_telegrama(mensaje1)
print(f"El costo del mensaje '{mensaje1}' es: ${costo1}")

mensaje2 = "El martes tengo parcial de Base de Datos."
costo2 = calcular_costo_telegrama(mensaje2)
print(f"El costo del mensaje '{mensaje2}' es: ${costo2}")

mensaje3 = "Aprobare ese parcial de Base de Datos!!"
costo3 = calcular_costo_telegrama(mensaje3)
print(f"El costo del mensaje '{mensaje3}' es: ${costo3}")