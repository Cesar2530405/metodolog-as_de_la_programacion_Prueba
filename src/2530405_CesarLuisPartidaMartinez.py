
# PORTADA

# Nombre: Cesar Luis Partida Martinez
# Matrícula: 2530405
# Grupo: IM 1-2

# Programa: CRUD con funciones en Python




# RESUMEN EJECUTIVO

# Este programa implementa un CRUD (Create, Read, Update, Delete)
# usando un diccionario como estructura de datos en memoria.
# Cada operación está separada en funciones para mantener una
# responsabilidad clara y un código modular. El sistema permite
# crear, consultar, actualizar, eliminar y listar ítems.
# Las entradas son validadas para evitar datos incorrectos.
# El programa incluye un menú que permite al usuario ejecutar
# cada una de las operaciones del CRUD.


# PROBLEMA ÚNICO: CRUD EN MEMORIA CON FUNCIONES

# Problem: In-memory CRUD manager with functions

# Descripción:
# Programa que administra un conjunto de ítems en memoria mediante
# operaciones CRUD. Usamos un diccionario donde:
#   key   -> item_id
#   value -> dict con name, price y quantity.

# Elegí la opción A (diccionario) porque permite búsquedas rápidas
# por id y acceso directo a los datos.

# Inputs:
# - Opciones del menú (0–5)
# - Para CREATE/UPDATE: item_id, name, price, quantity
# - Para READ/DELETE: item_id

# Outputs:
# - Mensajes como: "Item created", "Item deleted", "Item not found"

# Validaciones:
# - item_id no vacío
# - price >= 0, quantity >= 0
# - option válida

# Test cases:
# 1) Normal:
#    create_item("A1", "Mouse", 150, 10)
#    read_item("A1")  -> Found
#    update_item("A1", "Mouse Pro", 199, 8)
#    delete_item("A1") -> Deleted

# 2) Border:
#    Crear con quantity = 0 (válido)

# 3) Error:
#    Crear con price = -5 → "Error: invalid input"
#    Leer id inexistente → "Item not found"


# CRUD FUNCTIONS


def create_item(data, item_id, name, price, quantity):
    """Create a new item if id does not already exist."""
    if item_id in data:
        return False  # ID already exists
    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data, item_id):
    """Return item dict if exists, otherwise None."""
    return data.get(item_id)


def update_item(data, item_id, new_name, new_price, new_quantity):
    """Update existing item."""
    if item_id not in data:
        return False
    data[item_id] = {
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    }
    return True


def delete_item(data, item_id):
    """Delete an item by id."""
    if item_id not in data:
        return False
    del data[item_id]
    return True


def list_items(data):
    """Return a list of all items."""
    return data



# MAIN MENU


def main():
    inventory = {}  # Diccionario principal

    while True:
        print("\n------ CRUD MENU ------")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")

        option = input("Option: ").strip()

        if option not in ["0", "1", "2", "3", "4", "5"]:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        # ----------------------
        # CREATE
        # ----------------------
        if option == "1":
            item_id = input("Item id: ").strip()
            name = input("Item name: ").strip()

            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
            except:
                print("Error: invalid input")
                continue

            if item_id == "" or price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if create_item(inventory, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: id already exists")

        # ----------------------
        # READ
        # ----------------------
        elif option == "2":
            item_id = input("Item id: ").strip()

            item = read_item(inventory, item_id)
            if item is None:
                print("Item not found")
            else:
                print("Item found:", item)

        # ----------------------
        # UPDATE
        # ----------------------
        elif option == "3":
            item_id = input("Item id: ").strip()

            if item_id not in inventory:
                print("Item not found")
                continue

            new_name = input("New name: ").strip()

            try:
                new_price = float(input("New price: "))
                new_quantity = int(input("New quantity: "))
            except:
                print("Error: invalid input")
                continue

            if new_price < 0 or new_quantity < 0:
                print("Error: invalid input")
                continue

            if update_item(inventory, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        # ----------------------
        # DELETE
        # ----------------------
        elif option == "4":
            item_id = input("Item id: ").strip()

            if delete_item(inventory, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # ----------------------
        # LIST ITEMS
        # ----------------------
        elif option == "5":
            items = list_items(inventory)
            print("Items list:")
            for k, v in items.items():
                print(f"{k} -> {v}")


# Ejecutar programa
if __name__ == "__main__":
    main()

# CONCLUSIONES

# El uso de funciones permitió separar cada operación del CRUD,
# logrando un programa más claro, organizado y reutilizable.
# El diccionario facilitó búsquedas rápidas por id y manejo simple
# de los datos. La validación fue clave para evitar entradas no
# válidas y mantener la estabilidad del programa. Este CRUD puede
# escalar fácilmente añadiendo almacenamiento en archivos o bases
# de datos.

# REFERENCIAS

# 1) Python Documentation – Data Structures (dict, list)
# 2) Python Documentation – Defining Functions
# 3) Tutoriales sobre CRUD básico en Python


# URL

# https://github.com/Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
# git@github.com:Cesar2530405/metodolog-as_de_la_programacion_Prueba.git