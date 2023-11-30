
def solution(n):
    output = []
    i = 2
    while i <= n:
        if n % i == 0:
            output.append(i)
            while n % i == 0:
                n //= i
        i += 1
    return output
        
            
                