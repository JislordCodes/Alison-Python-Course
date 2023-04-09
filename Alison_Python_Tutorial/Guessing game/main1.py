import random
randomNumber = random.randint(1,10)
score=10

while True:
    userNumberInput = int(input('Guess: '))

    if userNumberInput == randomNumber:
        print('Congratulations you guessed it right! your score is' + str(score)) #Changed into a str`ing to use +
        break
    else:
        print('better luck next time')
        score -=1
