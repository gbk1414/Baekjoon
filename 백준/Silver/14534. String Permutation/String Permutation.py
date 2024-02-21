def str_permute(L_str):
    if len(L_str) == 1:
        return L_str
    
    L_str_list = []

    for i in range(len(L_str)):
        new_L_str = L_str[:i]+L_str[i+1:]
        for permute_L in str_permute(new_L_str):
            L_str_list.append(L_str[i]+permute_L)

    return L_str_list


def main():
    T = int(input())
    for i in range(1,T+1):
        print("Case # {}:".format(i))
        L = list(input())
        for s in str_permute(L):
            print(s)

if __name__ == "__main__":
    main()
    