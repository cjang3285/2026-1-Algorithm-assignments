# CSE304-2026-1-Algorithms
# Week05-3.4.floyd2_problem.py

# 실습 2 (3.4.floyd2_problem.py)
# •문제: 가중치 포함 그래프의 각 정점에서 다른 모든 정점까지의 최단거리를 계산하라.
# •입력: 가중치 포함 방향성 그래프 W와 그 그래프에서의 정점의 수n.
# •출력: 최단경로의 길이가 포함된 배열 D, 그리고 최단경로 출력을 위한 배열 P.
#
# 핵심 직관:
# - 마치 각진 여러 경로들을 잘게 쪼개서 곡선처럼 더 매끈한 최단경로로 다듬는 느낌이다.
# - 각 정점쌍 (i, j)는 자기 구간의 최단거리만 따로 기억한다.
# - k를 하나씩 경유 정점으로 허용하면서 더 짧은 조각이 있으면 D와 P를 갱신한다.
# - P는 경로 전체가 아니라, 그 구간을 다시 둘로 쪼개는 기준점 하나만 저장한다.
# - 그래서 작은 구간들의 최단이 재귀로 이어지면 전체 최단경로가 복원된다.

def floyd2(n, W):
    # D[행][열] = 행 정점 -> 열 정점 최단거리
    # P[행][열] = 그 최단경로를 반으로 쪼갤 때의 중간 정점 k
    #
    # 왜 D와 P를 따로 만드는가?
    # - D[i][j]는 i에서 j까지 최단거리만 기억한다.
    # - P[i][j]는 i에서 j까지 최단경로를 반으로 쪼갤 때의 중간 정점 k만 기억한다.
    # - 마치 각진 여러 경로들을 잘게 쪼개서 곡선처럼 더 매끈한 최단경로로 다듬는 느낌이다.
    # - 각 (i, j) 칸은 자기 구간의 최단만 기억한다.
    # - 경유 정점이 여러 개면, 그건 한 칸에 누적 저장하지 않는다.
    # - 대신 작은 구간들의 P 칸에 나뉘어 저장된다.
    # - path(i, j)는 그 조각들을 재귀로 다시 이어 붙여 전체 경로를 만든다.
    #
    # 예:
    #   P[1][3] = 9
    #   P[1][9] = 7
    # 이면 path(1, 3)은 1 -> 7 -> 9 -> 3처럼 복원된다.
    P = [[-1] * n for _ in range(n)]
    D = [row[:] for row in W]
    # Complete the code here

    # 반복문 순서:
    #   k: 경유 정점을 하나씩 허용
    #   i: 출발 정점(행)
    #   j: 도착 정점(열)
    #
    # 갱신 규칙:
    #   현재 D[i][j]
    #   vs D[i][k] + D[k][j]
    #   더 짧으면 D[i][j]를 바꾸고 P[i][j] = k
    #
    # 행/열 번호를 붙여 보면 각 칸이 자기 최단만 따로 기억한다.
    # 예: Example 2 초기 D
    #       열0 열1 열2 열3
    # 행0   [ 0,  3, INF,  7]
    # 행1   [ 8,  0,  2, INF]
    # 행2   [ 5, INF,  0,  1]
    # 행3   [ 2, INF, INF,  0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    return D, P


def path(i, j):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end=" ")
        path(k, j)


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_floyd(n, W, expected_D=None, path_start=None, path_end=None):
    print("Before Floyd-Warshall computation")
    global P
    D, P = floyd2(n, W)
    print("After computation (D and P):")

    print("D = ")
    for row in D:
        print(row)
    print("P = ")
    for row in P:
        print(row)

    if path_start is not None and path_end is not None:
        print(f"Path from v{path_start} to v{path_end}: ", end="")
        path(path_start, path_end)
        print()

    if expected_D is not None:
        correct = True
        for i in range(n):
            for j in range(n):
                if D[i][j] != expected_D[i][j]:
                    correct = False
                    print(f"Mismatch at D[{i}][{j}]: Expected {expected_D[i][j]}, got {D[i][j]}")
        if correct:
            print("✅Test Passed!")
        else:
            print("❌Test Failed!")
    print("-" * 40)


INF = float("inf")

print("**************Testing floyd2()**************")

print("######Example 1######")
n1 = 5
W1 = [
    [0, 1, INF, 1, 5],
    [9, 0, 3, 2, INF],
    [INF, INF, 0, 4, INF],
    [INF, INF, 2, 0, 3],
    [3, INF, INF, INF, 0]
]
expected_D1 = [
    [0, 1, 3, 1, 4],
    [8, 0, 3, 2, 5],
    [10, 11, 0, 4, 7],
    [6, 7, 2, 0, 3],
    [3, 4, 6, 4, 0]
]
test_floyd(n1, W1, expected_D1, 4, 2)

print("######Example 2######")
n2 = 4
W2 = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
expected_D2 = [
    [0, 3, 5, 6],
    [5, 0, 2, 3],
    [3, 6, 0, 1],
    [2, 5, 7, 0]
]
test_floyd(n2, W2, expected_D2, 0, 2)

print("######Example 3######")
n3 = 6
W3 = [
    [0, 6, INF, INF, INF, 8],
    [3, 0, 2, INF, INF, INF],
    [INF, INF, 0, 1, 7, INF],
    [INF, INF, INF, 0, 2, INF],
    [INF, 4, INF, INF, 0, 5],
    [INF, INF, INF, 4, 6, 0]
]
expected_D3 = [
    [0, 6, 8, 9, 11, 8],
    [3, 0, 2, 3, 5, 10],
    [10, 7, 0, 1, 3, 8],
    [9, 6, 8, 0, 2, 7],
    [7, 4, 6, 7, 0, 5],
    [13, 10, 12, 4, 6, 0]
]
test_floyd(n3, W3, expected_D3, 0, 4)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_floyd(n, W, expected_D, start, end)