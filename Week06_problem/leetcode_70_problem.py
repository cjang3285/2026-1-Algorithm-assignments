# CSE304-2026-1-Algorithms
# Week06-leetcode_70_problem.py

import signal
import time

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Use dynamic programming with O(n) time.
        # Let dp[i] be the number of ways to reach step i.

        # Base case
        if n == 1:
            return 1
        
        # DP 배열: dp[i] = i번째 계단에 오르는 방법의 수
        dp = [0] * (n + 1)
        dp[1] = 1  # 1칸: 1가지 (1)
        dp[2] = 2  # 2칸: 2가지 (1+1, 2)
        
        # Recurrence relation: dp[i] = dp[i-1] + dp[i-2]
        # i번째 계단에는 (i-1)번째에서 1칸, 또는 (i-2)번째에서 2칸으로 올 수 있음
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
class TimeLimitExceeded(Exception):
    pass


def _handle_timeout(signum, frame):
    raise TimeLimitExceeded


def test_climbStairs(n, expected=None, timeout_sec=None):
    print("Before computation")
    print(f"n = {n}")

    sol = Solution()
    ways = None
    timed_out = False
    start_time = time.perf_counter()

    try:
        if timeout_sec is not None:
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, timeout_sec)
        ways = sol.climbStairs(n)
    except TimeLimitExceeded:
        timed_out = True
    finally:
        if timeout_sec is not None:
            signal.setitimer(signal.ITIMER_REAL, 0)

    elapsed_time = time.perf_counter() - start_time

    print("After computation")
    if timed_out:
        print(f"Execution timed out after {timeout_sec} second(s).")
    else:
        print("Number of ways =", ways)
    print(f"Elapsed time = {elapsed_time:.6f} sec")

    if expected is not None:
        if timed_out:
            print("❌Test Failed!")
            print("Your code is too slow for this test case.")
        elif ways == expected:
            print("✅Test Passed!")
        else:
            print("❌Test Failed!")
            print(f"Expected result: {expected}")
            print(f"Your Result: {ways}")
    print("-" * 40)


print("**************Testing climbStairs()**************")

print("######Example 1######")
test_climbStairs(2, expected=2)

print("######Example 2######")
test_climbStairs(3, expected=3)

print("######Example 3######")
test_climbStairs(5, expected=8)

print("######Example 4######")
test_climbStairs(100, expected=573147844013817084101, timeout_sec=5.0)

print("######Example 5######")
test_climbStairs(200, expected=453973694165307953197296969697410619233826, timeout_sec=5.0)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 6 (Custom)
# test_climbStairs(n, expected, timeout_sec)
