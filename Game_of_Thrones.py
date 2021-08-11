
def gameOfThrones(s):
    # Write your code here

    no_of_letters = {}

    for x in range(26):
        
        no_of_letters.update({chr(97+x):0})
        
    
    # 1) start from the first letter of the string\
    for x in range(len(s)):
        
        # 2) note how many times each letter appeared in string
        no_of_letters[s[x]] += 1
    
    no_of_odd = 0

    for x in range(26):
        
        if(no_of_letters[chr(97+x)]%2 == 1):

            no_of_odd += 1
            if(no_of_odd == 2):
                return "NO"
    
    return 'YES'
    
    # 4) only a single letter can be odd

gameOfThrones('cdcdcdcdeeeef')