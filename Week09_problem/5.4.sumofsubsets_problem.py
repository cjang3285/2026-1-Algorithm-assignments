# CSE304-2026-1-Algorithms
# Week09-5.4.sumofsubsets_problem.py

def promising(i, weight, total):
    """현재 분기에서 목표 합 `W`에 도달할 가능성이 남아있는지 판단한다.

    사용 전역변수: `n` (항목 수), `W` (목표 합), `w` (무게 리스트), `include` (선택 플래그).

    매개변수:
    - i (int): 마지막으로 고려한 항목의 인덱스 (-1이 초기값, 항목은 0부터).
    - weight (int): 현재까지 선택된 항목들의 합.
    - total (int): 아직 고려하지 않은 항목들의 전체 합 (i+1부터 끝까지).

    반환값:
    - bool: 이 상태에서 `W`에 도달할 가능성이 있으면 True, 없으면 False.
    """
    global n, W, w, include
    is_promising = True  # 현재 상태가 유망하다고 가정한다.

    # 남은 모든 수를 더해도 목표 W에 도달하지 못하면 더 볼 필요가 없다.
    if weight + total < W:
        is_promising = False

    # 현재 합이 이미 W와 같으면 해답이 될 수 있다.
    elif weight == W:
        is_promising = True

    # 다음 수를 하나 더 넣어도 W를 넘지 않으면 계속 탐색할 수 있다.
    elif i + 1 < n and weight + w[i + 1] <= W:
        is_promising = True

    # 위 조건에 걸리지 않으면 더 진행할 의미가 없다.
    else:
        is_promising = False

    return is_promising  # 지금 상태가 유망하면 True, 아니면 False를 반환한다.


def sumofsubsets(i, weight, total):
    """합이 `W`가 되는 부분집합들을 열거하는 백트래킹 함수.

    매개변수:
    - i (int): 마지막으로 고려한 항목의 인덱스 (-1이 초기값).
    - weight (int): 현재 포함된 항목들의 합.
    - total (int): 남은 항목들의 합 (i+1부터 끝까지).

    사용 전역변수: `n`, `W`, `w`, `include`, `solutions`.
    """
    global n, W, w, include, solutions
    if promising(i, weight, total):  # 현재 상태가 가능성 있는 경우에만 재귀를 진행한다.
        if weight == W:  # 목표 합에 정확히 도달하면 해답 하나를 찾은 것이다.
            print("found:", [w[j] for j in range(n) if include[j]])  # 선택된 수들을 출력한다.
            solutions.append([w[j] for j in range(n) if include[j]])  # 해답 목록에 저장한다.
        else:  # 아직 목표 합에 도달하지 못했으면 다음 수를 선택해 본다.
            include[i + 1] = 1  # 다음 수를 포함하는 경우를 먼저 탐색한다.
            sumofsubsets(i + 1, weight + w[i + 1], total - w[i + 1])  # 포함했을 때의 상태로 재귀 호출한다.

            include[i + 1] = 0  # 같은 위치에서 이번에는 포함하지 않는 경우를 탐색한다.
            sumofsubsets(i + 1, weight, total - w[i + 1])  # 제외했을 때의 상태로 재귀 호출한다.


def sumofsubsets_solver(n_val, W_val, w_val):
    """전역 변수를 초기화하고 백트래킹 탐색을 시작하는 헬퍼 함수.

    매개변수:
    - n_val (int): 항목 수.
    - W_val (int): 찾고자 하는 목표 합.
    - w_val (list[int]): 항목들의 무게 리스트 (길이는 `n_val`).

    반환값:
    - list[list[int]]: 찾은 부분집합들의 리스트 (각 부분집합은 합이 `W_val`인 무게들의 리스트).
    """
    global n, W, w, include, solutions
    
    n = n_val  # 입력으로 받은 원소 개수를 저장한다.
    W = W_val  # 만들고 싶은 목표 합을 저장한다.
    w = w_val  # 탐색할 숫자 배열을 저장한다.
    include = [0] * n  # 각 수를 선택했는지 기록할 배열을 준비한다.
    solutions = []  # 찾은 모든 부분집합을 저장할 리스트를 만든다.

    sumofsubsets(-1, 0, sum(w))  # 아직 아무 것도 고르지 않은 상태에서 탐색을 시작한다.
    return solutions  # 찾은 해답들을 반환한다.


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_sumofsubsets(n, W, w, expected_subsets):
    print(f"\n--- 테스트 케이스: n = {n}, W = {W}, w = {w} ---")
    actual_subsets = sumofsubsets_solver(n, W, w)
    if set(tuple(sorted(subset)) for subset in actual_subsets) == set(
        tuple(sorted(subset)) for subset in expected_subsets
    ):
        print("✅ 테스트 통과: 정답입니다.")
    else:
        print("❌ 테스트 실패:")
        print("  예상된 부분집합:")
        for subset in expected_subsets:
            print(f"    {subset}")
        print("  실제 출력된 부분집합:")
        for subset in actual_subsets:
            print(f"    {subset}")


def main():
    test_sumofsubsets(4, 13, [3, 4, 5, 6], [[3, 4, 6]])
    test_sumofsubsets(5, 10, [1, 2, 3, 4, 5], [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]])
    test_sumofsubsets(4, 7, [2, 4, 6, 8], [])


if __name__ == "__main__":
    main()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_sumofsubsets(n, W, w, expected_subsets)