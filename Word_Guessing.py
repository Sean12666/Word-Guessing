import time
import easygui

word = list(easygui.enterbox('Enter a word:', 'Word Guessing'))
guess = list(len(word) * '_')
times = 0
while guess != word:
    for i in guess:
        print(i, end=' ')
    print('\n')
    letter = input('Guess a character:\n')
    print('')
    time.sleep(1)
    if len(letter) != 1:
        print('Please enter ONE character.\n')
    else:
        correct = False
        for i in range(len(word)):
            if letter == word[i]:
                correct = True
                guess[i] = word[i]
        if correct:
            print('"', letter, '" is in this word.\n', sep='')
        else:
            print('"', letter, '" is not in this word.\n', sep='')
        times += 1
    time.sleep(1)
print('Wow, you did it!\n')
time.sleep(1)
print('The word is:')
for i in word:
    print(i, end='')
print('\n')
time.sleep(1)
print('You guessed', times, 'times.')
