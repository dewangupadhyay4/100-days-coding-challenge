class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self._bank="Tata Capital"    #protected
        self.__balance=balance    #private

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount > 0:
            self.__balance=amount
        else:
            print("Invalid Amount")

acc=BankAccount("Dewang", 120000)
print(acc.owner)
print(acc._bank)
print(acc.get_balance())
acc.set_balance(30000)
print(acc.get_balance())
print(acc.__balance)  #will raise error since it is private