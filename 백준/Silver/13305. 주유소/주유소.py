def cal_min_price(dist, price):
    min_price = 10**9 + 1
    total_cost = 0
    for i in range(len(dist)):
        min_price = price[i] if min_price > price[i] else min_price
        total_cost += min_price * dist[i]
    return total_cost


def main():
    N = int(input())
    dist = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(cal_min_price(dist, price))


if __name__ == "__main__":
    main()
