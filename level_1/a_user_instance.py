"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str) -> None:
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    lev = User('lev', 'pythonic_animal', 20, '8 777 999 888')
    print('Информация о пользователе:')
    print(lev.name, lev.username, lev.age, sep='\n')

