#find element with most occurences in list

def mostfrequent(list1):
    count = {}
    maxcount = 0
    maxelt = None

    for i in list1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > maxcount:
            maxcount = count[i]
            maxelt = i

    return maxelt

print(mostfrequent([1, 5, 8, 6, 5, 8, 3, 8, 7]))

print(mostfrequent(["one","two", "three", "four", "two", "one", "two"]))

