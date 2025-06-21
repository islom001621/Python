# Lesson 8 Homework 

# Task 1

def sonlarni_bolish(a, b):
    try:
        result = a / b
        print(f"{a} ni {b} ga bo‘lish natijasi: {result}")
    except ZeroDivisionError:
        print("Xatolik: Nolga bo‘lish mumkin emas.")

son1 = float(input("Iltimos, suratni kiriting (a): "))
son2 = float(input("Iltimos, maxrajni kiriting (b): "))

sonlarni_bolish(son1, son2)

4.0 ni 2.0 ga bo‘lish natijasi: 2.0

# Task 2

def get_integer_input():
    user_input = input("Please enter an integer: ")
    try:
        number = int(user_input)
        print(f"You entered the integer: {number}")
    except ValueError:
        raise ValueError("Invalid input! That is not a valid integer.")

try:
    get_integer_input()
except ValueError as e:
    print(e)
  Invalid input! That is not a valid integer.

# task 3

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = input("Enter the name of the file to open: ")
open_file(filename)
Error: The file 'Python' does not exist.

# Task 4

def get_two_numbers():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    try:
        number1 = float(num1)
        number2 = float(num2)
        print(f"You entered: {number1} and {number2}")
    except ValueError:
        raise TypeError("Invalid input! Both inputs must be numbers.")

try:
    get_two_numbers()
except TypeError as e:
    print(e)

You entered: 2.0 and 3.0

# Task 5

def open_file_with_permission_check(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{filename}'.")

filename = input("Enter the name of the file to open: ")
open_file_with_permission_check(filename)

# Task 6

def access_list_element(my_list, index):
    try:
        element = my_list[index]
        print(f"Element at index {index} is: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")


my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
try:
    user_index = int(input("Enter an index to access: "))
    access_list_element(my_list, user_index)
except ValueError:
    print("Invalid input! Please enter a valid integer index.")

List: [10, 20, 30, 40, 50]
Element at index 3 is: 40

# Task 7

def get_user_number():
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        print(f"You entered: {number}")
    except KeyboardInterrupt:
        print("\nInput cancelled by user (KeyboardInterrupt).")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

get_user_number()
You entered: 5.0

# Task 8 

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result of {a} divided by {b} is: {result}")
    except ArithmeticError as e:
        print(f"Arithmetic error occurred: {e}")

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    safe_divide(num1, num2)
except ValueError:
    print("Invalid input! Please enter numeric values.")
Result of 6.0 divided by 2.0 is: 3.0

# Task 9

def read_file_handling_encoding(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print(f"Error: Could not decode the contents of '{filename}' using UTF-8 encoding.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = input("Enter the name of the file to open: ")
read_file_handling_encoding(filename)
Error: The file 'all photos' does not exist.

# Task 10 

def perform_list_operation(my_list):
    try:
        my_list.push(100)  
    except AttributeError as e:
        print(f"Attribute error occurred: {e}")

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
perform_list_operation(my_list)

Original list: [1, 2, 3, 4, 5]
Attribute error occurred: 'list' object has no attribute 'push'

# File handling 

# task 1

def read_entire_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the name of the text file to read: ")
read_entire_file(filename)
Error: The file 'Videos' was not found.

# task 2

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break  
                print(f"Line {i+1}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Task 3

def append_and_display(filename, text_to_append):
    try:
        with open(filename, 'a') as file:
            file.write(text_to_append + '\n')

        print("\nUpdated file contents:")
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except Exception as e:
        print(f"An error occurred: {e}")

filename = input("Enter the filename: ")
text = input("Enter the text to append: ")
append_and_display(filename, text)

Updated file contents:
Bugun meeting qilamiz 

# task 4

def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            total_lines = len(lines)
            print(f"\nLast {n} line(s) of the file:")
            for line in lines[-n:]:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the filename: ")
try:
    n = int(input("Enter the number of lines to read from the end: "))
    read_last_n_lines(filename, n)
except ValueError:
    print("Invalid input! Please enter a valid number.")

Error: The file 'Logestics' was not found.

# Task 5

def read_file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]  
        print("\nLines stored in the list:")
        print(lines)
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

filename = input("Enter the filename: ")
lines_list = read_file_to_list(filename)

Error: The file 'All good' was not found.

# Task 6 

def read_file_to_variable_list(filename):
    try:
        with open(filename, 'r') as file:
            content = [line.strip() for line in file]  
        print("File content stored in variable (as list):")
        print(content)
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

  # Task 7

def read_file_to_array(filename):
    try:
        with open(filename, 'r') as file:
            array = [line.strip() for line in file]  
        print("Contents stored in array:")
        print(array)
        return array
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

filename = input("Enter the filename: ")
lines_array = read_file_to_array(filename)

Error: The file 'Third World War' was not found.

# task 8

def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()  
            if not words:
                print("The file is empty.")
                return

            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]

            print(f"\nLongest word(s) of length {max_length}:")
            for word in longest_words:
                print(word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the filename: ")
find_longest_words(filename)

Error: The file 'War' was not found.

# task 9 

def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for _ in file)
        print(f"The file '{filename}' has {line_count} line(s).")
        return line_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

filename = input("Enter the filename: ")
count_lines_in_file(filename)

Error: The file 'War 3' was not found.
0

# Task 10 

from collections import Counter
import re

def count_word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  
            words = re.findall(r'\b\w+\b', text)  
            word_counts = Counter(words)  

        print("Word frequencies:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
        return word_counts
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

filename = input("Enter the filename: ")
count_word_frequency(filename)

Error: The file 'Lessons' was not found.
{}

# task 11

import os

def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        print(f"The size of '{filename}' is {size} bytes.")
        return size
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

filename = input("Enter the filename: ")
get_file_size(filename)
Error: The file 'F25' was not found.
0

# task 12

def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')  
        print(f"List successfully written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

my_list = ["apple", "banana", "cherry", "date"]
filename = input("Enter the filename to write the list to: ")
write_list_to_file(filename, my_list)

List successfully written to 'All lists '.

# Task 13 

def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

source = input("Enter the source filename: ")
destination = input("Enter the destination filename: ")
copy_file_contents(source, destination)

Error: The source file 'maab' was not found.

# Task 14 

def combine_files_line_by_line(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            for line1, line2 in zip(f1, f2):
                combined = line1.strip() + " " + line2.strip()
                out.write(combined + '\n')
        print(f"Lines from '{file1}' and '{file2}' combined and saved to '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e.filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file1 = input("Enter the first filename: ")
file2 = input("Enter the second filename: ")
output = input("Enter the output filename: ")
combine_files_line_by_line(file1, file2, output)

Error: Birinchi file was not found.

# Task 15

import random

def read_random_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("The file is empty.")
                return
            random_line = random.choice(lines)
            print("Random line from the file:")
            print(random_line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the filename: ")
read_random_line(filename)

Error: The file 'Action' was not found.

# task 16 

def check_file_closed(filename):
    try:
        file = open(filename, 'r')
        print(f"Is the file closed? {file.closed}")  
        file.close()
        print(f"Is the file closed after closing? {file.closed}")  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the filename: ")
check_file_closed(filename)

Error: The file 'Data monsterlar' was not found.

# task 17 

def remove_newlines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read().replace('\n', '')  

        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print(f"Newlines removed and content saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

in_file = input("Enter the input filename: ")
out_file = input("Enter the output filename: ")
remove_newlines(in_file, out_file)

Error: The file 'Nma gaap ' was not found.

# task 18 

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        print(f"The file '{filename}' contains {word_count} word(s).")
        return word_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

filename = input("Enter the filename: ")
count_words_in_file(filename)

Error: The file 'Files' was not found.
0

# Task 19 

import os

def extract_characters_from_files(file_list):
    characters = []
    for filename in file_list:
        try:
            with open(filename, 'r') as file:
                content = file.read()
                characters.extend(list(content))  
            print(f"Characters extracted from '{filename}'.")
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {e}")
    return characters


file_names = input("Enter file names separated by commas: ").split(',')
file_names = [name.strip() for name in file_names]

character_list = extract_characters_from_files(file_names)
print("\nExtracted characters:")
print(character_list)

Error: The file 'Bar' was not found.
Error: The file 'Var' was not found.
Error: The file 'Char' was not found.

Extracted characters:
[]

# Task 20 

import string

def create_alphabet_files():
    for letter in string.ascii_uppercase:  
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(f"This is file {filename}\n")
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Failed to create {filename}: {e}")

create_alphabet_files()

Created: A.txt
Created: B.txt
Created: C.txt
Created: D.txt
Created: E.txt
Created: F.txt
Created: G.txt
Created: H.txt
Created: I.txt
Created: J.txt
Created: K.txt
Created: L.txt
Created: M.txt
Created: N.txt
Created: O.txt
Created: P.txt
Created: Q.txt
Created: R.txt
Created: S.txt
Created: T.txt
Created: U.txt
Created: V.txt
Created: W.txt
Created: X.txt
Created: Y.txt
Created: Z.txt

# task 21 

import string

def write_alphabet_to_file(filename, letters_per_line):
    try:
        alphabet = string.ascii_uppercase  # 'A' to 'Z'
        with open(filename, 'w') as file:
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i + letters_per_line]
                file.write(' '.join(line) + '\n')
        print(f"Alphabet written to '{filename}' with {letters_per_line} letters per line.")
    except Exception as e:
        print(f"An error occurred: {e}")

output_file = input("Enter the output filename: ")
letters_per_line = int(input("Enter the number of letters per line: "))
write_alphabet_to_file(output_file, letters_per_line)

Alphabet written to 'All problems' with 12 letters per line.
  
