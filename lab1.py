import cmath
def get_coefficient(name, min_value=-1000, max_value=1000, non_zero=False):
    while True:
        try:
            value = float(input(f"Введите коэффициент {name}: "))
            if non_zero and value == 0:
                print(f"Коэффициент {name} не должен быть равен нулю. Попробуйте снова.")
                continue
            if not (min_value <= value <= max_value):
                print(f"Коэффициент {name} должен быть в диапазоне от {min_value} до {max_value}. Попробуйте снова.")
                continue
            return value
        except ValueError:
            print(f"Некорректное значение для коэффициента {name}. Попробуйте снова.")
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1.real, root2.real if discriminant > 0 else (root1.real, None)
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2   # сложные корни
def format_complex(num):
    # Форматируем комплексное число в виде a + bi или a - bi
    real_part = round(num.real, 2)
    imaginary_part = round(num.imag, 2)
    
    if imaginary_part == 0:
        return f"{real_part}"
    elif imaginary_part > 0:
        return f"{real_part} + {imaginary_part}i"
    else:
        return f"{real_part} - {abs(imaginary_part)}i"
def main():
    print("Решение квадратного уравнения Ax^2 + Bx + C = 0")
    a = get_coefficient("A", non_zero=True)
    b = get_coefficient("B")
    c = get_coefficient("C")
    
    roots = solve_quadratic(a, b, c)
    if isinstance(roots[0], complex) or roots[1] is None:
        root1 = format_complex(roots[0])
        root2 = format_complex(roots[1])
        print(f"Уравнение имеет комплексные корни: x1 = {root1}, x2 = {root2}")
    else:
        print(f"Корни уравнения: x1 = {roots[0]}, x2 = {roots[1]}")
if __name__ == "__main__":
    main()