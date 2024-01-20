def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if int(finished[i])==0:
               answer.append(todo_list[i])
    return answer

'''
    return list(filter(lambda x : finished(x) != true, todo_list))???
'''    