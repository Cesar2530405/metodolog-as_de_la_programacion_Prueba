# Numbers


"""
Integers - Enteros 

Son numeros sin punto decimal,
-infty , ..., -2, -1, 0, 1, 2, ... hasta infinito

Ejemplo:


#tipado dinamico 
age=33

las podemos sumar (+), restar (-), multiplicar (*) y dividir (/)

Potencias (**2, **3,)

Modulo (Dividiendo%Divisor)


"""

number_1 = 39
number_2 = 13

suma = number_1+number_2
difference = number_1-number_2
multiplication = number_1*number_2
division = number_1/number_2
modulo = number_1%number_2
power = number_1**2

print("suma: ",suma)
print("difference: ", difference)
print("multiplication: ", multiplication)
print("division:", division)
print("modulo:", modulo)
print("power:", power)

print("La suma es del tipo", type(suma))
print("La resta es del tipo", type(difference))
print("La multiplicacion es del tipo", type(multiplication))
print("La division es del tipo", type(division))
print("La modulo es del tipo", type(modulo))
print("La power es del tipo", type(power))     




# Floats 

"""
Floats - Reales

Son numeros con punto decimal, van desde -infty infty

Ejemplo:


# Tipado dinamico
age = 22,5

Las podemos sumar (+), restar (-), multiplicar(*) y dividir (/)


"""

print(0.1,+0,2)
# Numbers


"""
Integers - Enteros 

Son numeros sin punto decimal,
-infty , ..., -2, -1, 0, 1, 2, ... hasta infinito

Ejemplo:


#tipado dinamico 
age=33

las podemos sumar (+), restar (-), multiplicar (*) y dividir (/)

Potencias (**2, **3,)

Modulo (Dividiendo%Divisor)


"""

number_1 = 39
number_2 = 13

suma = number_1+number_2
difference = number_1-number_2
multiplication = number_1*number_2
division = number_1/number_2
modulo = number_1%number_2
power = number_1**2

print("suma: ",suma)
print("difference: ", difference)
print("multiplication: ", multiplication)
print("division:", division)
print("modulo:", modulo)
print("power:", power)

print("La suma es del tipo", type(suma))
print("La resta es del tipo", type(difference))
print("La multiplicacion es del tipo", type(multiplication))
print("La division es del tipo", type(division))
print("La modulo es del tipo", type(modulo))
print("La power es del tipo", type(power))     


# floats

"""
floats - reales 

son numeros con punto decimal van desde -infinity - infinity

ejemplo:

#tipado dinamico
age = 25.5

lo podemos sumar (+), restar (-), multiplicar() y dividir (/)


"""

print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

print(0.2+0.1)
print(3*0.1)











### Imprimir la edad de alguien 

age = 33
message = "Cesar tiene " + str (age) + "años"
print (message)

"""
TypeError: Python no puede reconocer el tipo de informacion que se esta utilizando.

Para convertir a string utilizo: str()

"""
message_f = f"Cesar tiene {age} años"
print(message_f)