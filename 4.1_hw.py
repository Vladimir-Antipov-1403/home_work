class Car:
    def __init__(self, color: str, car_type: str, year: int):
        self.color = color
        self.type = car_type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведен")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        self.year = year

    def set_type(self, car_type: str) -> None:
        self.type = car_type

    def set_color(self, color: str) -> None:
        self.color = color


car1 = Car("красный", "седан", 2020)
car1.start()
car1.stop()
car1.set_year(2022)
car1.set_type("кроссовер")
car1.set_color("синий")
print(car1.color, car1.type, car1.year)
