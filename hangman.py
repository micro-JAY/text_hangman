import random
wins = 0
losses = 0

print("H A N G M A N  # 8 attempts")
def status():
    while True:
        menu = input("""Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: """)
        if menu == "play":
            game()
        if menu == 'exit':
            exit()
        if menu == 'results':
            print(f"""You won: {wins} times.
You lost: {losses} times.""")

def game():
    global wins
    global losses
    chance = 8
    # print(f"""H A N G M A N  # {chance} attempts\n""")
    word_list = ["python", "java", "swift", "javascript"]
    correct = word_list[random.randint(0, len(word_list) - 1)]
    correct_set = set(correct)
    hint = "-" * (len(correct))
    guesses = []

    while True:
        print(hint)
        # if chance == 0:
        #     print("Thanks for playing!")
        #     exit()
        if hint == correct:
            print(f"You guessed the word {correct}!\nYou survived!")
            wins += 1
            game = False
            status()
        if chance == 0:
            print("You lost!")
            losses += 1
            game = False
            status()

        guess = input(f"Input a letter: ")
        if guess in guesses:
            print("You've already guessed this letter.")
            continue
        if len(guess) > 1 or len(guess) == 0:
            print("Please, input a single letter.")
            continue
        if not guess.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        guesses.append(guess)
        if guess in correct:
            if guess not in correct_set:
                chance -= 1
                print(f"No improvements.  # {chance} attempts")
                continue
            pos = [i for i, c in enumerate(correct) if c == guess]
            if guess in correct_set:
                correct_set.discard(guess)
                for point in pos:
                    hint = hint[:point] + guess + hint[point + 1:]
        else:
            chance -= 1
            print(f"That letter doesn't appear in the word.  # {chance} attempts\n")

status()
