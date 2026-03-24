# CSE304-2026-1-Algorithms
# Week03-2.1.location_problem.py

# • 문제: 크기가 n인 정렬된 배열 S에 x가 있는지를 분할 정복법으로 확인하라. (시간복잡도 O(lg n))
# • 입력: 정수 n, 비내림차순으로 정렬된 배열 S, 찾고자 하는 값 x
# • 출력: S에서의 x의 위치, 만약 x가 S에 없다면 -1
def location(low, high, S, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if S[mid] == x:
            return mid
        elif S[mid] > x:
            return location(low, mid - 1, S, x)
        else:
            return location(mid + 1, high, S, x)

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(S, x, expected_result):
    result = location(0, len(S)-1, S, x)
    
    if result == expected_result:
        print("Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array: {S}")
    print(f"Search value: {x}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)


if __name__ == "__main__":
    print("######Example 1######")
    S = [5, 7, 8, 10, 11, 13]
    x = 15 
    expected_result = -1
    test_case(S, x, expected_result)
    
    print("######Example 2######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 10 
    expected_result = 3
    test_case(S, x, expected_result)
    
    print("######Example 3######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 5
    expected_result = 0
    test_case(S, x, expected_result)
    
    print("######Example 4######") 
    S = [5, 7, 8, 10, 11, 13]
    x = 13
    expected_result = 5
    test_case(S, x, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# S = []
# x = 
# expected_result =
# test_case(S, x, expected_result)