# CSE304-2026-1-Algorithms
# Week08-4.7.0-1_knapsack_problem.py

def knapsack(n, W, DP):
    # 함수 매개변수 의미:
    # n: 처리할 아이템의 개수 (1부터 n번째 아이템까지 고려)
    #    예: n=3이면 w[0], w[1], w[2] (3개 아이템)을 고려
    #    매 재귀호출마다 n이 감소 (n-1로 호출)
    # 
    # W: 남은 용량 (현재 배낭에 더 넣을 수 있는 공간)
    #    초기값: 배낭의 전체 용량
    #    재귀호출: W - w[n-1] (아이템을 선택하면 용량 감소)
    # 
    # DP: 메모이제이션용 딕셔너리 (계산 결과 캐시)
    #    키: (n, W) 튜플
    #    값: knapsack(n, W)의 계산 결과 (최대 이익)
    #    이미 계산한 부분문제는 재계산하지 않고 여기서 조회
    
    # 메모이제이션 (Top-down) 방식: 큰 문제부터 작은 문제로 재귀적으로 해결
    # DP 딕셔너리에 계산 결과를 저장하여 같은 부분문제는 한 번만 계산
    # 예: (2, 30)이 여러 번 호출되면 첫 번째만 계산하고 나머지는 메모리에서 조회
    
    global w, p
    # 1. 이미 계산한 부분문제면 메모리에서 바로 반환
    if (n, W) in DP:
        return DP[(n, W)]

    # 2. 아이템이 없거나 용량이 0이면 이익은 0
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        # n은 "처리할 아이템 개수"를 의미하므로,
        # 실제 배열 인덱스는 n-1 (0-based indexing)
        # 예: n=3 → w[2], p[2] (3번째 아이템)
        #     n=2 → w[1], p[1] (2번째 아이템)
        #     n=1 → w[0], p[0] (1번째 아이템)
        if w[n - 1] > W:
            # 2. 현재 아이템의 무게가 용량을 초과하면 제외
            DP[(n, W)] = knapsack(n - 1, W, DP) # n-1로 호출하여 다음 아이템인 n-2로 넘어감
        else:
            # 3. 두 경우의 최대값 선택
            # Case 1: 현재 아이템 제외 → knapsack(n-1, W, DP) -> 다음 아이템인 n-2로 넘어감
            # Case 2: 현재 아이템 포함 → p[n-1] + knapsack(n-1, W-w[n-1], DP) -> 이번 아이템 n-1을 포함하고 다음 아이템인 n-2로 넘어감
            DP[(n, W)] = max(knapsack(n - 1, W, DP), p[n - 1] + knapsack(n - 1, W - w[n - 1], DP))
    return DP[(n, W)]


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_knapsack_01_dp(n, W, w_input, p_input, expected=None):
    global w, p
    w = w_input
    p = p_input

    print(f"아이템 수: {n}")
    print(f"배낭 용량: {W}")
    print(f"무게: {w}")
    print(f"이익: {p}")
    DP = {}
    maxprofit = knapsack(n, W, DP)
    print(f"maxprofit: {maxprofit}")
    if expected is not None:
        if maxprofit == expected:
            print("✅ 테스트 통과: maxprofit 일치")
        else:
            print(f"❌ 테스트 실패: 기대값 = {expected}, 출력값 = {maxprofit}")
    print("-" * 40)


if __name__ == "__main__":
    print("**************Testing knapsack()**************")

    print("######Example 1######")
    n1, W1 = 3, 30
    w1 = [5, 10, 20]
    p1 = [50, 60, 140]
    test_knapsack_01_dp(n1, W1, w1, p1, expected=200)

    print("######Example 2######")
    n2, W2 = 4, 50
    w2 = [10, 20, 30, 40]
    p2 = [60, 100, 120, 240]
    test_knapsack_01_dp(n2, W2, w2, p2, expected=300)

    print("######Example 3######")
    n3, W3 = 5, 15
    w3 = [2, 3, 4, 5, 9]
    p3 = [3, 4, 5, 8, 10]
    test_knapsack_01_dp(n3, W3, w3, p3, expected=20)

    print("######Example 4######")
    n4, W4 = 8, 35
    w4 = [3, 8, 7, 6, 12, 4, 5, 10]
    p4 = [8, 20, 18, 14, 30, 10, 12, 25]
    test_knapsack_01_dp(n4, W4, w4, p4, expected=88)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# test_knapsack_01_dp(n, W, w_input, p_input, expected)