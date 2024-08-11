import sys
input = sys.stdin.readline

def union(parent_a, parent_b):
    root_a = find(parent_a)
    root_b = find(parent_b)
    parents[root_b] = root_a

def find(node):
    if node != parents[node]:
        parents[node] = find(parents[node])  # 경로 압축
    return parents[node]

# 좌표를 x, y, z 별로 저장하고 정렬
n = int(input())
x_coords, y_coords, z_coords = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    x_coords.append((x, i))
    y_coords.append((y, i))
    z_coords.append((z, i))
x_coords.sort()
y_coords.sort()
z_coords.sort()

# 인접한 행성들끼리 간선 구성
edges = []
for coord_list in (x_coords, y_coords, z_coords):
    for i in range(1, n):
        weight_a, index_a = coord_list[i - 1]
        weight_b, index_b = coord_list[i]
        edges.append((abs(weight_a - weight_b), index_a, index_b))
edges.sort(reverse=True)

# 크루스칼 알고리즘 진행
parents = [i for i in range(n + 1)]
remaining_edges, total_cost = n - 1, 0
while remaining_edges:
    weight, planet_a, planet_b = edges.pop()
    if find(planet_a) == find(planet_b):
        continue
    union(planet_a, planet_b)
    remaining_edges -= 1
    total_cost += weight

print(total_cost)
