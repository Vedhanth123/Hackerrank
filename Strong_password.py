
# 1) find out that if password contains all the listed categories of characters in it.

# 2) if not then find out how many categories of characters are missing

# 3) if the length of the password is greater than or equal to 6 then add only required characters to the password


def minimumNumber(n, password):

    categories_of_characters = [0,0,0,0]

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    for i in range(len(password)):

        if(password[i] in numbers):
            categories_of_characters[0] += 1
        elif(password[i] in lower_case):
            categories_of_characters[1] += 1
        elif(password[i] in upper_case):
            categories_of_characters[2] += 1
        else:
            categories_of_characters[3] += 1
    
    no_of_zeros = 0

    for i in range(len(categories_of_characters)):

        if(categories_of_characters[i] == 0):
            no_of_zeros += 1
        
    if(len(password) >= 6):
        return no_of_zeros
    else:
        return no_of_zeros + (6 - (no_of_zeros + len(password)))

string = "Abcefg"

print(minimumNumber(len(string), string))