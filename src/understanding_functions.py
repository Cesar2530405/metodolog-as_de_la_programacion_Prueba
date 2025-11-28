"""
Functions 

Las funciones son bloques de codigo diseñados 
para realizar una tarea específica.

Cuando queremos realizar la tarea que se ha definido 
en una funcion, tenemos que llenar el nombre 
de la funcion responsable de esto 

Definicion de una funcion (Syntax)

def name_of_function(parameters):
    actions

"""
def greeting_cesar():
    print("Hola Cesar, que gusto verte")

for i in range(10): 
    greeting_cesar()

def greet(username,msj):
    print(f"Hola{username}, {msj}!!!")

# Argumentos
#greeting_cesar()
#greet("Jorge", "Se te pegaron las cobijas")

"""
Vamos a realizar un pograma que genere 
el nombre completo de3 una persona

Vamos a pasarle el primer nombre, el segundo 
y el apellido

La funion debe generar el nombre completo 
y regresarlo

"""
def create_full_name(first_name, middle_name, last_name):
    """
    Docstrings - This function creates the fullname
    of a person given its three names.
    
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.tittle()

user_first_name = input("Escribe tu primer nombre").strip().lower()
user_middle_name = input("Escribe tu segundo nombre").strip().lower()
user_last_name = input("Escribe tu apellido").strip().lower()

# Argumentos Posicionales - > Positional Arguments
print(create_full_name(
    user_first_name,
    user_middle_name, 
    user_last_name))

# Argumento Posicionales - > Positional Arguments
full_name = create_full_name(
    user_first_name, 
    user_middle_name,
    user_last_name)

print(full_name)

# Argumentos Clave ->  Keyword Arguments
full_name_key = create_full_name (
     last_name = user_last_name, 
    first_name = user_first_name,
   middle_name =  user_middle_name
)
   

print(full_name)

# Parametros Opcionales 
profe_falso = create_full_name(user_first_name, user_last_name)
print(profe_falso)

# Temas para estudiar a futuro
# Funciones: args, kwargs
# Manejo de datos: abrir archivos csv, .json, .yml, .txt
# argumentos por linea de comandos - sys
# cli - command line interface 
# generadores, iteradores, yield 
# Testing -> 