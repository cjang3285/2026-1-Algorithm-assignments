# CSE304-2026-1-Algorithms
# Week02-1.5.binsearch_problem.py

def binsearch(n, S, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if S[mid] == x:
            return mid
        if S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

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