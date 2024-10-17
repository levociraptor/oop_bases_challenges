"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username):
        if username not in self.usernames:
            print('Такого пользователя не существует.')
            return
        
        self.usernames.remove(username)


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()


if __name__ == '__main__':
    manager = UserManager()
    admin = AdminManager()
    super_admin = SuperAdminManager()

    print(f'Users: {manager.get_users()}')
    manager.add_user('user1')
    manager.add_user('user2')
    manager.add_user('user3')
    print(f'Users: {manager.get_users()}')

    print('##################################################')

    print(f'Users: {admin.get_users()}')
    admin.add_user('user_1')
    admin.add_user('user_2')
    admin.add_user('user_3')
    print(f'Users: {admin.get_users()}')

    print('##################################################')

    admin.ban_username('user_2')
    admin.ban_username('user')
    print(f'Users: {admin.get_users()}')

    print('##################################################')

    print(f'Users: {super_admin.get_users()}')
    super_admin.add_user('user__1')
    super_admin.add_user('user__2')
    super_admin.add_user('user__3')
    print(f'Users: {super_admin.get_users()}')

    print('##################################################')

    super_admin.ban_username('user__2')
    super_admin.ban_username('user')
    print(f'Users: {super_admin.get_users()}')

    print('##################################################')

    super_admin.ban_all_users()
    print(f'Users: {super_admin.get_users()}')




