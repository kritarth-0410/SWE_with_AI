# OOP - Object Oriented Programming : It is a way of writing software by 
# modelling real-world things/entities as objects.

# Object - Real world instance of the class.
# Class - Blueprint of a real world entity.

# Student - name, email, phone, password, college, company.....
# Car 

# class Student:
#     def __init__(self, name, age, email = ""):
#         self.name = name
#         self.age = age
#         self.email = email
    
#     def display_student(self):
#         print(f"Name: {self.name}, age: {self.age}, email: {self.email}")

# student1 = Student("Khushi", 20, "khushi@gmail.com")
# student2 = Student("Nikhil", 21)
# student3 = Student("Aman", 22, "aman@gmail.com")
# student1.name = "Khushi"
# student1.age = 20
# student1.email = "khushi@gmail.com"

# student2 = Student()
# student1.name = ""
# student1.age = 
# student1.email = ""

# student3 = Student()
# student1.name = ""
# student1.age = 
# student1.email = ""

# print(student1.name, " ", student1.age)
# print(student2.name, " ", student2.age)
# print(student3.name, " ", student3.age)

# student1.display_student()
# student2.display_student()
# student3.display_student()

# bank_name, account_holder_name, account_balance.
# class BankAccount: 
#     bank_name = "HDFC Bank" # Class attributes

#     def __init__(self, account_holder_name, account_balance): # instance attributes
#         self.account_holder_name = account_holder_name
#         self.account_balance = account_balance

#     def display_account_details(self):
#         print(f"Customer name: {self.account_holder_name}, Balance: {self.account_balance}, Bank: {self.bank_name}")

# # acc1 = BankAccount("HDFC Bank", "Kritarth", 100000000)
# # acc2 = BankAccount("HDFC Bank", "Khushi", 500000000)
# # acc3 = BankAccount("HDFC Bank", "Aman", 70000000)
# # acc4 = BankAccount("HDFC Bank", "Deepak", 500000)

# acc1 = BankAccount("Kritarth", 100000000)
# acc2 = BankAccount("Khushi", 500000000)
# acc3 = BankAccount("Aman", 70000000)
# acc4 = BankAccount("Deepak", 500000)

# acc1.display_account_details()
# acc2.display_account_details()
# acc3.display_account_details()
# acc4.display_account_details()

# Instance Attributes belongs to specific objects.
# Class Attributes belongs to all the instances/objects of the class.

# Methods in Python Classes.
# Methods - Functions inside python class.

#There are 3 types of methods in python classes:
# Instance Methods
# Class Methods
# Static Methods

# Instance Methods - Modifies the specific object attributes.
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def apply_discount(self, percentage):
#         discount = self.price * percentage / 100
#         self.price = self.price - discount

# product = Product("Laptop", 10000)
# print(product.name, " ", product.price)
# product.apply_discount(20)
# print(product.name, " ", product.price)
# product.apply_discount(10)
# print(product.name, " ", product.price)
# product.apply_discount(50)
# print(product.name, " ", product.price)

# Class Methods
# class Product:
#     discount_percentage = 10

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     @classmethod
#     def update_discount(cls, new_discount):
        # cls.discount_percentage = new_discount

# product = Product("Laptop", 10000)
# print(Product.discount_percentage)

# Product.update_discount(20)

# print(Product.discount_percentage)

# Static Methods don't need object data or class data.
# These are utility methods kept inside a class as they are logically related.

# class PriceValidator:
#     @staticmethod
#     def is_valid_price(price): # static method
#         return price > 0

# print(PriceValidator.is_valid_price(100))
# print(PriceValidator.is_valid_price(-100))

# Object Oriented Programming Principles.

# Encapsulation - Wrapping data and methods together inside a class and protecting the access.
# Don't allow direct and uncontrolled access to important data.

# class BankAccount: 
#     bank_name = "HDFC Bank" # Class attributes

#     def __init__(self, account_holder_name, account_balance): # instance attributes
#         self.account_holder_name = account_holder_name
#         self.__account_balance = account_balance

#     def display_account_details(self):
#         print(f"Customer name: {self.account_holder_name}, Balance: {self.__account_balance}, Bank: {self.bank_name}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Amount to be deposited should be greater than 0.")
#             return
        
#         self.__account_balance += amount
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Amount to be withdrawn should be greater than 0.")
#             return
        
#         if amount > self.__account_balance:
#             print("Insufficient Balance")
#             return
        
#         self.__account_balance -= amount

#     def get_account_balance(self):
#         return self.__account_balance
    

# bank_account = BankAccount("Deepak", 10000)
# bank_account.display_account_details()

# # bank_account.account_balance = -100
# # bank_account.display_account_details()
# # Ideally the bank account balance shouldn't be allowed to be updated from outside.

# bank_account.withdraw(2000)
# bank_account.display_account_details()

# bank_account.deposit(500)
# bank_account.display_account_details()

# print(bank_account.get_account_balance())

# bank_account.__account_balance = -100

# print(bank_account.get_account_balance())

# Abstraction - Hiding internal implementation details from the user and exposing only the essential behaviour.

# Python provides an 'abc' module for abstraction.
# Any Payment Gateway must have a pay method.

# from abc import ABC, abstractmethod

# class PaymentGateway(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class PhonePePaymentGateway(PaymentGateway):
#     def pay(self, amount):
#         print(f"Paying amount: {amount} via PhonePe")

# class PaytmPaymentGateway(PaymentGateway):
#     def pay(self, amount):
#         print(f"Paying amount: {amount} via Paytm")

# class RazorpayPaymentGateway(PaymentGateway):
#     def pay(self, amount):
#         print(f"Paying amount: {amount} via Razorpay")

# payment1 = RazorpayPaymentGateway()
# payment1.pay(100)

# payment2 = PhonePePaymentGateway()
# payment2.pay(1000)

# payment3 = PaytmPaymentGateway()
# payment3.pay(400)

# Why Abstraction is Useful ? 
# E-Commerce Application like Amazon.

# class CheckoutService:
#     def __init__(self, payment_gateway):
#         self.payment_gateway = payment_gateway

#     def checkout(self, amount):
#         self.payment_gateway.pay(amount)

# # user
# pg = PhonePePaymentGateway()

# checkout1 = CheckoutService(pg)
# checkout1.checkout(1000)

# Inheritance allows one class to reuse the properties/attributes and methods of another class.

# Vehicle 
# Car is a type of Vehicle.
# Bike is a type of Vehicle.

# Both car and bike will have common attributes like speed, rating, brand, price, start()

class Vehicle:
    def __init__(self, name, brand, speed, price):
        self.name = name
        self.brand = brand
        self.speed = speed
        self.price = price
    
    def drive(self):
        pass

# super -> Parent class
class Car(Vehicle): # Car class is inheriting the Vehicle class.
    def __init__(self, name, brand, speed, price, boot_capacity):
        super().__init__(name, brand, speed, price)
        self.boot_capacity = boot_capacity

    def drive(self):
        print("Driving a car")
    
    def open_boot(self):
        print("Opening the boot of the car.")

class Bike(Vehicle):
    def __init__(self, name, brand, speed, price):
        super().__init__(name, brand, speed, price)

    def drive(self):
        print("Driving a Bike.")

class Cycle(Vehicle):
    def __init__(self, name, brand, speed, price):
        super().__init__(name, brand, speed, price)
    
    def drive(self):
        print("Driving a Cycle.")


car = Car("Safari", "Tata", 200, 25000000, 300)
print(car.name)
print(car.brand)
print(car.speed)
print(car.price)
print(car.boot_capacity)
car.drive()
car.open_boot()

# super() is sued to call the parent class method.
# In constructors (init method), super is commonly used to initialize the parent class attributes.

# Types of Inheritance - Single, MultiLevel, Hierarchical, Multiple 
# Method Overriding.
# Polymorphism

# Vehicle <----- Car
