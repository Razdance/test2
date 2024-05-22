import random

def hangman():
    word_list = ["python", "programmering", "spel", "dator", "kod", "pannkaka", "pannkaksdeg"]
    chosen_word = random.choice(word_list)
    guessed_word = ["_"] * len(chosen_word)
    attempts = 6
    guessed_letters = set()

    print("Välkommen till Hänga Gubbe!")
    
    while attempts > 0 and "_" in guessed_word:
        print(f"Ord: {' '.join(guessed_word)}")
        print(f"Antal försök kvar: {attempts}")
        print(f"Gissade bokstäver: {' '.join(guessed_letters)}")
        
        guess = input("Gissa en bokstav: ").lower()
        
        if guess in guessed_letters:
            print("Du har redan gissat den bokstaven. Försök igen.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"Fel! Bokstaven {guess} finns inte i ordet.")
        
        print()
    
    if "_" not in guessed_word:
        print(f"Grattis! Du har gissat ordet: {''.join(guessed_word)}")
    else:
        print(f"Du förlorade! Ordet var: {chosen_word}")

hangman()
