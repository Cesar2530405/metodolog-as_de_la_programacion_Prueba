
# Portada 
# Nombre / Name: Cesar Luis Partida Martinez
# Matrícula / Student ID: 2530405
# Grupo / Group: IM 1-2

# Resumen ejecutivo / Executive summary:
# EN: This file contains 6 problems using numeric types (int, float)
# and booleans (True/False). It demonstrates arithmetic operations,
# comparisons, logical operations, type conversion, rounding and input
# validation. Each problem includes description, inputs, outputs,
# validations and three test cases (normal, border, error).
# ES: Este archivo contiene 6 problemas que usan tipos numéricos y
# booleanos. Se muestran operaciones aritméticas, comparaciones,
# conversiones de tipo, redondeo y validaciones de entrada.

# Principles / Principios (short):
# - Use int for discrete counts and float for continuous quantities.
# - Validate inputs before processing (e.g., non-negative, non-zero).
# - Avoid division by zero by checking denominators.
# - Use descriptive variable names in lower_snake_case.
# - Document what True/False means in each context.

# Problem 1: Temperature converter and range flag
# Description:
# EN: Convert Celsius (float) to Fahrenheit and Kelvin. Produce a boolean
#     is_high_temperature true if temp_c >= 30.0.
# ES: Convierte Celsius a Fahrenheit y Kelvin. is_high_temperature true si >=30.0.

# Inputs:
#  - temp_c (float)
# Outputs:
#  - "Fahrenheit: <value>"
#  - "Kelvin: <value>"
#  - "High temperature: true|false"
# Validations:
#  - temp_c convertible to float
#  - Kelvin must be >= 0.0 (physical constraint)
# Test cases:
#  1) Normal: 25.0
#  2) Border: 30.0
#  3) Error: -300.0 (Kelvin < 0) 

def problem1_temperature_converter(temp_c_input):
    try:
        temp_c = float(str(temp_c_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    temp_f = temp_c * 9.0 / 5.0 + 32.0
    temp_k = temp_c + 273.15

    # Validate physical Kelvin
    if temp_k < 0.0:
        print("Error: invalid input")
        return None

    is_high_temperature = temp_c >= 30.0

    # Print outputs with sensible formatting
    # Fahrenheit rounded to 2 decimals, Kelvin to 2 decimals
    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {'true' if is_high_temperature else 'false'}")

    return {"fahrenheit": temp_f, "kelvin": temp_k, "is_high_temperature": is_high_temperature}



# Problem 2: Work hours and overtime payment
# Description:
# EN: Calculate weekly pay. Up to 40 hours at hourly_rate. Overtime (>40)
#     paid at 150% of hourly_rate. Produce has_overtime boolean.
# ES: Calcular pago semanal con horas extra al 150%.

# Inputs:
#  - hours_worked (float)
#  - hourly_rate (float)
# Outputs:
#  - "Regular pay: <value>"
#  - "Overtime pay: <value>"
#  - "Total pay: <value>"
#  - "Has overtime: true|false"
# Validations:
#  - hours_worked >= 0
#  - hourly_rate > 0
# Test cases:
#  1) Normal: 38.0, 80.0
#  2) Border: 40.0, 50.0
#  3) Error: -5, 10  (negative hours)

def problem2_weekly_pay(hours_worked_input, hourly_rate_input):
    try:
        hours_worked = float(str(hours_worked_input).strip())
        hourly_rate = float(str(hourly_rate_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return None

    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(0.0, hours_worked - 40.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = overtime_hours > 0.0

    # Print with 2 decimals
    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {'true' if has_overtime else 'false'}")

    return {
        "regular_pay": regular_pay,
        "overtime_pay": overtime_pay,
        "total_pay": total_pay,
        "has_overtime": has_overtime,
    }



# Problem 3: Discount eligibility with booleans
# Description:
# EN: Customer eligible for discount if is_student OR is_senior OR purchase_total >= 1000.0.
#     If eligible, apply 10% discount.
# ES: Elegible si estudiante, senior o compra >= 1000. Aplicar 10% si aplica.

# Inputs:
#  - purchase_total (float)
#  - is_student_text ("YES" or "NO", case-insensitive)
#  - is_senior_text ("YES" or "NO", case-insensitive)
# Outputs:
#  - "Discount eligible: true|false"
#  - "Final total: <value>"
# Validations:
#  - purchase_total >= 0.0
#  - Text inputs must be YES or NO
# Test cases:
#  1) Normal: 1200.0, "NO", "NO" -> eligible (by total)
#  2) Border: 1000.0, "NO", "NO" -> eligible (>=1000)
#  3) Error: 200.0, "MAYBE", "NO" -> invalid input

def problem3_discount_eligibility(purchase_total_input, is_student_text, is_senior_text):
    # Validate purchase_total
    try:
        purchase_total = float(str(purchase_total_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    if purchase_total < 0.0:
        print("Error: invalid input")
        return None

    # Normalize YES/NO inputs (strip and uppercase)
    if not isinstance(is_student_text, str) or not isinstance(is_senior_text, str):
        print("Error: invalid input")
        return None

    is_student_norm = is_student_text.strip().upper()
    is_senior_norm = is_senior_text.strip().upper()

    if is_student_norm not in ("YES", "NO") or is_senior_norm not in ("YES", "NO"):
        print("Error: invalid input")
        return None

    is_student = is_student_norm == "YES"
    is_senior = is_senior_norm == "YES"

    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    if discount_eligible:
        final_total = round(purchase_total * 0.9, 2)
    else:
        final_total = round(purchase_total, 2)

    print(f"Discount eligible: {'true' if discount_eligible else 'false'}")
    print(f"Final total: {final_total}")

    return {"discount_eligible": discount_eligible, "final_total": final_total}


# Problem 4: Basic statistics of three integers
# Description:
# EN: Read three integers and compute sum, average (float), max, min and
#     all_even boolean indicating if all three are even.
# ES: Leer tres enteros y calcular suma, promedio, máximo, mínimo y all_even.
#
# Inputs:
#  - n1, n2, n3 (int)
# Outputs:
#  - "Sum:", "Average:", "Max:", "Min:", "All even: true|false"
# Validations:
#  - Inputs convertible to int
# Test cases:
#  1) Normal: 10, 20, 30  -> all_even true
#  2) Border: 0, 1, 2
#  3) Error: "abc", 3, 4

def problem4_three_int_stats(n1_input, n2_input, n3_input):
    try:
        n1 = int(str(n1_input).strip())
        n2 = int(str(n2_input).strip())
        n3 = int(str(n3_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0  # float
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    # Print results, average rounded to 2 decimals
    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {'true' if all_even else 'false'}")

    return {
        "sum": sum_value,
        "average": average_value,
        "max": max_value,
        "min": min_value,
        "all_even": all_even,
    }


# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# EN: Determine loan eligibility given monthly_income, monthly_debt, credit_score.
#     debt_ratio = monthly_debt / monthly_income.
#     Eligible if monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650.
# ES: Elegibilidad de préstamo usando ratio de deuda y puntaje.

# Inputs:
#  - monthly_income (float)
#  - monthly_debt (float)
#  - credit_score (int)
# Outputs:
#  - "Debt ratio:" <value>
#  - "Eligible: true|false"
# Validations:
#  - monthly_income > 0.0
#  - monthly_debt >= 0.0
#  - credit_score >= 0
# Test cases:
#  1) Normal: income=9000, debt=2000, score=700 -> eligible true
#  2) Border: income=8000, debt=3200, score=650 -> debt_ratio=0.4 -> eligible true
#  3) Error: income=0 -> invalid input (division by zero)

def problem5_loan_eligibility(monthly_income_input, monthly_debt_input, credit_score_input):
    # Convert and validate numeric inputs
    try:
        monthly_income = float(str(monthly_income_input).strip())
        monthly_debt = float(str(monthly_debt_input).strip())
        credit_score = int(str(credit_score_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return None

    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {'true' if eligible else 'false'}")

    return {"debt_ratio": debt_ratio, "eligible": eligible}



# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# EN: Compute BMI = weight_kg / (height_m * height_m). Provide booleans:
#     is_underweight, is_normal, is_overweight.
# ES: Calcular IMC y banderas según rangos.

# Inputs:
#  - weight_kg (float)
#  - height_m (float)
# Outputs:
#  - "BMI:" rounded to 2 decimals
#  - "Underweight: true|false"
#  - "Normal: true|false"
#  - "Overweight: true|false"
# Validations:
#  - weight_kg > 0.0
#  - height_m > 0.0
# Test cases:
#  1) Normal: 70, 1.75
#  2) Border: 50, 1.65
#  3) Error: -10, 1.7  (invalid weight)

def problem6_bmi_category(weight_kg_input, height_m_input):
    try:
        weight_kg = float(str(weight_kg_input).strip())
        height_m = float(str(height_m_input).strip())
    except Exception:
        print("Error: invalid input")
        return None

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return None

    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)

    is_underweight = bmi < 18.5
    is_normal = (bmi >= 18.5) and (bmi < 25.0)
    is_overweight = bmi >= 25.0

    print(f"BMI: {bmi_rounded}")
    print(f"Underweight: {'true' if is_underweight else 'false'}")
    print(f"Normal: {'true' if is_normal else 'false'}")
    print(f"Overweight: {'true' if is_overweight else 'false'}")

    return {
        "bmi": bmi,
        "is_underweight": is_underweight,
        "is_normal": is_normal,
        "is_overweight": is_overweight,
    }



# Test runner: executes 3 cases (normal, border, error) for each problem

def run_all_tests():
    print("\n--- Problem 1 Tests ---")
    # Problem 1: normal, border, error
    problem1_temperature_converter(25.0)      # normal
    problem1_temperature_converter(30.0)      # border
    problem1_temperature_converter(-300.0)    # error (Kelvin negative)

    print("\n--- Problem 2 Tests ---")
    problem2_weekly_pay(38.0, 80.0)           # normal
    problem2_weekly_pay(40.0, 50.0)           # border
    problem2_weekly_pay(-5, 10.0)             # error (negative hours)

    print("\n--- Problem 3 Tests ---")
    problem3_discount_eligibility(1200.0, "NO", "NO")  # normal (total >=1000)
    problem3_discount_eligibility(1000.0, "NO", "NO")  # border (exact 1000)
    problem3_discount_eligibility(200.0, "MAYBE", "NO")# error (invalid YES/NO)

    print("\n--- Problem 4 Tests ---")
    problem4_three_int_stats(10, 20, 30)       # normal (all even)
    problem4_three_int_stats(0, 1, 2)          # border
    problem4_three_int_stats("abc", 3, 4)      # error (invalid int)

    print("\n--- Problem 5 Tests ---")
    problem5_loan_eligibility(9000.0, 2000.0, 700)  # normal (eligible)
    problem5_loan_eligibility(8000.0, 3200.0, 650)  # border (debt_ratio=0.4)
    problem5_loan_eligibility(0.0, 100.0, 600)      # error (income zero)

    print("\n--- Problem 6 Tests ---")
    problem6_bmi_category(70.0, 1.75)       # normal
    problem6_bmi_category(50.0, 1.65)       # border
    problem6_bmi_category(-10.0, 1.7)       # error (invalid weight)


if __name__ == "__main__":
    run_all_tests()



# Conclusions / Conclusiones 

# EN:
# Integers and floats complement each other when modeling real-world quantities:
# ints for counts, floats for continuous measures. Comparisons produce booleans
# that enable program decisions (if statements). Validating ranges and checking
# denominators prevents runtime errors like division by zero. Using logical
# operators (and, or, not) we can combine conditions to express complex rules.
# Practicing these patterns is essential for payroll, discount, loan and BMI tasks.
#
# ES:
# Los enteros y flotantes se usan juntos para modelar cantidades reales: ints
# para conteos y floats para medidas decimales. Las comparaciones generan
# booleanos que permiten tomar decisiones. Validar rangos y evitar divisiones
# por cero previene errores. Los operadores lógicos permiten combinar condiciones
# y diseñar reglas reales (nómina, descuentos, préstamos, IMC).

# References / Referencias 

# 1) Python documentation - Numeric types: int, float
# 2) Python documentation - Boolean type: bool
# 3) Python docs - Built-in functions (round, max, min)
# 4) Tutorials on operators and type conversion (int(), float())
# 5) Course notes on validation and defensive programming

# URL

# https://github.com/Cesar2530405/metodolog-as_de_la_programacion_Prueba.git
# git@github.com:Cesar2530405/metodolog-as_de_la_programacion_Prueba.git