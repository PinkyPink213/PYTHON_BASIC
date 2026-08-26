"""ตัวอย่างผลงาน: Space Hangman"""

import random

WORDS = {
    "rocket": "It carries people into space.",
    "planet": "It travels around a star.",
    "comet": "It is an icy space traveler.",
}
ART = ("[🚀____]", "[🚀___🔥]", "[🚀__🔥🔥]", "[💥 GAME OVER 💥]")


def choose_word():
    word = random.choice(list(WORDS))
    return word, WORDS[word]


def hidden_word(word, correct):
    result = []
    for letter in word:
        result.append(letter.upper() if letter in correct else "_")
    return " ".join(result)


def play():
    word, hint = choose_word()
    guessed = set()
    correct = set()
    mistakes = 0

    print("╔══════════════════════╗")
    print("║    SPACE HANGMAN     ║")
    print("╚══════════════════════╝")

    while mistakes < 3 and not set(word).issubset(correct):
        print("\n" + ART[mistakes])
        print("Hint: " + hint)
        print("Word: " + hidden_word(word, correct))
        print("Guessed: " + " ".join(sorted(guessed)))
        guess = input("Letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Type one letter.")
        elif guess in guessed:
            print("Already guessed!")
        else:
            guessed.add(guess)
            if guess in word:
                correct.add(guess)
            else:
                mistakes += 1

    if set(word).issubset(correct):
        print("🌟 MISSION COMPLETE: " + word.upper() + " 🌟")
    else:
        print(ART[-1])
        print("The word was " + word.upper())


play()

