#rotation
# check if all elements of list1 are in list2 and in same order even if does not start at same index 
# return boolean

def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key_index = 0

    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i
            break

    if key_index == 0:
        return False

    
    for j in range(len(list1)):
        key2_index = (key_index + j) % len(list1)

        if list1[j] != list2[key2_index]:
            return False

    return True

print(rotation([2, 4, 6, 8, 10, 12], [6, 8, 10, 12, 4, 2]))

print(rotation([2, 4, 6, 8, 10, 12], [6, 8, 10, 12, 2, 4]))