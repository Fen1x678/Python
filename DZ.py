def display(result, operation=None):
    """Вывод на "дисплей" калькулятора."""
    if operation:
        print(f"  {result} {operation} ", end="")
    else:
       print(f"  {result}")

def get_input():
    """Получение ввода от пользователя."""
    return input("> ")

def calculate(result, operand, operation):
    """Выполнение вычислений."""
    if operation == "+":
        return result + operand
    elif operation == "-":
        return result - operand
    elif operation == "*":
        return result * operand
    elif operation == "/":
        if operand == 0:
            print("Ошибка: Деление на ноль!")
            return result
        return result / operand
    return result

def main():
    """Основная логика калькулятора."""
    result = 0
    operation = None
    display(result)

    while True:
        input_str = get_input().strip()

        if input_str == 'c' or input_str == 'C':
           result = 0
           operation = None
           display(result)
           continue

        if input_str in ['+', '-', '*', '/']:
           operation = input_str
           display(result, operation)
           continue

        try:
            operand = float(input_str)
            if operation is None:
                result = operand
            else:
               result = calculate(result, operand, operation)
               operation = None

            display(result)

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число или операцию (+, -, *, /, c)!")

if __name__ == "__main__":
    print("Простой калькулятор в стиле iOS (консольный)\n")
    print("Доступные операции: +, -, *, /. Для очистки 'c'")
    main()
