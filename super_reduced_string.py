

string = "baab"

# 1) find out any adjacent same letters in a string

for x in range(len(string) - 1):

    if(string[x] == string[x+1]):
        string[x] = string[x+1] = " "

string = string.strip()

# 2) remove them

# 3) repeat the first step again

for x in range(len(string) - 1):

    if(string[x] == string[x+1]):
        string[x] = string[x+1] = " "

# 4) do that untill no adjacent and repeated contains

# 5) return the string if the string doesn't contain any letters return empty string