from random import randrange

def user_select():
    print("-------------------------" + '\n' + 
          "SELECT YOUR WEAPON (1-3)" + '\n' + 
          "-------------------------")
    print("1. Rock" + '\n' + "2. Paper" + '\n' + "3. Scissors")
    while (user_choice := int(input("Enter weapon choice (1/2/3): "))) not in (1,2,3):
        print("Please enter choice of '1', '2', or '3'")
    return user_choice


def opponent_select():
    opp_choice = randrange(1,4)
    print(f"Opponent's weapon choice: {opp_choice}")
    return opp_choice


def battle(user_weapon,opp_weapon):
    decision = user_weapon - opp_weapon
    weapons = {1:"rock",2:"paper",3:"scissors"}
    win = 'win'
    lose = 'lose'
    print('\n' + f"{f'You {win if decision in (1,-2) else lose}, {weapons[user_weapon] if decision in (1,-2) else weapons[opp_weapon]} beats {weapons[opp_weapon] if decision in (1,-2) else weapons[user_weapon]}!' if decision != 0 else 'You tied!'}")
        
        
def main():
    continue_option = "y"
    while continue_option == "y":
        user = user_select()
        opponent = opponent_select()
        battle(user, opponent)
        while (continue_option := input("Want to play again? (y/n): ").lower()) not in ("y","n"):
            print("Please input either 'y' or 'n'")
    print('\n' + "Thanks for playing!")
    
    
if __name__ == "__main__":
    main()

print("\n" +"Completed by, Jeremiah Vela")
