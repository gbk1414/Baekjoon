#dp로 문제 해결
def combination(m, n, comb_val):
    for i in range(m + 1):
        comb_val[i][0] = 1
        comb_val[i][i] = 1

    for i in range(1, m + 1):
        for j in range(1, min(i, n) + 1):
            comb_val[i][j] = comb_val[i - 1][j - 1] + comb_val[i - 1][j]

def main():
    T = int(input())
    combination_table = [[0 for _ in range(31)] for _ in range(31)]
    combination(30, 30, combination_table)
    
    for _ in range(T):
        N, M = map(int, input().split())
        print(combination_table[M][N])

if __name__ == "__main__":
    main()