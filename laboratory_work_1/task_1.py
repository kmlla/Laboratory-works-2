# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Car:
    def __init__(self, car_brand: str, color: str, amount_of_gasoline: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param car_brand: Марка машины
        :param color: Цвет машины
        :param amount_of_gasoline: Количество бензина в баке

        Пример:
        >>> car = Car("Toyota", "red", 10)  # инициализация экземпляра класса
        """
        if not isinstance(car_brand, str):
            raise TypeError("Марка машины должна быть типа str")
        self.car_brand = car_brand
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть типа str")
        self.color = color
        if not isinstance(amount_of_gasoline, (int, float)):
            raise TypeError("Количество бензина должно быть типа float или int")
        if amount_of_gasoline < 0 or amount_of_gasoline > 60:
            raise ValueError("Количество бензина должно быть неотрицательным числом и не должно превышать 60")
        self.amount_of_gasoline = amount_of_gasoline

    def change_color(self, another_color: str) -> None:
        """
        Функция, которая меняет цвет машины
        :param another_color: Другой цвет машины
        Пример:
        >>> car = Car("Toyota", "red", 10)
        >>> car.change_color("green")
        """
        ...

    def add_gasoline(self, gasoline: float) -> None:
        """
        Добавление бензина в бак
        :param gasoline: Объем добавляемого количества бензина

        :raise ValueError: Если количество добавляемого количества бензина превышает количество свободного места в баке, то вызываем ошибку

        Пример:
        >>> car = Car("Toyota", "red", 10)
        >>> car.add_gasoline(40)
        """
        ...


class Student:
    def __init__(self, name: str, marks: list):
        """
        Создание и подготовка к работе объекта "Студент".

        :param name: Имя студента.
        :param marks: Список оценок.

        Пример:
        >>> student = Student("Иван", [5,5,5,4,5]) # инициализация экземпляра класса
        """
        if not isinstance (name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name
        for i in range (len(marks)):
            if marks[i]<2 or marks[i]>5:
                raise ValueError ("Оценки должны быть от 2 до 5 включительно")
            if not isinstance(marks[i], int):
                raise TypeError("Оценки должны быть типа int")
        self.marks = marks


    def add_mark(self, mark: int) -> list:
        """
        Добавлние оценки.

        :param mark: Оценка, которую нужно добавить.

        :raise ValueError: Если оценка не от 2 до 5 включительно, то вызываеи ошибку.

        Пример:
        >>> student = Student ("Иван", [5,5,5,4,5])
        >>> student.add_mark(4)
        """
        ...

    def change_name(self, another_name: str) -> None:
        """
        Изменение имени студента.

        :param another_name: Другое имя студента.

        Пример:
        >>> student = Student ("Иван", [5,5,5,4,5])
        >>> student.change_name("Андрей")

        """
        ...

class Cafe:
    def __init__ (self, name: str, profit: float, number_of_orders: int):
        """
         Создание и подготовка к работе объекта "Кафе"

        :param name: Название кафе.
        :param profit: Прибыль кафе в рублях.
        :param number_of_orders: Количество заказов.

        Пример:
        >>> cafe = Cafe("Rest", 500000, 3000) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название кафе должно быть типа str")
        self.name = name
        if not isinstance(profit, (int,float)):
            raise ValueError("Прибыль должна быть типа int или float")
        self.month_profit = profit
        if not isinstance(number_of_orders, int):
            raise TypeError("Количесто заказов должно быть типа int")
        if number_of_orders < 0:
            raise ValueError ("Количество заказов не может быть отрицательным")
        self.number_of_orders = number_of_orders

    def average_check (self) -> float:
        """
        Функция, которая считает средний чек.

        :return: Средний чек. (Прибыль делит на количество заказов).

        Примеры:
        >>> cafe = Cafe("Rest", 500000, 3000)
        >>> cafe.average_check()
        """
        ...

    def add_or_subtract_money(self, sum: float) -> None:
        """
        Функция, которая считает прибыль кафе.

        :param sum: Сумма денег, которую получило или потеряло кафе. (Она может быть как отрицательной, так и положительной)

        Пример:
        >>> cafe = Cafe("Rest", 500000, 3000)
        >>> cafe.add_or_subtract_money(5000)
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest

