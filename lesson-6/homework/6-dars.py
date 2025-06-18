# Lesson 6 

# Task 1

txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]
'abc_abcd_abcdeab_cdef_abcdefg'

# Task 2 

n = int(input())  

for i in range(n):  
    print(i * i)    
0
1
4
9
16

# Task 3
 
# exercise 1
 
i = 1            
while i <= 10:   
    print(i)     
    i += 1       
1
2
3
4
5
6
7
8
9
10

# Exersice 2
 
for i in range(1, 6):         
    for j in range(1, i + 1): 
        print(j, end=' ')     
    print()                   
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

# Exersice 3

n=int(input())
total=0

for i in range (1,n+1):
    total = total + i

print("Yig'indisi:", total)
Yig'indisi: 55

# Exercise 4

n= int(input())

for i in range (1,11):
    print(f"{n}*{i}={n*i}")
  2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18
2*10=20
# Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    num>=150
    print (num)
  12
75
150
180
145
525
50
# Exercise 6

number=75869
count=0

while number !=0:
    number = number //10 
    count+=1

print(count)
5

# Exercise 7

for i in range(5, 0,-1):         
    for j in range(i, 0, -1): 
        print(j, end=' ')     
    print()                   
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
# Exercise 8

list1 = [10, 20, 30, 40, 50]

for l1 in range(len(list1)-1,-1,-1):
    print(list1[l1])
  50
40
30
20
10
# Exercise 9 

for i in range (-10,0):
    print(i)
  -10
-9
-8
-7
-6
-5
-4
-3
-2
-1
# Exercise 10 

for i in range (0,5):
    print(i)
print('Done!')
0
1
2
3
4
Done!
# Exercise 11

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(25, 50):
    if is_prime(num):
        print(num, end=' ')

29 31 37 41 43 47 
# Exercise 12

n_terms = 10

a, b = 0, 1

print("Fibonacci series up to 10 terms:")
for _ in range(n_terms):
    print(a, end=' ')
    a, b = b, a + b
  Fibonacci series up to 10 terms:
0 1 1 2 3 5 8 13 21 34 
# Exercise 13

# num = int(input(" Son kiriting: "))
factorial = 1

if num < 0:
    print("Manfiy sonning faktoriali yuq")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")
  5! = 120

#Task 4

# from collections import Counter

def not_common_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    result = []

    # Elementlar faqat list1 da bor, list2 da yo‘q yoki kamroq marta uchrasa
    for elem in c1:
        diff = c1[elem] - c2.get(elem, 0)
        result.extend([elem] * max(0, diff))

    # Elementlar faqat list2 da bor, list1 da yo‘q yoki kamroq marta uchrasa
    for elem in c2:
        diff = c2[elem] - c1.get(elem, 0)
        result.extend([elem] * max(0, diff))

    return result
  
