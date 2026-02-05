class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0   # starts from 0

    def change_score(self, points):
        self.score += points


player1 = Player("Michael")
player2 = Player("Jackson")

player1.change_score(10)

print(player1.name, player1.score)  # Michael 10
print(player2.name, player2.score)  # Jackson 0



#modification

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0   # starts from 0

    def change_score(self, points):
        if points < 0:
            print("Negative score is not allowed ")
        else:
            self.score += points


player1 = Player("Michael")
player2 = Player("Jackson")

player1.change_score(-1)

print(player1.name, player1.score)  # Michael 10
print(player2.name, player2.score)  # Jackson 0


#final program

class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
    
acc = BankAccount("Ali")
acc.deposit(1000)
success = acc.withdraw(1000)  # False

print(acc.balance)
        