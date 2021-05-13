import random
random_no= random.randint(1,100)
guesses= 1
print("Guess the number:")
while(guesses<=9):

    input1= int(input())

    if random_no<input1:
        print("Please guess smaller no.")


    elif random_no>input1:
        print("Please guess greater no.")

    else:
        print(f"Congrats You Have Guessed the right no in {guesses} guesses")
        break

    print(9-guesses,"no. of guesses left")
    guesses = guesses + 1

if guesses>9:
    print("Game Over!!!")
    print(f"The number was{random_no}")