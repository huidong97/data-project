def custom_mean(*_list): #1번 과정
    # while문
    # 초기값 지정
    i = 0
    sum = 0 #3-1과정
    while i < len(_list):  #2번 과정
        # print(_list[i])
        sum += _list[i]
        # i값을 증가
        i += 1 #이거 안해주면 무한반복
    # print(sum)  3-2r과정
    result = sum/len(_list)
    return result  

def custom_max(*_list):
    result = _list[0]
    #첫 번째 원소를 출력?
    #첫 번째 원소와 두번째 원소의 값을 비교하여 큰 값을  result에 대입
    #if _list[0] > _list[1]:
    #    result = _lsit[0]
    #else:
    #    result = _list[1]
    # if result < _list[1]:
    #  result = _list[1]

     #result와 세번째 원소를 비교
    # if result > _list[2]:
    #    result = result
    # else:
    #    result = _list[2]
    # if result < _list[2]:
    #    result = _list[2]
    for i in _list:
       if result < i:
          result = i
    return result                  