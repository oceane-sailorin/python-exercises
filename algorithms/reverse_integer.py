# reverse integer

def solution(n):
    s = str(n)
    
    if s[0] == '-':
        return int('-'+s[:0:-1])
    else:
        return int(s[::-1])
    
print(solution(-654))
print(solution(698))