def main():
    N = int(input())
    M = int(input())
    x_list = list(map(int, input().split()))
    new_x_list = [(x_list[i+1]-x_list[i]+1)//2 for i in range(M-1)]
    if new_x_list:
        print(max(x_list[0], N-x_list[-1], max(new_x_list)))
    else:
        print(max(x_list[0], N-x_list[-1]))

if __name__ == "__main__":
    main()