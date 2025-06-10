#Lesson 3 Homework 

# Task 1

fruits = ["apple", "banana", "cherry", "mango", "orange"]

print("The third fruit is:", fruits[2])
The third fruit is: cherry

#task 2

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)
Combined list: [1, 2, 3, 4, 5, 6]

#task 3

numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]

middle_index = len(numbers) // 2
middle = numbers[middle_index]

last = numbers[-1]

extracted = [first, middle, last]

print("Extracted elements:", extracted)
Extracted elements: [10, 40, 70]

#Task 4

favorite_movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Forrest Gump"]

movies_tuple = tuple(favorite_movies)

print("Movies tuple:", movies_tuple)
Movies tuple: ('Inception', 'Interstellar', 'The Matrix', 'The Dark Knight', 'Forrest Gump')

#task 5

cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")
Paris is in the list.

  #task 6

numbers = [1, 2, 3, 4, 5]

duplicated_list = numbers + numbers

print("Duplicated list:", duplicated_list)
Duplicated list: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#Task 7

numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping:", numbers)
List after swapping: [50, 20, 30, 40, 10]

#Task 8

numbers = tuple(range(1, 11))

sliced_tuple = numbers[3:7]

print("Sliced tuple (index 3 to 6):", sliced_tuple)
Sliced tuple (index 3 to 6): (4, 5, 6, 7)

#Task 9

colors = ["red", "blue", "green", "blue", "yellow", "blue"]

blue_count = colors.count("blue")

print("The color 'blue' appears", blue_count, "times.")
The color 'blue' appears 3 times.

#Task 10 

animals = ("cat", "dog", "lion", "tiger", "elephant")

lion_index = animals.index("lion")

print("The index of 'lion' is:", lion_index)
The index of 'lion' is: 2

#Task 11

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2

print("Merged tuple:", merged_tuple)
Merged tuple: (1, 2, 3, 4, 5, 6)

#Task 12

my_list = [10, 20, 30, 40]
my_tuple = (1, 2, 3)

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)
Length of the list: 4
Length of the tuple: 3

#task 13 

number_tuple = (5, 10, 15, 20, 25)

number_list = list(number_tuple)

print("Converted list:", number_list)
Converted list: [5, 10, 15, 20, 25]

#Task 14 

numbers = (12, 45, 7, 89, 23, 5, 67)

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
Maximum value: 89
Minimum value: 5

#Task 15 

words = ("apple", "banana", "cherry", "date", "elderberry")

reversed_words = words[::-1]

print("Reversed tuple:", reversed_words)
Reversed tuple: ('elderberry', 'date', 'cherry', 'banana', 'apple')
