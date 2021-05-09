# given the element at the last

# 1) take the before element and copy that to the last one

# 2) continue this untill the current element we are searching now is less than the element we selected

# 3) start from the 2nd element of the array and compare it with the element left to it

# 4) if the element left to it is greater than the element right to it then start swapping

arr = [1,2,4,5,3]

element_selected = arr[-1]


for j in range(1, len(arr)):

    if(arr[j] < arr[j-1]):

        i = j - 1


        while(i >= 0 and arr[i] > element_selected):

            arr[i+1] = arr[i]    
            i -= 1
        
    arr[i+1] = arr[j]

    for x in range(len(arr)):
        print(arr[x],end = " ")
    print("")
            
            
        

        