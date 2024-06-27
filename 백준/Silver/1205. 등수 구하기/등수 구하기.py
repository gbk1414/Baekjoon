N, new_score, P = map(int, input().split())

score_list = []

if N != 0:
    score_list = list(map(int, input().split()))
    
sorted_score = sorted(score_list, reverse= True)

for _ in range(N, P):
    sorted_score.append(-1)

i = 0
rank = 1
while i < P:
    if sorted_score[i] < new_score:
        break
    elif sorted_score[i] > new_score:
        rank += 1
    i += 1

if i == P:
    print(-1)
else:
    print(rank)