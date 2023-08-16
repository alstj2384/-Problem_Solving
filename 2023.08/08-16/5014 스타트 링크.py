from collections import deque
f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)
result = []
def bfs(s, c):
    queue = deque()
    queue.append((s, c))
    while queue:
        n, c = queue.popleft()
        if n == g:
            result.append(c)
            return
        for i in [u, -d]:
            k = n + i
            if k > f or k < 1:
                continue
            if visited[k] == 0:
                visited[k] = True
                queue.append((k, c+1))

bfs(s, 0)

if result:
    print(min(result))
else:
    print("use the stairs")

# 35분

