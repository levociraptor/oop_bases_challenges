"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

# код писать тут
class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    my_bank_account = BankAccount('Lev Upensky', 454545.45)
    my_credit_account = CreditAccount('Vel Ykysnepu', 1000.45)

    print(f'Full name: {my_bank_account.owner_full_name}',
          f'Balance: {my_bank_account.balance}',
          sep = '\n'
        )
    
    my_bank_account.increase_balance(0.56)
    print(f'Increased balanse: {my_bank_account.balance}')

    my_bank_account.decrease_balance(500)
    print(f'Decreased balanse: {my_bank_account.balance}')


    print(f'Full name: {my_credit_account.owner_full_name}',
          f'Balance: {my_credit_account.balance}',
          sep = '\n'
        )
        
    my_credit_account.increase_balance(0.56)
    print(f'Increased balanse: {my_credit_account.balance}')

    my_credit_account.decrease_balance(500)
    print(f'Decreased balanse: {my_credit_account.balance}')

    print(my_credit_account.is_eligible_for_credit())

    my_credit_account.increase_balance(1000)
    print(my_credit_account.is_eligible_for_credit())
