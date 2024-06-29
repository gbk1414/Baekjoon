def filter_oil_price_list(N, oil_price_list:list):
    min_val = float('inf')
    for i in range(N):
        if oil_price_list[i] < min_val:
            min_val = oil_price_list[i]
        else:
            oil_price_list[i] = min_val
    return oil_price_list


def main():
    N = int(input())
    dist_list = list(map(int, input().split()))
    oil_price_list = list(map(int, input().split()))
    oil_price_list = filter_oil_price_list(N, oil_price_list)

    answer = sum([dist_list[i]* oil_price_list[i] for i in range(N-1)])
    print(answer)

if __name__ == "__main__":
    main()