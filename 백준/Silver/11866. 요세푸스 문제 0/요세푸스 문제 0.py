from collections import deque

def yosepus(N: int, K: int) -> list[int]:
    que = deque(range(1, N + 1))
    answer = []
    while que:
        for _ in range(K - 1):
            que.append(que.popleft())
        answer.append(que.popleft())
    return answer

def main():
    N, K = map(int, input().split())
    answer = yosepus(N, K)
    print("<" + ", ".join(map(str, answer)) + ">")

if __name__ == "__main__":
    main()