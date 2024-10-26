import math

def area_triangle():
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_rectangle():
    a = float(input("Введите длину прямоугольника: "))
    b = float(input("Введите ширину прямоугольника: "))
    return round(a * b, 2)

def area_square():
    a = float(input("Введите длину ребра куба: "))
    return round(a * a, 2)

def area_sphere():
    r = float(input("Введите радиус шара: "))
    return round(4 * math.pi * r ** 2, 2)

if __name__ == '__main__':
    print("Запустите основной файл")