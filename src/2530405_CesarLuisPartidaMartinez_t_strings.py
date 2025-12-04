
#                   PORTADA 

# Nombre / Name: Cesar Luis Partida Martinez
# Matrícula / Student ID: 2530405
# Grupo / Group: IM 1-2


#                    RESUMEN EJECUTIVO 

# ES:
# Un string en Python es una secuencia de texto inmutable. Se pueden realizar
# operaciones como concatenación, extracción de subcadenas, búsqueda y reemplazo.
# La validación y normalización del texto es esencial para evitar errores.
# Este archivo contiene seis problemas que muestran el uso práctico de strings
# con validaciones, métodos de texto y ejemplos completos.
#

#             PRINCIPIOS Y BUENAS PRÁCTICAS 

# - Strings are immutable (cada cambio crea una nueva cadena).
# - Normalize input using strip() y lower() antes de comparar.
# - Avoid magic numbers en slicing; comentar cada operación.
# - Use built-in string methods en lugar de reescribir lógica básica.
# - Validar primero que no esté vacío, luego formato.
# - Nombres de variables claros; mensajes de error comprensibles.

#                    PROBLEM 1

# Problem 1: Full name formatter
# Description:
# EN: Given a full name, normalize spacing and capitalization, and display
#     the formatted name in Title Case plus its initials.
# ES: Dado un nombre completo, normalizar espacios, usar Title Case y mostrar iniciales.
#
# Inputs:
# - full_name (string)

# Outputs:
# - Formatted name
# - Initials

# Validations:
# - Not empty after strip()
# - Must contain at least two words

# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Border: "  MARÍA  LOPEZ  "
# 3) Error: "   "


def format_full_name(full_name):
    full_name = full_name.strip()
    if not full_name:
        print("Error: invalid input")
        return

    parts = full_name.split()
    if len(parts) < 2:
        print("Error: full name must contain at least two words")
        return

    formatted_name = " ".join(word.title() for word in parts)
    initials = ".".join(word[0].upper() for word in parts) + "."

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


#                       PROBLEM 2

# Problem 2: Simple email validator
# Description:
# EN: Validate that email contains exactly one '@', no spaces, and a domain.
# ES: Validar correo con un '@', sin espacios y dominio correcto.

# Inputs: email_text
# Outputs: valid or not valid, and domain

# Validations:
# - Not empty
# - No spaces
# - Exactly one '@'
# - Domain must contain '.'

# Test cases:
# 1) Normal: "user@example.com"
# 2) Border: "a@b.co"
# 3) Error: "invalid email"


def validate_email(email_text):
    email_text = email_text.strip()
    if not email_text:
        print("Valid email: false")
        return

    if " " in email_text:
        print("Valid email: false")
        return

    if email_text.count("@") != 1:
        print("Valid email: false")
        return

    at_index = email_text.find("@")
    domain = email_text[at_index + 1:]

    if "." not in domain:
        print("Valid email: false")
        return

    print("Valid email: true")
    print(f"Domain: {domain}")



#                       PROBLEM 3

# Problem 3: Palindrome checker
# Description:
# EN: Check if a phrase is a palindrome ignoring spaces and case.
# ES: Verificar si una frase es palíndromo ignorando espacios y mayúsculas.

# Inputs: phrase
# Outputs: true/false

# Validations:
# - Not empty
# - Minimum length (after cleaning) >= 3

# Test cases:
# 1) Normal: "Anita lava la tina"
# 2) Border: "A b A"
# 3) Error: "  "


def is_palindrome(phrase):
    phrase = phrase.strip()
    if not phrase:
        print("Error: invalid input")
        return

    cleaned = phrase.replace(" ", "").lower()
    if len(cleaned) < 3:
        print("Error: phrase too short")
        return

    is_p = cleaned == cleaned[::-1]
    print(f"Is palindrome: {str(is_p).lower()}")


#                       PROBLEM 4

# Problem 4: Sentence word stats
# Description:
# EN: Given a sentence, return word count, first word, last word,
#     shortest and longest word.
# ES: Obtener estadísticas sobre palabras en una oración.

# Inputs: sentence
# Outputs: stats

# Validations:
# - Not empty
# - At least one valid word

# Test cases:
# 1) Normal: "Python is very powerful"
# 2) Border: "   Hello   "
# 3) Error: ""

def sentence_stats(sentence):
    sentence = sentence.strip()
    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()
    if len(words) == 0:
        print("Error: invalid sentence")
        return

    shortest = min(words, key=len)
    longest = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest}")
    print(f"Longest word: {longest}")



#                       PROBLEM 5

# Problem 5: Password strength classifier
# Description:
# EN: Classify password as weak, medium, or strong.
# ES: Clasificar contraseña según reglas mínimas.

# Rules:
# - Weak: length < 8 OR only lowercase OR too simple
# - Medium: length >= 8 and mix of letters/digits
# - Strong: length >= 8 and contains upper, lower, digit, symbol
#
# Inputs: password_input
# Outputs: strength

# Test cases:
# 1) Normal: "Pass123!"
# 2) Border: "abcD1234"
# 3) Error: ""


def classify_password(password_input):
    password_input = password_input.strip()
    if not password_input:
        print("Error: invalid input")
        return

    has_upper = any(c.isupper() for c in password_input)
    has_lower = any(c.islower() for c in password_input)
    has_digit = any(c.isdigit() for c in password_input)
    has_symbol = any(not c.isalnum() for c in password_input)

    length = len(password_input)

    if length < 8:
        print("Password strength: weak")
        return

    if has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")



#                       PROBLEM 6

# Problem 6: Product label formatter
# Description:
# EN: Create a fixed-width (30 chars) product label with name and price.
# ES: Crear etiqueta de 30 caracteres con nombre y precio.

# Inputs: product_name, price_value
# Outputs: formatted label

# Validations:
# - product_name not empty
# - price_value must be numeric and positive

# Test cases:
# 1) Normal: ("Chocolate", 25)
# 2) Border: ("A", 1)
# 3) Error: ("   ", "abc")


def product_label(product_name, price_value):
    product_name = product_name.strip()
    if not product_name:
        print("Error: invalid product name")
        return

    # Validate price
    try:
        price = float(price_value)
        if price <= 0:
            raise ValueError
    except:
        print("Error: invalid price")
        return

    label = f"Product: {product_name} | Price: ${price}"
    if len(label) > 30:
        label = label[:30]
    else:
        label = label.ljust(30)

    print(f"Label: '{label}'")



#                       CONCLUSIONES

# ES:
# El manejo de strings es fundamental para validar datos, limpiar entrada
# y producir salidas formateadas. Normalizar texto evita errores y diferencias
# innecesarias. Los métodos strip(), split(), lower() y slicing facilitan
# muchas operaciones. La inmutabilidad de los strings ayuda a prevenir cambios
# inesperados. Diseñar validaciones sólidas evita datos basura y mejora la
# robustez del programa.



#                       REFERENCES

# 1) Python documentation: Text Sequence Type — str
# 2) Python Tutorial – Data types and operations
# 3) Real Python – String manipulation guide
# 4) Automate the Boring Stuff with Python – Strings chapter
# 5) W3Schools – Python strings

# URL 

# https://github.com/Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
# git@github.com:Cesar2530405/metodolog-as_de_la_programacion_Prueba.git