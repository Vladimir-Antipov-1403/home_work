# 2. Наибольшее из двух чисел
def max_of_two(a: float, b: float) -> None:
    print(max(a, b))

max_of_two(10, 25)


# 3. Разница 135
def diff_135(a: float, b: float) -> None:
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

diff_135(200, 65)
diff_135(300, 100)


# 4. Время года по номеру месяца
def season(month: int) -> None:
    if month in (12, 1, 2):
        print("зима")
    elif month in (3, 4, 5):
        print("весна")
    elif month in (6, 7, 8):
        print("лето")
    elif month in (9, 10, 11):
        print("осень")
    else:
        print("Некорректный номер месяца")

season(3)
season(11)


# 5. Все числа > 10
def all_greater_than_10(a: float, b: float, c: float) -> None:
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

all_greater_than_10(11, 12, 13)
all_greater_than_10(5, 15, 20)


# 6. Количество положительных чисел в списке
def count_positive(nums: list[float]) -> None:
    positive_count = sum(1 for n in nums if n > 0)
    print(positive_count)

count_positive([-1, 2, -3, 4, 5])


# 7. Количество дней по годам и месяцам
def days_in_period(years: int, months: int) -> None:
    total_days = (years * 12 + months) * 29
    print(total_days)

days_in_period(2, 5)
