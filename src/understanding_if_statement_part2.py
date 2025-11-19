"""
    Vamos a realizar un programa que pregunte al usuario por su edad y muestre un mensaje  
    diferente segun el rango de edad en el que se encuentre:

"""

try: 

    age = int(input("Dime cual es tu edad: "))

    if age >= 18:
        print("Eres mayor de edad")

    elif age < 18:
        print("Eres menor de edad")
except:
    print("Tuviste un error al ingresar la edad")


print("Hola Cesar")



 

age = int(input("Dime cual es tu edad: "))

age = -1
print("Ingresaste un caracter no valido")

if age > 100:
        print("Tienes mas de un siglo de vida")

elif age >= 18 and age <= 100:
        print("Eres mayor de edad")
elif age < 18 and age >=0:
     print("Eres menor de edad")
elif age < 0:
     print("Tuviste un error ")


# Multiple elif
guisos= ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Si hay asado")
else:
    print("No hay asado")
if "tamales" in guisos:
    print("Si hay tamales")
else:
    print("No hay tamales")
if "salsa verde" in guisos:
    print("Si hay salsa verde")
else:
    print("No hay salsa verde")