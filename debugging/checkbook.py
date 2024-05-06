class Checkbook:
    """
    Una clase que representa una libreta de cheques.

    Attributes:
        balance (float): El saldo actual en la libreta de cheques.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la libreta de cheques con un saldo inicial de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposita una cantidad especificada en la libreta de cheques.

        Args:
            amount (float): La cantidad a depositar.

        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retira una cantidad especificada de la libreta de cheques, si hay suficientes fondos.

        Args:
            amount (float): La cantidad a retirar.

        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Obtiene y muestra el saldo actual de la libreta de cheques.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Función principal que ejecuta el programa de la libreta de cheques.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

