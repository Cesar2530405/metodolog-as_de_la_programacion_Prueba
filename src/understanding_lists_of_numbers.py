"""
Las listas tambien pueden almacenar numeros y de echo son ideales para almacenarlos.
Python ofrece cantidad de funciones integradas para trabajar con listas de numeros.

Por ejemplo, funcion range():

"""

# La funcion range() genera una lista de numeros 
# En un rango especificado
# Por ejemplo, para generar una lista de numeros del 0 al 9
numbers = list(range(10))
print(numbers) # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) # Salida : <class 'list'>

# Podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)
    print(type(num)) # Salida: <class 'int'> (10 veces)


print("\nNumeros del 1 al 4:")
for num in range(1, 5):
    print(num)  # Salida: 1, 2, 3, 4
numbers_1_to_4 = list(range(1, 5))
print(numbers_1_to_4) # Salida: [1, 2, 3, 4]


print("\nNumeros impares:")    
for num in range(1, 10, 2): # Numweoas impares del 1 al 9
    print(num)  # Salida: 1, 3, 5, 7, 9
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # Salida: [1, 3, 5, 7, 9]


print("\nNumeros pares:")
for num in range(2, 10, 2): # Numeros pares del 2 al 8
    print(num)  # Salida: 2, 4, 6, 8, 10
even_numbers = list(range(2, 10, 2))
print(even_numbers) # Salida: [2, 4, 6, 8]


## Podemos crear caulquier lista de numeros 
## Utilizando la funcion range() y la funcion list()
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares) # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Metodos built-in para listas de numeros
print("\n Metodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Lista de digitos:", digits)
print("Minimo:", min(digits)) # Salida: Minimo: 0
print("Maximo:", max(digits)) # Salida: Maximo: 9
print("Suma:", sum(digits))   # Salida: Suma: 45