
def jumpingOnClouds(c, k):


    # energy level
    e = 100

    # variable for index of array
    i = 0

    # written a new line 

    # another new line
    
    while(i == 0 and e < 100):

        # increment the index of the array by two
        i = (i+k)%len(c)

        # cloud landed on is a thunder cloud then decrement energy by 3
        if(c[i] == 1):
            e -= 3
        else:
            e -= 1

    return e

jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2) 
    