N = int(input())
answer = N//5
leftover = N%5
while leftover%3 != 0:
    answer -= 1
    leftover += 5
    if answer < 0:
        break
if answer <0:
    print(-1)
else:
    print(answer + leftover//3)