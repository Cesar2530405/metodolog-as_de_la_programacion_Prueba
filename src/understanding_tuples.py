"""
    Las tuplas son listas de elementos que no se pueden modificar
    Las tuplas se definen con parentesis ()


    Ejemplo:
"""

# Rectangulo (largo, ancho)
rectangle_dimensions = (200, 50) # Tupla
print(rectangle_dimensions)
print(f"El largo del rectangulo es: {rectangle_dimensions[0]} mm") # 200
print(f"El ancho del rectangulo es: {rectangle_dimensions[1]} mm") # 50


# Vamos a intentar modificar una tupla
# rectangle_dimensions[0] = 250 # Esto va a generar un error
# rectangle_dimensions[1] = 100 # Esto va a generar un error

for dimension in rectangle_dimensions:
    print(dimension)


""""
    No podemos eliminar una tupla, ni tampoco agregar/ eliminar elementos. lo qie si podemos
    hacer es cambiar la asignacion a una variable que almacena una tupla.

"""
rectangle_dimensions = (300, 150) # Nueva tupla

