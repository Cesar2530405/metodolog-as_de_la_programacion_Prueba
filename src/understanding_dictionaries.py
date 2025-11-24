# Simple dictionary
alien_0 = {'color': 'green', 'points': 5}

# The simpliest dictionary
alien_1 = {'color': 'yellow'}

# Accessing values in a dictionary
print(alien_1['color'])  # Output: green
print(alien_0['points'])  # Output: 5

# Empty dictionary
alien_2 = {}

# Modifying values in a dictionary
alien_2 = {'color': 'yellow'}
alien_2['color'] = 'blue'

# Adding new key-value pairs
alien_2["x_position"] = 0
alien_2["y_position"] = 25


# Dictionary to store similar objects
favorite_lenguages = {
    'cesar': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


# Looping through all key-value pairs in a dictionary
for key, value in favorite_lenguages.items():
    print (f"{key.title()}'s favorite language is {value.title()}.")

    #Lopping trhough all keys and values separately
for key in favorite_lenguages.keys():
    print(key.title())
  
  # Looping through all values in a dictionary
for value in favorite_lenguages.values():
    print(value.title())    

    # Nesting dictionaries

    ##Listas de diccionarios
    ## Listas en diccionarios
    ## Diccionarios en diccionarios