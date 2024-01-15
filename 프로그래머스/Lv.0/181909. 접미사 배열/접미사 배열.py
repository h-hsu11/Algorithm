''''''
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    answer.sort()
    return answer
    

# sort() 함수는 list를 정렬하고 none을 리턴한다. 
# 따라서 sort를 먼저하고 리턴해야 한다.
'''
      answer.append(my_string[i:])
   return answer.sort()
'''