# length of last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = list(filter(None,s.split(" ")))
        print(words)
        return len(words[-1])

s1 = Solution()

print(s1.lengthOfLastWord("here is the day of the days"))
print(s1.lengthOfLastWord("here is the day of the days  "))
print(s1.lengthOfLastWord("   fly me   to   the moon  "))