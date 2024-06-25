N = int(input())

numbox = 1
cnt = 1

while numbox < N:
    numbox += cnt * 6
    cnt += 1

print(cnt)