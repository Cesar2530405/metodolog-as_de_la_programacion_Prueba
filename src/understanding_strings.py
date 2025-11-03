"""
Un string es de manera sencilla una serie de caracteres.
En python todo lo que se encuentre dentro de comilas simples  
'' o dobles comillas "" es considerado un string.

" Esto es un string"

' Le dije a un amigo, " Python es mi lenguage favorito!"'
" El lenguage 'Python' lleva el nombre por Monty Python, no por la serpiente"


"""

name = " clase de programacion"
print(name)
print (name.title())
print(name)



"""
Un metodo es una accion que ohyton puede realizar en un fragmento de datos o sobre una variable.

El punto . despues de una variable seguida del metodo title() dice que se tiene que ejecutar el metodo title () de la variable name 

Todos los metodos van seguidos de parentesis porque en ocasiones necesitan informacion adicional para funcionar, lo cual iria dentro de los parentesis.
En esta ocasion el metodo .title() no requiere informacion adicional para ejecutarse.


"""


print(name.upper())
print(name.lower())



# Concatenacion de STRINGS
print("CONCATENACION DE STRINGS")
first_name = "cesar"
last_name = "martinez"
full_name = first_name +" "+ last_name
print (full_name)

print("Hola," + full_name.title() + "!") 


#  Whitespaces
"""
Whitespaces se refiere a cualquier caracter que no se imprime, es decir, un tabulador y finales de linea. Los whitespaces se utilizan comunmente para organizar las salidas (prints) de tal manera que sea mas amigable de leer o ver para los usuarios

"""

#Ejemplos
print("Python")
print("\tPython") # Tabulador
print("\t\tPython") # Tabulador 

# Ejemplo salto de linea
print("Languages: \n Python \n C \n Javascript")

print("Cesar")
print("Martinez")




#Sintax error con strings
error_sintaxis = "Una fortaleza de Python es su comunidad"
print(error_sintaxis + "Python"+ "Python")


# Concatenacion con f-strings
famous_person = "Cesar Martinez"
quote = "Python is love"

#Concatenacion convencional
message = famous_person +" una vez dijo "+ quote
print(message)

# Concatenacion con fstring
message_f_string = f"{famous_person} una vez dijo {quote}"
print (message_f_string)

# Actividad
"""
1) Elige un personaje famoso e igualalo a una variable del tipo string 
2) Elige una frase famosa que haya dicho e iguala a una variable de tipo string 
3) Genera un mensaje con las dos varibles utilizando f-string
4) Imprime el mensaje 




"""



# Eliminacion de espacios en blanco 
programming_languages = "Python"
print(programming_languages)
print(programming_languages.lstrip())
print(programming_languages.rstrip ())
print(programming_languages.strip())