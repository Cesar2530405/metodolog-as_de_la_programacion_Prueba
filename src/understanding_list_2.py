# SLICING
players = ["cr7", "messi", "Travis", "chicha", "corona"]
print(players[0:3])
# Slice es trabajar con un grupo especifico
# de elementos de una lista
print(players[1:4]) # ["messi", "Travis", "chicha"]
print(players[:4]) # players = ["cr7", "messi", "Travis", "chicha"]
print(players[2:]) 

print(players[-3:])

print(players[-3:-1])
print(players[4:2]) # No se puede, me va a dar una lista vacia

# Slicing en for 
players = ["axel", "ignacio", "cr7", "messi", "Travis", "chicha", "corona"]
first_three_player = players [0:3]
print("First three player: ", first_three_player)

print("Aqui vienen los tres mejores del salon:")
for player in players[0:3]:
    print(player.upper())

    # Copia dde listas
    my_food =["pizza", "gorditas de jaumave", "machacado"]
    # copy_of_food = my_food # Manerra erronea de copiar una lista

    copy_of_food_1 = my_food[:]
    copy_of_food_2 = my_food.copy()
    copy_of_food_3 = list(my_food)

"Las listas son mutables eso siginifica que pueden ser modificados "
"tuplas: son listas inmutables, que no se pueden modificar"

# Modificando elementos 
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0]="bwm"
cars=[1]="porshe"
cars=[2]="mazda"
cars[3]="toyota"