import random
import time
import sys
import os

# --- Game Constants ---
PLAYER_START_MONEY = 1000
CASINO_MIN_BET = 10
CASINO_MAX_BET = 500
INVENTORY_SIZE = 10
SHOP_ITEMS = [
    {"name": "Lucky Charm", "price": 200, "desc": "Slightly increases your luck in games."},
    {"name": "Energy Drink", "price": 50, "desc": "Restores energy for more actions."},
    {"name": "VIP Pass", "price": 500, "desc": "Unlocks high-stakes games."},
    {"name": "Mystery Box", "price": 150, "desc": "Contains a random item or cash."},
    {"name": "Dice Set", "price": 100, "desc": "Lets you play dice games at home."},
    {"name": "Stock Tips", "price": 300, "desc": "Improves your odds in the stock market."},
    {"name": "Lottery Ticket", "price": 20, "desc": "Chance to win big money."},
    {"name": "Snack", "price": 10, "desc": "Restores a little energy."},
    {"name": "Gadget", "price": 250, "desc": "Can be sold for a profit."},
    {"name": "Old Coin", "price": 75, "desc": "Collectors might pay more for this."}
]

# --- Utility Functions ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.01):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Enter a value between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

def press_enter():
    input("\nPress Enter to continue...")

# --- Player Class ---
class Player:
    def __init__(self, name):
        self.name = name
        self.money = PLAYER_START_MONEY
        self.energy = 100
        self.inventory = []
        self.luck = 0
        self.vip = False
        self.stock_tips = False
        self.day = 1
        self.stats = {
            "games_played": 0,
            "games_won": 0,
            "games_lost": 0,
            "money_earned": 0,
            "money_lost": 0,
            "items_bought": 0,
            "items_sold": 0,
            "lottery_wins": 0
        }

    def add_item(self, item):
        if len(self.inventory) < INVENTORY_SIZE:
            self.inventory.append(item)
            return True
        return False

    def remove_item(self, item_name):
        for i, item in enumerate(self.inventory):
            if item["name"] == item_name:
                del self.inventory[i]
                return True
        return False

    def has_item(self, item_name):
        return any(item["name"] == item_name for item in self.inventory)

    def adjust_luck(self, amount):
        self.luck += amount

    def adjust_energy(self, amount):
        self.energy = max(0, min(100, self.energy + amount))

    def adjust_money(self, amount):
        self.money += amount
        if amount > 0:
            self.stats["money_earned"] += amount
        else:
            self.stats["money_lost"] += -amount

    def next_day(self):
        self.day += 1
        self.energy = min(100, self.energy + 20)
        if self.has_item("Lucky Charm"):
            self.luck = min(10, self.luck + 1)
        else:
            self.luck = max(0, self.luck - 1)

# --- Casino Games ---
def casino_menu(player):
    while True:
        clear()
        print(f"--- Casino --- (Money: ${player.money}, Energy: {player.energy})")
        print("1. Slot Machine")
        print("2. Blackjack")
        print("3. Roulette")
        print("4. Dice Game")
        print("5. Leave Casino")
        choice = input("Choose a game: ")
        if choice == "1":
            slot_machine(player)
        elif choice == "2":
            blackjack(player)
        elif choice == "3":
            roulette(player)
        elif choice == "4":
            dice_game(player)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            press_enter()

def slot_machine(player):
    clear()
    print("--- Slot Machine ---")
    bet = input_int(f"Enter your bet (${CASINO_MIN_BET}-{CASINO_MAX_BET}): ", CASINO_MIN_BET, min(CASINO_MAX_BET, player.money))
    if player.energy < 5:
        print("You're too tired to play.")
        press_enter()
        return
    player.adjust_money(-bet)
    player.adjust_energy(-5)
    player.stats["games_played"] += 1
    symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
    result = [random.choice(symbols) for _ in range(3)]
    print("Spinning...")
    time.sleep(1)
    print(" | ".join(result))
    win = False
    if result.count(result[0]) == 3:
        win = True
        payout = bet * 10
    elif result.count(result[0]) == 2 or result.count(result[1]) == 2:
        win = True
        payout = bet * 2
    else:
        payout = 0
    if win:
        print(f"You win ${payout}!")
        player.adjust_money(payout)
        player.stats["games_won"] += 1
    else:
        print("You lose.")
        player.stats["games_lost"] += 1
    press_enter()

def blackjack(player):
    clear()
    print("--- Blackjack ---")
    bet = input_int(f"Enter your bet (${CASINO_MIN_BET}-{CASINO_MAX_BET}): ", CASINO_MIN_BET, min(CASINO_MAX_BET, player.money))
    if player.energy < 10:
        print("You're too tired to play.")
        press_enter()
        return
    player.adjust_money(-bet)
    player.adjust_energy(-10)
    player.stats["games_played"] += 1

    def draw_card():
        return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    def hand_value(hand):
        value = sum(hand)
        aces = hand.count(11)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    while True:
        print(f"Your hand: {player_hand} (Total: {hand_value(player_hand)})")
        print(f"Dealer shows: {dealer_hand[0]}")
        if hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            player.adjust_money(int(bet * 2.5))
            player.stats["games_won"] += 1
            press_enter()
            return
        move = input("Hit or Stand? (h/s): ").lower()
        if move == "h":
            player_hand.append(draw_card())
            if hand_value(player_hand) > 21:
                print(f"Busted! Your hand: {player_hand} (Total: {hand_value(player_hand)})")
                player.stats["games_lost"] += 1
                press_enter()
                return
        elif move == "s":
            break
        else:
            print("Invalid input.")

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())
    print(f"Dealer's hand: {dealer_hand} (Total: {hand_value(dealer_hand)})")
    if hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
        print("You win!")
        player.adjust_money(bet * 2)
        player.stats["games_won"] += 1
    elif hand_value(player_hand) == hand_value(dealer_hand):
        print("Push. You get your bet back.")
        player.adjust_money(bet)
    else:
        print("You lose.")
        player.stats["games_lost"] += 1
    press_enter()

def roulette(player):
    clear()
    print("--- Roulette ---")
    bet = input_int(f"Enter your bet (${CASINO_MIN_BET}-{CASINO_MAX_BET}): ", CASINO_MIN_BET, min(CASINO_MAX_BET, player.money))
    if player.energy < 8:
        print("You're too tired to play.")
        press_enter()
        return
    player.adjust_money(-bet)
    player.adjust_energy(-8)
    player.stats["games_played"] += 1
    print("Bet on:")
    print("1. Red (pays 2x)")
    print("2. Black (pays 2x)")
    print("3. Number (0-36, pays 36x)")
    choice = input("Your bet: ")
    if choice == "1":
        color = "red"
    elif choice == "2":
        color = "black"
    elif choice == "3":
        number = input_int("Pick a number (0-36): ", 0, 36)
        color = None
    else:
        print("Invalid choice.")
        press_enter()
        return
    print("Spinning the wheel...")
    time.sleep(2)
    result = random.randint(0, 36)
    result_color = "red" if result % 2 == 1 else "black"
    print(f"The ball lands on {result} ({result_color})!")
    win = False
    if color:
        if result != 0 and result_color == color:
            win = True
            payout = bet * 2
    else:
        if result == number:
            win = True
            payout = bet * 36
    if win:
        print(f"You win ${payout}!")
        player.adjust_money(payout)
        player.stats["games_won"] += 1
    else:
        print("You lose.")
        player.stats["games_lost"] += 1
    press_enter()

def dice_game(player):
    clear()
    print("--- Dice Game ---")
    bet = input_int(f"Enter your bet (${CASINO_MIN_BET}-{CASINO_MAX_BET}): ", CASINO_MIN_BET, min(CASINO_MAX_BET, player.money))
    if player.energy < 5:
        print("You're too tired to play.")
        press_enter()
        return
    player.adjust_money(-bet)
    player.adjust_energy(-5)
    player.stats["games_played"] += 1
    print("Guess the sum of two dice (2-12).")
    guess = input_int("Your guess: ", 2, 12)
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    print(f"Dice rolled: {d1} + {d2} = {d1 + d2}")
    if guess == d1 + d2:
        payout = bet * 10
        print(f"Correct! You win ${payout}!")
        player.adjust_money(payout)
        player.stats["games_won"] += 1
    else:
        print("Wrong guess. You lose.")
        player.stats["games_lost"] += 1
    press_enter()

# --- Shop ---
def shop_menu(player):
    while True:
        clear()
        print(f"--- Shop --- (Money: ${player.money})")
        for idx, item in enumerate(SHOP_ITEMS):
            print(f"{idx+1}. {item['name']} - ${item['price']} ({item['desc']})")
        print(f"{len(SHOP_ITEMS)+1}. Sell Item")
        print(f"{len(SHOP_ITEMS)+2}. Leave Shop")
        choice = input("Choose an option: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(SHOP_ITEMS):
                item = SHOP_ITEMS[choice-1]
                if player.money >= item["price"]:
                    if player.add_item(item):
                        player.adjust_money(-item["price"])
                        player.stats["items_bought"] += 1
                        print(f"Bought {item['name']}.")
                        if item["name"] == "Lucky Charm":
                            player.adjust_luck(2)
                        elif item["name"] == "Energy Drink":
                            player.adjust_energy(30)
                        elif item["name"] == "VIP Pass":
                            player.vip = True
                        elif item["name"] == "Stock Tips":
                            player.stock_tips = True
                        elif item["name"] == "Snack":
                            player.adjust_energy(10)
                        elif item["name"] == "Lottery Ticket":
                            lottery(player)
                        elif item["name"] == "Mystery Box":
                            mystery_box(player)
                    else:
                        print("Inventory full!")
                else:
                    print("Not enough money.")
                press_enter()
            elif choice == len(SHOP_ITEMS)+1:
                sell_item(player)
            elif choice == len(SHOP_ITEMS)+2:
                break
            else:
                print("Invalid choice.")
                press_enter()
        else:
            print("Invalid input.")
            press_enter()

def sell_item(player):
    if not player.inventory:
        print("You have nothing to sell.")
        press_enter()
        return
    print("Your inventory:")
    for idx, item in enumerate(player.inventory):
        print(f"{idx+1}. {item['name']} ({item['desc']})")
    choice = input_int("Select item to sell (0 to cancel): ", 0, len(player.inventory))
    if choice == 0:
        return
    item = player.inventory[choice-1]
    sell_price = int(item["price"] * random.uniform(0.5, 1.5))
    print(f"Sold {item['name']} for ${sell_price}.")
    player.adjust_money(sell_price)
    player.remove_item(item["name"])
    player.stats["items_sold"] += 1
    press_enter()

def lottery(player):
    print("Scratching lottery ticket...")
    time.sleep(1)
    win = random.choices([True, False], weights=[1, 19])[0]
    if win:
        prize = random.randint(100, 1000)
        print(f"You win ${prize}!")
        player.adjust_money(prize)
        player.stats["lottery_wins"] += 1
    else:
        print("No win this time.")
    press_enter()

def mystery_box(player):
    print("Opening mystery box...")
    time.sleep(1)
    if random.random() < 0.5:
        cash = random.randint(50, 300)
        print(f"You found ${cash} inside!")
        player.adjust_money(cash)
    else:
        item = random.choice(SHOP_ITEMS)
        print(f"You found a {item['name']}!")
        player.add_item(item)
    press_enter()

# --- Stock Market ---
def stock_market(player):
    clear()
    print("--- Stock Market ---")
    stocks = [
        {"name": "TechCorp", "price": random.randint(50, 200)},
        {"name": "GreenEnergy", "price": random.randint(30, 150)},
        {"name": "Foodies", "price": random.randint(20, 100)},
        {"name": "CryptoX", "price": random.randint(10, 500)}
    ]
    print("Today's stocks:")
    for idx, stock in enumerate(stocks):
        print(f"{idx+1}. {stock['name']} - ${stock['price']}")
    print("You can buy or sell stocks (simulated).")
    choice = input("Buy (b), Sell (s), or Leave (l): ").lower()
    if choice == "b":
        idx = input_int("Which stock to buy? (1-4): ", 1, 4) - 1
        amount = input_int("How many shares? ", 1)
        cost = stocks[idx]["price"] * amount
        if player.money >= cost:
            print(f"Bought {amount} shares of {stocks[idx]['name']} for ${cost}.")
            player.adjust_money(-cost)
            # Simulate profit/loss
            if player.stock_tips:
                profit = int(cost * random.uniform(0.05, 0.25))
            else:
                profit = int(cost * random.uniform(-0.2, 0.2))
            print("Waiting for market movement...")
            time.sleep(2)
            if profit >= 0:
                print(f"You made a profit of ${profit}!")
                player.adjust_money(profit)
            else:
                print(f"You lost ${-profit}.")
                player.adjust_money(profit)
        else:
            print("Not enough money.")
        press_enter()
    elif choice == "s":
        print("You don't own any stocks yet. (Feature coming soon!)")
        press_enter()
    else:
        return

# --- Home Activities ---
def home_menu(player):
    while True:
        clear()
        print(f"--- Home --- (Energy: {player.energy})")
        print("1. Rest (restore energy)")
        print("2. Play Dice Game (if you own Dice Set)")
        print("3. View Inventory")
        print("4. Leave Home")
        choice = input("Choose an option: ")
        if choice == "1":
            print("Resting...")
            time.sleep(1)
            player.adjust_energy(50)
            print("Energy restored.")
            press_enter()
        elif choice == "2":
            if player.has_item("Dice Set"):
                dice_game(player)
            else:
                print("You need a Dice Set to play at home.")
                press_enter()
        elif choice == "3":
            view_inventory(player)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            press_enter()

def view_inventory(player):
    print("Your inventory:")
    if not player.inventory:
        print("Empty.")
    else:
        for item in player.inventory:
            print(f"- {item['name']}: {item['desc']}")
    press_enter()

# --- Main Game Loop ---
def main_menu(player):
    while True:
        clear()
        print(f"Day {player.day} | {player.name} | Money: ${player.money} | Energy: {player.energy}")
        print("1. Go to Casino")
        print("2. Visit Shop")
        print("3. Go Home")
        print("4. Stock Market")
        print("5. View Stats")
        print("6. Next Day")
        print("7. Quit Game")
        choice = input("Choose an action: ")
        if choice == "1":
            casino_menu(player)
        elif choice == "2":
            shop_menu(player)
        elif choice == "3":
            home_menu(player)
        elif choice == "4":
            stock_market(player)
        elif choice == "5":
            show_stats(player)
        elif choice == "6":
            player.next_day()
            print("A new day begins...")
            press_enter()
        elif choice == "7":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid choice.")
            press_enter()

def show_stats(player):
    clear()
    print("--- Player Stats ---")
    for k, v in player.stats.items():
        print(f"{k.replace('_', ' ').title()}: {v}")
    print(f"VIP: {'Yes' if player.vip else 'No'}")
    print(f"Luck: {player.luck}")
    print(f"Stock Tips: {'Yes' if player.stock_tips else 'No'}")
    press_enter()

def intro():
    clear()
    slow_print("Welcome to Console Tycoon: Casino Edition!")
    name = input("Enter your name: ")
    player = Player(name)
    return player

if __name__ == "__main__":
    player = intro()
    main_menu(player)