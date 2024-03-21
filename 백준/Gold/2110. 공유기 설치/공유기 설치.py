def calc_l_dist(house_pos:list[int], C:int) -> int:
    answer = 0
    start = 1
    end = house_pos[-1]-house_pos[0]
    while start <= end:
        mid = (start + end)//2
        installed = house_pos[0]
        count = 1

        for i in house_pos:
            if i >= installed + mid:
                count += 1
                installed = i
        if count >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid-1
    return answer

def main():
    N, C = map(int, input().split())
    house_pos = [int(input()) for _ in range(N)]
    house_pos.sort()
    longest_dist = calc_l_dist(house_pos,C)

    print(longest_dist)

if __name__ == "__main__":
    main()