import os, random

def menu():
    choice = input("""
~~~MAKE YOUR CHOICE~~~

1.Login
2.Sign Up
3.Exit

""")
    
    if choice == "1" or choice == "Login":
        Login()
    elif choice == "2" or choice == "Sign Up":
        Sign_Up()
    elif choice == "3" or choice == "Exit":
       os. _exit(1)
        

def Login():
    name = input("Username: ")
    myFile = open("Usernames.txt", "r")
    for i in myFile:
        text = myFile.readline()
    if name in text:
        print("~~~Username accepted~~~")
        for i in range(0, 3):
            password = input("Password: ")
            myFile2 = open("Passwords.txt", "r")
            for i in myFile2:
                text2 = myFile2.readline()
            if password in text2:
                print("~~~Password accepted~~~")
                print("~~~Login successful~~~")
                Im_A_God_Of_Coding()
        else:
            print("~~~Password not in database, please sign up~~~")
            menu()
    else:
        print("~~~Username not in database, please sign up~~~")
        menu()
        
def Sign_Up():
    Username = input("Enter username: ")
    myFile = open("Usernames.txt", "a")
    myFile.write("\n" + Username)
    myFile.close()

    Password= input("Enter password: ")
    myFile = open("Passwords.txt", "a")
    myFile.write("\n" + Password)
    myFile.close()
    menu()

def Im_A_God_Of_Coding():
    choice = input("""
~~~Make your choice~~~
1.Start program
2.Leave
""")

    if choice == "1":
        game()
    elif choice == "2":
        os.exit(1)
    elif choice == "roulette":
        Roulette()


def FltCheck(BetAmount):
    try:
        float(BetAmount)
        return True
    except ValueError:
        return False

def Roulette():
    Money=1000
    Hack=False
    Wins=0
    while True:
        Hack=False
        ValidAnswer=False
        while ValidAnswer==False:
            print(" You have £",Money)
            BetAmount=input("How much would you like to bet?")
            if BetAmount.isdigit()==False and FltCheck(BetAmount)==False:
                print("Error, please try again")
            else:
                BetAmount=float(BetAmount)
                if BetAmount>Money or BetAmount<0:
                    print("Error, please try again")
                else:
                    ValidAnswer=True
        ValidAnswer=False
        while ValidAnswer==False:
            Bet=input("Red or black").title()
            if Bet!="Red" and Bet!="Black" and Bet!="Red " and Bet!="Black ":
                print("Error, please try again")
            else:
                if Bet.strip()!=Bet:
                    Hack=True
                ValidAnswer=True
                print("You are betting £",BetAmount,"on",Bet)
        Res=random.randint(0,1)
        if Res==0:
            print("""
It landed on...
...Red!
""")
        else:
            print("""
It landed on...
...Black!
""")
        if Hack==False:
            if Res==1 and Bet=="Black":
                print("You Win!")
                Money=Money+BetAmount
                Wins=Wins+1
            elif Res==0 and Bet=="Red":
                print("You Win!")
                Money=Money+BetAmount
                Wins=Wins+1
            else:
                print("You Lose!")
                Money=Money-BetAmount
        else:
            print("You Win!")
            Money=Money+BetAmount
        if Money<=0:
            print("You're out of money. Leave")
            menu()
        if Wins>=10:
            print("You are banned out the casino for cheating. Be ashamed of yourself. Now leave before we call the bouncer")
            menu()


# user chooses number of decks of cards to use
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# initialize scores
wins = 0
losses = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

   
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        # score function now updates to global win/loss variables
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry. You busted. You lose.\n")
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Dealer busts. You win!\n")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Congratulations. Your score is higher than the dealer. You win\n")
            wins += 1

def game():
    global wins
    global losses
    choice = 0
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("The dealer is showing a " + str(dealer_hand[0]))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('You busted')
                losses += 1
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    wins += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            quit=True
            exit()


if __name__ == "__main__":
    menu()
