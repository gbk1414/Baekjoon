P = int(input())

for case in range(1, P + 1):
    list_T = list(map(int, input().split()))
    cnt = 0
    length = len(list_T)
    for i in range(2, length):
        for j in range(1,i):
            if list_T[j] > list_T[i]:
                cnt += i - j
                temp = list_T[i]
                list_T = list_T[:j] + [temp] + list_T[j:i] + list_T[i+1:]
                break
    print(list_T[0], cnt)
