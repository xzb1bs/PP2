class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount} руб. выполнено. Новый баланс: {self.balance} руб.")
        else:
            print("Ошибка: Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снятие {amount} руб. выполнено. Новый баланс: {self.balance} руб.")
        else:
            print("Ошибка: Недостаточно средств для снятия или сумма снятия некорректна.")

# Пример использования класса BankAccount
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)

    account.deposit(500)  # Пополнение на 500 руб. выполнено. Новый баланс: 1500 руб.
    account.withdraw(200)  # Снятие 200 руб. выполнено. Новый баланс: 1300 руб.
    account.withdraw(1600)  # Ошибка: Недостаточно средств для снятия или сумма снятия некорректна.
    account.deposit(-100)  # Ошибка: Сумма пополнения должна быть положительной.
