# CSE304-2026-1-Algorithms
# Week06-3.6.minmatrixmult_problem.py

# 이 함수로 i부터 j까지의 행렬 곱셈에서 최소 곱셈 횟수와 그 때의 k값을 구한다.
def minimum(i, j, M, d): # M는 최소 곱셈 횟수를 저장하는 테이블, d는 행렬의 차원을 나타내는 리스트이다.
    minvalue, mink = INF, 0 # minvalue는 현재 i, j에서 최소 곱셈 횟수를 저장하는 변수이고, mink는 그 때의 k값을 저장하는 변수이다.
    for k in range(i, j): # 분할점 k을 옮겨보면서 최소 곱셈 횟수를 계산한다. k는 (Ai) i부터 Aj-1) j-1까지 가능하다.
        value = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
        if value < minvalue: # k, 즉 분할점을 Ai(Ai+1...Aj)인 i부터 (AiAi+1...Aj-1)Aj인 j-1까지 바꿔가면서 최소 곱셈 횟수를 계산한다. 
            minvalue = value # 현재 분할점 k에서 최소 곱셈 횟수가 현재 i,j 조합에서 지금까지 기록된 최소횟수보다 더 작은 경우, minvalue와 mink를 업데이트한다.
            mink = k

    return minvalue, mink 

# 이 함수는 n개의 행렬과 각 행렬의 차원을 나타내는 리스트 d를 입력으로 받아서, 최소 곱셈 횟수와 그 때의 M과 P 테이블을 반환한다.
def minmult(n, d):
    # 1 based indexing을 사용하기 위해서 M과 P 테이블의 크기를 (n+1) x (n+1)로 설정한다. 
    # M[i][j]는 i부터 j까지의 행렬 곱셈에서 최소 곱셈 횟수를 저장하고, 
    # P[i][j]는 그 때의 k값을 저장한다.
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1): # 대각성분은 자기자신과의 곱이므로 0으로 초기화.
        M[i][i] = 0
    for diagonal in range(1, n): # diagonal은 diagonal은 한 행렬 입장에서 곱해질 행렬(들) 개수이다. 총 n개의 행렬이 있으므로 1~n-1까지만 가능.
        for i in range(1, (n - diagonal) + 1): # 행렬이 n개 있다고 치면 번호는 1번부터 n번까지이다. 
            j = i + diagonal # 코드에서 항상 j = i + diagonal
            M[i][j], P[i][j] = minimum(i, j, M, d) # minimum은 i부터 j까지의 행렬 곱셈에서 최소 곱셈 횟수와 그 때의 k값을 구하는 함수이다. 이를 호출해 M과 P 테이블을 업데이트한다.

    return M[1][n], M, P 

# 이 함수는 P 테이블을 이용해서 i부터 j까지의 행렬 곱셈의 최적 순서를 문자열로 반환한다.
def order(i, j, P):
    if i == j:
        return "A" + str(i)
    else:
        k = P[i][j]
        return "(" + order(i, k, P) + order(k + 1, j, P) + ")"


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