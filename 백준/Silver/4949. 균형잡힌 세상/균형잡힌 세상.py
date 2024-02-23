from collections import deque


def balance_check(string_list):
    stack = deque()
    brackets = {")": "(", "]": "["}
    for s in string_list:
        if s in brackets.values():
            stack.append(s)
        elif s in brackets.keys():
            if not stack or stack[-1] != brackets[s]:
                return "no"
            stack.pop()
    return "yes" if not stack else "no"


def main():
    while True:
        a = input()
        if a == ".":
            break
        print(balance_check(a))


if __name__ == "__main__":
    main()
