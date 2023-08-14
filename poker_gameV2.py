import random
from poker import Card, Hand

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'value': value, 'suit': suit} for suit in suits for value in values]

# Function to evaluate the hand's rank
def evaluate_hand(hand):
    card_strings = [f"{card['value']}{card['suit'][0].lower()}" for card in hand]
    hand_string = " ".join(card_strings)
    return hand_string

# Function to simulate a single hand
def play_hand(num_players):
    random.shuffle(deck)
    player_hands = [deck[i:i+2] for i in range(0, num_players * 2, 2)]
    community_cards = deck[num_players * 2:num_players * 2 + 5]

    player_ranks = []

    for player_hand in player_hands:
        player_hand.extend(community_cards)
        player_hand.sort(key=lambda card: values.index(card['value']))

        # Get hand representation for evaluation
        hand_representation = evaluate_hand(player_hand)

        # Store the hand representation
        player_ranks.append(hand_representation)

    # Determine the winning hand(s) based on representations
    winning_representation = min(player_ranks)
    winning_players = [index + 1 for index, rep in enumerate(player_ranks) if rep == winning_representation]

    if len(winning_players) == 1:
        print(f"Player {winning_players[0]} wins with {winning_representation}!")
    else:
        print(f"It's a tie between players {', '.join(map(str, winning_players))} with {winning_representation}!")

# Get the number of players from the user
num_players = int(input("Enter the number of players: "))
play_hand(num_players)
