"""
Vamos a realizar un programa que sume numeros 
hasta que el usuario escriba la palabra "salir"

El programa tambien debe decirme cuantos numeros 
ingreso el usuario, cual fue el minimo y cual fue el maximo

"""

sum_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:


    print("Ingresa la palabra salir para terminar ")
    user_input = input("Ingresa una cantidad (MXN)")

    # Centinel
    if user_input == "salir":
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print("Cantidad no valida, intenta de nuevo")
        continue
    except KeyboardInterrupt:
        break


    counter += 1 # counter = counter + 1 # Estructura contadora 
    sum_numbers += quantity # sum_numbers = sum_numbers + quantity

    if minimum is None or quantity < minimum:
        minimum = quantity
    
    if maximum is None or quantity > maximum:
        maximum = quantity
    
    print("SUM", sum_numbers)
    print("CONTADOR", counter)
    print("MINIMO", minimum)
    print("MAXIMO", maximum)