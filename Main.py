from CardGame import CardGame
from time import sleep

name_player1 = input("name of first player: ")  # Taking the names of the participants from the user and defining a new game
name_player2 = input("name of second player: ")
game = CardGame(name_player1, name_player2)
player1 = game.player1
player2 = game.player2

print()
print(player1)
print(player2)
sleep(2)

print("\nBeginning...")
sleep(5)

for i in range(10):  # Ten rounds where in each round both players throw a card
    print(f"\n{i+1}st turn")
    card1 = player1.get_card()
    card2 = player2.get_card()
    print(f"The cards drawn: {card1}, {card2}.\nThe winner:", end=" ")

    winner = player1  # The player with the highest card is the winner
    if card1 < card2:
        winner = player2
    winner.add_card(card1)  # The player who won the round collects the two cards
    winner.add_card(card2)
    print(winner.name)

    sleep(2)

print("\nThe winner of the game:\n" + str(game.get_winner()))  # The winner is the player with the highest number of cards
