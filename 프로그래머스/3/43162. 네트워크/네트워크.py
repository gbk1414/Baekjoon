def solution(n, computers):
    def dfs(node, visited, computers):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in range(n):
                if computers[current][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    answer = 0
    visited = set()

    for i in range(n):
        if i not in visited:
            dfs(i, visited, computers)
            answer += 1

    return answer