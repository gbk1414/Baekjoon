def calc_max_triangle(int_triangle:int, N:int):
    for i in range(1,N):
        for j in range(i+1):
            upper_idx = [j+k  for k in range(-1,1) if (j+k) in range(i)]
            max_upper_val = int_triangle[i-1][upper_idx[0]]
            for idx in upper_idx:
                max_upper_val = max(max_upper_val,int_triangle[i-1][idx])
            int_triangle[i][j] += max_upper_val
    
    return max(int_triangle[-1])
        






def main():
    N = int(input())
    int_triangle = [list(map(int,input().split())) for _ in range(N)]
    print(calc_max_triangle(int_triangle, N))


if __name__ == "__main__":
    main()