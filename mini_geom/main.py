# ejemplo de como usarlo 

# main.py

# Importación limpia gracias al __init__.py:
from mini_geom import area_circulo, perimetro_rectangulo

# 1. Uso de las funciones:
radio_c = 4
area = area_circulo(radio_c)
print(f"Área del círculo de radio {radio_c}: {area:.2f}")

# 2. Reutilización simple:
lado1 = 10
lado2 = 5
perimetro = perimetro_rectangulo(lado1, lado2)
print(f"Perímetro del rectángulo ({lado1}x{lado2}): {perimetro}")
