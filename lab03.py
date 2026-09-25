# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):

    if (word[0] == "aeiou"):
        word = word[1:] + "way"
    else:
        word = word[1:] + word[0] + "ay"

    return word

def word_lengths(sentence):

    words = sentence.split()
    lengths = []
    
    for word in words:
        lengths.append(len(word))

    return lengths

def reverse_words(sentence):

    words = sentence.split()
    A = words[::-1]
    reverseWords = ""

    for word in A:
        reverseWords = reverseWords + word + " "

    return reverseWords

def letter_counts(text):

    dictionary = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1

    return dictionary

def main():

    print(pig_latin("banana"))                    # ananabay
    print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    print(reverse_words("the quick brown fox"))   # fox brown quick the
    print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

if __name__ == "__main__":
    main()