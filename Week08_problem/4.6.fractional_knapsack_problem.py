# CSE304-2026-1-Algorithms
# Week08-4.6.fractional_knapsack_problem.py

from heapq import heappush, heappop

class Item:
    def __init__(self, id, weight, profit):
        self.id = id
        self.weight = weight
        self.profit = profit
        self.profit_per_weight = profit / weight

    def __lt__(self, other):
        return self.profit_per_weight > other.profit_per_weight


def knapsack_fractional(n, W, w, p):
    heap = []
    for i in range(n):
        item = Item(i + 1, w[i], p[i])
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit = 0
    total_weight = 0

    # Complete the code here
    while heap and total_weight < W:
        _, item = heappop(heap)
        if total_weight + item.weight <= W:
            maxprofit += item.profit
            total_weight += item.weight
        else:
            remain = W - total_weight
            maxprofit += item.profit_per_weight * remain
            total_weight += remain
    return maxprofit


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_knapsack_fractional(n, W, w, p, expected=None):
    print(f"아이템 수: {n}")
    print(f"배낭 용량: {W}")
    print(f"무게: {w}")
    print(f"이익: {p}")
    maxprofit = knapsack_fractional(n, W, w, p)
    print(f"maxprofit: {maxprofit}")
    if expected is not None:
        if abs(maxprofit - expected) < 1e-6:
            print("✅ 테스트 통과")
        else:
            print("❌ 테스트 실패: 기대값 =", expected, "출력값 =", maxprofit)
    print("-" * 40)


if __name__ == "__main__":
    print("**************Testing knapsack_fractional()**************")

    print("######Example 1######")
    n1, W1 = 3, 30
    w1 = [5, 10, 20]
    p1 = [50, 60, 140]
    test_knapsack_fractional(n1, W1, w1, p1, expected=220)

    print("######Example 2######")
    n2, W2 = 4, 50
    w2 = [10, 20, 30, 40]
    p2 = [60, 100, 120, 240]
    test_knapsack_fractional(n2, W2, w2, p2, expected=300)

    print("######Example 3######")
    n3, W3 = 5, 15
    w3 = [2, 3, 4, 5, 6]
    p3 = [3, 4, 5, 8, 6]
    test_knapsack_fractional(n3, W3, w3, p3, expected=21)

    print("######Example 4######")
    n4, W4 = 8, 34
    w4 = [3, 8, 7, 6, 12, 4, 5, 10]
    p4 = [8, 20, 18, 15, 30, 10, 12, 25]
    test_knapsack_fractional(n4, W4, w4, p4, expected=86)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# test_knapsack_fractional(n, W, w, p, expected)
