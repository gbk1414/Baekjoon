def str_permute(input_str):
    if len(input_str) == 1:
        return input_str

    perm_str = []
    for i in range(len(input_str)):
        for permute_L in str_permute(input_str[:i]+input_str[i+1:]):
            perm_str.append(input_str[i]+permute_L)

    return perm_str


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case # {}:".format(i))
        L = list(input())
        for s in str_permute(L):
            print(s)


if __name__ == "__main__":
    main()
