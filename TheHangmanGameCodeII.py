#HangmanGameII

import random
import time
import os

def play_again():
    question = "Do you want to play again? Y = YES, N = NO \n"
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)
    if play_game.lower() == 'y':
        return True
    else:
        return False
def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print ('Invalid input. Enter a single letter: \n')
            guess = input (
                f'Hangman Word:{display} Enter your guess: \n').strip()
        if guess in guessed:
            print ('Oops! You already tried that guess, try again \n')
            continue
        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]
        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print(' __\n'
                     ' |  \n'
                     ' |  \n'
                     ' |  \n'
                     ' |  \n'
                     ' |  \n'
                     ' |  \n'
                     '_|_ \n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')
            elif count == 2:
                time.sleep(1)
                print(' __\n'
                      '|  |\n'
                      '|  |\n'
                      '|  \n'
                      '|  \n'
                      '|  \n'
                      '|  \n'
                     '_|_ \n')

                print(f'Wrong guess: {limit - count} guesses remaining\n')
            elif count == 3:
                time.sleep(1)
                print(' __\n'
                      '|  |\n'
                      '|  |\n'
                      '|  |\n'
                      '|  \n'
                      '|  \n'
                      '|  \n'
                     '_|_ \n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')
            elif count == 4:
                time.sleep(1)
                print('__\n'
                     '|  |\n'
                     '|  |\n'
                     '|  |\n'
                     '|  O\n'
                     '|  \n'
                     '|  \n'
                    '_|_ \n')
                print(f'Wrong guess: {limit - count} guesses remaining\n')
            elif count == 5:
                time.sleep(1)
                print('__\n'
                     '|  |\n'
                     '|  |\n'
                     '|  |\n'
                     '|  O\n'
                     '| /|\n'
                     '| / \\n'
                    '_|_ \n')
            print('Wrong guess: You have been hanged!\n')
            print('The Word was:{word}')
        if display == word:
            print(f'Congratulations! You have guessed the word \'{word}\' correctly!')
            break
def play_hangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck')
    time.sleep(1)
    print(f"The game is about to start! \nLet's play Hangman!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    word_to_guess = [
        'python','frontend','backend','fullstack','coding','helloworld','cibersegurança','CTD','cosntancia'
        'developer','hypertext','javascript','CSS','HTML','MIT','linkedin','carater','pomodoro','PRICO','constroi'
            ]
    play = True
    while play:
        word = random.choice(word_to_guess)
        hangman(word)
        play = play_again()
    print('Thanks for playing! We expect you have enjoyed!')
    exit()
if __name__ == '__main__':
    play_hangman()
                                                  

                                    
                                         
                        

                    

                      
