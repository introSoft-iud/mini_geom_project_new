    
    
    
    # Mini Geom 📐

    Un paquete utilitario de Python simple para el cálculo de áreas y perímetros de figuras geométricas básicas.

    ## 🚀 Instalación

    Este paquete no está publicado en PyPI (por ahora), pero puede instalarlo localmente clonando el repositorio:

    ```bash
    git clone git@github.com:introSoft-iud/mini_geom_project_new.git
    cd mini_geom_project
    pip install .

    ```


    ## ✨ Uso

    Una vez instalado, importe las funciones directamente desde el paquete `mini_geom`:

    ```python
    from mini_geom import area_circulo, perimetro_rectangulo
    import math

    # Área del círculo: A = π * r²
    print(f"Área del círculo de radio 5: {area_circulo(5):.2f}") 
    # Salida: 78.54

    # Perímetro del rectángulo: P = 2 * (a + b)
    print(f"Perímetro del rectángulo (10x5): {perimetro_rectangulo(10, 5)}")
    # Salida: 30
    ```