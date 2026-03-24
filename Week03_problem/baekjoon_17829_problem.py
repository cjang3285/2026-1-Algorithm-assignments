# CSE304-2026-1-Algorithms
# Week03-baekjoon_17829_problem.py
# https://www.acmicpc.net/problem/17829

# • 문제: N×N 행렬에 222-풀링을 반복 적용하여 크기를 1×1로 만들었을 때 남는 값을 구하라. (Hint: 분할 정복법을 활용)
# • 입력: 첫 줄: N (2 ≤ N ≤ 1024, 2의 거듭제곱), 이후 N개의 줄: N×N 행렬의 원소 (-10,000 ~ 10,000) 
# • 출력: 마지막에 남은 하나의 값
class Solution: # 풀링이란 2x2 블록에서 두 번째로 큰 값을 선택하는 연산이다.
    def pooling(self, matrix, x, y, N): # 이 함수는 matrix의 x, y 좌표에서 시작하는 N x N 크기의 블록에 대해 222-풀링을 재귀로 적용하여 마지막에 1x1 크기만 남았을 때 그 1칸의 값을 반환한다.
        if N == 1: # 기저 케이스 : N이 1이 되면 더 이상 풀링할 수 없으므로 현재 위치의 값을 반환한다.
            return matrix[x][y] # 현재 1 x 1 블록의 값을 반환한다.
        
        half = N // 2 # 현재  N * N 블록을 4등분할 때 각 부분 블록의 한 변 길이(정수 인덱스를 위해 // 사용).
        values = [] # 4개 부분 블록 각각의 '풀링 결과값'들을 저장할 것이다. 총 4개의 값이 저장될 것이다.
        
        for i in range(2): # 현재 N x N 블록의 4개 사분면(왼위, 오른위, 왼아래, 오른아래)을 순회한다.
            for j in range(2):
                values.append(self.pooling(matrix, x + i * half, y + j * half, half)) # 각 사분면에 재귀적으로 같은 연산을 적용한다.
        
        values.sort()
        return values[2]  # 4개 값 중 두 번째로 큰 값

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_pooling(matrix, expected_result):
    n = len(matrix)
    solution = Solution()
    result = solution.pooling(matrix, 0, 0, n)
    
    if result == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    
    print(f"Input Matrix Size: {n}x{n} (N=2^{n.bit_length()-1})")
    
    if n > 8:
        print("Input Matrix (too large, showing partial):")
        for i in range(min(4, n)):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
        print("...")
        for i in range(max(0, n-4), n):
            print(" ".join(map(str, matrix[i][:4])) + " ... " + " ".join(map(str, matrix[i][-4:])))
    else:
        print("Input Matrix:")
        for row in matrix:
            print(" ".join(map(str, row)))
    
    print(f"Result: {result}")
    print("-" * 40)



if __name__ == "__main__":
    print("######Example 1######") 
    matrix1 = [
        [-6, -8, 7, -4],
        [-5, -5, 14, 11],
        [11, 11, -1, -1],
        [4, 9, -2, -4]
    ]
    test_pooling(matrix1, 11)
    
    print("######Example 2######") 
    matrix2 = [
        [-1, 2, 14, 7, 4, -5, 8, 9],
        [10, 6, 23, 2, -1, -1, 7, 11],
        [9, 3, 5, -2, 4, 4, 6, 6],
        [7, 15, 0, 8, 21, 20, 6, 6],
        [19, 8, 12, -8, 4, 5, 2, 9],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24]
    ]
    test_pooling(matrix2, 17)
    
    print("######Example 3######") 
    matrix3 = [
        [-7, -9, 8, -5],
        [-6, -6, 15, 12],
        [12, 12, -2, -2],
        [5, 10, -3, -5]
    ]
    test_pooling(matrix3, 12)
    
    print("######Example 4 (Minimum Size N=2)######") 
    matrix4 = [
        [-10000, 10000],
        [10000, -10000]
    ]
    test_pooling(matrix4, 10000)

    print("######Example 5 (Maximum Size N=1024)######") 
    matrix5 = []
    for i in range(1024):
        row = []
        for j in range(1024):
            if (i + j) % 3 == 0:
                value = 10000
            elif (i + j) % 3 == 1:
                value = -10000 
            else:
                value = (i * j) % 10000 - 5000
            row.append(value)
        matrix5.append(row)
    solution = Solution()
    expected_result5 = solution.pooling(matrix5, 0, 0, 1024)
    test_pooling(matrix5, expected_result5)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# matrix6 = []
# test_pooling(matrix6, ...)