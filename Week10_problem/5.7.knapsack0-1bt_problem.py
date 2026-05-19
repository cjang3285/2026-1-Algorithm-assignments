# CSE304-2026-1-Algorithms
# Week10-5.7.knapsack0-1bt_problem.py

# 문제: 0/1 배낭 문제(분기한정, backtracking with bounding)
# 설명: n개 아이템들 중에서 무게의 합이 W 이하면서 이익의 합이 최대가 되는 아이템 집합 bestset을 찾는 문제입니다. 각 아이템은 무게 w[i]와 이익 p[i]를 가집니다.
#       각 아이템을 '포함' 또는 '미포함'으로 결정하며, 남은 용량을
#       이용해 이론상 얻을 수 있는 이익의 상한(bound)을 계산하여
#       더 이상 기대 이익이 없으면 분기하지 않는 방식으로 해결합니다.

def promising(i, weight, profit):
    global n, W, w, p, maxprofit
    # 파라미터 설명:
    # i: 마지막으로 결정한(처리한) 아이템 인덱스 (레벨). 초기에는 0.
    # weight: 현재까지 포함된 아이템들의 총 무게 (이전 상태의 누적값).
    # profit: 현재까지 포함된 아이템들의 총 이익 (이전 상태의 누적값).
    # 전역 변수 설명: n(아이템 수), W(배낭 용량), w(무게 배열, 1-based), p(이익 배열, 1-based), maxprofit(현재까지의 최댓값)

    # 목적: 현재 노드에서 앞으로 얻을 수 있는 이익의 상한(upper bound)을 계산.
    # 상한 계산 방법: fractional knapsack 완화를 사용.
    # - 다음 아이템들을 무게 허용 범위 내에서 전부 더하고
    # - 마지막으로 남는 용량이 있으면 그 다음 아이템을 부분적으로 넣는다고 가정
    # => 이렇게 계산한 bound가 현재 maxprofit보다 크면 이 노드는 유망함.

    j = i + 1           # 다음으로 고려할 아이템 인덱스
    bound = profit      # 현재까지의 이익을 시작값으로 사용
    totweight = weight  # 현재까지의 총 무게를 시작값으로 사용

    # 가능한 아이템들을 전부 더한다(정수 단위로 추가)
    while j <= n and totweight + w[j] <= W: # 남은 아이템이 있고, 다음 아이템을 추가해도 용량 초과가 안 되는 동안
        totweight += w[j]  # 아이템 j를 넣는다.
        bound += p[j]      # 아이템 j에서 얻는 이익을 더함
        j += 1             # 다음 아이템으로 이동

    # 아직 아이템이 남아있고
    # 다음 아이템을 부분적으로 넣는다고 가정하여 부분 이익을 더함
    if j <= n:
        remain = W - totweight # remain이 0보다 크면
        if w[j] > 0: # zero division 방지
            bound += p[j] * (remain / w[j])  # 부분 이익 비례 계산
            # 이 때 remain은 항상 0 이상이다. 왜냐하면 while문에서 totweight + w[j] > W가 되어야 탈출하므로 totweight <= W < totweight + w[j]가 성립한다. 따라서 remain = W - totweight >= 0이다.

    # 현재 계산된 최대 이익이 maxprofit보다 크면 유망하다고 판단
    return bound > maxprofit


# 자료구조를 반환하지 않고 전역 상태를 갱신합니다.
# knapsack 함수는 현재까지의 선택 상태를 include 배열에 기록하고, 최적해는 bestset 배열에 저장합니다. maxprofit은 현재까지 발견된 최대 이익을 저장합니다.
# 현재 노드가 "유효한 해 확인" 및 "최적해 갱신"
# 그리고 "유망한지 검사" 후 "분기"하는 함수입니다.

# 한줄로 요약하면 "여기가 정답인가? 정답이면 저장하자. 그리고 앞으로도 유망한지 검사해보자. 유망하면 분기하고 아니면 포기."
def knapsack(i, weight, profit): 
    global n, W, w, p, bestset, include, maxprofit
    # 파라미터 설명:
    # i: 마지막으로 결정된 아이템 인덱스(레벨)
    # weight: 현재까지 선택된 아이템들의 총 무게
    # profit: 현재까지 선택된 아이템들의 총 이익
    # 전역변수(사용 및 갱신되는 것들): bestset, include, maxprofit, n, W, w, p

    # --- 현재 노드가 "유효한 해인지 확인" 및 "최적해 갱신" ---
    if weight <= W and profit > maxprofit:
        # (조건) 현재 무게가 용량 이내이고, 현재 이익이 지금까지의 최고보다 크면
        maxprofit = profit
        # (작업) 현재 탐색 경로의 선택 상태(include)를 복사하여 bestset으로 저장
        for k in range(1, n + 1):
            bestset[k] = include[k]

    # --- 이 노드가 유망한지 검사하고 분기 진행 ---
    if promising(i, weight, profit): # 각 파라미터가 현 노드 상태를 의미
        # 현 노드에서 promising이 True면 더 확장할 가치가 있으므로 분기
        if i + 1 <= n: # 다음 아이템이 존재하면
            # (분기 A) 다음 아이템을 포함해보고
            include[i + 1] = 1
            # 포함했을 때의 누적 무게와 이익을 계산하여 재귀 호출
            knapsack(i + 1, weight + w[i + 1], profit + p[i + 1])
            # 백트래킹: 포함 표시를 되돌림
            include[i + 1] = 0

            # (분기 B) 다음 아이템을 포함하지 않는 경우
            # include[i+1]는 이미 0이므로 바로 재귀 호출
            knapsack(i + 1, weight, profit)


def knapsack_solver(n_val, W_val, w_val, p_val):
    global n, W, w, p, bestset, include, maxprofit

    # 파라미터 설명:
    # - n_val: 아이템 개수 (정수)
    # - W_val: 배낭 최대 허용 무게 (정수)
    # - w_val: 아이템 무게 리스트 (0-based list, 길이 n_val)
    # - p_val: 아이템 이익 리스트 (0-based list, 길이 n_val)

    # 전역 변수 초기화
    n = n_val              # 전체 아이템 수를 전역에 저장
    W = W_val              # 배낭 용량을 전역에 저장
    w = [0] + w_val        # 1-based 인덱스를 사용하기 위해 앞에 더미 0 추가
    p = [0] + p_val        # 1-based 인덱스 맞춤
    bestset = [0] * (n + 1)  # 최적해를 저장할 공간(1..n)
    include = [0] * (n + 1)  # 현재 탐색 경로의 선택 상태(1..n)
    maxprofit = 0          # 현재까지 발견된 최댓값 초기화

    # 탐색 시작: 아무 것도 결정되지 않은 상태에서 시작
    knapsack(0, 0, 0)

    # bestset은 1-based이므로 반환 시 0번째 요소를 제외
    return maxprofit, bestset[1:]


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_knapsack(n, W, w, p, expected_maxprofit, expected_bestsets=None):
    print(f"\n--- 테스트 케이스: n = {n}, W = {W}, w = {w}, p = {p} ---")
    actual_maxprofit, actual_bestset = knapsack_solver(n, W, w, p)

    print(f"maxprofit = {actual_maxprofit}")
    print(f"bestset = {actual_bestset}")

    ok = (actual_maxprofit == expected_maxprofit)

    if expected_bestsets is not None:
        ok = ok and (actual_bestset in expected_bestsets)

    if ok:
        print("✅ 테스트 통과: 정답입니다!")
    else:
        print("❌ 테스트 실패:")
        print(f"  예상된 maxprofit: {expected_maxprofit}, 실제: {actual_maxprofit}")
        if expected_bestsets is not None:
            print(f"  가능한 bestset 중 하나: {expected_bestsets}, 실제: {actual_bestset}")


def main():
    test_knapsack(
        4, 16,
        [2, 5, 10, 5],
        [40, 30, 50, 10],
        90, [[1, 0, 1, 0]]
    )

    test_knapsack(
        3, 7,
        [3, 4, 2],
        [20, 30, 10],
        50, [[1, 1, 0]]
    )


if __name__ == "__main__":
    main()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example (Custom)
# test_knapsack(n, W, w, p, expected_maxprofit, expected_bestsets)
