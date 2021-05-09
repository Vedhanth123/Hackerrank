
# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

# Example
# a = [1,1,2,2,4,4,5,5,5]


# There are two subarrays meeting the criterion:[1,1,2,2]  and [4,4,5,5,5]. The maximum length subarray has  elements.

a = [1,1,2,2,4,4,5,5,5]

def pickingNumbers(a):

    number = 1

    # taking a list to store all the numbers
    list_to_store_numbers = []

    # taking a counter to count the number of iterations which loop took
    counter = 0

    # 1) finding out numbers which when differentiated absolutely give result less than or equal to 1
    for x in range(len(a)):

        if(counter == 0):
            list_to_store_numbers.append(a[x])
        

        # a) opt a number and find out numbers which are in the range of {number - 1, number, number + 1}
        if((number == a[x]) or (a[x] == (number-1)) or (a[x] == (number + 1))):
            list_to_store_numbers.append(a[x])
        
        counter += 1

    print(list_to_store_numbers)        

pickingNumbers(a)


    
    
    