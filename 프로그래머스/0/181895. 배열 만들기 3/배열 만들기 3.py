def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        for j in range(intervals[i][0], intervals[i][1]+1):  #i=0일 때, intervals[i][0] : intervals의 첫번째 내부리스트의 첫번째 요소, intervals[i][1] : 첫번째 내부리스트의 두번째 요소
            answer.append(arr[j])
    return answer
        
        
        
'''        
풀이
1) 배열 arr의 두 구간을 추출하여 리턴할 것.
2) 그 두 구간에 해당하는 값은 intervals에서 찾을 것
'''
