"""
AUTHOR: JOSE OKITANDENDE 
"""
#START
print("Welcome to the Word guessing game! ")
print()
#VARIABLES
secret_word = "mosiah"
user_guess = ""
guess_count = 0
#GAME WHILE LOOP
#USER GUESS INPUT
while secret_word != user_guess:
    user_guess = input("What is your guess? ").lower()
    guess_count += 1
    if secret_word == user_guess:
        print("Congratulation! You guessed it!")
        print(f"It took you {guess_count} guesses. ")
    else:
        print("your guess was incorrect.")                             