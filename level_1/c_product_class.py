"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


if __name__ == '__main__':
    apple = Product('apple', 'red apple', 100, 50)
    print('Информация о продукте:')
    print(apple.name, apple.description, apple.price, apple.weight, sep='\n')
