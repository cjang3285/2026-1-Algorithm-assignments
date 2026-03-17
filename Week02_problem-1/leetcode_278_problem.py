# CSE304-2026-1-Algorithms
# Week02-leetcode_278_problem.py
# https://leetcode.com/problems/first-bad-version
import time
import threading

def isBadVersion(version):
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # mid가 bad이므로 첫 bad 버전은 [left, mid] 구간에 있다.
                right = mid
            else:
                # mid가 good이므로 첫 bad 버전은 [mid + 1, right] 구간에 있다.
                left = mid + 1

        # 불량이 최소 1개 존재한다는 가정 하에, 첫 불량 버전은 항상 [left, right] 구간 안에 남도록 했다.
        # left == right가 되면 후보가 1개만 남으므로 그 값이 정답이다.
        return left
    
########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(n, expected_bad_version, timeout=1):
    global bad_version
    bad_version = expected_bad_version
    sol = Solution()
    
    result_container = []

    def run_test():
        try:
            start = time.time()
            result = sol.firstBadVersion(n)
            elapsed = round(time.time() - start, 5)
            result_container.append((result, elapsed))
        except Exception as e:
            result_container.append(e)

    test_thread = threading.Thread(target=run_test)
    test_thread.start()
    test_thread.join(timeout)

    if test_thread.is_alive():
        print(f"Test Failed!: n={n}, bad={expected_bad_version}, Timeout (too slow)")
    elif not result_container:
        print(f"Test Failed!: n={n}, bad={expected_bad_version}, No result returned")
    else:
        result = result_container[0]
        if isinstance(result, Exception):
            print(f"Test Failed!: n={n}, bad={expected_bad_version}, Error={result}")
        else:
            output, elapsed_time = result
            if output == expected_bad_version:
                print(f"Test Passed!: n={n}, bad={expected_bad_version}, Time={elapsed_time}s")
            else:
                print(f"Test Failed!: n={n}, bad={expected_bad_version}, Output={output}, Time={elapsed_time}s")
    
    print("-" * 40)

print("######Example 1######")
test_case(5, 4)

print("######Example 2######")
test_case(1, 1)

print("######Example 3######")
test_case(100, 10)

print("######Example 4######")
test_case(100, 50)

print("######Example 5######")
test_case(10**6, 987654)

print("######Example 6######")
test_case(10**6, 500000)

print("######Example 7######")
test_case(2147483648, 2147483000)

print("######Example 8######")
test_case(10**8, 99999999)  # 큰 n에서 성능 차이 확실히 드러남
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 9 (Custom)
# test_case(n, expected_bad_version)