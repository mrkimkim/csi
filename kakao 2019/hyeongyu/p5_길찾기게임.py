import sys

x = 10000
sys.setrecursionlimit(x)

# Parent가 없는 노드가 Root다.
def get_root(graph):
    for i in range(len(graph)):
        if graph[i][0] == -1:
            return i

# DFS
def dfs(cur, graph):
    ret = [cur + 1]
    if graph[cur][1] != -1:
        ret += dfs(graph[cur][1], graph)
    if graph[cur][2] != -1:
        ret += dfs(graph[cur][2], graph)
    return ret

# BFS
def bfs(cur, graph):
    ret = []
    if graph[cur][1] != -1:
        ret += bfs(graph[cur][1], graph)
    if graph[cur][2] != -1:
        ret += bfs(graph[cur][2], graph)
    return ret + [cur + 1]


def solution(nodeinfo):
    nodes = {}
    graph = []
    # 각 노드에 대해 [Parent, Left Child, Right Child, Left boundary, Right boundary]
    # 각 Boundary는 노드의 child가 가질 수 있는 x의 범위를 규정한다.
    # Parent A를 갖는 노드 B가 Child C를 가질 때, C의 x가 parent를 넘어가선 안되기 때문이다.
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        graph.append([-1, -1, -1, -1, 10000000])
        if y not in nodes:
            nodes[y] = []
        # 같은 레벨의 노드는 같은 y를 가지므로, 같은 y를 가지는 것끼리 묶는다.
        nodes[y].append([x, i])

    # y가 클수록 레벨이 낮으므로, y역순으로 다음 레벨에서 child를 찾는다.
    y_list = list(nodes.keys())
    y_list.sort(reverse=True)
    for y in y_list:
        nodes[y].sort()

    for i in range(len(y_list) - 1):
        y = y_list[i]
        # 다음 레벨의 노드들을 탐색하는데 쓸 인덱스
        k = 0
        # 현재 레벨의 노드들에 대해
        for j in range(len(nodes[y])):
            cur = nodes[y][j]
            next_y = y_list[i + 1]
            # 다음 레벨의 child 후보들에 대해
            while k < len(nodes[next_y]):
                child_candidate = nodes[next_y][k]
                # 왼쪽 child가 가능한지
                # 현재 노드보다 왼쪽에 있고, 노드의 left boundary 보다는 오른쪽
                if cur[0] > child_candidate[0] and graph[cur[1]][3] < child_candidate[0]:
                    graph[cur[1]][1] = child_candidate[1]
                    graph[child_candidate[1]][0] = cur[1]
                    graph[child_candidate[1]][3] = graph[cur[1]][3]
                    graph[child_candidate[1]][4] = cur[0]
                    k += 1
                # 현재 노드보다 오른쪽에 있고, 노드의 right boundary 보다는 왼쪽
                elif cur[0] < child_candidate[0] and graph[cur[1]][4] > child_candidate[0]:
                    graph[cur[1]][2] = child_candidate[1]
                    graph[child_candidate[1]][0] = cur[1]
                    graph[child_candidate[1]][3] = cur[0]
                    graph[child_candidate[1]][4] = graph[cur[1]][4]
                    k += 1
                else:
                    break
    # dfs, bfs 결과를 출력
    return ([dfs(get_root(graph), graph), bfs(get_root(graph), graph)])