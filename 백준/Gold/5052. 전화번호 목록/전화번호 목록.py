from sys import stdin
input = stdin.readline


def check_prefix(strings):
    for i in range(len(strings)-1):
        if strings[i+1].startswith(strings[i]):
            return "NO"
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        phone_numbers = [input().rstrip() for _ in range(n)]
        phone_numbers.sort()
        print(check_prefix(phone_numbers))


if __name__ == "__main__":
    main()
