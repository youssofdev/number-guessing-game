import random

def play_game():
    attempts = 10
    best_score = float("inf")
    
    while True:
        print("\nWelcome to the Guessing Game!")
        print("You have {} attempts to guess the number.".format(attempts))
        print("Please enter a number between 1 and 100.")
        
        target_number = random.randint(1, 100)
        guess_count = 0
        found = False
        
        while guess_count < attempts:
            guess = int(input("Enter your guess: "))
            
            if guess == target_number:
                found = True
                guess_count += 1
                print("Congratulations! You guessed the number in {} attempts.".format(guess_count))
                
                if guess_count < best_score:
                    best_score = guess_count
                    print("New best score: {} attempts.".format(best_score))
                    
                break
            
            elif guess < target_number:
                guess_count += 1
                print("Too low! You have {} attempts left.".format(attempts - guess_count))
                
            else:
                guess_count += 1
                print("Too high! You have {} attempts left.".format(attempts - guess_count))
        
        if not found:
            print("Game over! You ran out of attempts.")
            print("The correct number was {}.".format(target_number))
            
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

play_game()