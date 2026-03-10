# CSE304-2025-2-Algorithms
# Week01-1.3.exchangesort.py

def exchangesort(n, S):
    for i in range(len(S)-1): # S의 모든 원소에 대해서 (range(배열의 크기)과 동일 = 0 1 2 ... n-1) # 일명 ANCHOR
        # Complete the code here
        for j in range(i + 1, len(S)): # i + 1번째 (이번 원소의 다음 원소) 부터 n - 1 (마지막 원소) 까지 순회 # ANCHOR와의 비교대상
            if S[i] > S[j]: # 이번 원소가 다음 원소보다 크다면 
                S[i], S[j] = S[j], S[i] # 더 큰 이번 원소를 그 원소 위치로 보내고 그 원소는 이번 원소 자리로 가져온다

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(S, expected):
    n = len(S)
    data = S.copy()
    exchangesort(n, data)
    if data == expected:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input array: {S}")
    print(f"Expected result: {expected}")
    print(f"Your result: {data}")
    print("-" * 40)

# Example 1
print("###### Example 1 ######")
S = [10, 7, 11, 5, 13, 8]
test_case(S, sorted(S))

# Example 2
print("###### Example 2 ######")
S = []
test_case(S, sorted(S))

# Example 3
print("###### Example 3 ######")
S = [1, 2, 3, 4, 5]
test_case(S, sorted(S))

# Example 4
print("###### Example 4 ######")
S = [3, 1, 2, 1]
test_case(S, sorted(S))

# Example 5
print("###### Example 5 ######")
S = [42]
test_case(S, sorted(S))
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# S = [...]
# test_case(S, sorted(S))