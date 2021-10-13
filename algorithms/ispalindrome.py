# ispalindrome - only alphanumeric characters count
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        news = re.sub("[^0-9a-zA-Z]+", "", s).lower()
        for l in range(1, len(news) + 1):          
            result += news[len(news) - l]
           
        return result == news

s1 = Solution()

#check examples

print(s1.isPalindrome("A man, a plan, a canal: Panama"))


print(s1.isPalindrome("race a car"))

print(s1.isPalindrome("A nut for a jar of tuna"))

print(s1.isPalindrome("Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era"))

print(s1.isPalindrome("Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned."))

print(s1.isPalindrome("Yo, banana boy!"))

print(s1.isPalindrome("Marge lets Norah see Sharron’s telegram."))