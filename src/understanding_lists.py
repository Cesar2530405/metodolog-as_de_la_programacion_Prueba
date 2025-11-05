# LISTAS
# Una lista es una coleccion ordenada y mutable de elementos.
# Se pueden crear listas utilizando corchetes [] y separando los elementos con comas 
fruits = ["manzana", "banana", "cereza"]
print (fruits) # Salida: ["manzana, banana", "cereza"]

# Acceso a elementos
print(fruits[0].upper()) # Salida: manzana 
print(fruits[1]) #Salida: banana
print(fruits[2].title()) # Salida: cereza

# print(fruits[3]) # IndexError: list index out of range

# Acceso al ultimo elemento
print(fruits[-1].capitalize()) # Salida: cereza  
print(fruits[-2]) # Salida: banana
print(fruits[-3]) # Salida: manzana

message = f"mi fruta favorita es {fruits[0].title()}."
print(message) # Salida: mi fruta favorita es Manzana.

"""
Agregar elementos a una lista
- append(): Agrega un elemento al final de la lista

"""
print ("\n Agregar elementos a una lista: Metodo append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""

Agregar elementos a una lista
- insert(): Agrega un elemento en una posicion especifica de la lista

"""

print("\n Agregar elementos a una lista: Metodo insert() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)
print(motorcycles[0]) # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']

