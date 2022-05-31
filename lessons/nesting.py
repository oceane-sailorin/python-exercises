# nesting
"""
A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.


"""
def solution(S):
    dict = {")":"("}
    brack = [")","("]
    res = []
    for car in S:
        if car not in brack:
            return 0
            
        if car in dict.keys():
            if not res or dict[car] != res.pop(): 
                return 0
        elif car in dict.values():
            res.append(car)
    return 1 if len(res) == 0 else 0



print(solution("(()(())())"))

print(solution("())"))

print(solution(""))

print(solution("(())(())()((()))((()()())())"))

print(solution("(())(())()((()))((()()())("))

print(solution("((()))()()((((()()()((()))()())()())((((())))))())"))