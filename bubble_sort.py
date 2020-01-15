def bubbleSort(arr):
    '''
     This function takes an unsorted array as input, sorts it,
     and returns the sorted arrey     
    '''
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr