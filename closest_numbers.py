
from typing_extensions import ParamSpec


array = [5, 4, 3, 2]

# 1) sort the array 

array.sort()

# 2) then find the smallest absolute difference between the elements

smallest_absolute_difference = abs(array[0] - array[1])

for i in range(len(array) - 1):

    if(smallest_absolute_difference > abs(array[i] - array[i + 1])):
        smallest_absolute_difference = abs(array[i] - array[i + 1])

# 3) if the absolute difference betweent the numbers is the smallest then add those numbers to the array

pairs_of_numbers = []

for i in range(len(array) - 1):

    if(smallest_absolute_difference == abs(array[i] - array[i + 1])):
        pairs_of_numbers.append(array[i])
        pairs_of_numbers.append(array[i + 1])


print(pairs_of_numbers)
