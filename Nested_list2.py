"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
list (array). The element value in the i-th row and j-th column of the array 
should be i *j.
Note: i=0,1.., X-1; j=0,1,¡¬Y-1. Suppose the following inputs are given to the 
program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Test case 1:
3,5                                                                                                                     
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Test case 2:
3,2                                                                                                                     
[[0, 0], [0, 1], [0, 2]] 
"""
x,y = map(int,input().split(','))
l1 = []
for i in range(x):
    l2 = []
    for j in range(y):
        n = i * j
        l2.append(n)
    l1.append(l2)
print(l1)

# # no of sublists
# X = int(input())

# # no of elements in sublists
# Y = int(input())

# Main_list = []
# # 1) write a loop till x
# for i in range(X):

#     Sub_list = []
#     for j in range(Y):
#         Sub_list.append(i*j)

#     Main_list.append(Sub_list)

# print(Main_list)