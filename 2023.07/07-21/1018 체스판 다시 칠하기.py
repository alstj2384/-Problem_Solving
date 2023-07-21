from collections import deque

# 크기를 8로 제한을 둬버린다 그러면 전체 크기 50이어도, 42

n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(input())

visited = [[0 for _ in range(m) for _ in range(n)]]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))

    while queue:
        x, y, c = queue.popleft()
        if m >= y + 8 and n >= x + 8:
            for dx, dy in [(0, 1), (1, 0)]:
                nx = x + dx
                ny = y + dy

                if not visited[nx][ny]:
                    if graph[nx][ny] != graph[x][y]:
                        queue.append((nx, ny))

        else :
            continue
