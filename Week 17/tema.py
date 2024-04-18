import mysql.connector

# Exercise 1:
# Write a Python program that asks the user for two numbers and performs division. Handle the ZeroDivisionError exception to display a custom error message when the second number is zero.

def division_numbers():
    x = int(input('First number: '))
    y = int(input('Second number: '))
    try:
        return x//y

    except ZeroDivisionError:
        return f'Error: The second number must be different from zero'

# print(division_numbers())

# Exercise 2:
# Write a Python function that takes a list of integers as input and calculates the average of the numbers. Handle the ValueError exception to display a custom error message when the user enters a non-integer value.

def average():
    list = []
    sum = 0
    try:
        x = int(input('First number: '))
        y = int(input('Second number: '))
        z = int(input('Third number: '))
        list.append(x)
        list.append(y)
        list.append(z)
        for nr in list:
            sum += nr
        average = sum // len(list)
        return average

    except ValueError:
        return 'Error: The value must be integer'  
# print(average())

# Exercise 3:
# Write a Python program that reads a file and prints its contents. Handle the FileNotFoundError exception to display a custom error message when the file does not exist.

def read_file():
    file_name = input('Enter the file name(exemple.txt): ')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file with name {file_name} doesn't exist"

# print(read_file())

# Exercise 4:
# Write a Python program that asks the user to enter their age. Handle the TypeError exception to display a custom error message when the user enters a non-numeric value.

def age():
    try:
        age = int(input('Your age: '))
        return age
    
    except ValueError:
        return 'Error: The value must be integer'

# print(age())

# Exercise 5:
# Write a Python function that takes a dictionary as input and prints the value associated with a given key. Handle the KeyError exception to display a custom error message when the key is not found in the dictionary.

def get_key():
    dict = {'name': 'Teo',
            'age': 22,
            }
    key = input('Enter key: ')
    try:
        return dict[key]
    
    except KeyError:
        return 'Error: The entered key is wrong'

# print(get_key())

# Exercise 6:
# Write a Python program that asks the user to enter a filename and then reads and prints the contents of the file. Handle the IOError exception to display a custom error message when an error occurs while reading the file.

def read_file2():
    file_name = input('Enter the file name(exemple.txt): ')
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except IOError:
        return 'Error: An error occurred while reading the file'

# print(read_file2())

# Exercise 7:
# Write a Python function that takes a list of numbers as input and calculates the product of all the numbers. Handle the OverflowError exception to display a custom error message when the result exceeds the maximum representable value.

def product_numbers():
    try:
        list = [4,4213,424,442,12465,54,3,123,432]
        result = 1
        for num in list:
            result *= num
        return result
    except OverflowError:
        return 'Error: The result exceed the maximum representable value'

# print(product_numbers())

# Exercise 8:
# Write a Python program that performs a database query. Handle the ConnectionError exception to display a custom error message when there is a problem connecting to the database.

def db_connect():
    try:
        connect = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'curs')
        cursor =  connect.cursor()
        cursor.execute('select * from persoane')
        persons = cursor.fetchall()
        return persons

    except ConnectionError:
        return 'Error: There is a problem connecting to the database'

# print(db_connect())

# Exercise 9:
# Write a Python function that takes a string as input and converts it to an integer. Handle the ValueError exception to display a custom error message when the input string cannot be converted to an integer.

def convert():
    try:
        string = input('Input text: ')
        int_string = int(string)
        return type(int_string)
    
    except ValueError:
        return 'Error: The input string cannot be converted to an integer.'

# print(convert())

# Exercise 10:
# Write a Python program that asks the user to enter two file names and then copies the contents of one file to another. Handle the PermissionError exception to display a custom error message when there is a problem accessing the files.

def copy_file_contents():
    try:
        source_file = input('Enter the name of the source file: ')
        destination_file = input('Enter the name of the destination file: ')

        with open(source_file, 'r') as file:
            content = file.read()
        with open(destination_file, 'w') as file:
            file.write(content)
        return 'File contents copied successfully'

    except PermissionError:
        return 'Error: Unable to access the files.'    

# print(copy_file_contents())

# Exercise 1:
# Write a Python function that takes a list of integers as input and returns the maximum value in the list.

def max_value():
    list = [45,8,56,47,1,32,0,721,56]
    # print(max(list))
    #or
    maximum = 0
    for nr in list:
        if nr > maximum:
            maximum = nr
    return maximum

# print(max_value())


# Exercise 2:
# Write a Python function that takes a list of strings as input and returns the index of the first occurrence of the string "apple" in the list.

def index_of_string():
    list = ['pear', 'cherry','apple', 'strawberry']
    for i in range(len(list)):
        if  list[i] == 'apple':
            return i
            break

# print(index_of_string())

# Exercise 3:
# Write a Python function that takes a list of integers as input and returns the index of the minimum value in the list.

def index_of_min():
    list = [4,6,86,2,14,21,11]
    minimum = list[0]
    for i in range(len(list)):
        if list[i] < minimum:
            minimum = list[i]
            return i

# print(index_of_min())

# Exercise 4:
# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that start with the letter "A".

def start_with_a():
    list = ['pear', 'cherry','apple', 'strawberry', 'Avocado']
    new_list = []
    for fruit in list:
        if fruit[0].lower() == 'a':
            new_list.append(fruit)
    return new_list

# print(start_with_a())

# Exercise 5:
# Write a Python function that takes a list of integers as input and returns the sum of all the even numbers in the list.

def sum_even():
    list = [4,6,86,2,14,21,11]
    sum = 0
    for nr in list:
        if nr%2 == 0:
            sum += nr
    return sum

# print(sum_even())

# Exercise 6:
# Write a Python function that takes a list of strings as input and returns the number of occurrences of the string "banana" in the list.

def occurrence():
    list = ['pear','banana', 'cherry','apple','banana', 'strawberry', 'Avocado']
    occurrence = 0
    for fruit in list:
        if fruit == 'banana':
            occurrence += 1
    return occurrence

# print(occurrence())        

# Exercise 7:
# Write a Python function that takes a list of integers as input and returns a new list where each element is multiplied by 2.

def multiplied_by_2():
    list = [4,6,8,2,14,1,11]
    for i in range(len(list)):
        list[i] *= 2
    return list

# print(multiplied_by_2())

# Exercise 8:
# Write a Python function that takes a list of strings as input and returns a new list containing the lengths of each string.

def lengths_of_string():
    list = ['pear','banana', 'cherry','apple','banana', 'strawberry', 'Avocado']
    new_list = []
    for fruit in list:
        lengths = len(fruit)
        new_list.append(lengths)
    return new_list

# print(lengths_of_string())

# Exercise 9:
# Write a Python function that takes a list of integers as input and returns the second smallest value in the list.

def second_smallest():
    list = [0,6,8,2,14,11]
    smallest = float('inf')
    second_smallest = float('inf')
    for nr in list:
        if nr < smallest:
            second_smallest = smallest
            smallest = nr
        elif nr < second_smallest and nr != smallest:
            second_smallest = nr
    return second_smallest

# print(second_smallest())

# Exercise 10:
# Write a Python function that takes a list of strings as input and returns a new list containing only the unique strings (removing duplicates).

def unique_strings():
    list = ['pear','banana', 'cherry','apple','banana', 'strawberry', 'avocado', 'cherry','pear']
    new_list = []
    for fruit in list:
        if fruit not in new_list:
            new_list.append(fruit)
    return new_list

# print(unique_strings())