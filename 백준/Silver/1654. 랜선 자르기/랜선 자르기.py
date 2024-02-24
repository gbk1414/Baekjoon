def cut_lan(lan_list:list[int], N:int):
    lan_list.sort()
    start = 1
    end = lan_list[-1]
    while start <= end:
        mid = (start+end)//2
        new_lan = [i//mid for i in lan_list]
        if sum(new_lan) < N:
            end = mid-1
        else:
            start = mid + 1
    return end



def main():
    K, N = map(int,input().split())
    lan_list = [int(input()) for _ in range(K)]
    print(cut_lan(lan_list, N))


if __name__ == "__main__":
    main()