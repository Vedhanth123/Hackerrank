testcases = 20

for x in range(1, testcases):
    
    coins = x
    
    coins_in_row = 1
    no_of_rows = 0
    
    while(coins_in_row <= coins and coins != 0):
        
        coins -= coins_in_row
        coins_in_row += 1
        
        no_of_rows += 1
    
    print(no_of_rows)