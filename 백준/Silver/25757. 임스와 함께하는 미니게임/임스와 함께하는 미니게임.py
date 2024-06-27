N, game = input().split()

N = int(N)

game_list = ["Y", "F", "O"]
people_list = set()


for i in range(N):
    people_list.add(input())

num_people = len(people_list)

game_num =  game_list.index(game) + 1

answer = num_people // game_num

print(int(answer))
