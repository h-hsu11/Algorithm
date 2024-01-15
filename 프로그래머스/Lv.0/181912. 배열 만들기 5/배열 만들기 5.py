def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer

# 왜 answer += int(i[s:s+l]) 은 안될까
# int object is not iterable