def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if is_suffix == my_string[i:]:
            return 1
    else:
        return 0
    
#주의!
#for문이 언제 다 도는지, 
#돌고 나서 어디로 빠지는지 잘 살펴볼것
            