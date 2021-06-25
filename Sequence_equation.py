
def permutationEquation(p):
    # Write your code here

    y_array = []

    # 1) start from the 0th index of the array

    for a in range(len(p)):

        # find out the index in which the value of x is at

        for x in range(len(p)):

            if(p[x] == a+1):

                first_index = x + 1

        
        # find out the index in which the value of p[x] is at
        for y in range(len(p)):

            if(p[y] == first_index):

                second_index = y + 1
        
        y_array.append(second_index)
    
    return y_array
    
permutationEquation([4,3,5,1,2])


                