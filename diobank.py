from datetime import datetime

# Global variables to store account data
account_balance = 0.0
transactions = []

def display_menu():
    print("\nBank Menu:")
    print("1. Deposito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

def deposit():
    global account_balance
    amount = float(input("Insira o valor do deposito: "))
    account_balance += amount
    transactions.append({
        'transaction': 'Deposito',
        'amount': amount,
        'balance': account_balance,
        'datetime': datetime.now()
    })
    print("Deposito efetuado com sucesso. Saldo atualizado: $", account_balance)

def withdraw():
    global account_balance
    amount = float(input("Enter withdrawal amount: "))
    if amount <= account_balance:
        account_balance -= amount
        transactions.append({
            'transaction': 'Saque',
            'amount': -amount,
            'balance': account_balance,
            'datetime': datetime.now()
        })
        print("Saque efetuado com sucesso. Saldo: $", account_balance)
    else:
        print("Saldo insuficiente")

def display_statement():
    print("\nExtrato:")
    print("{:<12} {:<10} {:<10} {:<20}".format('Transacao', 'Valor', 'Saldo', 'Data Hora'))
    for transaction in transactions:
        print("{:<12} {:<10} {:<10} {:<20}".format(transaction['transaction'],
                                                    transaction['amount'],
                                                    transaction['balance'],
                                                    transaction['datetime'].strftime('%d/%m/%Y %H:%M')))

def main():
    while True:
        display_menu()
        choice = input("\nSelecione a opcao (1-4): ")
        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            display_statement()
        elif choice == '4':
            print("Exiting the bank. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()