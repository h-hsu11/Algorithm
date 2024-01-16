def solution(q, r, code):
    answer = ''
    return code[r::q]
    return answer


#1차원 배열을 행렬로 표현할 때, 각 자리의 인덱스 (a,b)
#b는 행의 갯수로 나눈 나머지이다. 
#q로 나눈 나머지가 r인 위치의 문자는, 
#q개의 행으로 배열하고 r번째 열의 숫자를 의미한다.