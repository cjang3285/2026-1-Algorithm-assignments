# CSE304-2026-1-Algorithms
# Week11-6.2.knapsack.0-1.bb_bestfs_problem.py

from heapq import heappush, heappop

class Node:
    def __init__(self, level, weight, profit):
        # 현재 노드가 결정한 아이템 깊이(몇 번째 아이템까지 결정했는지)
        self.level = level
        # 현재까지 선택한 아이템들의 누적 무게
        self.weight = weight
        # 현재까지 선택한 아이템들의 누적 이익
        self.profit = profit
        # 이 노드에서 앞으로 얻을 수 있는 "총 이익 상한(누적 포함)"
        self.bound = 0


def boundof(u, n, W, w, p):
    # 이미 용량을 넘겼다면 유효하지 않으므로 상한을 0으로 반환
    if u.weight >= W:
        return 0
    else:
        # 상한 계산은 현재 누적 이익에서 시작
        profit_bound = u.profit
        # 다음으로 고려할 아이템 인덱스
        j = u.level + 1
        # 현재 누적 무게에서 시작
        total_weight = u.weight

        # 남은 아이템을 통째로 담을 수 있는 만큼 담아 상한을 계산
        while j <= n and total_weight + w[j] <= W:
            # 아이템 j의 무게를 누적
            total_weight += w[j]
            # 아이템 j의 이익을 누적
            profit_bound += p[j]
            # 다음 아이템으로 이동
            j += 1

        # 더 이상 통째로 못 담는 첫 아이템은 분수 배낭 방식으로 일부만 반영
        if j <= n:
            profit_bound += (W - total_weight) * (p[j] / w[j])

        # 이 노드에서 가능한 최대 총이익 상한 반환
        return profit_bound


def knapsack3(n, W, w, p):
    global count
    # Best-First Search를 위한 힙(우선순위 큐)
    heap = []  # Initialize Queue
    # 루트 노드: 아직 아무 아이템도 결정하지 않은 상태
    v = Node(0, 0, 0)
    # 루트의 상한 계산
    v.bound = boundof(v, n, W, w, p)
    # 지금까지 찾은 최대 이익
    maxprofit = 0

    # bound가 같을 때 Node 비교 오류를 피하기 위한 증가 카운터
    counter = 0
    # 파이썬 heapq는 최소 힙이므로 -bound를 넣어 최대 bound 우선으로 동작시킴
    heappush(heap, (-v.bound, counter, v))
    # 다음 삽입을 위해 카운터 증가
    counter += 1

    # 힙이 빌 때까지 가장 유망(bound 최대)한 노드부터 확장
    while len(heap) != 0:
        # 우선순위가 가장 높은 노드(= bound 최대)를 꺼냄
        _, _, v = heappop(heap)

        # 상한이 현재 최적보다 크고 아직 마지막 레벨 전이면 자식 확장
        if v.bound > maxprofit and v.level < n:
            # 왼쪽 자식: 다음 아이템을 선택한 경우
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
            # 유효한 무게이고 이익이 더 좋으면 최적 이익 갱신
            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit
            # 왼쪽 자식의 상한 계산
            u.bound = boundof(u, n, W, w, p)
            # 아직 희망이 있으면 힙에 삽입
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, counter, u))
                # 삽입 후 카운터 증가
                counter += 1

            # 오른쪽 자식: 다음 아이템을 선택하지 않은 경우
            u = Node(v.level + 1, v.weight, v.profit)
            # 오른쪽 자식의 상한 계산
            u.bound = boundof(u, n, W, w, p)
            # 상한이 현재 최적보다 크면 힙에 삽입
            if u.bound > maxprofit:
                heappush(heap, (-u.bound, counter, u))
                # 삽입 후 카운터 증가
                counter += 1

    # 최종 최대 이익 반환
    return maxprofit


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_knapsack(n, W, w, p, expected_profit):
    print(f"\n--- 테스트 케이스: n = {n}, W = {W} ---")
    print(f"weights: {w[1:]}")
    print(f"profits: {p[1:]}")
    
    maxprofit = knapsack3(n, W, w, p)
    
    print(f"최대 이익: {maxprofit}")
    
    if maxprofit == expected_profit:
        print("✅ 테스트 통과: 정답입니다!")
    else:
        print(f"❌ 테스트 실패: 예상 이익은 {expected_profit}이지만, {maxprofit}을 찾았습니다.")
    
    print("-" * 40)
    return maxprofit


def main():
    n, W = 4, 16
    w = [0] + [2, 5, 10, 5]
    p = [0] + [40, 30, 50, 10]
    test_knapsack(n, W, w, p, 90)

    n, W = 3, 10
    w = [0] + [2, 5, 7]
    p = [0] + [20, 30, 35]
    test_knapsack(n, W, w, p, 55)

    n, W = 5, 15
    w = [0] + [4, 1, 2, 1, 12]
    p = [0] + [10, 2, 2, 1, 4]
    test_knapsack(n, W, w, p, 15)


if __name__ == "__main__":
    main()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example (Custom)
# test_knapsack(n, W, w, p, expected_profit)