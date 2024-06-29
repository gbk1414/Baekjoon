import sys

def main():
    N, X = map(int, input().split())
    visiter = list(map(int, sys.stdin.readline().rstrip().split()))
    new_visiter = [0 for _ in range(N-X+1)]
    new_visiter[0] = sum(visiter[0:X])
    for i in range(1, N-X+1):
        new_visiter[i] = new_visiter[i-1] - visiter[i-1] + visiter[i+X-1]
    answer = max(new_visiter)
    if answer == 0:
        print("SAD")
        return
    cnt = new_visiter.count(answer)
    print(answer)
    print(cnt)
    return

if __name__ == "__main__":
    main()