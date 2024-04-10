from collections import deque

def dfs_recursive(V:int, visited: list[int], graph:list[list[int]])->list[int]:
    visited.append(V)

    for adj in graph[V]:
        if adj not in visited:
            dfs_recursive(adj, visited, graph)

    return visited

def bfs(V:int, graph:list[list[int]])->list[int]:
    visited = [V]
    que = deque([V])
    while que:
        node = que.popleft()
        for adj in graph[node]:
            if adj not in visited:
                que.append(adj)
                visited.append(adj)

    return visited



def main():
    [N, M, V] = map(int, input().split(" "))
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        [x, y] = list(map(int, input().split(" ")))
        graph[x].append(y)
        graph[y].append(x)
    
    # for i in graph:
    #     print(i)
    for lst in graph:
        lst.sort()

    dfs = dfs_recursive(V, [], graph)
    bfs_1 = bfs(V, graph)
    
    print(' '.join(map(str, dfs)))
    print(' '.join(map(str, bfs_1)))
    
    return

if __name__ == "__main__":
    main()