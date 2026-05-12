# CSE304-2026-1-Algorithms
# Week09-5.1.nqueens_problem.py

def promising(i, n, col):
    """행 `i`에 놓은 퀸이 이전 퀸들과 충돌하지 않는지 검사한다.

    매개변수:
    - i (int): 방금 퀸을 놓은 행 인덱스 (1부터 시작).
    - n (int): 보드 크기 / 총 퀸 수.
    - col (list): 1부터 사용하는 리스트로, col[r]는 r행에 놓인 퀸의 열을 나타낸다.

    반환값:
    - bool: 이전 퀸들과 충돌이 없으면 True, 있으면 False.
    """
    is_promising = True  # 현재까지 놓은 퀸 배치가 가능하다고 가정한다.
    k = 1  # 이전 행들을 처음부터 하나씩 검사한다.
    while k < i and is_promising:  # 이전 퀸들과 충돌이 없는지 확인한다.
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:  # 같은 열이거나 대각선이면 실패다.
            is_promising = False  # 더 볼 필요 없이 현재 배치는 불가능하다.
        k += 1  # 다음 이전 행으로 이동한다.
    return is_promising  # 충돌이 없으면 True, 있으면 False를 돌려준다.


def nqueens(i, n, col, solutions):
    """모든 N-Queens 해법을 찾기 위한 재귀적 백트래킹 함수.

    매개변수:
    - i (int): 마지막으로 채운 행의 인덱스 (퀸을 하나도 놓지 않았을 때는 0).
    - n (int): 보드 크기 / 놓아야 할 퀸 수.
    - col (list): 1부터 사용하는 리스트로, 각 행의 열 위치를 기록한다.
    - solutions (list): 찾아낸 해법들을 추가할 리스트 (각 해법은 열 번호 리스트).
    """
    if promising(i, n, col):  # 지금까지의 배치가 괜찮을 때만 다음 단계로 간다.
        if i == n:  # n번째 행까지 모두 퀸을 놓았으면 해답 하나를 찾은 것이다.
            solutions.append(col[1:].copy())  # 현재 배치를 해답 목록에 저장한다.
            print("found=", col[1:])  # 찾은 해답을 화면에 출력한다.
        else:  # 아직 더 놓아야 할 행이 남아 있다.
            for j in range(1, n + 1):  # 다음 퀸을 1열부터 n열까지 하나씩 시도한다.
                col[i + 1] = j  # 다음 행의 퀸을 j열에 놓아본다.
                nqueens(i + 1, n, col, solutions)  # 재귀적으로 다음 행을 탐색한다.


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_nqueens(n, expected_solutions):
    col = [0] * (n + 1)
    solutions = []
    
    print(f"\n--- 테스트 케이스: n = {n} ---")
    print(f"{n}-Queens 문제에 대한 모든 해법 찾기:")
    
    nqueens(0, n, col, solutions)
    
    if solutions:
        print(f"총 {len(solutions)}개의 해법을 찾았습니다.")
    else:
        print("해법이 존재하지 않습니다.")
    
    expected_sorted = sorted([tuple(e) for e in expected_solutions])
    solutions_sorted = sorted([tuple(s) for s in solutions])
    
    if solutions_sorted == expected_sorted:
        print("✅ 테스트 통과: 정답입니다.")
    else:
        print("❌ 테스트 실패: 오답입니다.")
        
        missing = [list(e) for e in expected_sorted if e not in solutions_sorted]
        if missing:
            print(f"  누락된 해법: {missing}")
        
        extra = [list(s) for s in solutions_sorted if s not in expected_sorted]
        if extra:
            print(f"  잘못 찾은 해법: {extra}")
    
    print("-" * 40)
    return solutions


if __name__ == "__main__":   
    test_nqueens(4, [[2, 4, 1, 3], [3, 1, 4, 2]])
    test_nqueens(2, [])
    test_nqueens(5, [[1, 3, 5, 2, 4], [1, 4, 2, 5, 3], [2, 4, 1, 3, 5], [2, 5, 3, 1, 4],
                    [3, 1, 4, 2, 5], [3, 5, 2, 4, 1], [4, 1, 3, 5, 2], [4, 2, 5, 3, 1],
                    [5, 2, 4, 1, 3], [5, 3, 1, 4, 2]])
    test_nqueens(6, [[2, 4, 6, 1, 3, 5], [3, 6, 2, 5, 1, 4], [4, 1, 5, 2, 6, 3], [5, 3, 1, 6, 4, 2]])

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# test_nqueens(8, [...])