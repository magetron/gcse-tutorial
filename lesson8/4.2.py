def main():
    secret_word = "hello"
    correct = False
    give_up = False
    guess_word = ""
    while (not correct and not give_up):
        guess_word = input("Please guess a word:")
        if (guess_word == secret_word):
            print("yes")
            correct = True
        else:
            print("no")
            again = input("Guess again?")
            if (again == "n"):
                print("answer is {}".format(secret_word))
                give_up = True
            else:
                give_up = False

main()

