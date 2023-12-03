def solution(s):
    mylist = []
    for num in s.split(' '):
        try:
            mylist.append(int(num))
        except:
            mylist.pop()
    return sum(mylist)

    