def MergeSort(array, l, r):
        
        if(len(array) == 1):
            return array
        
        # 1) divide the array into two parts till the len of array is 1
        
        avg = len(array) // 2
        
        left = array[:avg]
        right = array[avg:]
        
        MergeSort(left, l, avg)
        MergeSort(right, avg+1, r)
        
        # 2) Merging two arrays into one single array as well as sorting them
        def Merge(array, left, right):
            
            # indexes for left, right and main array
            i = 0
            j = 0
            k = 0
            
            # sorting and inserting the elements into the array
            while(i < len(left) and j < len(right)):
                if(left[i] < right[j]):
                    array[k] = left[i]
                    k += 1
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                    k += 1
                
            # sending remaining the elements into the main array
            if(i < len(left)):
                while(i < len(left)):
                    array[k] = left[i]
                    k += 1
                    i += 1
                
            else:
                while(j < len(right)):
                    array[k] = right[j]
                    k += 1
                    j += 1
        
        Merge(array, left, right)
    MergeSort(prices, 0, len(prices))
    
    bill = 0
    no_of_toys = 0
    
    for x in range(len(prices)):
        
        bill += prices[x]
        no_of_toys += 1
        
        if(bill > k):
            no_of_toys -= 1
            break
    
    return no_of_toys


