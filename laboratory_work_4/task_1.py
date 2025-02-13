class Animal:
    """
    Базовый класс для представления животных.
    Имеет общие атрибуты и методы для всех животных.
    """
    def __init__(self, animal_type: str, age: int) -> None:
        """
        Конструктор базового класса Animal.

        :param animal_type: вид животного
        :param age: возраст животного
        """
        self._animal_type = animal_type  # Непубличный атрибут, вид не должен изменяться напрямую
        self.age = age  # Публичный атрибут, возраст животного может изменяться напрямую

    @property
    def animal_type(self) -> str:
        """
        Геттер для атрибута animal_type

        :return: Вид животного
        """
        return self._animal_type

    @property
    def age(self) -> int:
        """
        Геттер для атрибута age

        :return: Возраст животного
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """
        Сеттер для атрибута age

        :param value: значение, на которое нужно поменять возраст животного
        """

        if not isinstance(value, int) or value <= 0:
            raise ValueError("Возраст должен быть целым положительным числом.")
        self._age = value

    def __str__(self) -> str:
        """
        Магический метод для отображения информации об объекте Animal для пользователей .

        :return: строка с видом и возрастом
        """
        return f"Вид животного: {self.animal_type}. Возраст животного: {self.age}."

    def __repr__(self) -> str:
        """
        Магический метод для отображения информации об объекте Animal в режиме отладки.

        :return: строка, представляющая объект
        """
        return f"{self.__class__.__name__}(animal_type={self.animal_type!r}, age={self.age!r})"

    def sound(self) -> str:
        """
        Метод для воспроизведения звука животного.

        :return: строка со звуком животного
        """
        ...

class Pet(Animal):
    """
    Дочерний класс для представления домашних животных.
    Включает дополнительные атрибуты и методы для класса домашних животных.
    """
    def __init__(self, animal_type: str, age: int, name: str, owner: str) -> None:
        """
        Конструктор дочернего класса Pet.

        :param animal_type: вид животного
        :param age: возраст животного
        :param name: кличка животного
        :param owner: имя владельца животного
        """
        super().__init__(animal_type, age)  # Вызов конструктора родительского класса
        self.name = name  #  Публичный атрибут, кличка животного может изменяться напрямую
        self.owner = owner  # Публичный атрибут, имя владельца может изменяться напрямую

    @property
    def name(self) -> str:
        """
        Геттер для атрибута name

        :return: Кличка животного
        """
        return self._name

    @name.setter
    def name(self, string: str) -> None:
        """
        Сеттер для атрибута name

        :param string: значение, на которое нужно поменять кличку животного
        """
        if not isinstance(string, str):
            raise ValueError("Кличка животного должна быть типа str.")
        self._name = string

    @property
    def owner(self) -> str:
        """
        Геттер для атрибута owner

        :return: Имя владельца
        """
        return self._owner

    @owner.setter
    def owner(self, string: str) -> None:
        """
        Сеттер для атрибута owner

        :param string: значение, на которое нужно поменять имя владельца
        """
        if not isinstance(string, str):
            raise ValueError("Имя владельца должно быть типа str.")
        self._owner = string

    def __str__(self) -> str:
        """
        Перегруженный метод __str__ для более подробного описания домашних животных.

        :return: строка с видом, возрастом, кличкой и владельцем
        """
        return f"Вид животного: {self.animal_type}. Возраст животного: {self.age}. Кличка животного: {self.name}. Владелец: {self.owner}"

    def __repr__(self) -> str:
        """
        Магический метод для отображения информации об объекте Pet в режиме отладки.

        :return: строка, представляющая объект домашнего животного
        """
        return f"{self.__class__.__name__}(animal_type={self.animal_type!r}, age={self.age}, name={self.name!r}, owner={self.owner!r})"

    def sound(self) -> str:
        """
        Перегруженный метод speak, который возвращает звук, характерный для домашних животных.

        Домашние животные имеют более разнообразные и специфические звуки, поэтому метод перегружен.

        :return: строка с характерным звуком для домашних животных
        """
        ...

if __name__ == "__main__":
    animal = Animal("Панда", 4)
    print(animal.animal_type)
    print(animal.age)
    print(animal)
    print(repr(animal))
    print(animal.sound())

    pet = Pet("Кошка", 3, "Луна", "Алиса")
    print(pet.animal_type)
    print(pet.age)
    print(pet.name)
    print(pet.owner)
    print(pet)
    print(repr(pet))
    print(pet.sound())
    pass
