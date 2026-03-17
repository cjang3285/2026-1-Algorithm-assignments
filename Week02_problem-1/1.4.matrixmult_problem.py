# CSE304-2026-1-Algorithms
# Week02-1.4.matrixmult_problem.py

def matrixmult(n, A, B):
    # n x n result matrix initialized with zeros
    C = [[0] * n for _ in range(n)]

    # Standard matrix multiplication: C[i][j] = sum(A[i][k] * B[k][j])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

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