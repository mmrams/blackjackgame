# -*- coding: utf-8 -*-
"""Blackjack

This is a Blackjack game for 1 player. The player can either play normally or use
an automated card counting strategy where the programm decides if another card should 
be drawn or not and if the bet should be increased or not.

This is a project by Christoph Hirt, Manuel Ramsler, Thimo Hengartner, Luca Möhr
and Fortunat Ramming.

"""


import random  
import time


"""##Set up colors of game"""
class style():
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"


"""##Initialize the main menu

This is the starting interface. Here the player can select what strategy to play.
"""
# Visualize players cards
def Cards_Player(Player_Card, Player_Score):
    #check if both cards are equal to 10
    if (Player_Card[0][1]==str(10)) and (Player_Card[1][1] == str(10)):
        print(f"""Your current score is {Player_Score}, and your cards are:
           _____            _____
          |     |          |     |
          |  {Player_Card[0][0]}  |          |  {Player_Card[1][0]}  |
          |  {Player_Card[0][1]} |          |  {Player_Card[1][1]} |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")  
    #check if first card is equal to 10
    elif Player_Card[0][1] == str(10):
        print(f"""Your current score is {Player_Score}, and your cards are:
           _____            _____
          |     |          |     |
          |  {Player_Card[0][0]}  |          |  {Player_Card[1][0]}  |
          |  {Player_Card[0][1]} |          |  {Player_Card[1][1]}  |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")
    #check if second card is equal to 10
    elif Player_Card[1][1] == str(10):
        print(f"""Your current score is {Player_Score}, and your cards are:
           _____            _____
          |     |          |     |
          |  {Player_Card[0][0]}  |          |  {Player_Card[1][0]}  |
          |  {Player_Card[0][1]}  |          |  {Player_Card[1][1]} |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")
    #check if no card is equal to 10
    else:
        print(f"""Your current score is {Player_Score}, and your cards are:
           _____            _____
          |     |          |     |
          |  {Player_Card[0][0]}  |          |  {Player_Card[1][0]}  |
          |  {Player_Card[0][1]}  |          |  {Player_Card[1][1]}  |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")

# Visualize the dealers card
def Cards_Dealer(Dealer_Card):
    print(f"The Dealer's score is {cards_values[Dealer_Card[0][1]]} and his head-up card is:")
    # Check if the card is equal to 10
    if Dealer_Card[0][1] == str(10):
        print(f"""
            _____ 
           |     |
           |  {Dealer_Card[0][0]}  |  
           |  {Dealer_Card[0][1]} | 
           |     | 
            ¯¯¯¯¯¯""")
    else:
        print(f"""
            _____ 
           |     |
           |  {Dealer_Card[0][0]}  |  
           |  {Dealer_Card[0][1]}  | 
           |     | 
            ¯¯¯¯¯¯""")
# Visualize players card for every new card he draws
def Cards_Player_Round2(Player_Card, Player_Score):
    #check if card is equal to 10
    if Player_Card[1] == str(10):
        print(f"""Your new card is:
           _____         
          |     |        
          |  {Player_Card[0]}  | 
          |  {Player_Card[1]} |
          |     |         
           ¯¯¯¯¯¯""")
    else:
        print(f"""Your new card is:
           _____            
          |     |          
          |  {Player_Card[0]}  |          
          |  {Player_Card[1]}  |          
          |     |          
           ¯¯¯¯¯¯""")

# Visualise dealers head up and second card
def Cards_Dealer_ALL(Dealer_Card):
    #check if both cards are equal to 10
    if (Dealer_Card[0][1] == str(10)) and (Dealer_Card[1][1] == str(10)):
        print(f"""The Dealer's cards are:
           _____            _____
          |     |          |     |
          |  {Dealer_Card[0][0]}  |          |  {Dealer_Card[1][0]}  |
          |  {Dealer_Card[0][1]} |          |  {Dealer_Card[1][1]} |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""") 
    #check if first card is equal to 10
    elif Dealer_Card[0][1] == str(10):
        print(f"""The Dealer's cards are:
           _____            _____
          |     |          |     |
          |  {Dealer_Card[0][0]}  |          |  {Dealer_Card[1][0]}  |
          |  {Dealer_Card[0][1]} |          |  {Dealer_Card[1][1]}  |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")
    #check if second card is equal to 10
    elif Dealer_Card[1][1] == str(10):
        print(f"""The Dealer's cards are:
           _____            _____
          |     |          |     |
          |  {Dealer_Card[0][0]}  |          |  {Dealer_Card[1][0]}  |
          |  {Dealer_Card[0][1]}  |          |  {Dealer_Card[1][1]} |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")
    #check if no card is equal to 10
    else:
        print(f"""The Dealer's cards are:
           _____            _____
          |     |          |     |
          |  {Dealer_Card[0][0]}  |          |  {Dealer_Card[1][0]}  |
          |  {Dealer_Card[0][1]}  |          |  {Dealer_Card[1][1]}  |
          |     |          |     |
           ¯¯¯¯¯¯           ¯¯¯¯¯¯""")
# Visualise dealers card for every new card he draws
def Cards_Dealer_Round2(Dealer_Card):
    #check if card is equal to 10
    if Dealer_Card[1] == str(10):
        print(f"""The Dealer's new card is:
           _____         
          |     |        
          |  {Dealer_Card[0]}  | 
          |  {Dealer_Card[1]} |
          |     |         
           ¯¯¯¯¯¯""")
    else:
        print(f"""The Dealer's new card is:
           _____            
          |     |          
          |  {Dealer_Card[0]}  |          
          |  {Dealer_Card[1]}  |          
          |     |          
           ¯¯¯¯¯¯""")


#define a function for card counting
def CardCount(deck):
    # set initial value of the count variable
    count = 0
    # we count the cards in the deck
    for i in range(len(deck)):
        k = deck[i][2]
        # if the card has a value lower or equal than 6 we substract 1
        if k <= 6:
            count -= 1
        # if the card has a value higher or equal than 10 we add 1
        elif k >= 10:
            count += 1
    return count


#define a function for the main screen
def Menu_Screen():
  # clear the console
  #clear_console()
  # print the options to select from
  print("""Welcome to Blackjack! Please select what you would like to do by 
  inputting the corresponding number:
  [1] Play a game of Blackjack
  [2] Play a game of Blackjack with card counting
  [3] Print out Blackjack game rules""")
  # require an input
  menu_input = input()
  valid_inputs_menu = ["1", "2", "3"]
  # ask until the right input is provided
  while menu_input not in valid_inputs_menu:
    menu_input = input("Wrong input was given, please choose between 1, 2 or 3: ")
  # Start the game
  if menu_input == "1":
    Game()
  # Start BlackJack with Card Counting
  elif menu_input == "2":
    Game(cardcount = True)
  # Show the rules of BlackJack
  elif menu_input == "3":
    Rules_Menu()

"""##Set up a deck of Cards"""


cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
# set up a function for deck of cards
def CardDeck():
  # setup all possibe values cards can have
  suits = (f"{style.GREEN}♠{style.RESET}", f"{style.RED}♥{style.RESET}",
           f"{style.GREEN}♣{style.RESET}", f"{style.RED}♦{style.RESET}")
  cards = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

  # define the deck of cards
  deck = []
  #loop over all possibel combinations
  for suit in suits:
    for card in cards:
      deck.append((suit, card, cards_values[card]))
  
  deck *= 4
  # return the deck of cards
  return deck


"""##Setting Bets"""

# define a function for the bets
def Bet(money):
  # initialize the bet with a value above the amount of available chips
  bet = money + 1
  # ask for a bet until an affordable amount is entered
  while bet > money:
    print("Please set a bet you can afford")
    # check if the input is a number
    while True:
      try:
        bet = int(input())
      except ValueError:
        print("Please enter a positive Number being a multiple of 1")
      else:
        break
  # the function returns the bet
  return bet

"""## Initial amout of money"""

# define a function for the initial amount of money
def Money():
  print("How many chips do you own? ", end = "")
  # check if the input is a number
  while True:
    try:
        money = 0
        while money <= 0:
            print("Please enter a positive multiple of 1:")
            money = int(input())
    except ValueError:
        print("Please enter a positive Number being a multiple of 1")
    else:
        break
  # the function returns the intitial amount of chips
  return money

"""##First Option
The following cells define functions for the standard game (Option 1).
Set the first round cards for the player. This means the player gets 2 cards.
"""

# define a function for the first round
def FirstRound_Player(deck):
  # initialize the cards and scores of the player
  player_cards = []
  player_score = 0
  # get the deck of cards
  deck = deck

  # as long as the player has less than two cards draw form the deck
  while len(player_cards) < 2:
    # draw from the deck and add the card to the player
    player_card = random.choice(deck)
    player_cards.append((player_card[0], player_card[1]))
    # remove the card from the deck
    deck.remove(player_card)
    # increase the players score
    player_score += player_card[2]

  # note that by default the ace has value 11. Hence if two are drawn set one to 1
  if player_score == 22:
    player_score = 12  
  
  # the function returns the overal score of the player, his cards, and the new deck
  return player_score, player_cards, deck

"""Set the first round cards of the dealer"""

# define a function for the first round for the dealer
def FirstRound_Dealer(deck):
  # initialize the cards and scores of the player
  dealer_cards = []
  dealer_score = 0
  # make sure that the new deck is entered as the argument of the function
  deck = deck

  # as long as the dealer has less than two cards draw form the deck
  while len(dealer_cards) < 2:
    # draw from the deck and add the card to the dealer
    dealer_card = random.choice(deck)
    dealer_cards.append((dealer_card[0], dealer_card[1]))
    # remove the card from the deck
    deck.remove(dealer_card)
    # increase the dealer's score
    dealer_score += dealer_card[2]

  # note that by default the ace has value 11. Hence if two are drawn set one to 1
  if dealer_score == 22:
    dealer_score = 12
  
  # the function returns the overal score of the dealer, his cards, and the new deck
  return dealer_score, dealer_cards, deck

"""Second round for the player"""

# define a function for the second round of cards
def SecondRound_Player(deck, player_score, player_cards, auto_card, cardcount = False):
  # initialize the score and the cards by the values of the first round
  player_cards = player_cards
  player_score = player_score
  deck = deck
  # ask if the player wants a card until he does not want another card
  card = "NaN"
  while card.upper() != "STAND":
    # If the players count is 21 stop asking
    if player_score >= 21:
        #check if player draws exactly 21
        if player_score == 21:
            print("Your score is", player_score)
            break
        #check if player draws more than 21
        else:
            print("Too much!")
            break
    # Otherwise ask if he wants another card
    else:
      if cardcount is True:
          card = auto_card
      else:
          print("Do you want another card? Input HIT or STAND.")
          card = input()
      # if the player said HIT give him another card
      if card.upper() == "HIT":
        # draw from the deck and add the card to the player
        player_card = random.choice(deck)
        player_cards.append((player_card[0], player_card[1]))
        # remove the card from the deck
        deck.remove(player_card)
        # increase the players score
        player_score += player_card[2]
        # visualize the new card
        Cards_Player_Round2(player_card, player_score)
        if player_score != 21:
            print("Your score is", player_score)
      # for any other input just return the player score
      else:
        print("Your score is", player_score)
  
  # the function returns the overal score of the player, his cards, and the new deck
  return(player_score, player_cards, deck)

"""Second round for the dealer"""

# define a function for the second round of cards for the dealer
def SecondRound_Dealer(deck, dealer_score, dealer_cards):
  # initialize the score and the cards by the values of the first round
  dealer_cards = dealer_cards
  dealer_score = dealer_score
  deck = deck
  # visualize dealers cards
  time.sleep(0.5)
  Cards_Dealer_ALL(dealer_cards)
  # check the hand of the dealer if his score is 16 or less he must hit
  print("The dealers score is is now", dealer_score, ".")
  while dealer_score < 17:
    time.sleep(0.5)
    print("He must HIT")
    time.sleep(0.5)
    # draw from the deck and add the card to the dealer
    dealer_card = random.choice(deck)
    dealer_cards.append((dealer_card[0], dealer_card[1]))
    # remove the card from the deck
    deck.remove(dealer_card)
    # visualize new cards dealer draws
    Cards_Dealer_Round2(dealer_card)
    # increase the dealers score
    dealer_score += dealer_card[2]
    time.sleep(0.5)
    print("The dealers score is is now", dealer_score, ".")
    time.sleep(0.5)
  # otherwise he must stand
  if dealer_score >16:
    time.sleep(0.5)  
    print("He must STAND")
    time.sleep(0.5)

  # the function returns the overal score of the dealer, his cards, and the new deck
  return(dealer_score, dealer_cards, deck)

"""Play BlackJack"""

# define the main game
def BlackJack(money, deck, count, cardcount = False, countbet = 0):
  # player sets his bet, 
  if cardcount is False:
      bet = Bet(money)
  else:
      bet = countbet

  # play the first round of the player
  Player_Score, Player_Card, deck = FirstRound_Player(deck)
  # visualize players initial two cards
  Cards_Player(Player_Card, Player_Score)
  # Check if player has BlackJack
  if Player_Score == 21:
    print("Winner winner chicken dinner! You won", bet,".")
    money += bet
    print("You now have ", money, "chips.")
  
  else:
    # play the first round for the dealer
    Dealer_Score, Dealer_Card, deck = FirstRound_Dealer(deck)
    # visualize dealers head up card
    Cards_Dealer(Dealer_Card)

    # play the second round
    # If card count is true, we have to check the value of the count variable
    if cardcount is True:
        if count > 7:
            # For count > 7, the player stands when his score is higher than 11
            if Player_Score > 11:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                     auto_card = "STAND", cardcount=True)
            # For count > 7, the player hits when his score is 11 or lower
            else:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                 auto_card = "HIT", cardcount=True)
        if count < -7:
            # For couunt < -7, the player stands when his score is higher than 17
            if Player_Score > 17:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                     auto_card = "STAND", cardcount=True)
            # For count < -7, the player hits when his score is 17 or lower
            else:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                 auto_card = "HIT", cardcount=True)
        else:
            # for -7 < count < 7, the player stands when his score is higher than 14
            if Player_Score > 14:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                     auto_card = "STAND", cardcount=True)
            # for -7 < count < 7, the player hits when his score is lower or equal to 14
            else:
                Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                                 auto_card = "HIT", cardcount=True)
        print("The current card-count index is", count, ".")
    else:
        # If the card counting mode is not active, the second round is normally played
        Player_Score, Player_Card, deck = SecondRound_Player(deck, Player_Score, Player_Card,
                                                             auto_card = "NaN", cardcount=False)
    # check winning condition
    if Player_Score == 21:
      print("Winner winner chicken dinner! You won", bet,".")
      # increase his amount of chips
      money += bet
      print("You now have ", money, "chips.")
    # check lossing condition
    elif Player_Score > 21:
      # reduce his chips by the amount bet
      money -= bet
      print("You lost ", bet, ". You now own ", money, "chips.")
    # if the player is still in the game check all possible winning conditions
    if Player_Score < 21:
      # if the player is still in the game also the dealer plays the second round
      Dealer_Score, Dealer_Card, deck = SecondRound_Dealer(deck, Dealer_Score, Dealer_Card)
      # check if dealer lost
      if Dealer_Score > 21:
        # in this case the player wins
        print("You won", bet,".")
        # increase his amout of chips
        money += bet
        print("You now have ", money, "chips.")
      # check if the player wins
      elif Player_Score > Dealer_Score:
        print("You won", bet,".")
        # add the bet to his chips
        money += bet
        print("You now have ", money, "chips.")
      # check if the dealers and the players scores are equal
      elif Player_Score == Dealer_Score:
        print("It is a draw. You get your money back.") 
        print("You now have ", money, "chips.")
      # otherwise the player loses
      else:
        # reduce his chips
        money -= bet
        print("You lost ", bet, ". You now own ", money, "chips.")
  # the function then returns the new stock of chips
  return money, deck


"""##Third Option

The third option is to call the rules of the game. After reading it one can return to the main menu.
"""

# define a function printing the rules of the game
def Rules_Menu():
  print("""The rules of Blackjack are simple.

  At the beginning of each round, all players place their bets in their betting  
  positions - also known as ‘boxes’. After the bets have been placed,  
  all players are dealt two cards face-up in front of their respective betting  
  positions. The dealer receives two cards, one face-up and another face-down.
  
  Starting to the left of the dealer, each player is given a chance to draw 
  more cards. The players can either ‘hit’ or ‘stand’. If the player calls 
  out ‘HIT’, they are given an extra card. They can then either call out 
  ‘HIT’ again, or ‘STAND’ if they do not wish to draw any more cards. The 
  player can ‘HIT’ as many times as they wish, but have to aim not to 
  ‘bust’ (exceed a total of 21).

  If the player busts, they immediately lose their bet.

  After each player has played and either stood or busted, the dealer takes 
  their turn. They can, again, either ‘HIT’ or ‘STAND’. If the dealer’s hand 
  exceeds 21, all players who didn't bust win immediately - their bet is 
  returned along with a matching amount from the dealer's bank.
  If the dealer reaches a valid hand, the cards are totalled and each player’s 
  hand is compared to the dealer’s. If the player scored higher than the 
  dealer, they win. If the player ties with the dealer, the original bet is 
  returned to the player. Otherwise, the player loses their bet.

  A perfect hand combines an ace with a 10, Jack, Queen or King and is known 
  as a ‘Blackjack’.
  
  Instructions from mastersofgames.com

  The size of the deck in this game is 52 cards.
  
  If you would like to improve your odds, select the game with card counting 
  which will help you play the best moves \n """)
  
  # return to the main screen
  Menu_Screen()

"""##The Game
This is te function iterating over the single games and counting the stock of chips.
"""

# define a function for the overall game
def Game(cardcount = False):
  # Ask how much money the player has
  money = Money()
  deck = CardDeck()

  # set an intitial value for the loop
  play = "YES"
  # ask if the player wants to play or not
  while play.upper() != "NO":
    if len(deck)<10:
        deck = CardDeck()
        count = 0
    # check that the player has enough money
    if money == 0:
      print("I am sorry, but you run out of money!")
      break
    # if he has enough money ask if he wants to play
    else:
      print("Do you want to play BlackJack? Please enter YES or NO")
      play = input()
      # If he does not want to play end the game
      if play.upper() == "NO":
        print("Ok, good bye!")
        break
      # If he wants to play start the game
      elif play.upper() == "YES":
          # If we are in the cardcounting mode, we count the cards in the deck
          if cardcount is True:
              count = CardCount(deck)
              # If the count variable is greater than 7 or smaller than -7, a higher bet than normal is placed
              if abs(count) > 7:
                  money, deck = BlackJack(money, deck, count, cardcount = True, countbet = int(money/4))
              # If the count variable is between -7 and 7, the bet is equal to 1
              else:
                  money, deck = BlackJack(money, deck, count, cardcount = True, countbet = 1)
          # If we are not in the cardcounting mode, the game is normally initialized.
          else:
              money, deck = BlackJack(money, deck, CardCount(deck))
      # If neither yes nor no is entered, this message appears.         
      else:
        print("Please tell us what you want.")

"""## The main script to run the code
Here the game is played
"""

# start BlackJack
Menu_Screen()


