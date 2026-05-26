# CSE304-2026-1-Algorithms
# Week11-6.1.knapsack.0-1.bb_bfs_problem.py

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
    # 이미 용량을 넘겼다면 유효한 해가 아니므로 상한을 0으로 반환
    if u.weight >= W:
        return 0
    else:
        # 상한 계산은 현재 누적 이익에서 시작
        profit_bound = u.profit
        # 다음으로 고려할 아이템 인덱스(1-based 배열 사용)
        j = u.level + 1
        # 현재 누적 무게에서 시작
        total_weight = u.weight

        # 남은 아이템을 통째로 넣을 수 있는 동안 모두 넣어 상한을 키움
        while j <= n and total_weight + w[j] <= W:
            # 아이템 j를 통째로 넣었을 때의 무게 반영
            total_weight += w[j]
            # 아이템 j를 통째로 넣었을 때의 이익 반영
            profit_bound += p[j]
            # 다음 아이템으로 이동
            j += 1

        # 다음 아이템을 통째로 못 넣으면, 분수 배낭처럼 일부만 넣어 상한 계산
        if j <= n:
            profit_bound += (W - total_weight) * (p[j] / w[j])

        # 이 노드의 총 이익 상한 반환
        return profit_bound


def knapsack2(n, W, w, p):
    global count
    # BFS 탐색을 위한 큐
    queue = []  # Initialize Queue
    # 루트 노드: 아직 아무 아이템도 결정하지 않은 상태
    v = Node(0, 0, 0)
    # 루트 노드의 상한 계산
    v.bound = boundof(v, n, W, w, p)
    # 지금까지 찾은 최적(최대) 이익
    maxprofit = 0
    # 루트부터 큐에 삽입
    queue.append(v)

    # 큐가 빌 때까지 레벨 순서(BFS)로 탐색
    while len(queue) != 0:
        # 가장 먼저 들어온 노드를 꺼냄(FIFO)
        v = queue.pop(0)

        # "상한이 현재 최적보다 크고, 아직 마지막 아이템 전이면 확장 가치가 있음"
        if v.bound > maxprofit and v.level < n:
            # 왼쪽 자식: 다음 아이템을 "선택"한 경우
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
            # 무게 조건을 만족하고 이익이 더 좋으면 현재 최적 이익 갱신
            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit
            # 왼쪽 자식의 상한 계산
            u.bound = boundof(u, n, W, w, p)
            # 상한이 여전히 희망적이면 큐에 넣어 나중에 확장
            if u.bound > maxprofit:
                queue.append(u)

            # 오른쪽 자식: 다음 아이템을 "선택하지 않음" 경우
            u = Node(v.level + 1, v.weight, v.profit)
            # 오른쪽 자식의 상한 계산
            u.bound = boundof(u, n, W, w, p)
            # 상한이 현재 최적보다 크면 큐에 삽입
            if u.bound > maxprofit:
                queue.append(u)

    # 최종 최대 이익 반환
    return maxprofit


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_knapsack(n, W, w, p, expected_profit):
    print(f"\n--- 테스트 케이스: n = {n}, W = {W} ---")
    print(f"weights: {w[1:]}")
    print(f"profits: {p[1:]}")
    
    maxprofit = knapsack2(n, W, w, p)
    
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