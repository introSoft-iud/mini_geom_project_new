# Mini Geom

Un paquete de Python sencillo para calcular áreas y perímetros de figuras geométricas básicas.

## 📦 Qué incluye

- Cálculo de áreas (círculo, rectángulo, triángulo, etc.)  
- Cálculo de perímetros (rectángulo, triángulo, circunferencia, etc.)  
- Código limpio, documentado y fácil de usar  

## Instalación

> Este paquete **no está publicado** en PyPI (por ahora). Para usarlo, clona el repositorio e instálalo localmente:

```bash
git clone https://github.com/introSoft-iud/mini_geom_project_new.git
cd mini_geom_project_new
pip install .
```

También puedes instalar con SSH:
```bash
git clone git@github.com:introSoft-iud/mini_geom_project_new.git
cd mini_geom_project_new
pip install .
```
Uso

Una vez instalado, importa directamente desde el paquete mini_geom. Por ejemplo:
```bash
from mini_geom import area_circulo, perimetro_rectangulo
import math

# Área de un círculo de radio 5
print(f"Área del círculo de radio 5: {area_circulo(5):.2f}")
# → 78.54

# Perímetro de un rectángulo 10 × 5
print(f"Perímetro del rectángulo (10x5): {perimetro_rectangulo(10, 5)}")
# → 30
