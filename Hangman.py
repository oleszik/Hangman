import random

def play_game():
    words = [
    "python", "java", "swift", "javascript",  # original list
    "pocket", "bright", "jumped", "signal", "laptop",
    "window", "travel", "crisp", "master", "bottle",
    "danger", "flight", "puzzle", "rocket", "secret",
    "garden", "basket", "planet", "wizard", "thunder"
]

    secret_word = random.choice(words)
    display = ['-' for _ in secret_word]
    attempts = 8
    guessed_letters = set()
    revealed_letters = set()

    while attempts > 0:
        print(''.join(display))
        print("Input a letter: ", end='')
        letter = input()

        # 1. Check single character input
        if len(letter) != 1:
            print("Please, input a single letter.\n")
            continue

        # 2. Check for lowercase a-z
        if not letter.isalpha() or not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.\n")
            continue

        # 3. Already guessed
        if letter in guessed_letters:
            print("You've already guessed this letter.\n")
            continue

        guessed_letters.add(letter)

        # 4. Check if letter is in the word
        if letter in secret_word:
            for i, ch in enumerate(secret_word):
                if ch == letter:
                    display[i] = letter
            revealed_letters.add(letter)
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1

        print()

        if '-' not in display:
            print(''.join(display))
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return True  # win
    else:
        print("You lost!")
        return False  # lose

print("H A N G M A N\n")
wins = 0
losses = 0

while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:', end=' ')
    command = input()

    if command == "play":
        result = play_game()
        if result:
            wins += 1
        else:
            losses += 1
    elif command == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times.")
    elif command == "exit":
        break
    else:
        continue