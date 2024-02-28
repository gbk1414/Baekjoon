def least_cost(rgb_list, N):
    rec_cost = [rgb_list[0]] + [[0, 0, 0] for _ in range(N-1)]

    for i in range(1, N):
        rec_cost[i][0] = rgb_list[i][0] + min(rec_cost[i-1][1], rec_cost[i-1][2])
        rec_cost[i][1] = rgb_list[i][1] + min(rec_cost[i-1][0], rec_cost[i-1][2])
        rec_cost[i][2] = rgb_list[i][2] + min(rec_cost[i-1][0], rec_cost[i-1][1])
    
    return min(rec_cost[-1])


def main():
    N = int(input())
    rgb_list = [list(map(int, input().split())) for _ in range(N)]

    print(least_cost(rgb_list, N))


if __name__ == "__main__":
    main()
