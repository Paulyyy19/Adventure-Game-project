def purchase_item(item_price: int, starting_money: int, quantity_to_purchase: int) -> tuple[int, int]:
    total_cost = item_price * quantity_to_purchase
    if starting_money >= total_cost:
        remaining_money = starting_money - total_cost
        return quantity_to_purchase, remaining_money
    else:
        max_affortable = starting_money // item_price 
        remaining_money = starting_moeny - (item_price * max_affortable) 
        return max_affortable, remaing_money

def new_random_monster():
    name = random.choice(["Goblin", "Orc", "Wraith"])
    if name == "Goblin":
        health = random.randint(30, 50)
        power = random.randint(5, 10)
        money = random.randint(1, 5)
        description = "Sneaky small and fast be carful"
    elif name == "Orc":
        health = random.randint(60, 90)
        power = random.randint(10, 15)
        money = random.randunt(5, 10)
        description = "Strong and aggressive they will overpower you"
    elif name == "Wraith":
        health = random.randint(40, 70)
        power = randmom.randint(8,12)
        money = random.randint(10, 20)
        description = "Almost like a ghost but they are lot more aggressive"
    return {"name": name,
            "description": description,
            "helth": health,
            "power": power,
            "money": money
            }
def print_welcome(name: str, width: int):
    message = f"Welcome, {name}!"
    print(f'"{message.center(width)}"')
    
def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
   
    border = "+" + "-" * 23 + "+"
    line1 = f"{item1Name:<12}{'$'+format(item1Price, '.2f'):>8}"
    line2 = f"{item2Name:<12}{'$'+format(item2Price, '.2f'):>8}"

    print(border)
    print(f"|{line1}|")
    print(f"|{line2}|")
    print(border)

def test_functions():
    """Calls each function three times with different test cases (where applicable)."""
    print("Testing print_welcome():")
    print_welcome()
    print_welcome()
    print_welcome()

    print("\nTesting print_shop_menu():")
    print_shop_menu()
    print_shop_menu()
    print_shop_menu()

    print("\nTesting print_game_over():")
    print_game_over()
    print_game_over()
    print_game_over()

    print("\nTesting print_victory():")
    print_victory()
    print_victory()
    print_victory()

if __name__ == "__main__":
    test_functions()
