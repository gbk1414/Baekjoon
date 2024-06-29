def calculate_total(N, budget:list, val):
    value = 0
    for i in range(N):
        if budget[i] < val:
            value += budget[i]
        else:
            value += val
    return value


def main():
    N = int(input())
    budget = list(map(int, input().split()))
    total_budget = int(input())
    if sum(budget) <= total_budget:
        print(max(budget))
        return
    answer = total_budget//N
    total_val = calculate_total(N, budget, answer)
    while total_val <= total_budget:
        answer += 1
        total_val = calculate_total(N, budget, answer)
    print(answer-1)
    return

if __name__ == "__main__":
    main()
