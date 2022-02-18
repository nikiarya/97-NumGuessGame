print('Number Guessing Game')
guess = int(input('Guess a Number Between 1 - 9 : '))

if(guess > 7):
    print("Too High! Try Again!")
elif(guess == 7):
    print("You got it! Congratutions you win an imaginary cookie!")
else: 
    print("Too Low! Try Again!")