#PHASE 1
#** What classes should be be made?**
    #If it was for a website with multiple card games, I would probably need to
    #create multiple classes for "Deck", "Shuffle", "Deal", and "Player".
    #But in this case, for a singular game, I'll make it simpler by only having the 
    #game as a class itself with the "Deck", "Shuffle", "Deal" as functions and/or
    #lists/dictionaries


#Build players
    #Variables representing players that contain their hands as dictionaries 
        # Player1 = {a:b, c:d, e:f ...}
        # Player2 = {a:b, c:d, e:f ...}
        # Player3 = {a:b, c:d, e:f ...}
        # Player4 = {a:b, c:d, e:f ...}
    #Access "hand" by calling the variables directly
    #Returns a dictionary containing cards in hand {suit:value}

    #AND
    #Have a list containing all the players as variables
        # Players = [Player1, Player2, Player3, Player4]
    #Access "hand" by Players[Num] which contains the dict hand {suit:value}

    #OR
    #A dicionary with values as a list
    #A Dictionary of player:values(Suit:Numberpairs)
            #Players = {Player1:[hand], 
            #           Player2:[hand], 
            #           Player3:[hand], 
            #           Player4:[hand]
            #           }
    #Access "hand" by calling the key "PlayerNum.values"
    #Returns a list containing the cards in hand

    #OR
    #A dictionary of dictionaries
    #       Players = { player1 : {hand}, 
    #                   player2 : {hand}, 
    #                   player3 : {hand}, 
    #                   player4 : {hand},
    #                   }
    #Access "hand" by calling the key "PlayerNum.values"
    #Returns a dictionary containing cards in hand

#Build Deck Function
#Build a dictionary called "Deck" that contains all the "suit" / "number" pairs.
    #**How to build this dictionary?**
        #Option 1
        # - Hardcode the dictionary
        
        #Option 2
        # - Combine two lists to a dictionary
        # - A numbers list from 1 to 13
        # - A card_suit list of the 4 suits
        # - Deck is a dictionary of suit:number pairs?

#Shuffle Deck Function
        # - Shuffle the dictionary
        # - Fetch all keys from a dictionary as a list
        # - shuffle that list and access dictionary values using shuffled keys

#Build hands Function
        # - Each hand should be a dictionary?
        # - Place Cards (suit:number) from shuffled deck dictionary to player hands
        
        #** How would the cards be placed into each players hand?**
        # - It depends on the data structure of the players and player's hand

#Build players
#Creates a class of players
#Initializes the player variables and their empty hand
class players():
    def __init__(self):
        self.player_1 = []
        self.player_2 = []
        self.player_3 = []
        self.player_4 = []
        self.players = [self.player_1, self.player_2, self.player_3, self.player_4]

#Build deck function
#A function to make a list of a full deck of cards with suit/number pairs in individual dicts
#Should return a list to whatever called it. 
    def make_deck(self):
        deck = []
        suits = ["♦", "♣", "♥", "♠"]
        for suit in suits:
            for num in range(1,14):
                deck.append({suit:num})
        return deck

#Shuffle Deck function
#A function that calls upon the make_deck() function to retrieve a deck of cards and then shuffle it
#Should return a shuffled list to whatever called it. 
    def shuffle_deck(self):
        import random
        deck = self.make_deck()
        random.shuffle(deck)
        return(deck)

#Build Hand Function
#A function that distributes the items in list from shuffle_deck()func to players
#Players should have a list of 13 dicts of key:value pairs. 

    def distribute_hand(self):
        shuffled_deck = self.shuffle_deck()
        #print(shuffled_deck[0])
        for player in self.players:
            for i in range(0,13):
                player.append(shuffled_deck[0])
                del shuffled_deck[0]
            

game_start = players()
game_start.distribute_hand()
print("Player 1's hand")
print(game_start.player_1) 
print("Player 2's hand")
print(game_start.player_2)
print("Player 3's hand")
print(game_start.player_3)
print("Player 4's hand")
print(game_start.player_4)




#PHASE 2
#PLAYING CARDS FROM HAND
#Remember all the cards are stored as instance variables so will need to be called from the class

"""
print("Choose a suit")
player_suit = input()

for cards in game_start.player_1:
    if '♣' in cards.keys():
        print("Has suit")
"""

#Some code to display suit choices to user
suits = ["♦", "♣", "♥", "♠"]
print("Choose a suit (type a number)")
for count, suit in enumerate(suits):
    print(f"{count+1}) {suit}")

#Player inputs their choice of suit
player_suit_choice = input()

#Prompt user for number choice
print("Pick a number between 1 and 13 (type a number)")
player_number_choice = input()

#Shows player's suit and number choice after selection
print(f" You chose {suits[int(player_suit_choice)-1]} : {player_number_choice}")


#Player Choose Card
    #A prompt from the terminal asking player to choose suit 
    #From a list!!
        #If suit exists in hand
            #Display cards with only that suit
        #Else
            #print "You don't have that suit in hand"
            #Start suit_choice prompt again
    #A prompt for the terminal asking player to choose a number
        #If number in temp list
            #Display the suit:number card
            #Ask if user wishes to play that card
                #Add chosen card to current round list
            #Else start from beginning
        #Else:
            #Print "You don't have that number in hand"
            #Start from choosing number again. 

        #Remove card from players hand

#Bot play card
    #FOR NOW - just remove first card from hand to test if can add to current round list

#Collecting all the played cards in a list forming the "trick" of the round
    #Maybe call this list "cards_played"



#PHASE 3
#BASIC RULES
#Probably will need a function called play_round

#Check "game_start.players" list for the 2 of clubs
    #That player will be the first player in player order
    #Subsequent players will be next 

#Player order
    #Put players in a list. 

#Players must follow suit
    #Check hand
        #If hand has suit in "cards_played"
            #Then can only play those cards
        #Otherwise can play any higher card

#Check winner of round
    #

#PHASE 4