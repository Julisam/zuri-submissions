import random

options = {"R":"Rock", "P":"Paper", "S":"Scissors"}

def get_input():
    while True:
        usr_input = input('Pick an option between "R", "P" or "S":   ')
        if usr_input.upper() in options:
            return usr_input.upper()


def CPU_choice():
    return random.choice(list(options.keys())).upper()

def print_moves(user, cpu):
    print(f"Player {options[user]} : CPU {options[cpu]}")
    
    
def check_moves(user, cpu):
    if user == cpu:
        print("It's a tie: Starting over...")
        main()
    else:
        if user=='R':
            if cpu=='P':
                print("CPU wins!")
            else:
                print("You win!")
        
        elif user=='P':
            if cpu=='S':
                print("CPU wins!")
            else:
                print("You win!")        
        elif user=="S":
            if cpu=='R':
                print("CPU wins!")
            else:
                print("You win!")        
        else:
            print("Error!!!")

def main():
    user = get_input()
    cpu  = CPU_choice()
    print_moves(user, cpu)
    check_moves(user, cpu)
    
if __name__ == "__main__":
    print("Welcome to the game!!!")
    print("Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.")
    main()