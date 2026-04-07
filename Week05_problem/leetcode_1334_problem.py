# CSE304-2026-1-Algorithms
# Week05-leetcode_1334_problem.py
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

# •문제: n개의 도시가 주어진다. 각 도시는 양방향 간선으로 연결되어 있으며, 간선에는 가중치가 있다. 각 도시에 대해 distanceThreshold 이하로 도달 가능한 다른 도시들의 개수를 구하고, 그 수가 가장 적은 도시의 번호를 출력하라. 
# •입력: 함수의 첫 번째 매개변수 n은 도시의 수를 의미하며, 2 ≤ n ≤ 100 이다. 두 번째 매개변수 edges 는 간선 정보를 담은 2차원 리스트로, 각 요소는 [fromi, toi, weighti] 형태로 주어진다. 이는 두 도시 fromi와 toi 사이를 연결하는 가중치 weighti의 양방향 간선을 의미한다. 간선의 수는 1 ≤ len(edges) ≤ n*(n-1)/2 이다. 세 번째 매개변수 distanceThreshold 는 경로의 최대 거리로 1 ≤ distanceThreshold ≤ 10^4이다.실습 3 (leetcode_1334_problem.py)
# •출력: 가장 적은 수의 도달 가능한 도시를 가지는 도시 번호를 반환한다. (단, 후보가 여러 개일 경우 그 중 도시 번호가 가장 큰 도시의 번호를 출력
#
# 핵심 직관:
# - 먼저 모든 도시쌍의 최단거리를 dist에 다 구해 둔다.
# - 그 과정도 결국 각진 경로를 잘게 쪼개서 곡선처럼 더 매끈한 최단거리로 다듬는 느낌이다.
# - 그다음 각 도시에서 threshold 이하로 닿는 다른 도시 수만 센다.
# - 결국 "가장 적게 닿는 도시"를 찾고, 동률이면 번호가 큰 도시를 고른다.
from typing import List

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # dist[행][열] = 행 도시에서 열 도시로 가는 최단거리
    # 내 해석:
    # - 각 도시쌍의 최단거리를 먼저 전부 구해 둔다.
    # - 그다음 threshold 이하로 도달 가능한 도시 수를 각 도시마다 센다.
    # - 가장 적은 도시를 고르고, 동률이면 번호가 큰 도시를 고른다.
    dist = [[float('inf')] * n for _ in range(n)]

    # 자기 자신까지의 거리는 0
    for i in range(n):
        dist[i][i] = 0

    # 양방향 간선이므로 두 방향을 같이 넣는다.
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # Floyd-Warshall:
    # k를 하나씩 중간 정점으로 허용하면서
    # 각 (i, j) 쌍의 최단거리를 계속 갱신한다.
    #
    # 예시 1처럼 보면:
    #   초기 dist는 간선 정보만 가진 상태다.
    #   예: 0->1 = 3, 1->2 = 1, 2->3 = 1
    #
    #   k=1을 허용하면
    #   0->3은 0->1->3 = 3+4 = 7
    #   0->2는 0->1->2 = 3+1 = 4
    #   이런 식으로 "중간 도시를 하나 끼웠을 때 더 짧아지는지"를 본다.
    #
    #   k를 0,1,2,...로 늘리면서
    #   각 도시쌍의 최단거리가 자기 최선값으로 계속 줄어든다.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # 이제 각 도시가 threshold 이하로 도달 가능한 도시 수를 센다.
    # count가 더 작으면 갱신, 같으면 번호가 더 큰 도시를 선택.
    city = -1 # 최종 출력할 도시 번호, 도달가능한 도시 수가 가장 적은 출발 도시의 번호.
    min_count = float('inf')
    for i in range(n): # 각 도시 i에서
        count = 0 # i에서 threshold 이하로 도달 가능한 도시 수
        for j in range(n): # 도시 j에 대해
            if i != j and dist[i][j] <= distanceThreshold: # i와 j가 서로 다른 도시이고, i에서 j로 가는 최단거리가 threshold 이하이면
                count += 1 # i의 도달가능 도시 수++
        if count < min_count or (count == min_count and i > city): # count가 더 작으면 문제가 요구하는 출력인 가장 도달가능 도시수가 적은 도시 번호로 갱신, 같으면 고유번호가 더 큰 도시를 선택
            min_count = count
            city = i

    return city 

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_findTheCity(n: int, edges: List[List[int]], distanceThreshold: int, expected: int):
    print("Before computation")
    print(f"n = {n}, distanceThreshold = {distanceThreshold}")
    print(f"edges = {edges}")

    result = findTheCity(n, edges, distanceThreshold)

    print(f"After computation: result = {result}")

    if result == expected:
        print("✅Test Passed!")
    else:
        print("❌Test Failed!")
        print(f"Expected result: {expected}")
        print(f"Your Result: {result}")
    print("-" * 40)


print("**************Testing findTheCity()**************")

print("######Example 1######")
test_findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4, 3)

print("######Example 2######")
test_findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2, 0)

print("######Example 3######")
test_findTheCity(6, [[0,1,10],[1,2,10],[2,3,10],[3,4,10],[4,5,10]], 20, 5)

print("######Example 4######")
test_findTheCity(2, [[0,1,5]], 2, 1)

print("######Example 5######")
test_findTheCity(9, [[0,1,1],[1,2,2],[2,3,3],[3,4,4],[4,5,5],[5,6,6],[6,7,7],[7,8,8]], 20, 8)

print("######Example 6######")
test_findTheCity(15, [
    [0,1,1],[1,2,2],[2,3,3],[3,4,4],[4,5,5],
    [5,6,6],[6,7,7],[7,8,8],[8,9,9],[9,10,10],
    [10,11,11],[11,0,12]
], 55, 14)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 7 (Custom)
# test_findTheCity(n, edges, distanceThreshold, expected)