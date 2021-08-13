# merge two sorted lists
class Solution:
    def mergeTwoLists(self, l1: list, l2: list) -> list:

        if not l1 : return l2
        if not l2 : return l1

        index_arr1 = 0
        index_arr2 = 0

        result = []

        while index_arr1 < len(l1) and index_arr2 < len(l2):
            if l1[index_arr1] == l2[index_arr2]:
                result.append(l1[index_arr1])
                result.append(l2[index_arr2])
                index_arr1 += 1
                index_arr2 += 1
            elif l1[index_arr1] > l2[index_arr2]:
                result.append(l2[index_arr2])
                index_arr2 += 1
            else: 
                result.append(l1[index_arr1])
                index_arr1 += 1
            if index_arr1 >= len(l1): result.extend(l2[index_arr2:])
            if index_arr2 >= len(l2): result.extend(l1[index_arr1:])

        return result

s1 = Solution()

print(s1.mergeTwoLists([1, 2, 3, 4, 5, 6, 7],[2, 4, 6, 8, 10]))

print(s1.mergeTwoLists([],[2, 4, 6, 8, 10]))

print(s1.mergeTwoLists([-9,-5,-3,2,6],[2, 4, 6, 8, 10]))

print(s1.mergeTwoLists([5,9,12,19,22,26,28],[1,2,8,9,10]))
