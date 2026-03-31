# CSE304-2026-1-Algorithms
# Week04-2.8.strassen_problem.py

# ******The following are NOT allowed in your implementation******:
# - Any built-in/library matrix multiplication utilities
#   (e.g., numpy.dot(), numpy.matmul(), scipy matrix multiplication)
# You must implement Strassen's divide-and-conquer algorithm directly.
# ***************************************************************
import random

class Matrix:
    def __init__(self, mat):
        self.n = len(mat)
        self.matrix = mat
    
    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.n)] for i in range(self.n)])
    
    def __sub__(self, other):
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.n)] for i in range(self.n)])
    
    def __mul__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    mat[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(mat)
    
    def __str__(self):  
        return "\n".join(" ".join(f"{val:5}" for val in row) for row in self.matrix)

    __repr__ = __str__


def partition(n, M):
    m = n // 2
    m1 = [[0] * m for _ in range(m)] # 4분할의 밑판이 되는 0으로 초기화된 n/2 x n/2 크기의 행렬을 4개 만들어준다.
    m2 = [[0] * m for _ in range(m)]
    m3 = [[0] * m for _ in range(m)]
    m4 = [[0] * m for _ in range(m)]
    for i in range(m): # 행을 0 ~ n/2 까지  
        for j in range(m): # 열을 0 ~ n/2 까지 탐색하면서,
            # Complete the code here
            m1[i][j] = M.matrix[i][j] # m1이 좌상단 행렬이다. 그래서 i(행)과 j(열)에 m을 더하지 않고 그대로 원소들을 m1에 넣어준다.
            m2[i][j] = M.matrix[i][j + m] # m2가 우상단 행렬이다. 그래서 j(열)에 m을 더해서 오른쪽으로 이동한 원소들을 m2에 넣어준다.
            m3[i][j] = M.matrix[i + m][j] # m3이 좌하단 행렬이다. 그래서 i(행)에 m을 더해서 아래로 이동한 원소들을 m3에 넣어준다.
            m4[i][j] = M.matrix[i + m][j + m] # m4이 우하단 행렬이다. 그래서 i(행)와 j(열)에 m을 더해서 오른쪽 아래로 이동한 원소들을 m4에 넣어준다.

    return Matrix(m1), Matrix(m2), Matrix(m3), Matrix(m4) # 4개의 n/2 x n/2 크기의 이중 리스트를 Matrix 객체로 만들어서 반환한다.

# combine 함수는 별도 정의된 함수이며 매트릭스 객체 C11, C12, C21, C22를 받아서 하나의 n x n 크기의 매트릭스 객체로 결합해서 반환한다.
def combine(n, M1, M2, M3, M4):
    m = n // 2
    mat = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            # Complete the code here
            mat[i][j] = M1.matrix[i][j] # C11이 좌상단에 위치하므로 i(행)과 j(열)에 m을 더하지 않고 그대로 원소들을 mat에 넣어준다.
            mat[i][j + m] = M2.matrix[i][j] # C12가 우상단에 위치하므로 j(열)에 m을 더해서 오른쪽으로 이동한 원소들을 mat에 넣어준다.
            mat[i + m][j] = M3.matrix[i][j] # C21이 좌하단에 위치하므로 i(행)에 m을 더해서 아래로 이동한 원소들을 mat에 넣어준다.
            mat[i + m][j + m] = M4.matrix[i][j] # C22가 우하단에 위치하므로 i(행)와 j(열)에 m을 더해서 오른쪽 아래로 이동한 원소들을 mat에 넣어준다.

    return Matrix(mat) # 4개의 n/2 x n/2 크기의 이중 리스트들이 모인 mat 이중 리스트 객체를 Matrix 생성자로 매트릭스 객체로 만들어서 반환한다.


def strassen(n, A, B): # n은 현재 단계에서 행렬의 크기
    global threshold

    if n <= threshold:
        return A * B
    else:
        A11, A12, A21, A22 = partition(n, A) # 반환된 객체들은 Matrix 객체이므로, A11.matrix로 접근해서 이중 리스트 형태로 원소들을 사용할 수 있다.
        B11, B12, B21, B22 = partition(n, B)
        # Complete the code here
        M1 = strassen(n // 2, A11 + A22, B11 + B22) # 매트릭스 객체 간 합과 뺄셈은 Matrix 클래스에서 정의된 __add__와 __sub__ 메소드를 통해서 가능하다. 그래서 A11 + A22, B11 + B22 처럼 간단하게 표현할 수 있다. 
        M2 = strassen(n // 2, A21 + A22, B11) 
        M3 = strassen(n // 2, A11, B12 - B22)
        M4 = strassen(n // 2, A22, B21 - B11)
        M5 = strassen(n // 2, A11 + A12, B22)
        M6 = strassen(n // 2, A21 - A11, B11 + B12)
        M7 = strassen(n // 2, A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7 # 스트라센 알고리즘에서 결과 행렬의 4분할된 부분 행렬 C11, C12, C21, C22는 M1, M2, M3, M4, M5, M6, M7의 선형 조합으로 표현된다. C11은 M1 + M4 - M5 + M7로 계산된다.
        C12 = M3 + M5 # 이들 또한 매트릭스 클래스의 __add__와 __sub__ 메소드를 통해서 간단하게 표현할 수 있다. C12는 M3 + M5로 계산된다.
        C21 = M2 + M4 # C21은 M2 + M4로 계산된다.
        C22 = M1 - M2 + M3 + M6 # C22은 M1 - M2 + M3 + M6로 계산된다.

        return combine(n, C11, C12, C21, C22) # combine 함수는 별도 정의된 함수이며 매트릭스 객체 C11, C12, C21, C22를 받아서 하나의 n x n 크기의 매트릭스 객체로 결합해서 반환한다.


threshold = 1

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
class CountedInt:
    multiplication_count = 0

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, CountedInt):
            return CountedInt(self.value + other.value)
        return CountedInt(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, CountedInt):
            return CountedInt(self.value - other.value)
        return CountedInt(self.value - other)

    def __rsub__(self, other):
        if isinstance(other, CountedInt):
            return CountedInt(other.value - self.value)
        return CountedInt(other - self.value)

    def __mul__(self, other):
        CountedInt.multiplication_count += 1
        if isinstance(other, CountedInt):
            return CountedInt(self.value * other.value)
        return CountedInt(self.value * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, CountedInt):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


def to_counted_matrix(mat):
    return Matrix([[CountedInt(value) for value in row] for row in mat])


def unwrap_matrix(mat):
    return [
        [value.value if isinstance(value, CountedInt) else value for value in row]
        for row in mat.matrix
    ]


def test_strassen(A_matrix, B_matrix):    
    A = Matrix(A_matrix)
    B = Matrix(B_matrix)
    
    n = len(A_matrix)
    
    expected = A * B
    
    strassen_result = strassen(n, A, B)
    
    is_correct = all(strassen_result.matrix[i][j] == expected.matrix[i][j] 
                    for i in range(n) for j in range(n))
    
    if is_correct:
        print("✅Test Passed!")
    else:
        print(f"❌Test Failed!")
    print(f"Expected result: \n{expected}")
    print(f"Your Result: \n{strassen_result}")
    
    print("-" * 40)


def test_strassen_operation_count(n):
    global threshold

    print(f"######Operation Count Test (n={n})######")

    original_threshold = threshold
    threshold = 1

    random.seed(n)
    A_matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]
    B_matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(n)]

    expected = (Matrix(A_matrix) * Matrix(B_matrix)).matrix

    CountedInt.multiplication_count = 0
    counted_A = to_counted_matrix(A_matrix)
    counted_B = to_counted_matrix(B_matrix)

    try:
        strassen_result = strassen(n, counted_A, counted_B)
    finally:
        threshold = original_threshold

    actual = unwrap_matrix(strassen_result)
    expected_count = 7 ** (n.bit_length() - 1)

    if actual == expected and CountedInt.multiplication_count == expected_count:
        print("✅Test Passed!")
    else:
        print("❌Test Failed!")
        if actual != expected:
            print("The matrix product is incorrect.")
        print(f"Expected scalar multiplications: {expected_count}")
        print(f"Your scalar multiplications: {CountedInt.multiplication_count}")

    print("-" * 40)


if __name__ == "__main__":
    A1 = [[1, 2], [3, 4]]
    B1 = [[5, 6], [7, 8]]
    print("######Example 1######")
    test_strassen(A1, B1)
    
    A2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
    B2 = [[8, 9, 1, 2], [3, 4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5]]
    print("######Example 2######")
    test_strassen(A2, B2)

    A3 = [
        [12, 8, 4, 0, 9, 6, 2, 7],
        [1, 5, 10, 3, 11, 15, 4, 8],
        [7, 13, 2, 9, 0, 5, 10, 14],
        [3, 6, 1, 8, 12, 4, 7, 2],
        [9, 4, 11, 5, 3, 8, 1, 6],
        [13, 0, 7, 10, 2, 14, 5, 9],
        [6, 12, 3, 15, 7, 1, 13, 4],
        [8, 2, 10, 4, 6, 11, 9, 0]
    ]
    
    B3 = [
        [5, 3, 8, 10, 1, 7, 4, 9],
        [11, 2, 6, 4, 13, 0, 8, 5],
        [3, 9, 1, 7, 12, 6, 2, 10],
        [14, 0, 5, 11, 8, 3, 7, 2],
        [4, 10, 2, 6, 9, 13, 1, 8],
        [7, 12, 15, 3, 0, 5, 11, 4],
        [9, 5, 10, 2, 7, 4, 6, 12],
        [1, 8, 4, 13, 3, 9, 0, 6]
    ]
    print("######Example 3######")
    test_strassen(A3, B3)
    test_strassen_operation_count(2)
    test_strassen_operation_count(4)
    test_strassen_operation_count(8)
    test_strassen_operation_count(16)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# A4 = [[], []]
# B4 = [[], []]
# test_strassen(A4, B4)
