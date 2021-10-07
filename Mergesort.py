class MergeSort:

    # 2) Merge the divided array into one single array
    def Merge(self, array, l, mid, r):

        # loop invariant for left array
        i = l

        # loop invariant for right arrray
        j = mid + 1

        # loop invariant for original array
        k = l
        
        # backing up array into left and right
        left = array[l: mid + 1]
        right = array[mid + 1:r + 1]
        
        # sorting out the array
        while(i <= mid and j <= r):

            if(left[i - l] < right[j - (mid + 1)]):
                array[k] = left[i - l]
                k += 1
                i += 1
            else:
                array[k] = right[j - (mid + 1)]
                j += 1
                k += 1
        
        # inserting the left over elements into their correct positions
        while(i <= mid):
            array[k] = left[i - l]
            i += 1
            k += 1
        while(j <= r):
            array[k] = right[j - (mid + 1)]
            j += 1
            k += 1

    # 1) divide the array into two parts left and right
    def Mergesort(self, array, l, r):

        # if the left part surpasses or equals to the right part then stop 
        # recursion
        if(l >= r):
            return array
        
        else:

            
            mid = ((l + r)// 2)

            # recursive case for the left and right part of the array
            self.Mergesort(array, l, mid)
            self.Mergesort(array, mid + 1, r)

            # Merging the array
            self.Merge(array, l, mid, r)


array = [6,3,9,5,2,8,7,1,0]
obj = MergeSort()

obj.Mergesort(array, 0, 8)

print(array)