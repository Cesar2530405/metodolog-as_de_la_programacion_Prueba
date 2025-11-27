"""
Docstring for understanding_while_loop

Utilizamos el while loop para ejecutar un bloque de código mientras una condición sea verdadera.

Estructura basica del while loop en Python:

while condición:
    # Bloque de código a ejecutar

"""
# Ejemplo basico de while loop
# Vericar si un numero esta en un
# Rango especifico(10 y entre 20)

while True: # while loop infinito
   try:
       numero = int(input("Ingresa un número entre 10 y 20: "))
       if 10 <= numero <= 20:
            print("¡Número válido!")
            break  # Salir del bucle si el número es válido
       else:
            print("Número inválido, intenta de nuevo.")     
   except ValueError:
                print("Por favor, ingresa un número entero válido.")
   except KeyboardInterrupt:
                print("\nEntrada interrumpida. Saliendo del programa.")
                break  # Salir del bucle si se interrumpe la entrada             
print("Fin del programa.")
