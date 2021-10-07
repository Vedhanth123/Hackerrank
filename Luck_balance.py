
"""

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
        
"""

def luckBalance(k, contests):
    # Write your code here
    
    # Lena should lose important matches which have high luck rating
    # Lena will obviously lose all the umimportant and addes up luck rating to the total luck.

    TotalLuckRatingOfLena = 0

    # 1) first add up the luck ratings of all the unimportant matches
    for x in range(len(contests)):

        if(contests[x][1] == 0):
            TotalLuckRatingOfLena += contests[x][0]
        
    HighestLuckRating = contests[x][1]

    for z in range(k):
        for y in range(len(contests)):

            # 2) find out the important match which has the highest luck rating
            if(contests[x][1] == 1):
                if(HighestLuckRating < contests[x][1]):
                    HighestLuckRating = contests[x][1]
            
        for x in range(len(contests)):

            if(contests[x][1] == HighestLuckRating):
                TotalLuckRatingOfLena = HighestLuckRating
                contests[x][1] = 0
                
luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])

    

    pass