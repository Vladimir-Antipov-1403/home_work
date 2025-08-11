# Задача 1
def task_1() -> None:
    # Создаём переменные разных типов
    number_int: int = 42
    number_float: float = 3.14
    text: str = "Привет"
    my_list: list = [1, 2, 3]
    flag: bool = True

    # Выводим тип каждой переменной
    print(type(number_int))
    print(type(number_float))
    print(type(text))
    print(type(my_list))
    print(type(flag))

# Вызов функции
task_1()


# Задача 2
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    # Выводим первые 3 значения списка
    print(a[:3])

# Вызов функции
task_2()


# Задача 3
def task_3(x: float) -> float:
    """Возвращает квадрат числа."""
    return x ** 2

# Вызов функции и вывод результата
print(task_3(5))

