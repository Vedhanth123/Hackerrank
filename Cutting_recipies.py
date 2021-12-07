# testcases = int(input())
testcases = 1
for x in range(testcases):
    
    # ingredients = input()
    # ingredients = ingredients.split()
    
    ingredients = [2,4,4]
    # find the smallest number in the list
    
    smallest_number = int(ingredients[1])
    for y in range(1, len(ingredients)):
        
        if(smallest_number > int(ingredients[y])):
            smallest_number = int(ingredients[y])
            
    shortened_ingredients = []
    for y in range(1, len(ingredients)):
        
        if(int(ingredients[y]) % smallest_number == 0):
            shortened_ingredients.append(int(ingredients[y]) // smallest_number)
        else:
            break
    
    if(len(shortened_ingredients) == len(ingredients)-1):
        
        for y in range(len(shortened_ingredients)):
            print(f"{shortened_ingredients[y]} ",end="")
    
    else:
        for y in range(1, len(ingredients)):
            print(ingredients[y], end=" ")
            
        
        
    
    # divide other numbers with that number and check if the other numbers are divisible by that smallest number
    # if they are divisible then note down their quotients and replace their quotients in the place of the numbers
    