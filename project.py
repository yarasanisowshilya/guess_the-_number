import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=="easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_choosen=="hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right.....The answer was {answer}")
        play=input("Do you want to play again?Type 'YES' or 'NO':").lower()
        if play=="yes":
            game()
        else:
           return
def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 100")
    answer=random.randint(1,100)
    level=input("choose level of difficulty------Type 'easy' or 'hard':")
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
       print("you have entered wrong difficulty level----- play again")
       game()
    guessed_number=0
    while guessed_number!=answer:
      print(f"you have {attempts} attempts remaining to guess the number")
      guessed_number=int(input("guess a number:"))
      attempts=check_answer(guessed_number,answer,attempts)
      if attempts==0:
         print("you are out of guesses......you lose!")
         play=input("Do you want to play again?Type 'YES' or 'NO':").lower()
         if play=="yes":
            game()
         else:
           return
      elif guessed_number!=answer:
         print("guess again!")
      
game()    


