def check_guess(letter, guess):
    if guess.isalpha() == False:
        print("Invalid")
        return False
    elif guess.lower() > letter.lower():
        print("Guess is high")
        return False;
    elif guess.lower() < letter.lower():
        print("Guess is low")
        return False
    else:
        print("Guess is correct")
        return guess.lower() == letter.lower()

def letter_guess(answer_letter):
    if check_guess(answer_letter,input("Enter guess: ")):
        return True
    elif check_guess(answer_letter,input("Enter guess: ")):
        return True
    elif check_guess(answer_letter,input("Enter guess: ")):
        return True
    else:
        return False

letter_guess("x")
