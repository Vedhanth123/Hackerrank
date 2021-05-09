
# 1) find out the number of capital letters in a string

# a) loop through the string
# b) find out how many number of capital letters are there in a string



def camelcase(s):

    no_of_capital_letters = 0

    for i in range(len(s)):

        if(65 <= ord(s[i]) <= 90):
            no_of_capital_letters += 1
        
    return no_of_capital_letters + 1


print(camelcase("oneTwoThree"))