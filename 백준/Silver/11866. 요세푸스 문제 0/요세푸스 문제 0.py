from collections import deque

def yosepus(que:deque, k:int)->list[int]:
    answer = []
    while que:
        for i in range(k):
            pop_val = que.popleft()
            if i != k-1:
                que.append(pop_val)
            else:
                answer.append(pop_val)
    return answer

def main():
    N, K = map(int, input().split())
    que = deque([i for i in range(1,N+1)])
    answer =yosepus(que,K)
    print("<" + ", ".join(str(x) for x in answer) + ">")


if __name__ == "__main__":
    main()