""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


def make_username_capitalized(username: str):
    return username.capitalize()


def generate_short_user_description(username: str, user_id: int, name: str):
    return f'User with id {user_id} has {username} username and {name} name'


class User:
    def __init__(self, username: str, user_id: int, name: str) -> None:
        self.username = username
        self.user_id = user_id
        self.name = name
        self.description = self._generate_short_user_description()

    
    def  make_username_capitalized(self) -> str:
        return self.username.capitalize()
    

    def _generate_short_user_description(self) -> str:
        description = f'User with id {self.user_id} has {self.username} username and {self.name} name'
        return description
    

some_user = User('cool_username', 4554, 'Vasily')

print(
    f'Username: {some_user.username}',
    f'User_id: {some_user.user_id}',
    f'Name: {some_user.name}',
    f'Description: {some_user.description}',
    sep='\n'
      )

print('', f'Username capitalize: {some_user.make_username_capitalized()}', sep='\n')
