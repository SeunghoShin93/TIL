import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = str(input())             # 0값 받기위해 str으로 받음
    new_arr = [i for i in arr]     # 새로운 리스트 생성
    targetdict = {}

    for m in new_arr:                      # int로 바꾼후  카드번호를 key로, 카드 장수를 value로 받는 딕셔너리 생성
        if int(m) in targetdict:
            targetdict[int(m)] += 1
        if int(m) not in targetdict:
            targetdict.update({int(m):1})


    realdict = {}
    Max_v = 0
    for v in targetdict.values():      # 최대 카드 장수 파악
        if v > Max_v:
            Max_v = v
    for k in targetdict.keys():           # 최대 카드 장수를 value로 갖는 키값을 뽑아 새로운 딕셔너리 생성 ->
        if targetdict[k] == Max_v:
            realdict.update({k:Max_v})
    if len(realdict) == 1:                     # 가장 많은 카드 종류가 하나 일때 -> 바로 출력
        for k, v in realdict.items():
            print('#{} {} {}'.format(test_case, k, v))
    else:          # 가장 많은 카드 종류가 복수 일때 => 키값을 판별하여 가장 큰 카드번호와 장수를 출력
        Max_k = 0
        count = 0
        for key, value in realdict.items():
            count += 1
            if key > Max_k:
                Max_k = key
            if count == len(realdict):
                print('#{} {} {}'.format(test_case, Max_k, value))









"""
판별기준

Max_val count == 1
1. key, value

Max_val count > 1
2. Max_val의 key의 최대값, Max_val





"""
