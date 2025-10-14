# class Circle:
#     def _init_(self, radius):
#         self.radius = radius

#     def area(self):
#         pi = 3.14159  
#         return pi * self.radius ** 2

# radius = float(input("Enter the radius of the circle: "))
# circle = Circle(radius)
# print(f"The area of the circle is: {circle.area():.2f}")



# class BankAccount:
#     def __init__(self,balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount

# account = BankAccount(230)
# account.deposit(70)
# account.withdraw(160)
# print(account.balance)

# class Phone:
#     def __init__(self, brand, storage):
#         self.brand = brand
#         self.storage = storage
#     def call(self, number):
#         print(f"Calling {number} from {self.brand}!")

# my_phone =Phone('Samsung','128GB')
# my_phone.call('001-090-986')
# print(Phone)

class Phone:
    def __init__(self, song, spotify):
        self.song = song
        self.spotify = spotify
    def play(self,song):
        print(f"Playing {song} from {self.spotify}!")

my_phone =Phone('Party On U','spotify')
my_phone.play('Party On u')
print(Phone)    