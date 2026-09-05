print("                          === PLAYER MANAGER ===                       ")

player_manager = ["0. OBLIGATORY first player" , "1. Add player" , "2. Show player" ,
"3. Search player" , "4. Delate a palyer" , "5. Exit"]

for x in player_manager:
    print(x)
    
players = []
choose0 = ""

while choose0 != "0":
    choose0 = input("Choose an option 0:")
    
    if choose0 == "0":
        choose02 = input("Write a player name:")
        players.append(choose02)
        player_manager.remove("0. OBLIGATORY first player")
    

for x in player_manager:
    print(x)
    
choose = input("Choose an option:")

while choose != "5":
    if choose == "1":
        player = ""
        
        while player != "end":
            player = input("Write a players name:")
    
            if player != "end":
                players.append(player)
                
        print("Registred players:")

        for player in players:
            print(player)
        
        choose = "5"
    
    elif choose == "2":
        print("Total players" , (len(players)))
        
        choose = "5"
        
    elif choose == "3":
        seeker = input("Enter the name of the player you want to search for:")
        
        if seeker in players:
            print("PLayer found" , seeker)
        else:
            print("Player not found" , seeker)
            
        choose = "5"
        
    elif choose == "4":
        decision  = input("Do you want to delete a player? (yes/no)")  
        
        if decision == "yes":
            while decision != "no":
                
                if decision == "yes":
                    eliminate = input("Which player do you want to eliminate:")
                    
                if eliminate in players:
                    players.remove(eliminate)
                    print(players)
                else:
                    print(eliminate , "does not exist")
                
                decision  = input("Do you want to delete a player? (yes/no)")
                    
        choose = "5"
        
    else:
        print("This is not option")
    
    for x in player_manager:
        print(x) 
         
    choose = input("Choose an option:") 
