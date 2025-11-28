"""
Vamos a realizar un programa que defina un  PIN como contraseña 

Despues vamos a darle 3 intentos al usuario    
para escribir el pin.

Si el ususario escribe correctamente el pin, el programa debe 
mostrar un mensaje de Acceso Permitido

Si el usuario se equivoca, el programa debe decirle cuatos intentos le quedan 
y en caso de que no le queden intentos el mensaje debe decir Acceso Denegado,
excediste tus intentos

"""

CORRECT_PIN = "1234"
attempts = 3
intents = 0

while intents < attempts:
    user_pin = input("Ingresa tu PIN: ")
    
    if user_pin == CORRECT_PIN:
        print("¡Acceso Permitido!")
        break
    else:
        intents += 1
        remaining_attempts = attempts - intents
        if remaining_attempts > 0:
            print(f"PIN incorrecto. Te quedan {remaining_attempts} intentos.")
        else:
            print("Acceso Denegado, excediste tus intentos.")