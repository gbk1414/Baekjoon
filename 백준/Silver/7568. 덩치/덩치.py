N = int(input())

people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

def checker(person, other_person):
    if person[0] < other_person[0] and person[1] < other_person[1]:
        return True

for person in people:
    cnt = 1
    for i in range(N):
        if checker(person, people[i]):
            cnt += 1
    print(cnt, end= " ")