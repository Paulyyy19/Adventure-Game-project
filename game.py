import gamefunctions

def main():
    name = input("Enter your name, brave adventurer: ")
    print(f"Greetings, {name}!\n")

    gamefunctions.print_welcome

    input("Press Enter to visit the shop...\n")
    gamefunctions.print_shop_menu

    choice = input("\nDid you win your battle? (yes/no): ").strip().lower()
    if choice == "yes":
        gamefunctions.print_victory
    else:
        gamefunctions.print_game_over

if __name__ == "__main__":
    main()
