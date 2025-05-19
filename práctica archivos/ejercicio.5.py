#Crea una estructura como:
#proyecto/
#├── datos/
#├── scripts/
#└── resultados/

import os

def crear_estructura(nombre_proyecto):
    ruta_proyecto = os.path.join(os.getcwd(), nombre_proyecto)
    os.makedirs(os.path.join(ruta_proyecto, "datos"), exist_ok=True)
    os.makedirs(os.path.join(ruta_proyecto, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(ruta_proyecto, "resultados"), exist_ok=True)
    print(f"Estructura del proyecto '{nombre_proyecto}' creada.")

# Ejemplo de como se usaria:
crear_estructura("mi_proyecto")
