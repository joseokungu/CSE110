"""
AUTHOR: JOSE OKITANDENDE 
"""
#START
print("Welcome to word guessing game ")
print()
#VARIABLES
secret_word = "mosiah"
user_guess = " "
guess_count = 0
#INITIAL HINT
hint = "_ " *len(secret_word) 

print(f"Your hint is:{hint}")
print()
#GAME WHILE LOOP
#USER GUESS INPUT
while secret_word != user_guess:
    user_guess = input("What is your guess? ").lower() #LOWER LETTERS
    guess_count += 1
    if secret_word == user_guess:
        print("congratulation! You guessed it!")
        print(F"It took you {guess_count} number of guesses")
    elif len(secret_word) != len(user_guess):
        print("Sorry, your guess must have same number of letters as the secret word")
        print()
    else:
        print("Your hint is: ")
        for index, letter in enumerate(user_guess):
            if user_guess[index] == secret_word[index]:
                print(letter.upper(), end = " ")
            elif letter in secret_word:
                print(letter.lower(), end = " ")
            else:
                print("_",end = " ",) 
              
                
                                