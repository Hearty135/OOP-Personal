# # class Student:
# #    def __init__(self, name):
# #     self.name = name      #public
# #     self._gpa = 3.5       #protected
# #     self.__password = "1234"   #private

# # student = Student("Zakaria John")
# # print(student.name)
# # print(student._gpa)
# # #print(student.__password)

# # student.name ="Mercy"
# # print(student.name)

# coins = 100
# coins2= 500+100
# print (coins2)

# class Piggybank:
#     def __init__(self,coins):
#         self._coins=coins
#         self.put_in(coins)

#     def put_in(self, amount):
#         if amount <= 0:
#             raise ValueError("Add real money")
#         self._coins += amount

#     def take_out(self, amount):
#         if amount <=0:
#             raise ValueError("Be for real")
#         if amount > self.coins:
#             raise ValueError("Money has come")
#         self._coins -= amount
    
#     def how_much(self):
#         return self._coins

# Margie= Piggybank(1000000)
# Margie.put_in(3000)
# print("Margie's box has:",Margie.how_much(),"coins")


class Person:
    def __init__(self, name):
        self.name=name

    def intro(self):
        return f"Hi,my name is {self.name}"
    


class Student(Person):
    def __init__(self,name,program):
        super().__init__(name)
        self.program = program

    def intro(self):
        return super().intro()+f", and my program is {self.program}"

class Lecturer(Person):
    def __init__(self,name,department):
        super().__init__(name)
        self.department=department

    def intro(self):
        return super().intro()+f", and i work in the {self.department} department"

p =Person("Mark")
s =Student("Martha","BSIT",2)
l =Lecturer("Noah","Data Science")

print(p.intro())
print(s.intro())
print(l.intro())




