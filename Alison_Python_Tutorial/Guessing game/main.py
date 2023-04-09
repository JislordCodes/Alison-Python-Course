import random
comp_gen = random.randint(1,10)


trial =  int(input("Enter how many trials: "))


def function():
    for i in range(0,trial):# Range from 0 to the number of trial, this allows us to iteriate for the amount of times the user want to play
        user_gen = int(input("Enter your guess: "))
        score = 0
        if comp_gen  == user_gen:
            print("You guessed correctly")
            score +=1
        elif comp_gen  != user_gen:
            print("You guessed wrong")

        else:
            print("You did not input a string... Please do")
            user_gen = input(int("Enter your guess:"))
    print("You scored",score,"over",trial)


function()
