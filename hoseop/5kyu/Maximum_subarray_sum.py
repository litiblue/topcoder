def maxSequence(arr):
    
    if len(arr)==0:
        return 0
    
    sum = 0
    for first in range(0,len(arr)):
        cur_sum=0
        for last in range(first, len(arr)):
            cur_sum = cur_sum + arr[last]
            
            if cur_sum > sum:    sum = cur_sum

    return sum
