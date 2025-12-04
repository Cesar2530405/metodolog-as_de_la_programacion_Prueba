# Portada:
# Nombre: Cesar Luis Partida Martinez
# Matrícula: 2530405
# Grupo: IM 1-2

# Resumen ejecutivo:

# Este archivo contiene seis programas pequeños en Python que demuestran
# el uso de tres tipos de colecciones: listas, tuplas y diccionarios.
# - Lista: secuencia ordenada y mutable, útil cuando los elementos cambian.
# - Tupla: secuencia ordenada e inmutable, útil para registros fijos (p.ej., coordenadas).
# - Diccionario: mapeo clave->valor, ideal para búsquedas por clave.
# Se incluyen descripciones de cada problema, diseño de entradas/salidas,
# validaciones, tres casos de prueba (normal, borde, error) y un conductor
# de pruebas que ejecuta todos los casos. El código imprime mensajes en
# inglés conforme a las convenciones solicitadas.

# Principios y buenas prácticas 

# - Use listas cuando necesite agregar o eliminar elementos con frecuencia.
# - Use tuplas para datos que no deben cambiar (coordenadas, fechas).
# - Use diccionarios para búsquedas rápidas por clave (nombre, id).
# - Evite modificar una lista mientras la recorre con un for simple.
# - Use nombres descriptivos para claves en diccionarios ("name", "age").
# - Mantenga nombres de variables en lower_snake_case y constantes en UPPER_SNAKE.
# - Valide entradas antes de procesarlas y muestre mensajes claros al usuario.

# CONSTANTS

PASS_THRESHOLD = 70.0




# Problem 1: Shopping list basics
# Description: 2–4 líneas explicando qué hace el programa.

# Inputs:
# - initial_items_text (string; productos separados por comas)
# - new_item (string; producto a agregar)
# - search_item (string; producto a buscar)

# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false

# Validations:
# - initial_items_text no vacío tras strip() (si está vacío se inicia lista vacía)
# - new_item y search_item no vacíos tras strip()
# - Eliminar espacios extra alrededor de cada elemento tras split

# Test cases:
# 1) Normal: initial_items_text="apple, banana, orange", new_item="grape", search_item="banana"
# 2) Border: initial_items_text="   " -> se considera lista vacía y se acepta new_item
# 3) Error: new_item="" -> imprime "Error: invalid input"

def problem1_shopping_list(initial_items_text, new_item, search_item):
    """
    Returns a dict with keys: items_list, total_items, found_item (bool) or prints an error.
    All printed messages are in English as required.
    """
    # Input validation for initial text
    if initial_items_text is None:
        print("Error: invalid input")
        return None

    initial_text_stripped = str(initial_items_text).strip()
    # Decision: if initial text is empty, start with empty list
    if initial_text_stripped == "":
        items_list = []
    else:
        # Split by comma, strip each item and ignore empty fragments
        items_list = [item.strip() for item in initial_text_stripped.split(",") if item.strip() != ""]

    # Validate new_item and search_item
    if new_item is None or search_item is None:
        print("Error: invalid input")
        return None

    if str(new_item).strip() == "" or str(search_item).strip() == "":
        print("Error: invalid input")
        return None

    # Append new item (keeps code in English)
    items_list.append(str(new_item).strip())

    # Compute outputs
    len_list = len(items_list)
    found = str(search_item).strip() in items_list

    # Print outputs exactly as specified (booleans as lowercase true/false)
    print("Items list:", items_list)
    print("Total items:", len_list)
    print("Found item:", "true" if found else "false")

    return {"items_list": items_list, "total_items": len_list, "found_item": found}



# Problem 2: Points and distances with tuples
# Description: Usar tuplas para representar dos puntos 2D; calcular distancia y punto medio.

# Inputs:
# - x1, y1, x2, y2 (floats)

# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)

# Validations:
# - Verificar que las 4 entradas puedan convertirse a float

# Test cases:
# 1) Normal: (1.0,2.0),(4.0,6.0) -> distance 5.0, midpoint (2.5,4.0)
# 2) Border: mismos puntos (0,0),(0,0) -> distance 0.0
# 3) Error: entrada no numérica -> "Error: invalid input"

def problem2_points_distance(x1, y1, x2, y2):
    """
    Returns dict with point_a, point_b, distance, midpoint or prints an error.
    """
    try:
        fx1 = float(x1)
        fy1 = float(y1)
        fx2 = float(x2)
        fy2 = float(y2)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None

    point_a = (fx1, fy1)
    point_b = (fx2, fy2)

    distance = ((fx2 - fx1) ** 2 + (fy2 - fy1) ** 2) ** 0.5
    midpoint = ((fx1 + fx2) / 2.0, (fy1 + fy2) / 2.0)

    # Print with reasonable precision
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 6))
    print("Midpoint:", (round(midpoint[0], 6), round(midpoint[1], 6)))

    return {"point_a": point_a, "point_b": point_b, "distance": distance, "midpoint": midpoint}



# Problem 3: Product catalog with dictionary
# Description: Administrar un catálogo product->unit price; calcular total por cantidad.

# Inputs:
# - product_name (string)
# - quantity (int)

# Outputs:
# - Si existe:
#   - "Unit price:" <unit_price>
#   - "Quantity:" <quantity>
#   - "Total:" <total_price>
# - Si no existe:
#   - "Error: product not found"

# Validations:
# - product_name no vacío tras strip()
# - quantity convertible a int y > 0

# Test cases:
# 1) Normal: product_name="apple", quantity=2
# 2) Border: quantity=1
# 3) Error: product_name desconocido -> "Error: product not found"

def problem3_product_catalog(product_name, quantity, product_prices=None):
    """
    product_prices: optional dict; default catalog used if None.
    Returns dict with unit_price, quantity, total or prints error messages.
    """
    if product_prices is None:
        product_prices = {
            "apple": 10.0,
            "banana": 5.5,
            "orange": 8.25,
            "milk": 12.0
        }

    if product_name is None or str(product_name).strip() == "":
        print("Error: invalid input")
        return None

    name = str(product_name).strip()

    try:
        q = int(quantity)
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None

    if q <= 0:
        print("Error: invalid input")
        return None

    if name not in product_prices:
        print("Error: product not found")
        return None

    unit_price = float(product_prices[name])
    total_price = round(unit_price * q, 2)

    print("Unit price:", unit_price)
    print("Quantity:", q)
    print("Total:", total_price)

    return {"unit_price": unit_price, "quantity": q, "total": total_price}



# Problem 4: Student grades with dict and list
# Description: Diccionario student->list of grades; calcular promedio e indicar aprobado.

# Inputs:
# - student_name (string)

# Outputs:
# - Si existe:
#   - "Grades:" <grades_list>
#   - "Average:" <average>
#   - "Passed:" true|false
# - Si no existe:
#   - "Error: student not found"

# Validations:
# - student_name no vacío tras strip()
# - la lista de calificaciones no debe estar vacía

# Test cases:
# 1) Normal: estudiante con múltiples calificaciones
# 2) Border: estudiante con una sola calificación
# 3) Error: estudiante no existe

def problem4_student_grades(student_name, grades_dict=None):
    """
    grades_dict: optional dict; default provided if None.
    Returns dict with grades, average, passed or prints error messages.
    """
    if grades_dict is None:
        grades_dict = {
            "Alice": [90.0, 85.5, 78.0],
            "Bob": [60.0, 70.0, 65.5],
            "Charlie": [100.0]
        }

    if student_name is None or str(student_name).strip() == "":
        print("Error: invalid input")
        return None

    name = str(student_name).strip()

    if name not in grades_dict:
        print("Error: student not found")
        return None

    grades_list = grades_dict[name]

    if not isinstance(grades_list, list) or len(grades_list) == 0:
        print("Error: invalid input")
        return None

    try:
        grades_floats = [float(g) for g in grades_list]
    except (TypeError, ValueError):
        print("Error: invalid input")
        return None

    average = sum(grades_floats) / len(grades_floats)
    is_passed = average >= PASS_THRESHOLD

    print("Grades:", grades_floats)
    print("Average:", round(average, 2))
    print("Passed:", "true" if is_passed else "false")

    return {"grades": grades_floats, "average": average, "passed": is_passed}



# Problem 5: Word frequency counter (list + dict)
# Description: Contar frecuencia de palabras en una oración; mostrar lista, diccionario y palabra más frecuente.

# Inputs:
# - sentence (string)

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>

# Validations:
# - sentence no vacío tras strip()
# - se elimina puntuación simple: . , ! ? ; : ( ) " '

# Test cases:
# 1) Normal: "Hello world hello!" -> hello:2, world:1
# 2) Border: solo puntuación/espacios -> error
# 3) Error: cadena vacía -> "Error: invalid input"

def problem5_word_frequency(sentence):
    """
    Returns dict with words_list, freq_dict, most_common_word or prints error.
    Simple punctuation removal is applied.
    """
    if sentence is None or str(sentence).strip() == "":
        print("Error: invalid input")
        return None

    text = str(sentence).strip().lower()

    # Remove basic punctuation
    for ch in [".", ",", "!", "?", ";", ":", "(", ")", "\"", "'"]:
        text = text.replace(ch, "")

    words = [w for w in text.split() if w != ""]

    if len(words) == 0:
        print("Error: invalid input")
        return None

    freq_dict = {}
    for w in words:
        if w in freq_dict:
            freq_dict[w] += 1
        else:
            freq_dict[w] = 1

    # Find most common word (any one if tie)
    most_common_word = None
    highest = -1
    for w, count in freq_dict.items():
        if count > highest:
            highest = count
            most_common_word = w

    print("Words list:", words)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)

    return {"words_list": words, "frequencies": freq_dict, "most_common_word": most_common_word}



# Problem 6: Simple contact book (dictionary CRUD)
# Description: Implementar acciones ADD/SEARCH/DELETE sobre un diccionario contacts.

# Inputs:
# - action_text (string; "ADD","SEARCH","DELETE")
# - name (string)
# - phone (string; solo para "ADD")

# Outputs:
# - ADD: "Contact saved:" name, phone
# - SEARCH: "Phone:" <phone> o "Error: contact not found"
# - DELETE: "Contact deleted:" name o "Error: contact not found"

# Validations:
# - Normalizar action_text a mayúsculas y validar las opciones
# - name no vacío tras strip()
# - Para ADD: phone no vacío tras strip()

# Test cases:
# 1) Normal: ADD -> SEARCH -> DELETE sobre contacto existente
# 2) Border: ADD con mismo nombre (actualiza teléfono)
# 3) Error: SEARCH/DELETE para contacto inexistente

def problem6_contact_book(action_text, name=None, phone=None, contacts=None):
    """
    contacts: optional dict to operate on; default contacts used if None.
    Returns updated contacts dict or phone string for SEARCH, or prints error messages.
    """
    if contacts is None:
        contacts = {
            "Alice": "1234567890",
            "Bob": "5550001234"
        }

    if action_text is None:
        print("Error: invalid input")
        return contacts

    action = str(action_text).strip().upper()

    if action not in {"ADD", "SEARCH", "DELETE"}:
        print("Error: invalid input")
        return contacts

    if name is None or str(name).strip() == "":
        print("Error: invalid input")
        return contacts

    name_key = str(name).strip()

    if action == "ADD":
        if phone is None or str(phone).strip() == "":
            print("Error: invalid input")
            return contacts
        phone_value = str(phone).strip()
        contacts[name_key] = phone_value  # add or update
        print("Contact saved:", name_key, phone_value)
        return contacts

    elif action == "SEARCH":
        if name_key in contacts:
            print("Phone:", contacts[name_key])
            return contacts[name_key]
        else:
            print("Error: contact not found")
            return None

    elif action == "DELETE":
        if name_key in contacts:
            contacts.pop(name_key)
            print("Contact deleted:", name_key)
            return contacts
        else:
            print("Error: contact not found")
            return None



# Test driver: ejecutar los 3 casos por problema (normal, borde, error)

def run_all_tests():
    print("\n" + "=" * 60)
    print("Problem 1 Tests (Shopping list basics)")
    print("-" * 60)
    # Normal
    print("\nTest 1 - Normal:")
    problem1_shopping_list("apple, banana, orange", "grape", "banana")
    # Border (initial empty)
    print("\nTest 2 - Border (empty initial):")
    problem1_shopping_list("   ", "apple", "apple")
    # Error (invalid new_item)
    print("\nTest 3 - Error (empty new_item):")
    problem1_shopping_list("apple,orange", "", "apple")

    print("\n" + "=" * 60)
    print("Problem 2 Tests (Points and distances with tuples)")
    print("-" * 60)
    # Normal
    print("\nTest 1 - Normal:")
    problem2_points_distance(1.0, 2.0, 4.0, 6.0)
    # Border (same point)
    print("\nTest 2 - Border (same point):")
    problem2_points_distance(0, 0, 0, 0)
    # Error (non-numeric)
    print("\nTest 3 - Error (non-numeric):")
    problem2_points_distance("a", 0, 1, 2)

    print("\n" + "=" * 60)
    print("Problem 3 Tests (Product catalog with dictionary)")
    print("-" * 60)
    # Normal
    print("\nTest 1 - Normal:")
    problem3_product_catalog("apple", 2)
    # Border (quantity 1)
    print("\nTest 2 - Border (quantity 1):")
    problem3_product_catalog("banana", 1)
    # Error (product not found)
    print("\nTest 3 - Error (unknown product):")
    problem3_product_catalog("chocolate", 3)

    print("\n" + "=" * 60)
    print("Problem 4 Tests (Student grades with dict and list)")
    print("-" * 60)
    # Normal
    print("\nTest 1 - Normal (Alice):")
    problem4_student_grades("Alice")
    # Border (single grade)
    print("\nTest 2 - Border (Charlie):")
    problem4_student_grades("Charlie")
    # Error (student not found)
    print("\nTest 3 - Error (unknown student):")
    problem4_student_grades("Dave")

    print("\n" + "=" * 60)
    print("Problem 5 Tests (Word frequency counter)")
    print("-" * 60)
    # Normal
    print("\nTest 1 - Normal:")
    problem5_word_frequency("Hello world hello!")
    # Border (only punctuation/spaces)
    print("\nTest 2 - Border (punctuation only):")
    problem5_word_frequency("   . , !   ")
    # Error (empty)
    print("\nTest 3 - Error (empty string):")
    problem5_word_frequency("")

    print("\n" + "=" * 60)
    print("Problem 6 Tests (Simple contact book CRUD)")
    print("-" * 60)
    # Prepare a contacts dict to persist across calls for testing
    test_contacts = {"Alice": "1234567890", "Bob": "5550001234"}

    # Normal: ADD
    print("\nTest 1 - Normal: ADD")
    test_contacts = problem6_contact_book("ADD", "Carlos", "9988776655", contacts=test_contacts) or test_contacts
    # SEARCH
    print("\nTest 1b - SEARCH:")
    problem6_contact_book("SEARCH", "Carlos", contacts=test_contacts)
    # DELETE
    print("\nTest 1c - DELETE:")
    test_contacts = problem6_contact_book("DELETE", "Carlos", contacts=test_contacts) or test_contacts

    # Border: ADD updating same name
    print("\nTest 2 - Border: ADD same name (update phone)")
    test_contacts = problem6_contact_book("ADD", "Alice", "0001112222", contacts=test_contacts) or test_contacts
    problem6_contact_book("SEARCH", "Alice", contacts=test_contacts)

    # Error: SEARCH missing
    print("\nTest 3 - Error: SEARCH missing")
    problem6_contact_book("SEARCH", "Nonexistent", contacts=test_contacts)
    # Error: DELETE missing
    print("\nTest 3b - Error: DELETE missing")
    problem6_contact_book("DELETE", "Nonexistent", contacts=test_contacts)

    print("\n" + "=" * 60)
    print("All tests completed.")
    print("=" * 60 + "\n")


# Ejecutar pruebas sólo si el archivo se ejecuta como script principal
if __name__ == "__main__":
    run_all_tests()


# Conclusiones 

# Las listas convienen cuando se requiere flexibilidad para agregar y eliminar
# elementos con frecuencia; permiten operaciones como append, pop e insert.
# Las tuplas son útiles para datos inmutables (coordenadas, registros fijos),
# ya que su inmutabilidad evita modificaciones accidentales.
# Los diccionarios facilitan búsquedas rápidas por clave y son ideales para
# catálogos, agendas y estructuras tipo "dictionary of lists" (p.ej., student->grades).
# Al combinar estas estructuras se pueden modelar registros complejos con búsquedas
# eficientes y colecciones internas flexibles.

# Referencias 

# References:
# 1) Python documentation - Built-in Types: list, tuple, dict
#    https://docs.python.org/3/library/stdtypes.html
# 2) The Python Tutorial — Data Structures (official tutorial)
#    https://docs.python.org/3/tutorial/datastructures.html
# 3) Real Python - articles on lists and dictionaries (realpython.com)
# 4) W. Grosso, "Core Python Programming" - chapters on lists/dicts/tuples
# 5) Online resources and classroom notes about Python collections and best practices


# URL

# https://github.com/Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
# git@github.com:Cesar2530405/metodolog-as_de_la_programacion_Prueba.git