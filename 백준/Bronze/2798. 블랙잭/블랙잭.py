def main():
    N, M = map(int, input().split())  # 카드의 개수 N과 합 M 입력
    cards = list(map(int, input().split()))  # 카드에 쓰여 있는 수 입력
    cards.sort()  # 카드를 정렬
    
    max_value = 0
    
    for i in range(N - 2):
        left, right = i + 1, N - 1
        while left < right:
            card_sum = cards[i] + cards[left] + cards[right]
            if card_sum <= M:
                max_value = max(max_value, card_sum)
                left += 1
            else:
                right -= 1
                
    print(max_value)

if __name__ == "__main__":
    main()
