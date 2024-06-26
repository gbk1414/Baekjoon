N, K = map(int,input().split())

record = []

for _ in range(N):
    result = list(map(int, input().split()))
    record.append(result)

sorted_record = sorted(record, key = lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if sorted_record[i][0] == K:
        answer = i
        break

while i>0 and sorted_record[i][1:] == sorted_record[i-1][1:]:
    i -= 1

print(i+1)