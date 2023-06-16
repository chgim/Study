def find_minimum_cost(N, M, K, S, T, roads):
    # 그래프 생성
    graph = {i: [] for i in range(1, N+1)}
    for u, v, w in roads:
        graph[u].append((v, w))

    # 최소 비용과 방문 여부를 저장하는 배열
    distance = [float('inf')] * (N+1)
    visited = [False] * (N+1)

    # 스택을 활용한 DFS
    stack = [(S, 0)]  # (도시, 비용)
    distance[S] = 0

    while stack:
        node, cost = stack.pop()

        if visited[node]:
            continue

        visited[node] = True

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                stack.append((next_node, new_cost))

    # 최소 비용 계산
    if distance[T] % K != 0:
        return "IMPOSSIBLE"

    return distance[T]

# 입력
N = 4
M = 5
K = 1
S = 1
T = 4
roads = [(1, 2, 2), (1, 3, 3), (2, 3, 5), (2, 4, 5), (3, 4, 6)]

# 최소 이용료 합 계산
result = find_minimum_cost(N, M, K, S, T, roads)
print(result)