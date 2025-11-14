cars = ["audi", "bmw" , "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# El condicional es el corazon de un if
# Condicional True
car = "bmw"
print(car == "bmw") # True

# Condicional False
car = "audi"
print(car == "Audi")

# Posible solucion a entradas del usuario 
car = "Audi"
print(car.lower() == "audi") # True


# Operador relacional != para determinar desigualdad
requested_topping = "mushroom"
if requested_topping != "anchovies":
    print("Hold the anchovies!")


# Comparaciones numericas
age = 18 # Entero
print(age == 18) # True

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 17
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False


# Multiples condiciones
age_0 = 22
age_1 = 18
# Operacion and 
print( age_0 >=21 and age_1 >=21 ) # False 
print( age_0 >=21 and age_1 >=18 ) # True
# Operacion or
print( age_0 >=21 or age_1 >=21 ) # True
print( age_0 >=23 or age_1 >=18 ) # False

"""
Para preguntarnos si un valor especifico esta presente en una lista, podemos 
utilizar el siguiente comparador:

    value in list
"""
motorcycles = [ "mortalika", "vento", "yamaha"]
moto_que_quiero = "Italika"
print("\n",moto_que_quiero in motorcycles) # False
print("vento" in motorcycles) # True

"""
Para preguntarnos si un valor especifico NO esta presente en una lista, podemos 
utilizar el siguiente comparador:

    value not in list

"""

banned_students = ["andres", "maria", "juan"]
student = "pedro"
print(student not in banned_students) # True
print("maria" not in banned_students) # False

# Variables del tipo booleano
game_active = True
can_edit = False

"""
    if statement

    sintaxis:


    if condicion:
        do something

    if condicion:
        do something
    else:   
        do something else

"""

age = input("Dime cual es tu edad: ")
age = int(age)
if age >= 18:
    print("Eres mayor de edad, puedes votar")
else:
    print("Eres menor de edad, no puedes votar")
