"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float)-> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float)-> None:
        self.balance += income

    def decrease_balance(self, loss: float)-> None:
        if self.balance - loss < 0:
            raise ValueError
        
        self.balance -= loss


if __name__ == '__main__':
    my_cart = BankAccount('Valentin Petrov Vladimirovich', 728.25)
    print(my_cart.balance)
    my_cart.increase_balance(500)
    print(my_cart.balance)
    my_cart.decrease_balance(300)
    print(my_cart.balance)
    my_cart.decrease_balance(1300)
    print(my_cart.balance)