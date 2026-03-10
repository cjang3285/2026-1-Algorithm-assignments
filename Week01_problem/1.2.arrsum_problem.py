# CSE304-2025-2-Algorithms
# Week01-1.2.arrsum.py

def arrsum(n, S):
    result = 0
    
    # Complete the code here
    for i in range(n):
        result += S[i]
        
    return result

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(S, expected):
    n = len(S)
    result = arrsum(n, S)
    if result == expected:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    print(f"Input array: {S}")
    print(f"Expected result: {expected}")
    print(f"Your result: {result}")
    print("-" * 40)

# Example 1
print("###### Example 1 ######")
S = [10, 7, 11, 5, 13, 8]
expected = sum(S) 
test_case(S, expected)

# Example 2
print("###### Example 2 ######")
S = [-1, -2, -3, -4]
expected = sum(S)
test_case(S, expected)

# Example 3
print("###### Example 3 ######")
S = [-1, 2, -3, 4]
expected = sum(S)
test_case(S, expected)

# Example 4
print("###### Example 4 ######")
S = []
expected = sum(S)
test_case(S, expected)

# Example 5
print("###### Example 5 ######")
S = list(range(100))
expected = sum(S)
test_case(S, expected)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# S = [...]
# expected =
# test_case(S, expected)