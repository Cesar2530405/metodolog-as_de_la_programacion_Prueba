magicians = ["ron", "harry","snape","hermione","draco"]
print(magicians[0]), magicians[1], magicians[2], magicians[3]

for magician in magicians:
    print(magician)
    print(magician.upper()) 
    print(f" {magician.title()}, ese fue un gran hechizo.")
    print("\n")


print("Gracias a todos. Fue un gran espectáculo!")

"""
Indentacion

Python utiliza la identacion pata determinar cuando una linea de codigo esta conectada a la linea de codigo anterior


Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir codigo ordenado y estructurado.

"""

# No olvidemos identar (donde se necesita)
# Ejemplo
magicians = ["alice", "david", "jorge"]
for magician in magicians:
    print(magician)
    #Print(magician) # Error
    print(magician) # Solucion



    # Identation Error 
    magicians = ["alice", "david", "jorge", "candelario"]
    for magician in magicians:
     print(magician) # Identation Error
print(f"Great {magician}, i can't wait to see your next trick.") # Solucion


# Identacion innecesaria 

message = "Hola Cesar"
print(message) # IndentationError: unexpected indent


# Logical error 
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians:
     print(magician) # Identation Error
print(f"Great {magician}, i can't wait to see your next trick.") # Solucion
print ("Thank you everyone, that was a great magic show!") # Logical error


# Error de sintaxis
magicians = ["alice", "david", "jorge", "candelario"]
for magician in magicians: # (Sintaxis Error): olvidar colocar los dos puntos (:) al final de la linea
     print(magician) 

