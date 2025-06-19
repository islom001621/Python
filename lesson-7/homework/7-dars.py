# Lesson 7 Homework

# task 1 

def is_prime(n):
    if n< 2:
        print('False')
    for i in range(2, int(n** 0.5) + 1):  
        if n % i == 0:
         print('False')
        print ('True') 

print(is_prime(4))
False
True
None

# task 2 

def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10  
        k //= 10         
    return total

print (digit_sum(24))
6

# task 3
def powers_of_two(N):
    k = 1
    while 2 ** k <= N:
        print(2 ** k, end=' ')
        k += 1
print(powers_of_two(16))

2 4 8 16 None
