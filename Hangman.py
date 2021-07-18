# Python 3.9

import random

# open word list file and choose word
with open(r"wordlist.txt") as f:
    wordList = f.read()
    wordList = wordList.split()
    word = list(random.choice(wordList))

# inform player of rules
print('''
         The underscores represent the unknown letters in your mystery word. It will update with correct guesses.
        Guess one letter at a time or the whole word if you think you know it. After seven letter guesses you will be 
    prompted to guess the word. You may only guess the full word once, after which you will be informed of your result. 
                                                        Good luck!
      ''')

# game logic
currentGuess = []
guesses = []
s = ''
for n in range(len(word)):
    currentGuess.append(' _ ')
for i in range(7):
    print(s.join(currentGuess))
    if i == 6:
        print('Please guess the word: ')
        finalGuess = input()
        if finalGuess == s.join(word):
            print('Congratulations, you guessed the correct word!')
            break
        else:
            print('Better luck next time.')
            print('Your word was ' + s.join(word) + '.')
            break
    print('Please guess a letter:')
    letter = input()
    if len(letter) > 1:
        if letter == s.join(word):
            print('Congratulations, you guessed the correct word!')
            break
        else:
            print('Better luck next time.')
            print('Your word was ' + s.join(word) + '.')
            break
    if letter in guesses:
        print('You already guessed that letter.')
        continue
    else:
        guesses.append(letter)
    if letter in word:
        for c in range(len(word)):
            if word[c] == letter:
                currentGuess[c] = letter
    else:
        print('Try again.')
