def change(money: int, coin_list=list[int]):
    coin_num = 0
    for i in range(len(coin_list)-1, -1, -1):
        if money < coin_list[i]:
            continue
        coin_num += money // coin_list[i]
        money %= coin_list[i]
    return coin_num


def main():
    N, K = map(int, input().split())
    coin_list = [int(input()) for _ in range(N)]
    print(change(K, coin_list))


if __name__ == "__main__":
    main()
