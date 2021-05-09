# Given a set of distinct integers,
#  print the size of a maximal subset of  
# where the sum of any  numbers in  is not evenly divisible by .

"""
def nonDivisibleSubset(k, s):

    # 1) find out all the permutations and their coresponding sums

    # array containing values
    # values = [1,7,2,4]

    # # array to store the summed values
    # summed_values = []

    # for i in range(len(values)-1):

    #     for j in range(i+1,len(values)):

    #         summed_values.append(values[i]+values[j])

    # Pick out the permutations which do not divide by k.

    # k = 3

    # array to store the pairs which do not divide by k
    pairs = set()

    s = list(set(s))


    # set is chosen as set does not contain repeated values so set.add() 
    # won't add values already present in the array

    sums = 0

    for i in range(len(s)-1):

        for j in range(i+1,len(s)):

            # checking if the pairs are not divisible by k

            sums = s[i] + s[j]
            if(sums % k != 0):

                # adding numbers to the pairs which are not divisible by k to array
                pairs.add(s[i])
                pairs.add(s[j])

    # returning the maximum number of elements
    # return (len(pairs))


    pairs = list(pairs)

    final_pairs = set()

    sums = 0

    for i in range(len(pairs)-1):

        for j in range(i+1,len(pairs)):

            # checking if the pairs are not divisible by k

            sums = pairs[i] + pairs[j]
            if(sums % k != 0):

                # adding numbers to the pairs which are not divisible by k to array
                final_pairs.add(s[i])
                final_pairs.add(s[j])
        
    return len(final_pairs)

print(nonDivisibleSubset(7,[278 ,576 ,496 ,727, 410, 124, 338 ,149 ,209 ,702 ,282 ,718 ,771 ,575 ,436]))

"""

"""
def nonDivisibleSubset(k, s):

    # 1) find out permutation of each and every element added together not divisble by k

    # array to store all the size of permutations of each and every 
    # element added together not divisble by k
    subsets = []

    # array to store the permutations 
    permutation = set()

    # var to sum the pairs
    sums = 0

    for i in range(len(s)-1):

        # inserting the numbers which are not divisible by k
        permutation.add(s[i])

        for j in range(i+1, len(s)):

            # checking if pairs turn up to be not divisible
            sums = s[i] + s[j]
            if(sums % k != 0):

                # inserting the numbers which are not divisible by k
                permutation.add(s[j])

        # inserting the length of the permutation into list
        subsets.append(len(permutation))

        # clearing the current permutation to store the next permutation
        permutation.clear()

    # finding out subsets in it

    subset1 = list(subsets[0])

    subsets_1 = []

    for i in range(len(subset1)-1):

        # inserting the numbers which are not divisible by k
        permutation.add(subset1[i])

        for j in range(i+1, len(subset1)):

            # checking if pairs turn up to be not divisible
            sums = subset1[i] + subset1[j]
            if(sums % k != 0):

                # inserting the numbers which are not divisible by k
                permutation.add(subset1[j])

        # inserting the length of the permutation into list
        subsets_1.append(len(permutation))

        # clearing the current permutation to store the next permutation
        permutation.clear()

    

    # 2) find out the maximum length of permutation

    maximum_length = 0

    for x in range(len(subsets)):

        if(maximum_length < subsets[x]):
            maximum_length = subsets[x]
        
    return (maximum_length)

print(nonDivisibleSubset(4,[19,10,12,10,24,25,22]))
"""

278 576 496 727 410 124 338 149 209 702 282 718 771 575 436
