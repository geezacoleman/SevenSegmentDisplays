from collections import Counter
import re

# set the letters you can't use or those that the calculator can print upside down
displayLen = 6
unacceptableLetters = '[gkmqvwxz]'
calcLetters = '[^diehasgqlbgo]'

# open the txt file containing the words
with open("words_alpha.txt") as wordFile:
    words = list(wordFile.read().split())

# print the word length
print(len(words))


def longest_word():
    unacceptableWords = []
    longestWords = []

    [unacceptableWords.append(word) for word in words if re.search(unacceptableLetters, word)]
    acceptableWords = list((Counter(words) - Counter(unacceptableWords)).elements())
    longestWord = sorted(acceptableWords, key=len)[-1]

    # check for all words of that length if they exist
    [longestWords.append(word) for word in acceptableWords if len(word) == len(longestWord)]

    return longestWord


def calc_words():
    acceptedWords = []
    declinedWords = []
    notcalcWords = []

    [notcalcWords.append(word) for word in words if re.search(calcLetters, word)]

    calcWords = list((Counter(words) - Counter(notcalcWords)).elements())

    for w in calcWords:
        if len(w) <= displayLen:
            print("ADDED: {}, {}".format(w, len(w)))
            acceptedWords.append(w)

        else:
            declinedWords.append(w)
            print("REMOVED: {}, {}".format(w, len(w)))

    return acceptedWords, calcWords, declinedWords

longestWord = longest_word()
accepted, other, declined = calc_words()

print("The longest word is: {}\n".format(longestWord))
print("There are {} words that can be written on your calculator.".format(len(accepted)))

with open('calcwords.txt', 'w') as f:
    f.writelines("%s\n" % line for line in accepted)