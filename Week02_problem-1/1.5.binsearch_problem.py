# CSE304-2026-1-Algorithms
# Week02-1.5.binsearch_problem.py

def binsearch(n, S, x):
    # S의 유효 인덱스 범위가 0부터 n-1이므로
    low = 0
    high = n - 1

    while low <= high: # 이 조건이 깨지면 탐색 구간이 수렴하다가 사라진 것. 배열에서 x를 못 찾았으므로 -1을 반환.
        
        # mid는 가운데 원소를 가리키는 인덱스가 되길 원함. 인덱스가 소수점 아래로 가면 안되니 정수 나눗셈 // 사용.
        mid = (low + high) // 2 # 현재 탐색 구간 [low, high]의 길이가 홀수면 정중앙 인덱스,
                                # 짝수면 가운데 두 인덱스 중 왼쪽 인덱스가 mid가 된다.
        
        if S[mid] == x: # 가운데 원소가 x와 같으면 정답이므로 mid 인덱스 반환
            return mid
        
        if S[mid] < x: # 가운데 원소가 x보다 작으면 오른쪽 구간을 찾아봐야 함 
            # 탐색 범위의 low 값을 S[mid]의 바로 오른칸 인덱스로 해준다. 즉, low를 mid + 1로 업데이트. 
            low = mid + 1
        
        else: # 가운데 원소가 x보다 크면 왼쪽 구간을 찾아봐야 함
            # 현재 탐색 구간 [low, high]의 길이가 짝수라면 mid는 가운데 두 원소 중 왼쪽 원소의 인덱스고 S[mid]는 x가 아니었던 것이고
            # 현재 탐색 구간 [low, high]의 길이가 홀수라면 mid가 가운데 원소의 인덱스이고 마찬가지로 S[mid]는 x가 아니었던 것이다. 따라서 S[mid]는 탐색 범위에서 배제되어야 한다.
            # 따라서 S[mid]는 탐색범위에서 배제. 탐색범위의 high 값을 S[mid]의 바로 왼칸 인덱스로 해준다.
            # high를 mid -1로 해줌 
            high = mid - 1
        # 위 과정에서 low와 high가 갱신되며 점점 탐색범위가 x를 향해 수렴된다.
    
    return -1

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(S, x, expected_location):
    n = len(S)
    result = binsearch(n, S, x)
    
    if result == expected_location:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input array: {S}")
    print(f"Search value: {x}")
    print(f"Expected location: {expected_location}")
    print(f"Your location: {result}")
    print("-" * 40)

print("######Example 1######")
S = [5, 7, 8, 10, 11, 13]
x = 15 
expected_location = -1
test_case(S, x, expected_location)

print("######Example 2######") 
S = [5, 7, 8, 10, 11, 13]
x = 10 
expected_location = 3
test_case(S, x, expected_location)

print("######Example 3######") 
S = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 7
expected_location = 3
test_case(S, x, expected_location)

print("######Example 4######") 
S = [5]
x = 5
expected_location = 0
test_case(S, x, expected_location)

print("######Example 5######") 
S = []
x = 10
expected_location = -1
test_case(S, x, expected_location)

print("######Example 6######")
S = [5, 7, 9, 11]
x = 5
expected_location = 0
test_case(S, x, expected_location)

print("######Example 7######")
S = [5, 7, 9, 11]
x = 11
expected_location = 3
test_case(S, x, expected_location)

print("######Example 8######")
S = [5, 7, 9, 11]
x = 1
expected_location = -1
test_case(S, x, expected_location)

print("######Example 9######")
S = [5, 7, 9, 11]
x = 20
expected_location = -1
test_case(S, x, expected_location)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 10 (Custom)
# S = []
# x = 
# expected_location =
# test_case(S, x, expected_location)