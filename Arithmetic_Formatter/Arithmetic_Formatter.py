def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        #ENG: Check if the number of problems in the problems list is greater than 5.
        #SPA: Verifica si el número de problemas en la lista "problems" es mayor que 5.
        return 'Error: Too many problems.'

        # These lists will store the individual lines of each arithmetic problem.
        # Estas listas almacenarán las líneas individuales de cada problema aritmético.
    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

        #ENG: The parts variable will now hold three elements: the first number, the operator, and the second number.
        #SPA: La variable "parts" ahora contendrá tres elementos: el primer número, el operador y el segundo número.
    for problem in problems:
        parts = problem.split()

        # ENG: Check if the number of parts is not equal to 3.
        # SPA: Verifica si el numero de partes no es igual a 3.
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
                   #SPA: Formato del problema no soportado, es posible que falte un número o signo de operación

        num1, operator, num2 = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
                   #SPA: El operador debe ser '+' o '-'

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
                    #SPA:  Los numeros solo pueden contener dígitos

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
                    #SPA: Los numeros no pueden tener más de cuatro dígitos

        if operator == '+':
            answer = int(num1) + int(num2)
        else:
            answer = int(num1) - int(num2)

        #ENG: Calculate the maximum width needed to display the numbers and the answer.
        #ENG: It is the larger of the lengths of num1 and num2, plus 2
        #ENG: (one space for the operator and one space on the right).

        #SPA: Calcula el ancho máximo necesario para mostrar los números y la respuesta.
        #SPA: Es el mayor de los largos de num1 y num2, más 2
        #SPA: (un espacio para el operador y un espacio en el lado derecho).
        max_width = max(len(num1), len(num2)) + 2
        #ENG: The rjust() method is used to right-align the string by adding spaces
        #ENG: on the left to make it fit the maximum width.
        #SPA: El método rjust() se utiliza para alinear a la derecha la cadena agregando espacios
        #SPA: a la izquierda para que encaje en el ancho máximo.
        first_line.append(num1.rjust(max_width))
        second_line.append(f"{operator} {num2.rjust(max_width - 2)}")
        dash_line.append('-' * max_width)
        answer_line.append(str(answer).rjust(max_width))

        #ENG: Create a new list called arranged_problems and append the strings from first_line,
        #ENG: second_line, and dash_line, joining them together with four spaces in between using the join() method.
        #SPA: Crea una nueva lista llamada arranged_problems y agrega las cadenas de first_line, second_line y dash_line, 
        #SPA: unidas con cuatro espacios entre ellas utilizando el método join().
    arranged_problems = []
    arranged_problems.append("    ".join(first_line))
    arranged_problems.append("    ".join(second_line))
    arranged_problems.append("    ".join(dash_line))

    if show_answers:
        arranged_problems.append("    ".join(answer_line))

    return "\n".join(arranged_problems)


# Example of the usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
