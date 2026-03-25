import os
import random

# ===== GLOBALS =====
Money = 1000
Wins = 0
Losses = 0

# ===== UTIL =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def FltCheck(value):
    try:
        float(value)
        return True
    except:
        return False

# ===== MENU =====
def menu():
    while True:
        choice = input("""
~~~ MAKE YOUR CHOICE ~~~

1. Roulette
2. Blackjack
3. Slot Machine
4. Exit

> """).lower().strip()

        if choice in ["1", "roulette"]:
            Roulette()
        elif choice in ["2", "blackjack"]:
            game()
        elif choice in ["3", "slot machine"]:
            Slot_Machine()
        elif choice in ["4", "exit"]:
            print("Goodbye!")
            exit()
        elif choice in ["big boss"]:
            Big_Boss()
        else:
            print("Invalid choice.")

# ===== ROULETTE =====
def Roulette():
    global Money, Wins, Losses

    print("\n--- ROULETTE ---")

    # Get bet
    while True:
        print(f"You have £{Money}")
        bet = input("Bet amount: ")

        if not FltCheck(bet):
            print("Invalid number.")
            continue

        bet = float(bet)

        if bet <= 0 or bet > Money:
            print("Invalid bet.")
        else:
            break

    # Get color
    while True:
        choice = input("Red or Black: ").strip().title()
        if choice in ["Red", "Black"]:
            break
        print("Invalid choice.")

    # Spin
    result = random.choice(["Red", "Black"])
    print(f"\nIt landed on... {result}!")

    # Result
    if choice == result:
        print("You win!")
        Money += bet
        Wins += 1
    else:
        print("You lose!")
        Money -= bet
        Losses += 1

    check_status()

# ===== BLACKJACK HELPERS =====
def create_deck():
    return [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

def deal(deck):
    return [deck.pop(), deck.pop()]

def total(hand):
    total = sum(hand)
    aces = hand.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def hit(deck, hand):
    hand.append(deck.pop())

# ===== BLACKJACK GAME =====
def game():
    global Money, Wins, Losses

    clear()
    print("\n--- BLACKJACK ---")

    # Bet
    while True:
        print(f"You have £{Money}")
        bet = input("Bet amount: ")

        if not FltCheck(bet):
            print("Invalid number.")
            continue

        bet = float(bet)

        if bet <= 0 or bet > Money:
            print("Invalid bet.")
        else:
            break

    deck = create_deck()
    random.shuffle(deck)

    player = deal(deck)
    dealer = deal(deck)

    # Player turn
    while True:
        print(f"\nDealer shows: {dealer[0]}")
        print(f"Your hand: {player} (Total: {total(player)})")

        if total(player) == 21:
            print("Blackjack! You win!")
            Money += bet
            Wins += 1
            return check_status()

        if total(player) > 21:
            print("You busted!")
            Money -= bet
            Losses += 1
            return check_status()

        choice = input("[H]it or [S]tand: ").lower()

        if choice == "h":
            hit(deck, player)
        elif choice == "s":
            break
        else:
            print("Invalid choice.")

    # Dealer turn
    while total(dealer) < 17:
        hit(deck, dealer)

    print(f"\nDealer hand: {dealer} (Total: {total(dealer)})")
    print(f"Your hand: {player} (Total: {total(player)})")

    # Result
    if total(dealer) > 21 or total(player) > total(dealer):
        print("You win!")
        Money += bet
        Wins += 1
    elif total(player) < total(dealer):
        print("You lose!")
        Money -= bet
        Losses += 1
    else:
        print("It's a draw.")

    check_status()

# ===== Slot Machine =====
def Slot_Machine():
    global Money, Wins, Losses

    clear()
    print("\n--- SLOT MACHINE ---")

    # Bet
    while True:
        print(f"You have £{Money}")
        bet = input("Bet amount: ")

        if not FltCheck(bet):
            print("Invalid number.")
            continue

        bet = float(bet)

        if bet <= 0 or bet > Money:
            print("Invalid bet.")
        else:
            break
    num1 = [random.randint(1, 20)]
    num2 = [random.randint(1, 20)]
    num3 = [random.randint(1, 20)]
    num4 = [random.randint(1, 20)]
    print(num1, num2, num3, num4)
    if num1 == num2 and num1 == num3 and num1 == num4:
        print("You win!")
        Money += bet*5
        Wins += 1
        
    else:
        print("You lose!")
        Money -= bet
        Losses += 1

    check_status()
# ===== STATUS =====
def check_status():
    global Money

    print(f"\nMoney: £{Money}")

    if Money <= 0:
        print("You're out of money!")
        exit()

# ===== Big Boss =====
def Big_Boss():
    global Money
    Money = 1000000000
    print("Welcome Big Boss")
    menu()
    
# ===== START =====
if __name__ == "__main__":
    menu()
