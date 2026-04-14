# CSE304-2026-1-Algorithms
# Week06-3.6.minmatrixmult_problem.py

# minimum(i, j, M, d)
# i: 부분 문제의 시작 행렬 번호 (Ai)
# j: 부분 문제의 끝 행렬 번호 (Aj)
# M: 최소 곱셈 횟수를 저장하는 DP 테이블
#    M[i][j] = Ai..Aj를 곱할 때 필요한 최소 스칼라 곱셈 횟수
# d: 행렬 차원 배열
#    Ai의 크기 = d[i-1] x d[i]
#    예: A1 = d[0]xd[1], A2 = d[1]xd[2], ..., An = d[n-1]xd[n]
# 반환값: (minvalue, mink)
#    minvalue = M[i][j]의 최소값
#    mink = 그 최소값을 만드는 분할 인덱스 k
def minimum(i, j, M, d):
    # 아직 어떤 k도 보지 않았으므로 최솟값을 무한대로 시작
    minvalue, mink = INF, 0
    # 분할점 k는 i <= k < j 범위
    for k in range(i, j):
        # 왼쪽 부분(Ai..Ak) 최소 비용 + 오른쪽 부분(Ak+1..Aj) 최소 비용
        # + 두 결과 행렬을 마지막에 한 번 곱하는 비용
        # 왼쪽 결과 행렬의 크기: d[i-1] x d[k]
        # 오른쪽 결과 행렬의 크기: d[k] x d[j]
        # 두 결과 행렬의 최종 결합을 위한 곱셈 비용: d[i-1] * d[k] * d[j]
        value = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
        # 더 작은 비용을 찾으면 최소값과 분할점 갱신
        if value < minvalue:
            minvalue = value
            mink = k

    # 이 (i, j) 구간의 최소 비용과 최적 분할점 반환
    return minvalue, mink 


# minmult(n, d)
# n: 행렬의 개수 (A1..An)
# d: 차원 배열 (길이 n+1)
#    A1 = d[0]xd[1], A2 = d[1]xd[2], ..., An = d[n-1]xd[n]
# 반환값: (M[1][n], M, P)
#    M[1][n] = 전체 연쇄 A1..An의 최소 곱셈 횟수
#    M = 최소 비용 DP 테이블
#    P = 최적 분할점 테이블 (P[i][j] = M[i][j]를 만드는 k)
def minmult(n, d):
    # 1-based 인덱스를 쓰기 위해 (n+1)x(n+1) 테이블 생성
    # 바깥 루프: for _ in range(n + 1) → 행(row)을 n+1개 만든다 -> 이는 열 n+1개라고 인식해도 무방하다
    # 안쪽: [INF] * (n + 1) → 각 행을 INF를 n+1개로 구성한다
    # 초기에는 모두 INF로 채워 미계산 상태를 나타냄
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    # 분할점 테이블 P는 정수 인덱스를 저장하므로 0으로 초기화
    P = [[0] * (n + 1) for _ in range(n + 1)]
    # 길이 1 구간(i==i)은 곱셈이 필요 없으므로 비용 0
    for i in range(n + 1): # 0부터 n까지 (1-based 인덱스 사용)
        M[i][i] = 0
    # diagonal = j-i 행렬i부터 행렬j까지의 행렬 개수를 의미, dp 테이블에서 
    # diagonal = 1이면 행렬 2개 구간, ... , diagonal=n-1이면 전체 구간
    for diagonal in range(1, n):
        # 시작 인덱스 i를 순회하며 끝 인덱스 j를 결정
        # i 최대값은 n-diagonal 이고, j=i+diagonal
        for i in range(1, n - diagonal + 1):
            # 현재 계산할 부분 문제의 끝 행렬 번호
            j = i + diagonal
            # minimum()으로 (i, j) 최소 비용과 최적 분할점 동시 계산
            M[i][j], P[i][j] = minimum(i, j, M, d)

    # 전체 최적값과 복원용 테이블 반환
    return M[1][n], M, P 


# order(i, j, P)
# i: 현재 부분식의 시작 행렬 번호
# j: 현재 부분식의 끝 행렬 번호
# P: 최적 분할점 테이블
# 반환값: 최적 괄호 배치를 문자열로 표현한 결과
def order(i, j, P):
    # 행렬이 하나뿐이면 그대로 Ai 반환
    if i == j:
        return "A" + str(i)
    else:
        # 최적 분할점 k를 꺼내 왼쪽/오른쪽 부분식을 재귀적으로 구성
        k = P[i][j]
        # C 코드 예시 형태와 동일하게 (왼쪽오른쪽) 형식으로 결합
        return "(" + order(i, k, P) + order(k + 1, j, P) + ")"


# 충분히 큰 수 대신 파이썬 무한대를 사용
INF = float("inf")

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_minmult(n, d, expected=None):
    print("Before computation")
    print(f"n = {n}")
    print(f"d = {d}")

    minvalue, M, P = minmult(n, d)

    print("After computation")
    print("M = ")
    for i in range(1, n + 1):
        print(M[i][i:])
    print("P = ")
    for i in range(1, n + 1):
        print(P[i][i:])
    print("minmult =", minvalue)

    multorder = order(1, n, P)
    print("Order of multiplication:", multorder)

    if expected is not None:
        if minvalue == expected:
            print("✅Test Passed!")
        else:
            print("❌Test Failed!")
            print(f"Expected result: {expected}")
            print(f"Your Result: {minvalue}")
    print("-" * 40)


print("**************Testing minmult()**************")

print("######Example 1######")
test_minmult(6, [5, 2, 3, 4, 6, 7, 8], expected=348)

print("######Example 2######")
test_minmult(4, [10, 20, 30, 40, 30], expected=30000)

print("######Example 3######")
test_minmult(3, [10, 100, 5, 50], expected=7500)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_minmult(n, d, expected)