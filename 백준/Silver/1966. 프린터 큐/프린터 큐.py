def printQue(n: int, m: int, p: list) -> int:
    printque = list(enumerate(p))
    cnt = 0

    while True:
        if printque[0][1] == max(printque, key=lambda x: x[1])[1]:
            cnt += 1
            if printque[0][0] == m:
                return cnt
            printque.pop(0)
        else:
            printque.append(printque.pop(0))


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))
        result = printQue(N, M, priority)
        print(result)