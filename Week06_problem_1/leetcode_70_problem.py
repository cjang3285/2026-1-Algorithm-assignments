# CSE304-2026-1-Algorithms
# Week06-leetcode_70_problem.py

import multiprocessing as mp
import time
import traceback

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Use dynamic programming with O(n) time.
        # Let dp[i] be the number of ways to reach step i.
        # 기저 케이스 : dp[0] = 1 (계단이 없는 경우, 1가지 방법), dp[1] = 1 (첫 번째 계단에 도달하는 방법은 0->1로 한 가지)
        if n <= 1:
            return 1

        # dp[i]는 dp[i-1]에서 한 계단 올라가는 방법과 dp[i-2]에서 두 계단 올라가는 방법의 합이 된다.
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # dp[i] 계산
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]


        return dp[n]
########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
class TimeLimitExceeded(Exception):
    pass


def _run_climbStairs_in_subprocess(n, child_conn):
    try:
        sol = Solution()
        child_conn.send(("ok", sol.climbStairs(n)))
    except BaseException as exc:
        child_conn.send(("error", repr(exc), traceback.format_exc()))
    finally:
        child_conn.close()


def _run_with_timeout(n, timeout_sec):
    parent_conn, child_conn = mp.Pipe(duplex=False)
    process = mp.Process(target=_run_climbStairs_in_subprocess, args=(n, child_conn))
    process.start()
    child_conn.close()

    process.join(timeout_sec)
    if process.is_alive():
        process.terminate()
        process.join()
        parent_conn.close()
        raise TimeLimitExceeded

    if not parent_conn.poll():
        exitcode = process.exitcode
        parent_conn.close()
        raise RuntimeError(
            f"Worker process exited without returning a result (exit code {exitcode})."
        )

    status, *payload = parent_conn.recv()
    parent_conn.close()

    if status == "ok":
        return payload[0]

    error_repr, error_traceback = payload
    raise RuntimeError(
        "climbStairs() raised an exception in the worker process:\n"
        f"{error_repr}\n{error_traceback}"
    )


def test_climbStairs(n, expected=None, timeout_sec=None):
    print("Before computation")
    print(f"n = {n}")

    ways = None
    timed_out = False
    start_time = time.perf_counter()

    try:
        if timeout_sec is None:
            sol = Solution()
            ways = sol.climbStairs(n)
        else:
            ways = _run_with_timeout(n, timeout_sec)
    except TimeLimitExceeded:
        timed_out = True

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


def main():
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


if __name__ == "__main__":
    mp.freeze_support()
    main()
