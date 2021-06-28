#maxsum
#input = array of integers ( positive and negative), ouput = max contiguous sum we can have with numbers in array, only used once max

def maxsum(arr):

    if len(arr) == 0: print("array should have at least one element")

    current_max = final_max = arr[0]

    for n in arr[1:]:
        current_max = max(current_max + n, n)
        final_max = max(current_max,final_max)


    return final_max


print(maxsum([5,8,-9,7,4,6,-8,7]))

print(maxsum([5,6,-17,8,3,6,7,8,-2,6,-9]))