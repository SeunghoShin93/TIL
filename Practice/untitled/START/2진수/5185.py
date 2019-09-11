import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, arr = map(str, input().split())
    sixteen = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    lista = []

    for n in range(int(N)):
        if arr[n].isdigit():
            if int(arr[n]) == 0:
                lista.append('0000')
            elif int(arr[n]) < 2:
                lista.append('000'+'{0:b}'.format(int(arr[n])))
            elif int(arr[n]) <= 3:
                lista.append('00'+'{0:b}'.format(int(arr[n])))
            elif int(arr[n]) >= 8:
                lista.append('{0:b}'.format(int(arr[n])))
            else:
                lista.append('0'+'{0:b}'.format(int(arr[n])))
        else:
            lista.append('{0:b}'.format(sixteen[arr[n]]))
    print('#{} {}'.format(t, ''.join(lista)))
