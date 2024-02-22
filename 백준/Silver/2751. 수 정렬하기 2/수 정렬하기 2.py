from sys import stdin, setrecursionlimit
input = stdin.readline

def main():
    N = int(input())
    array = []
    for i in range(N):
        array.append(int(input()))
    array.sort()
    for e in array:
        print(e)


if __name__ == "__main__":
    main()
