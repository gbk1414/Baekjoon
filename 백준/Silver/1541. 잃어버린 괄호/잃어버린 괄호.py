import re


def get_smallest_val(num_list: list, minus_idx: int) -> int:
    return sum(num_list[:minus_idx])-sum(num_list[minus_idx:])


def main():
    expression = input()
    minus_idx = 1
    for i in expression:
        if i == "+":
            minus_idx += 1
        elif i == "-":
            break
    num_list = list(map(int, re.split(r'[+-]', expression)))
    print(get_smallest_val(num_list, minus_idx))


if __name__ == "__main__":
    main()
