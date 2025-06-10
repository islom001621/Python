# Task 1
from datetime import datetime

name = input("Please enter your name: ")
year_of_birth = input("Enter your year of birth: ")

try:
    year_of_birth = int(year_of_birth)
    current_year = datetime.now().year
    age = current_year - year_of_birth
    print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
Hello, Islom! You are 24 years old.
  
# task 2
txt = 'LMaasleitbtui'

txt[::2]
'Lasetti'

txt[1::2]
'Malibu'

# task 3
txt = 'MsaatmiazD'
txt[-1::-2]
'Damas'

txt[::2]
'Matiz'

# Task 4
txt = "I'am John. I am from London"

import re

txt = "I'm John. I am from London"
match = re.search(r"I am from (\w+)", txt)

if match:
    print("Residence area:", match.group(1))

Residence area: London


#Task 5


user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)

Reversed string: olleh

#Task 6

user_input = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_count = 0

for char in user_input:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

Number of vowels: 3

#Task 7

user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

max_value = max(numbers)

print("The maximum value is:", max_value)

The maximum value is: 9

#Task 8

word = input("Enter a word: ")

word = word.lower()

if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

The word is a palindrome.


#Task 9

email = input("Enter your email address: ")

parts = email.split('@')

if len(parts) == 2:
    domain = parts[1]
    print("The domain of the email is:", domain)
else:
    print("Invalid email address format.")

The domain of the email is: gmail.com

#Task 10 

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the desired password length: "))

password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)

Generated password: @[s<&8nY*7'&E|(Z2!QQ
