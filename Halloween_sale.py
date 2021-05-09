
def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    # find how many games can be bought using money

    no_of_games = 0
    # 1) start from the first game amount 
    bill = p

    no_of_games += 1

    while(bill < s):
            
        # 2) decrease the price of game by d 
        # till the price of the game reaches d or less than p 
        # if p is less than than d then price of p will be d
        # if p is greater than d then decrease the price of p by d
        if((p - d) <= m):
            p = m
        else:
            p -= d
        
        
        # 3) purchase the game after the price alteration
        bill += p

        # incrementing no of games
        no_of_games += 1

        # 4) repeat this untill all the amount is finished
    
    if(bill > s):
        bill -= p
        no_of_games -= 1
    
    return no_of_games

howManyGames(20, 3, 6, 85)
