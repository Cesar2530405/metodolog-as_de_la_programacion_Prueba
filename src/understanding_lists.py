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

El metodo append(elemento) toma un solo argumento, el elemento que se va a agregar a la lista.
"""
print ("\n Agregar elementos a una lista: Metodo append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""

Agregar elementos a una lista
- insert(): Agrega un elemento en una posicion especifica de la lista

El metodo insert(index, elemento) toma dos argumentos: el indice donde se va a insertar el elemento y el elemento que se va a agregar.
"""

print("\n Agregar elementos a una lista: Metodo insert() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)
print(motorcycles[0]) # Salida: ['ducati', 'honda', 'yamaha', 'suzuki']

"""
Eliminar elementos de una lista
- del: Elimina un elemento en una posicion especifica de la lista
La declaracion del indice de un elemento en una lista elimina ese elemento permanentemente.

"""
print("\n Eliminar elementos de una lista: Declaracion del \n")
motorcycles = ["honda", "yamaha", "suzuki"] 
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # Salida: ['honda', 'suzuki']

"""
Eliminar elemnentos de una lista
- pop(): Elimina el ultimo elemento de la lista y lo devuelve
El metodo pop() no requiere argumentos y elimina el ultimo elemento de la lista, devolviendolo para que pueda ser utilizado posteriormente.

"""
print("\n Eliminar elementos de una lista: Metodo pop() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) # Salida: ['honda', 'yamaha']
print(f"la motocicleta que fue eliminada es: {popped_motorcycle.title()}") # Salida: la motocicleta que fue eliminada es: Suzuki

"""
Elimiar elementos de una lista
- pop(index): Elimina y devuelve un elemento en una posicion especifica de la lista
El metodo pop(index) toma un argumento, el indice del elemento que se va a eliminar y lo devuelve para que pueda ser utilizado posteriormente.

"""

print("\n Eliminar elementos de una lista: Metodo pop(index) \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)
print(motorcycles) # Salida: ['yamaha', 'suzuki']
print(f"La primera motocicleta que fue eliminada es: {first_motorcycle.title()}") # Salida: La primera motocicleta que fue eliminada es: Honda

"""
Eliminar elementos de una lista
- remove(): Elimina la primera aparicion de un valor especifico de la lista
El metodo remove(valor) toma un argumento, que es el valor del elemento que se desea eliminar de la lista.
"""
print("\n Eliminar elementos de una lista: Metodo remove() \n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("ducati")
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']

# Ejemplo practico de remove()
names = ["carlos", "ana", "cesar", "maria", "ana"]
print(names) # Salida: ['carlos', 'ana', 'cesar', 'maria', 'ana']
deleted_name = input("ingresa el nombre que deseas eliminar: ")
names.remove(deleted_name.strip().lower())
print(names) # Salida depende del nombre ingresado


"""
Ordenar listas 

Metodo de las listas sort()

Ordenamiento permanente, es decir, ordena la lista permanentemente

"""

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars) # Salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # Salida: ['audi', 'bmw', 'subaru', 'toyota']


"""
Metodo reverse()    

"""

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.reverse()
print(motorcycles) # Salida: ['ducati', 'suzuki', 'yamaha', 'honda']    


"""
Cantidad de elementos en una lista
Metodo built-in len()

"""

cars = ["ford", "chevrolet", "toyota"]
print(cars) # Salida: ['ford', 'chevrolet', 'toyota']
print("\n Metodo built-in len() \n")
print(len(cars)) # Salida: 3

"""
Metodo built-in

sorted()    
Ordena una lista temporalmente

"""

favorite_students = ["jorge", "jose", "carlos", "emiliano"]
print(favorite_students) # Salida: ['jorge', 'jose', 'carlos', 'emiliano']

print("Lista ordenada temporalmnete : ", sorted(favorite_students)) # Salida: Lista ordenada temporalmente :  ['carlos', 'emiliano', 'jorge', 'jose']
print("Lista original: ", favorite_students) # Salida: Lista original:  ['jorge', 'jose', 'carlos', 'emiliano']
