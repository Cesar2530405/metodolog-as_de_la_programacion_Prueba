
# PORTADA
# Nombre: Cesar Luis Partida Martinez
# Matrícula: 2530405
# Grupo: IM 1-2

# RESUMEN EJECUTIVO

# La serie de Fibonacci es una sucesión numérica en la que cada número se obtiene
# sumando los dos anteriores, comenzando con 0 y 1. Calcular la serie hasta n términos
# significa generar los primeros n valores siguiendo esta regla. Este programa
# solicitará al usuario un número entero n, validará la entrada y luego generará
# la serie usando un bucle. Finalmente imprimirá los términos en una sola línea.

# PROBLEM: Fibonacci series generator

# Description:
# Programa que lee un entero n y genera los primeros n términos de la serie de
# Fibonacci iniciando en 0 y 1.

# Inputs:
# - n (int; number of terms to generate)

# Outputs:
# - "Fibonacci series:" seguido de los n términos separados por espacios

# Validations:
# - n must be an integer
# - n must be >= 1
# - Optional: n <= 50 (para evitar series demasiado largas)

# Test cases:
# 1) Normal case:
#       n = 7
#       Expected output: 0 1 1 2 3 5 8

# 2) Border case:
#       n = 1
#       Expected output: 0

# 3) Error case:
#       n = -4  → Expected: "Error: invalid input"
#       n = "abc" → Expected: "Error: invalid input"




user_input = input("Number of terms: ")

# Validate input
try:
    terms_count = int(user_input)
except ValueError:
    print("Error: invalid input")
    exit()

# Logical validations
if terms_count < 1 or terms_count > 50:
    print("Error: invalid input")
    exit()

# Special cases
if terms_count == 1:
    print("Fibonacci series: 0")
    exit()

# Start Fibonacci logic
first = 0
second = 1

print("Fibonacci series:", end=" ")
print(first, second, end=" ")

# Generate remaining terms
for _ in range(3, terms_count + 1):
    next_term = first + second
    print(next_term, end=" ")
    first = second
    second = next_term

print()  # newline at end



# CONCLUSIONES

# El uso de un bucle permitió generar la serie de Fibonacci de manera eficiente y
# repetitiva sin tener que escribir cada término manualmente. Los casos n = 1 y n = 2
# son importantes porque representan condiciones base de la serie y deben manejarse
# explícitamente para evitar errores. La lógica desarrollada en este programa puede
# reutilizarse fácilmente en algoritmos más complejos que requieran cálculos
# iterativos o secuencias numéricas.

# REFERENCIAS

# 1) Python documentation – “for” and “while” loops
# 2) Tutoriales oficiales de Python sobre funciones y estructuras de control
# 3) Material didáctico del curso de Programación Estructurada

# URL

# https://github.com/Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
# git@github.com:Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
