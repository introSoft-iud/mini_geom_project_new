# mini_geom/__init__.py

# Importamos las funciones desde el módulo interno (calculations.py)
from .calculations import (
    area_circulo, 
    perimetro_rectangulo, 
    area_triangulo
)

# Definimos la versión y la lista de elementos exportados
__version__ = "1.0.0"
__all__ = ["area_circulo", "perimetro_rectangulo", "area_triangulo"]