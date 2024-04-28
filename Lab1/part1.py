import math

# 1. Reverse the user's first and last name
def reverse_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(last_name + " " + first_name)

# 2. Compute the value of n+nn+nnn
def compute_n_n_n():
    n = int(input("Enter an integer (n): "))
    result = n + int(str(n)*2) + int(str(n)*3)
    print("Result:", result)

# 3. Print a multi-line heredoc string
def print_heredoc_string():
    print("""a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example""")

# 4. Calculate the volume of a sphere with radius 6
def sphere_volume():
    radius = 6
    volume = (4/3) * math.pi * radius**3
    print("Volume of the sphere:", volume)


# 5. Compute the area of a triangle given base and height
def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle:", area)

# 6. Construct a pattern using nested loops
def construct_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(4, 0, -1):
        print('*' * i)

# 7. Reverse a word entered by the user
def reverse_word():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print("Reversed word:", reversed_word)

# 8. Print numbers from 0 to 6 except 3 and 6
def print_numbers_except_3_and_6():
    for i in range(7):
        if i != 3 and i != 6:
            print(i)

# 9. Generate Fibonacci series between 0 to 50
def fibonacci_series():
    a, b = 0, 1
    print("Fibonacci series between 0 to 50:")
    while a < 50:
        print(a, end=' ')
        a, b = b, a + b
def count_digits_and_letters(input_string):
    num_digits = sum(c.isdigit() for c in input_string)
    num_letters = sum(c.isalpha() for c in input_string)
    return num_digits, num_letters

input_string = input("Enter a string: ")
digits, letters = count_digits_and_letters(input_string)
print("Number of digits:", digits)
print("Number of letters:", letters)
