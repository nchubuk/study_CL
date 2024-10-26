from mymath import * # импорт всего содержимого

modules = {'C': combinatorics, 'G': areas}

choice_m = input("Для выбора комбинаторики введите C, для геометрии - G: ")
if choice_m == 'C':
    functions = [i for i in dir(modules[choice_m]) if not i.startswith('__')]
elif choice_m == 'G':
    functions = [i for i in dir(modules[choice_m]) if not i.startswith('__')]

dict_functions = dict(enumerate(functions, 1))
print("Доступные функции из раздела комбинаторики: ")
for key, value in dict_functions.items():
    print(f"{key}: {value}")

choice_f = int(input("Введите номер требуемой функции: "))
f = getattr(modules[choice_m], dict_functions[choice_f])
print(f"Результат выполнения ф-ии {dict_functions[choice_f]} - ", f())



