import random

choice = 'y'

print("Guess the random number between (and including) 0 and 100 in 10 tries! (Integers Only)")

#Start the guessing game loop
while choice == 'y':
    
    #Get a random number from 0 to 100 for user to guess
    random_number = random.randrange(0,101)
    word = "guess"

    #Start for loop for 10 user guesses using variable 'guess_counter'
    for guess_counter in range(1,11):
        
        #Print the guess attempt number and get a guess from the user
        guess = int(input(f"\nGuess attempt {guess_counter} of 10; Input guess: "))
        
        #Check if their guess was right; if right, tell them and break for loop
        if guess == random_number:
            if guess_counter > 1:
                word += "es"
            print(f"You guessed correctly in {guess_counter} {word}!")
            break
        #If their guess wasn't right, then if they have more tries, check and tell them if their guess
        #was higher or lower than the number they're guessing
        elif guess_counter < 10:
            if guess > random_number:
                print("Incorrect, try guessing lower")
            elif guess < random_number:
                print("Incorrect, try guessing higher")
        #If their guess wasn't right, then if they're out of tries, tell the user they lost and what the
        #number was
        else:
            print("\nIncorrect and out of guesses, you lose!" + f"\nThe number was {random_number}")
            
    #Ask user if they want to play the game again and get input, re-asking if answer isn't 'y' or 'n'
    while (choice :=  input("\nWould you like to play again? (y/n): ").lower()) not in ('y', 'n'):
        print("Please input either  \"y\" or \"n\"")



print("\nCompleted by, Jeremiah Vela")
