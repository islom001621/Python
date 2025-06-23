# Lesson 9 Homework

# task 1

import math

class Aylana:
    def __init__(self, radius):
        self.radius = radius

    def yuzani_hisobla(self):
        return math.pi * self.radius ** 2

    def perimetrni_hisobla(self):
        return 2 * math.pi * self.radius

radius = float(input("Aylana radiusini kiriting: "))
aylana = Aylana(radius)

print("Aylananing yuzi:", aylana.yuzani_hisobla())
print("Aylananing perimetri:", aylana.perimetrni_hisobla())

Aylananing yuzi: 113.09733552923255
Aylananing perimetri: 37.69911184307752

# Task 2

class Person:
    pass

p1=Person()

p1.name='Islom'
p1.age=24
p1.country='Qashqadaryo'
p1.date_of_birth=26/12/2001

print(p1.age)
24

# Task 3

class Calculator:
    def __init__(self,x,y):
        self.x =x
        self.y =y
        
    def qoshish(self):
        return self.x + self.y
    def ayirish(self):
        return self.x-self.y
    def kopaytirish(self):
        return self.x*self.y
    def bolish(self):
        if self.y != 0:
         return self.x / self.y
        else:
            return "Nolga bo‘lish mumkin emas"
        
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

calc = Calculator(a, b)

print("qoshish:", calc.qoshish())

qoshish: 14.0

# Task 4

import math

class Shape:
    def area(self):
        raise NotImplementedError("Maydonni hisoblash metodi yuq")

    def perimeter(self):
        raise NotImplementedError("Perimetrni hisoblash metodi yuq")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # 1-yon
        self.b = b  # 2-yon
        self.c = c  # 3-yon

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Geron formulasi

# Sinflarni tekshirish:
print("--- Aylana ---")
aylana = Circle(5)
print("Maydon:", aylana.area())
print("Perimetr:", aylana.perimeter())

print("\n--- Kvadrat ---")
kvadrat = Square(4)
print("Maydon:", kvadrat.area())
print("Perimetr:", kvadrat.perimeter())

print("\n--- Uchburchak ---")
uchburchak = Triangle(3, 4, 5)
print("Maydon:", uchburchak.area())
print("Perimetr:", uchburchak.perimeter())

--- Aylana ---
Maydon: 78.53981633974483
Perimetr: 31.41592653589793

--- Kvadrat ---
Maydon: 16
Perimetr: 16

--- Uchburchak ---
Maydon: 6.0
Perimetr: 12

# Task 5

class Tugun:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.chap = None
        self.ong = None

class BST:
    def __init__(self):
        self.kok = None

    def insert(self, qiymat):
        if self.kok is None:
            self.kok = Tugun(qiymat)
        else:
            self._insert_recursive(self.kok, qiymat)

    def _insert_recursive(self, tugun, qiymat):
        if qiymat < tugun.qiymat:
            if tugun.chap is None:
                tugun.chap = Tugun(qiymat)
            else:
                self._insert_recursive(tugun.chap, qiymat)
        elif qiymat > tugun.qiymat:
            if tugun.ong is None:
                tugun.ong = Tugun(qiymat)
            else:
                self._insert_recursive(tugun.ong, qiymat)

    def search(self, qiymat):
        return self._search_recursive(self.kok, qiymat)

    def _search_recursive(self, tugun, qiymat):
        if tugun is None:
            return False
        if qiymat == tugun.qiymat:
            return True
        elif qiymat < tugun.qiymat:
            return self._search_recursive(tugun.chap, qiymat)
        else:
            return self._search_recursive(tugun.ong, qiymat)

daraxt = BST()
daraxt.insert(10)
daraxt.insert(5)
daraxt.insert(15)
daraxt.insert(7)

print("7 soni mavjudmi?", daraxt.search(7))   # True
print("3 soni mavjudmi?", daraxt.search(3))   # False

7 soni mavjudmi? True
3 soni mavjudmi? False

# Task 6 

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack bo‘sh"

    def is_empty(self):
        return len(self.stack) == 0

    def show(self):
        return self.stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack:", s.show())         # [10, 20, 30]
print("Chiqarildi:", s.pop())     # 30
print("Stack:", s.show())         # [10, 20]

Stack: [10, 20, 30]
Chiqarildi: 30
Stack: [10, 20]

# Task 7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        yangi_tugun = Node(data)
        if self.head is None:
            self.head = yangi_tugun
        else:
            hozirgi = self.head
            while hozirgi.next:
                hozirgi = hozirgi.next
            hozirgi.next = yangi_tugun

    def delete(self, data):
        hozirgi = self.head

        if hozirgi and hozirgi.data == data:
            self.head = hozirgi.next
            return

        oldingi = None
        while hozirgi and hozirgi.data != data:
            oldingi = hozirgi
            hozirgi = hozirgi.next

        if hozirgi is None:
            print(f"{data} ro‘yxatda topilmadi.")
            return

        oldingi.next = hozirgi.next

    def display(self):
        hozirgi = self.head
        if not hozirgi:
            print("Ro‘yxat bo‘sh.")
            return

        while hozirgi:
            print(hozirgi.data, end=" -> ")
            hozirgi = hozirgi.next
        print("None")

# Sinov:
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()            # 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()            # 10 -> 30 -> None

ll.delete(100)          # 100 ro‘yxatda topilmadi.

10 -> 20 -> 30 -> None
10 -> 30 -> None
100 ro‘yxatda topilmadi.

  # Task 8

class ShoppingCart:
    def __init__(self):
        self.items = {}  # mahsulot_nomi: (narx, miqdor)

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            old_price, old_quantity = self.items[name]
            self.items[name] = (price, old_quantity + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatda topilmadi.")

    def calculate_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Savat bo‘sh.")
        else:
            for name, (price, quantity) in self.items.items():
                print(f"{name} - {quantity} dona - {price} so‘m (har biri)")
            print("Umumiy narx:", self.calculate_total(), "so‘m")

# Sinov:
cart = ShoppingCart()
cart.add_item("Olma", 5000, 3)
cart.add_item("Non", 3000, 2)
cart.show_cart()

cart.remove_item("Non")
cart.show_cart()

Olma - 3 dona - 5000 so‘m (har biri)
Non - 2 dona - 3000 so‘m (har biri)
Umumiy narx: 21000 so‘m
Olma - 3 dona - 5000 so‘m (har biri)
Umumiy narx: 15000 so‘m

# task 9

class Stack:
    def __init__(self):
        self.stack = []

    # Element qo‘shish (push)
    def push(self, element):
        self.stack.append(element)
        print(f"{element} steckka qo‘shildi.")

    # Element chiqarish (pop)
    def pop(self):
        if not self.is_empty():
            element = self.stack.pop()
            print(f"{element} steckdan chiqarildi.")
            return element
        else:
            print("Steck bo‘sh, chiqarish mumkin emas.")
            return None

    # Steckdagi elementlarni ko‘rsatish
    def display(self):
        if self.is_empty():
            print("Steck bo‘sh.")
        else:
            print("Steck elementlari (yuqoridan pastga):")
            for element in reversed(self.stack):
                print(element)

    # Bo‘shligini tekshirish
    def is_empty(self):
        return len(self.stack) == 0

# Sinov:
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()

10 steckka qo‘shildi.
20 steckka qo‘shildi.
30 steckka qo‘shildi.
Steck elementlari (yuqoridan pastga):
30
20
10
30 steckdan chiqarildi.
Steck elementlari (yuqoridan pastga):
20
10

# task 10 

class Queue:
    def __init__(self):
        self.queue = []

    # Element qo‘shish (enqueue)
    def enqueue(self, element):
        self.queue.append(element)
        print(f"{element} navbatga qo‘shildi.")

    # Element chiqarish (dequeue)
    def dequeue(self):
        if not self.is_empty():
            element = self.queue.pop(0)
            print(f"{element} navbatdan chiqarildi.")
            return element
        else:
            print("Navbat bo‘sh, chiqarib bo‘lmaydi.")
            return None

    # Navbatdagi elementlarni ko‘rsatish
    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Navbat elementlari (oldindan oxirigacha):")
            for element in self.queue:
                print(element)

    # Bo‘shligini tekshirish
    def is_empty(self):
        return len(self.queue) == 0

# Sinov:
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.display()

q.dequeue()
q.display()

A navbatga qo‘shildi.
B navbatga qo‘shildi.
C navbatga qo‘shildi.
Navbat elementlari (oldindan oxirigacha):
A
B# Task 11

class BankAccount:
    def __init__(self, account_number, customer_name):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so‘m depozit qilindi. Yangi balans: {self.balance} so‘m.")
        else:
            print("Noto‘g‘ri summa kiritildi.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so‘m yechildi. Yangi balans: {self.balance} so‘m.")
        else:
            print("Yetarli mablag‘ mavjud emas yoki noto‘g‘ri summa.")

    def check_balance(self):
        print(f"{self.customer_name} hisobidagi balans: {self.balance} so‘m.")

# Sinov:
account1 = BankAccount("001", "Ali Valiyev")
account1.deposit(100000)
account1.withdraw(25000)
account1.check_balance()

account2 = BankAccount("002", "Laylo Karimova")
account2.deposit(50000)
account2.withdraw(60000)  # Yetarli mablag‘ yo‘q
account2.check_balance()



100000 so‘m depozit qilindi. Yangi balans: 100000.0 so‘m.
25000 so‘m yechildi. Yangi balans: 75000.0 so‘m.
Ali Valiyev hisobidagi balans: 75000.0 so‘m.
50000 so‘m depozit qilindi. Yangi balans: 50000.0 so‘m.
Yetarli mablag‘ mavjud emas yoki noto‘g‘ri summa.
Laylo Karimova hisobidagi balans: 50000.0 so‘m.


