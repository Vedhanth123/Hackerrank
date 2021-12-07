# 1) Right rotate the array once
# testcases = int(input())
testcases = 1

for x in range(testcases):

    # sizeof_array = int(input())
    sizeof_array = 5
    # Array = input()
    # Array = Array.split()
    Array = [1,8,2,9,3]
    # Coloured_boxes = input()
    Coloured_boxes = "BBWBB"

    # right rotate the array
    # start from the last element of the array
    for y in range(sizeof_array-1, -1, -1):

        # save the last element of the array in a variable
        if(y == sizeof_array-1):
            storage = Array[y]
        else:
        # then n-1 element to nth index of the array repeat this step till you reach the 0th index of the array
            Array[y+1] = Array[y]


        # After reaching 0th index transfer the element from the variable to the 0th index of array
        if(y == 0):
            Array[y] = storage

    # 2) Find out the max element in black box and min element in white box
    Max_element_in_black_box = int(Array[0])
    Min_element_in_white_box = int(Array[0])


    for x in range(len(Array)):

        # finding max element in black box
        if(int(Array[x]) > Max_element_in_black_box and Coloured_boxes[x] == 'B'):
            Max_element_in_black_box = int(Array[x])
        
        if(int(Array[x]) < Min_element_in_white_box and Coloured_boxes[x] == 'W'):
            Min_element_in_white_box = int(Array[x])


    # 3) Find the difference between maxb and minw
    print(Max_element_in_black_box - Min_element_in_white_box)





'''
Testcases:

2
4
5 1 2 6
BWBW
5
1 8 2 9 3
BBWBB
'''