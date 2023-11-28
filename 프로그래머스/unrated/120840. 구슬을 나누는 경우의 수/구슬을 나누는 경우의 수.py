from math import factorial

def solution(balls, share): 
    n = factorial(balls)
    m = factorial(share)
    nm = factorial(balls - share) * m
    return n / nm