class Bank:
    def __init__(self, num, name, type, balance):
        self.num = num
        self.name = name
        self.type = type
        self.balance = balance

    def deposit(self):
        cash = int(input("Enter the amount you want to deposit in the bank"))
        print(cash, " has been deposited to your account")
        self.balance = self.balance + cash
        print("The balance in your account is ", self.balance)
        print("Account Details \n 1)Account Number:", accnum, "\n 2)Bank Name",accname, "\n 3)Account Type", acctype, "\n 4)Old Balance", accbalance,"\n 5)New Balance",self.balance,"\n")

    def withdraw(self):
        self.money = int(
            input("Enter the amount of money you want to deposit from the bank"))
        if (self.balance < self.money):
            print("There is not enough money to withdraw from your account")
        else:
            print(self.money, " has been withdrawn from the bank")
            self.balance = self.balance - self.money
            print("The available balance in your account is ", self.balance)
            print("Account Details \n 1)Account Number:", accnum, "\n 2)Bank Name",accname, "\n 3)Account Type", acctype, "\n 4)Old Balance", accbalance,"\n 5)New Balance",self.balance,"\n")


flag=1
print("OPTIONS \n 1)Enter the account details \n 2) Deposit \n 3) Withdraw \n 4)View the current bank details\n 0)Exit")
while(flag!=0):
    flag = int(input("Enter the choice"))
    match flag:
        case 1:
            accnum = int(input("Enter your account number")) 
            accname = input("Enter the name of your bank")
            acctype = input("Enter the type of your account (Current/Savings)")
            accbalance = int(input("Enter the balance of your account"))
            acc = Bank(accnum, accname, acctype, accbalance)
        case 2:
            acc.deposit()
        case 3:
            acc.withdraw()
        case 4:
            print("Account Details \n 1)Account Number:", accnum, "\n 2)Bank Name",accname, "\n 3)Account Type", acctype, "\n 4)Balance",accbalance,"\n")
        case _:
            print("Invalid Choice")

