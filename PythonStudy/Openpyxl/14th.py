import heapq

def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if distance[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance

def find_minimum_cost(N, M, K, S, T, roads):
    graph = [[] for _ in range(N + 1)]

    for u, v, w in roads:
        graph[u].append((v, w))

    distances = dijkstra(graph, S)

    if distances[T] % K != 0:
        return "IMPOSSIBLE"

    return distances[T]

# 입력 예시
N = 4
M = 5
K = 1
S = 1
T = 4
roads = [(1, 2, 2), (1, 3, 3), (2, 3, 5), (2, 4, 5), (3, 4, 6)]

# 최소 이용료 합 계산
result = find_minimum_cost(N, M, K, S, T, roads)
print(result)