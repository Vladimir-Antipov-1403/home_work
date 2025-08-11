class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


# Создаём 3 объекта
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)
rect3 = Rectangle(7, 8)

# Выводим площадь и периметр
for rect in (rect1, rect2, rect3):
    print(f"Площадь: {rect.area()}, Периметр: {rect.perimeter()}")

class Math:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def addition(self) -> None:
        print(self.a + self.b)

    def multiplication(self) -> None:
        print(self.a * self.b)

    def division(self) -> None:
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Деление на ноль!")

    def subtraction(self) -> None:
        print(self.a - self.b)


m = Math(10, 5)
m.addition()
m.multiplication()
m.division()
m.subtraction()


class SidebarButton:
    def __init__(self, text: str, locator: str = ""):
        self.text = text
        self.type = "Кнопка"
        self.locator = locator

    def click(self) -> str:
        return f"Клик по кнопке {self.text}"


# Создаём объекты
btn_textbox = SidebarButton("Text Box")
btn_checkbox = SidebarButton("Check Box")
btn_radiobutton = SidebarButton("Radio Button")

buttons = [btn_textbox, btn_checkbox, btn_radiobutton]

# Выводим текст и клики
for btn in buttons:
    print(btn.text)
    print(btn.click())
