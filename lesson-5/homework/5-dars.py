# Lesson 5 Homework 

# Task 1

year=int(input('enter the year and you can know that your entered date is leap year or not:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('this year is leap year')
else:
    print('no, this year is not leap year')

no, this year is not leap year

# Task 2 

n=int(input('Enter number'))

if n%2 !=0:
    print('weird')

n=int(input('Enter number'))
if  n%2==0 and 2 <= n <= 5:
     print('not weird')


n=int(input('Enter number'))
if  n%2==0 and 6 <= n <= 20:
      print('weird')


n=int(input('Enter number'))
if  n%2==0 and  n >= 20:
     print('not weird')

# task 3 


a = 3
b = 12

# Boshlanish nuqtasini aniqlaymiz
if a % 2 == 0:
    start = a
else:
    start = a + 1

even_numbers = list(range(start, b + 1, 2))
print(even_numbers)


a = 3
b = 12

start = a + (a % 2)  # toq bo‘lsa +1, juft bo‘lsa 0
even_numbers = list(range(start, b + 1, 2))
print(even_numbers)

[4, 6, 8, 10, 12]
[4, 6, 8, 10, 12]

