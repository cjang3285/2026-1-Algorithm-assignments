# CSE304-2026-1-Algorithms
# Week03-2.2.mergesort_problem.py

# •문제: n개의 정수를 비내림차순으로 병합 정렬을 사용해 정렬하라! (시간복잡도 O(n lg n))
# •입력: 정수 n, 크기가 n인 배열 S
# •출력: 비내림차순으로 정렬된 배열 S
def merge(h, m, U, V, S):
    # i: U 배열 인덱스, j: V 배열 인덱스, k: 결과 S 배열 인덱스다. 모두 0으로 초기화한다.
    i = j = k = 0 
    
    # 두 배열에서 더 작은 값을 하나씩 S에 넣는다.
    # 왼쪽 배열 U와 오른쪽 배열 V 둘의 i, j번째 원소를 비교하여 더 작은 것부터 S에 값을 넣기를 반복한다.
    while i < h and j < m: # i가 h 즉 U의 크기가 되는 순간, 또는 j가 m 즉 V의 크기가 되면 반복을 멈춘다. 즉, 둘 중 하나의 배열이 모두 S에 들어간 순간 반복을 멈춘다.
        if U[i] <= V[j]:
            S[k] = U[i] # 이번엔 U의 원소가 작았으니 U의 i번째 원소를 S의 k번째 원소로 넣는다.
            i += 1 # U의 i번째 원소를 S의 k번째 원소로 넣었으니 U의 다음 원소를 비교하기 위해 i를 1 증가시킨다.
        else:
            S[k] = V[j] # 이번엔 V의 원소가 작았으니 V의 j번째 원소를 S의 k번째 원소로 넣는다.
            j += 1 # V의 j번째 원소를 S의 k번째 원소로 넣었으니 V의 다음 원소를 비교하기 위해 j를 1 증가시킨다.
        k += 1 # S의 다음 원소에 값을 넣기 위해 k를 1 증가시킨다.
    
    # 아직 U에 남은 값이 있으면 그대로 뒤에 붙인다.
    while i < h: 
        S[k] = U[i] 
        i += 1
        k += 1
    
    # 아직 V에 남은 값이 있으면 그대로 뒤에 붙인다.
    while j < m:
        S[k] = V[j]
        j += 1
        k += 1

def mergesort(n, S):
    # 배열을 반으로 나누기 위한 크기 계산
    # 정수 나눗셈 : S의 길이가 홀수냐 짝수냐에 따라서 가운데 원소나 왼쪽 배열의 마지막 원소가 S[h]이다.
    h = n // 2 # h는 왼쪽 배열의 크기이다. 
    m = n - h # m은 오른쪽 배열의 크기이다.

    # 원소가 1개 이하면 이미 정렬된 상태이므로 종료
    # 원소가 2개 이상이면 배열을 반으로 나누고 각각을 재귀적으로 정렬한 후 병합한다.
    if n > 1:
        # S를 왼쪽(U), 오른쪽(V) 두 부분 배열로 분할
        U = S[:h] # U는 왼쪽 부분배열이다. :h는 S의 0부터 h-1까지의 원소를 포함하는 부분 배열을 의미한다.
        V = S[h:] # V는 오른쪽 부분배열이다. h:는 S의 h부터 n-1까지의 원소를 포함하는 부분 배열을 의미한다.
        
        # 각각을 재귀적으로 정렬
        mergesort(h, U) # 왼쪽배열 U를 정렬한다. h는 U의 크기이다.
        mergesort(m, V) # 오른쪽배열 V를 정렬한다. m은 V의 크기이다.
        
        # 정렬된 두 배열을 합쳐서 S에 저장
        merge(h, m, U, V, S)

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_merge(U, V, expected_result):
    h = len(U)
    m = len(V)
    S = [-1] * (h + m)
    
    merge(h, m, U, V, S)
    
    if S == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array U: {U}")
    print(f"Input array V: {V}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {S}")
    print("-" * 40)

def test_mergesort(S, expected_result):
    original = S.copy()
    
    mergesort(len(S), S)
    
    if S == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array: {original}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {S}")
    print("-" * 40)

print("######Example 1 for 'merge()'######")
U = [17, 19, 39, 41, 73]
V = [16, 22, 66, 94, 98]
expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
test_merge(U, V, expected_result)

print("######Example 2 for 'merge()'######")
U = [1, 3, 5, 7, 9]
V = [2, 4, 6, 8, 10]
expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_merge(U, V, expected_result)

print("######Example 3 for 'mergesort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
expected_result = [16, 17, 19, 22, 39, 41, 66, 73, 94, 98]
test_mergesort(S, expected_result)

print("######Example 4 for 'mergesort()'######")
S = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
test_mergesort(S, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 for 'merge()'(Custom)
# U = []
# V = []
# expected_result = []
# test_merge(U, V, expected_result)

# Example 6 for 'mergesort()'(Custom)
# S = []
# expected_result = []
# test_mergesort(S, expected_result)s