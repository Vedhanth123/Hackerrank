
def permutationEquation(p):
    # Write your code here

    y = []

    # 1) start from the 0th index of the array

    for x in range(len(p)):

        # find out the index in which the value of x is at

        for x in range(len(p)):

            if(p[x] == x):

                first_index = p[x]

        
        # find out the index in which the value of p[x] is at
        for y in range(len(p)):

            if(p[y] == first_index):

                second_index = p[y]
        
        y.append(second_index)
    
    return y

permutationEquation([4,3,5,1,2])


                