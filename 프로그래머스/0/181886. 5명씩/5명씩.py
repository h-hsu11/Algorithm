def solution(names):
    answer = []
    for i in range(len(names)): 
        if i%5==0:
            answer.append(names[i])
    return answer

'''
enumerate 함수 쓰기


def solution(names):
    answer = []
    for i,str in enumerate(range(0,len(names),5))  -- range로 특정 간격의 인덱스 형성, enumerate 필요없음. 
        answer.append(names[i])
    return answer


수정코드:

def solution(names):
    answer = []
    for idx, name in enumerate(names[::5]):    
        answer.append(name)
    return answer
    
하지만 직접 5단계마다 리스트에서 가져오는 것이 메모리 사용상 효율적
'''