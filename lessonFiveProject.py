# Engage and Apply Project
# This program suggests activities based on the weather and mood.
def suggest_activities(weather, mood):
    if weather == "sunny" and mood == "happy":
        return "Go for a hike", "Have a picnic in the park"
    elif weather == "sunny" and mood == "tired":
        return "Take a walk in the park", "Relax on your balcony"
    elif weather == "rainy" and mood == "happy":
        return "Watch a fun movie", "Read a book"
    elif weather == "rainy" and mood == "tired":
        return "Take a nap", "Listen to calming music"
    else:
        return "Sorry, I don't have a suggestion for that combination.", None

def main():
    weather = input("What's the weather like? (sunny/rainy): ").lower()
    mood = input("How do you feel? (happy/tired): ").lower()

    activity1, activity2 = suggest_activities(weather, mood)

    if activity2:
        print(f"Here are two activities you could do:\n1. {activity1}\n2. {activity2}")
        
if __name__ == "__main__":
    main()

# <-------------------------------------------------------->
 
# Final Challenge
# Guessing Game
    
import random

def guess_the_number():
    secret_number = random.randint(1, 10)  # Secret number between 1 and 10
    guess = None  # Initialize the guess variable

    print("Welcome to the Guessing Game!")
    print("I have chosen a secret number between 1 and 10. Try to guess it!")

    # Loop until the user guesses correctly
    while guess != secret_number:
        guess = int(input("Enter your guess: "))  # Take user input

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")

# Run the game
guess_the_number()