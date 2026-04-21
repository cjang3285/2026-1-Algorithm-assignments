# CSE304-2026-1-Algorithms
# Week07-4.1.prim_problem.py

def prim(n, W):
    F = []
    nearest = [-1] * (n + 1)
    distance = [-1] * (n + 1)
    
    # 초기 상태: Y = {v1}
    # 아직 Y에 없는 각 vi(=V-Y)는
    # nearest[i]: 현재 Y 중 vi에 가장 가까운 정점 번호
    # distance[i]: 그 거리
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
        
    # v1은 이미 Y에 있으므로, 나머지 n-1개 정점을 하나씩 Y로 편입
    for _ in range(n - 1):
        vnear = -1
        min = float("inf")

        # (첫 번째 루프)
        # V-Y의 각 vi가 들고 있는 distance[i]로 경쟁해서
        # 현재 Y와 가장 가까운 정점 vi를 vnear로 선택
        for i in range(2, n + 1):
            if 0 <= distance[i] < min:
                min = distance[i]
                vnear = i

        if vnear == -1:
            break

        # (중간 처리)
        # 당첨된 vnear를 Y에 편입:
        # nearest[vnear] (Y 쪽 정점) -- vnear (V-Y 쪽 정점) 간선을 F에 추가
        e = (nearest[vnear], vnear, W[nearest[vnear]][vnear])
        F.append(e)
        # distance[vnear] = -1 은 "이미 Y에 포함됨(방문 완료)" 표시
        distance[vnear] = -1

        # (두 번째 루프)
        # 새로 Y에 들어온 vnear를 기준으로,
        # 남은 V-Y의 각 vi가 "vnear가 기존 nearest보다 더 가까운지" 확인 후 갱신
        for i in range(2, n + 1):
            if W[i][vnear] < distance[i]:
                distance[i] = W[i][vnear]
                nearest[i] = vnear

    return F


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_prim_mst(n, W, expected=None):
    print(f"그래프 정점 수: {n}")
    print("인접 행렬:")
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if W[i][j] == float("inf"):
                row.append("INF")
            else:
                row.append(W[i][j])
        print(row)
    
    result = prim(n, W)
    print(f"최소 신장 트리 간선 (시작, 끝, 가중치): {result}")
    print(f"총 가중치: {sum(edge[2] for edge in result)}")
    
    if expected is not None:
        expected_weight = sum(edge[2] for edge in expected)
        actual_weight = sum(edge[2] for edge in result)
        
        if sorted([(e[0], e[1]) for e in result]) == sorted([(e[0], e[1]) for e in expected]) and \
           actual_weight == expected_weight:
            print("✅Test Passed! 최소 신장 트리가 일치합니다.")
        else:
            print("❌Test Failed!")
            print(f"Expected edges: {expected}")
            print(f"Your Result: {result}")
            print(f"Expected weight: {expected_weight}, Your weight: {actual_weight}")
    print("-" * 40)


INF = float("inf")

print("**************Testing prim()**************")
print("######Example 1######")
W1 = [
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 1, 3, INF, INF],
    [INF, 1, 0, 3, 6, INF],
    [INF, 3, 3, 0, 4, 2],
    [INF, INF, 6, 4, 0, 5],
    [INF, INF, INF, 2, 5, 0]
]
expected1 = [(1, 2, 1), (1, 3, 3), (3, 5, 2), (3, 4, 4)]
test_prim_mst(5, W1, expected1)

print("######Example 2######")
W2 = [
    [INF, INF, INF, INF, INF],
    [INF, 0, 10, 15, 20],
    [INF, 10, 0, 35, 25],
    [INF, 15, 35, 0, 30],
    [INF, 20, 25, 30, 0]
]
expected2 = [(1, 2, 10), (1, 3, 15), (1, 4, 20)]
test_prim_mst(4, W2, expected2)

print("######Example 3######")
W3 = [
    [INF, INF, INF, INF, INF, INF, INF],
    [INF, 0, 4, 2, INF, INF, INF],
    [INF, 4, 0, 1, 5, 2, INF],
    [INF, 2, 1, 0, 8, 3, INF],
    [INF, INF, 5, 8, 0, 7, 9],
    [INF, INF, 2, 3, 7, 0, 6],
    [INF, INF, INF, INF, 9, 6, 0]
]
expected3 = [(1, 3, 2), (3, 2, 1), (2, 5, 2), (5, 6, 6), (2, 4, 5)]
test_prim_mst(6, W3, expected3)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_prim_mst(n, W, expected)
