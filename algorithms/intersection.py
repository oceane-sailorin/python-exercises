#intersection
# common elements of two sorted arrays

def intersection(arr1, arr2):
    index_arr1 = 0
    index_arr2 = 0

    result = []

    while index_arr1 < len(arr1) and index_arr2 < len(arr2):
        if arr1[index_arr1] == arr2[index_arr2]:
            result.append(arr1[index_arr1])
            index_arr1 += 1
            index_arr2 += 1
        elif arr1[index_arr1] > arr2[index_arr2]:
            index_arr2 += 1
        else: 
            index_arr1 += 1

    return result

print(intersection([1, 2, 3, 4, 5, 6, 7],[2, 4, 6, 8, 10]))
