

# reduce adjacent duplicates
def reduce_adjacent_duplicates(lst):
    reduced_list =list(set(lst))
    return reduced_list

original_list = [1, 2, 3, 3]
result = reduce_adjacent_duplicates(original_list)
print(result)


#​Consider dividing a string into two halves
def split_string(s):
    length = len(s)
    if length % 2 == 0:
        front_half = s[:length // 2]
        back_half = s[length // 2:]
    else:
        front_half = s[:(length // 2) + 1]
        back_half = s[(length // 2) + 1:]
    return front_half, back_half

def combine_halves(a, b):
    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)
    return a_front + b_front + a_back + b_back

a = "abcdef"
b = "123456"
result = combine_halves(a, b)
print(result)  # Output: "abc123def45


# Write a Python function that takes a sequence of numbers and determines
def all_unique(seq):
    return len(seq) == len(set(seq))


sequence1 = [1, 5, 7, 9]
sequence2 = [2, 4, 5, 5, 7, 9]

print(all_unique(sequence1))  # Output: True
print(all_unique(sequence2))  # Output: False


#Implement bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


unordered_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unordered_list)
print("Sorted list:", unordered_list)

import random


def play_guessing_game():
    target_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = set()

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while tries > 0:
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Number out of range! Please enter a number between 1 and 100.")
            continue

        if guess in guessed_numbers:
            print("You've already guessed this number! Try a different one.")
            continue

        guessed_numbers.add(guess)
        tries -= 1

        # Compare the guess with the target number
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {target_number}!")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                play_guessing_game()
            else:
                print("Thanks for playing!")
                return

    print(f"\nSorry, you've run out of tries. The number was {target_number}.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_guessing_game()
    else:
        print("Thanks for playing!")


# Start the game
play_guessing_game()






