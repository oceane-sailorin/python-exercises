#algoarray
#input = array and sum, output = all unique pairs that sum up sum value

def allpairs(arr,s):
    if len(arr) < 2: return print("not enough values in array")

    temp = set()
    result = set()

    for n in arr:
        target = s - n

        if target not in temp:
            temp.add(n)

        else:
            result.add((min(n, target),max(n, target)))

    print('\n'.join(map(str,list(result))))

allpairs([1,3,2,2],4)
print("\n")
allpairs([5,8,9,3],8)
print("\n")
allpairs([1,9,16],7)
print("\n")
allpairs([1,8,7,5,3,2,4,5,9,6,5,4,2,1,5,8,7],8)
print("\n")
allpairs([1],4)
