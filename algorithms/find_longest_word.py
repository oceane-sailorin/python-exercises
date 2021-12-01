#find longest word



class Solution:
    def find_longest_word(self,words_list):
        word_len = []
        for n in words_list:
            word_len.append((len(n), n))
        word_len.sort()
        return word_len[-1][0], word_len[-1][1]

s1 = Solution()

print(s1.find_longest_word(["remind","who","there"]))
print(s1.find_longest_word(["tremendous","inocuous","remindala"]))