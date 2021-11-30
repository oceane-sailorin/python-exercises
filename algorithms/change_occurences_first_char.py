#change a given string : all occurrences of its first char have been changed to '0', except the first char itself.


class Solution:
    def change_occurences_char(self,word):
        first_c = word[0]
        word = word.replace(first_c, '0')
        word = first_c + word[1:]

        return word


s1 = Solution()

print(s1.change_occurences_char('uluberlu'))
print(s1.change_occurences_char('ocarina'))
print(s1.change_occurences_char('p'))