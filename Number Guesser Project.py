import random

# Prompt the user to enter the range for the random number
top_of_range = input("Enter the upper limit for the number range (must be greater than 0): ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('The number must be greater than 0. Please try again next time.')
        quit()
else:
    print('Invalid input. Please enter a valid number next time.')
    quit()

# Generate a random number within the specified range
random_number = random.randint(0, top_of_range)
guesses = 0

# Start the guessing game
print(f"I've picked a random number between 0 and {top_of_range}. Try to guess it!")

while True:
    guesses += 1
    user_guess = input("Enter your guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('That is not a valid number. Please try again.')
        continue

    if user_guess == random_number:
        print(f"Congratulations! You guessed the correct number {random_number}.")
        break
    elif user_guess > random_number:
        print("Your guess is too high. Try a smaller number.")
    else:
        print("Your guess is too low. Try a larger number.")

print(f"Well done! You guessed the number in {guesses} attempts.")
