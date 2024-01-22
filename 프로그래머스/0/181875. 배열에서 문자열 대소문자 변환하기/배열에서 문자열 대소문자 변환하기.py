def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer

#strArr[::2] and strArr[1::2] 을 번갈아 나오게는 안될까?