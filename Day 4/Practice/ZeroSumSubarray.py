#To find the length of the longest zero sum subarray within an array

#Algorithm:
'''
prefix(i) = arr[0] + arr[1] +…+ arr[i] 
prefix(j) = arr[0] + arr[1] +…+ arr[j], j>i 
if prefix(i) == prefix(j) 
then prefix(j) – prefix(i) = 0 that means arr[i+1] + .. + arr[j] = 0
So a sub-array has zero sum , and the length of that sub-array is j-i+1  
'''




def maxLen(arr):
     
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictionary)
    hash_map = {}
 
    # Initialize result
    max_len = 0
 
    # Initialize sum of elements
    curr_sum = 0
 
    # Traverse through the given array
    for i in range(len(arr)):
         
        # Add the current element to the sum
        curr_sum += arr[i]
 
        if arr[i] == 0 and max_len == 0:
            max_len = 1
 
        if curr_sum == 0:
            max_len = i + 1
 
        # if sum repeats that means we have a subarray of zero sum that has been added
        # in this case, we can update max_len as maximum of current length and new length
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum] )
        else:
 
            # else put this sum in dictionary
            hash_map[curr_sum] = i
 
    return max_len
 
 
# test array
arr = [15, -2, 2, -8, 1, 7, 10, 13]
  
print("Length of the longest 0 sum subarray is % d" % maxLen(arr))