# CSE304-2026-1-Algorithms
# Week02-1.4.matrixmult_problem.py

def matrixmult(n, A, B):
    # n x n result matrix initialized with zeros
    C = [[0] * n for _ in range(n)]

    # Standard matrix multiplication: C[i][j] = sum(A[i][k] * B[k][j])
    for i in range(n): # A의 0행부터 n-1행까지
        for j in range(n): # B의 0열부터 n-1열까지
            for k in range(n): # A의 i행과 B의 j열의 각각의 k번째 원소를 뽑아서
                C[i][j] += A[i][k] * B[k][j] # 곱하고 결과를 C의 i행 j열에 누적하여 C[i][j]을 완성

    return C
    
########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(A, B, expected_result):
    n = len(A)
    result = matrixmult(n, A, B)
    
    if result == expected_result:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input array A: {A}")
    print(f"Input array B: {B}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)

print("######Example 1######") 
A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
expected_result = [[28, 38], [26, 36]]
test_case(A, B, expected_result)

print("######Example 2######") 
A = [[1, 2], [3, 4]]
B = [[4, 1], [1, 0]]
expected_result = [[6, 1], [16, 3]]
test_case(A, B, expected_result)

print("######Example 3######") 
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = [[5, 2, 3], [1, 7, 4], [6, 8, 9]]
expected_result = [[5, 2, 3], [1, 7, 4], [6, 8, 9]]
test_case(A, B, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# A = []
# B = []
# expected_result = []
# test_case(A, B, expected_result)