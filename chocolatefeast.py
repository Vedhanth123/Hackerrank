
def chocolateFeast(n, c, m):
    # 1) find out how many chocolates can be bought with the amount of money
    # currently having
    total_no_of_chocolates = n // c
    
    # 2) find out how many wrappers after buying the chocolates and eating them
    no_of_wrappers = total_no_of_chocolates
    
    while(no_of_wrappers >= m):
        
        # 3) find out how many chocolates can be bought by trading them in
        no_of_chocolates_after_trading = no_of_wrappers // m
        
        # 4) no of wrappers left after trading them in
        no_of_wrappers %= m
        
        # 5) no of wrappers left after eating traded chocolates
        no_of_wrappers += no_of_chocolates_after_trading
        
        # 6) keeping track of total no of chocolates made
        total_no_of_chocolates += no_of_chocolates_after_trading
        
        # 7) repeat this untill no_of_wrappers are less than the trading value

    return total_no_of_chocolates



    