"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    
    def should_be_banned(self, list_of_surname: list[str]) -> bool:
        for surname in list_of_surname:
            if surname.casefold() == self.surname.casefold():
                return True
        
        return False
    

trustworthy_user = User('Petr', 'Petrov', 23)
suspicious_user = User('Vladimir', 'Santaros', 39)

print(trustworthy_user.should_be_banned(SURNAMES_TO_BAN))
print(suspicious_user.should_be_banned(SURNAMES_TO_BAN))
