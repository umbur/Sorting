# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Initial commit   
        for j in range(cur_index + 1, len(arr)):
            # print(cur_index)
            if arr[j] < arr[smallest_index]:
                smallest_index = j 

        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr
print(selection_sort([8, 3, 0, 2, 1, 5]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr
arr = [14,46,43,27,57,41,45,21,70]
bubble_sort(arr)
print(arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr