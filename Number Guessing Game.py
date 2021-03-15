import random #import random library

print("Number guessing game!") #prints the title of the game

points = 0 #variable points set to 0
guesses = 0 #variable guesses set to 0

try: #error handling
    while guesses < 10: #repeats until the user has guessed for 10 times

        num = random.randint(1,10) #variable num is set to a random number between 1 and 10

        guess = int(input("Try to guess the number between 1 and 10: "))
        #user gets asked to input a number between 1 and 10

        if guess == num: #if the user's guess was the same as the randomly chosen number
            print("Correct!") #user gets feedback his input was correct
            points = points + 1 #user's score gains a point
            guesses = guesses + 1 #adds a guess so the user can guess again

        elif guess == 0: #in case the user inputs the number 0
            print("Can't you read? Only numbers between 1 and 10!")

        elif guess < num: #if the user inputs a number that's smaller than the randomly chosen number
            print("Nope, too low.") #user gets feedback that his guess was too low
            guesses = guesses + 1

        elif guess > 10: #if the user inputs a number that's bigger than the randomly chosen number
            print("Can't you read? Only numbers between 1 and 10!") #user feedback

        elif guess > num: #if user input is bigger than the randomly chosen number
            print("Nope, too high") #user gets feedback that his guess was too high
            guesses = guesses + 1

    print("Your score is: " + str(points)) #user's total score gets printed

except:
    print("Start over. Only numbers between 1 and 10 are allowed.") #if user inputs letters

