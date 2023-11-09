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


#Creates a class of players
#Initializes the player variables and their empty hand
class players():
    def __init__(self):
        self.player_1 = {}
        self.player_2 = {}
        self.player_3 = {}
        self.player_4 = {}
        self.players = [player_1, player_2, player_3, player_4]




#PHASE 2


#PHASE 3


#PHASE 4