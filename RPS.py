from random import randint

print("Welcome to the noob RPS game")
try:
    userChoice = input("Choose rock (r) paper (p) or scissors (s): ")
except:
    print("an error has occurred")


def c_choice():
    ray = ["r", "p", "s"]
    return ray[randint(0, 2)]

'''
rock wins scissors  paper wins rock       scissors wins paper
rock ties rock      paper ties paper      scissors ties scissors
rock loses paper    paper loses scissors  scissors loses rock
'''


def game(choice):
    cc = c_choice()
    print(cc)
    if cc == choice:
        print("computer also chose: " + cc + "!")
        print("It's a draw!")
    elif choice == ('r' or "rock"):
        if cc == 'p':
            print("computer chose: paper!")
            print("You lose :(")
        elif cc == 's':
            print("computer chose: rock!")
            print("You win!")
    elif choice == ('p' or "paper"):
        if cc == 'r':
            print("computer chose: rock!")
            print("You win!")
        elif cc == ('s' or "scissors"):
            print("computer chose: scissors!")
            print("You lose :(")
    elif choice == ('s' or "scissors"):
        if cc == ('r' or "rock"):
            print("computer chose: rock!")
            print("You lose :(")
        elif cc == ('p' or "paper"):
            print("computer chose: scissors!")
            print("You win!")
    else:
        print("Invalid choice mate! make sure to choose \'r\', \'p\' or \'s\' for your choice.")


for i in range(30):
    game(userChoice)


