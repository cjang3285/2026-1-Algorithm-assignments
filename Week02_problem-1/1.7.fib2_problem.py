# CSE304-2026-1-Algorithms
# Week02-1.7.fib2_problem.py
import time

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(n, expected_result):
    stime = time.time()
    result = fib2(n)
    etime = time.time() - stime
    
    if result == expected_result:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input value: {n}")
    print(f"Execution time: {round(etime, 5)}s")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)

print("######Example 1######")
n = 30
expected_result = 832040
test_case(n, expected_result)

print("######Example 2######") 
n = 36
expected_result = 14930352
test_case(n, expected_result)

print("######Example 3######") 
n = 40
expected_result = 102334155
test_case(n, expected_result)

print("######Example 4######") 
n = 0
expected_result = 0
test_case(n, expected_result)

print("######Example 5######") 
n = 1
expected_result = 1
test_case(n, expected_result)

print("######Example 6######") 
n = 1000
expected_result = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
test_case(n, expected_result)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 7 (Custom)
# n = 
# expected_result = 
# test_case(n, expected_result)