def factorial(n):
    return n * factorial(n - 1) if n else 1

# Количество перестановок
def count_permutations():
    n = int(input("Введите число для вычисления кол-ва перестановок: "))
    return factorial(n)

# Количество сочетаний (выбор m объектов из n)
def count_combinations():
    n = int(input("Введите кол-во элементов: "))
    m = int(input("Введите число выбираемых элементов: "))
    return int(factorial(n) / (factorial(n - m) * factorial(m)))

# Количество размещений: количество способов расположить некоторые m из n различных объектов на пронумерованных местах,
# при условии что каждое место занято в точности одним объектом
def count_placements():
    n = int(input("Введите кол-во элементов: "))
    m = int(input("Введите число выбираемых элементов: "))
    return int(factorial(n) / (factorial(n - m) * factorial(m)) * factorial(m))

# Количество перестановок с повторениями
def count_repeated_permutations(): # iterable
    input_list = [i for i in input("Введите строку или список для вычисления кол-ва перестановок: ").split()]
    repeatings = []
    set_from_list = set(input_list)
    for i in set_from_list:
        a = input_list.count(i)
        if a > 1:
            repeatings.append(a)
    divider = 1
    for i in repeatings:
        divider *= factorial(i)
    return int(factorial(len(input_list)) / divider)
        
# Количество сочетаний с повторениями: сочетание n объектов по m в предположении,
# что каждый объект может участвовать в сочетании несколько раз
def count_repeated_combinations():
    n = int(input("Введите число сочетаемых элементов: "))
    m = int(input("Введите кол-во требуемых сочетаний: "))
    result = factorial(m + n - 1) / (factorial(m) * factorial(n - 1))
    return int(result)

# Количество размещений с повторениями: всевозможные последовательности m различных элементов,
# выбранных из исходных n, которые содержат повторные элементы.
def count_repeated_placements():
    n = int(input("Введите кол-во элементов: "))
    m = int(input("Введите число выбираемых элементов: "))
    return n ** m

if __name__ == '__main__':
    print("Запустите основной файл")