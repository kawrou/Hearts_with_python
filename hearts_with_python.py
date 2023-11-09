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
    #Access the variables directly to get their card value

    #OR
    #A dicionary with values as a list
    #A Dictionary of player:values(Suit:Numberpairs)
            #Players = {Player1:[hand], 
            #           Player2:[hand], 
            #           Player3:[hand], 
            #           Player4:[hand]
            #           }
    #Access "hand" by calling the key "PlayerNum.values"

    #OR
    #A dictionary of dictionaries
    #       Players = { player1 : {hand}, 
    #                   player2 : {hand}, 
    #                   player3 : {hand}, 
    #                   player4 : {hand},
    #                   }

#Build a dictionary called "Deck" that contains all the "suit" / "number" pairs.
    #**How to build this dictionary?**
        #Option 1
        # - Hardcode the dictionary
        
        #Option 2
        # - Combine two lists to a dictionary
        # - A numbers list from 1 to 13
        # - A card_suit list of the 4 suits
        # - Deck is a dictionary of suit:number pairs?

#Shuffle Deck
        # - Shuffle the dictionary
        # - Fetch all keys from a dictionary as a list
        # - shuffle that list and access dictionary values using shuffled keys

#Build hands 
        # - Each hand should be a dictionary?
        # - Place suit:number pairs from shuffled deck dictionary to player hands
        # - 



#PHASE 2


#PHASE 3


#PHASE 4