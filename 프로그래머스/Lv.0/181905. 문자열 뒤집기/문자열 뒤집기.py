def solution(my_string, s, e):
    return (my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:])

#왜 my_string[s:e+1:-1]은 안돼??
#문자열은 reverse 메서드가 없다. 따라서 list로 바꾸어 reverse하고 join해줘야 한다.

        