
# 1) given how many matches can be lost of important

n = 6
k = 3

contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

# 2) find out how many matches are important to her and how many should she win by differentiating
# total_important - k

no_of_important_matches = 0

for i in range(len(contests)):

    if(contests[i][1] == 1):
        no_of_important_matches += 1

# 3) remove the lowest value match in the array by winning it

smallest_contest = 

for i in range(len(contests)):

    if(contests[i][0] != 1):
        
