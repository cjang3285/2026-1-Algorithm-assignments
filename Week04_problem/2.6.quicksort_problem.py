# CSE304-2026-1-Algorithms
# Week04-2.6.quicksort_problem.py

# ******The following are NOT allowed in your implementation******:
# - sorted()
# - list.sort()
# - any other built-in/library sorting functions or sorting utilities
# You must implement quicksort and partition directly.
# *************************************************************


import random
import time

def partition(low, high, S):
    pivotitem = S[low]
    j = low

    for i in range(low + 1, high + 1): # low + 1 to high 함수 인자로 주어진 범위를 끝까지 탐색하면서
        if S[i] < pivotitem: # 만약 pivotitem보다 작은 원소가 나오면,  
            j += 1 # j 곧 피봇아이템보다 작은 원소가 올 자리를 1 증가시켜서
            S[i], S[j] = S[j], S[i] # 지금까지 모은 작은 원소들의 바로 다음 자리 아직 피봇 아이템보다 큰 수가 있는 자리로 가게 하기 위해 S[i]와 S[j]를 교환한다.
            # 그러면 큰 원소가 멀리 i로 보내지고 i에 있던 피봇 아이템 보다 작은 원소는 j로 오게 된다. 이렇게 하면 피봇 아이템보다 작은 원소들은 모두 j를 포함하는 왼쪽배열에 모이게 된다.
    S[low], S[j] = S[j], S[low] # 마지막으로 피봇 아이템을 피봇 아이템보다 작은 아이템들 중 가장 마지막 자리인 j로 보내준다. 그러면 피봇 아이템보다 작은 원소들은 모두 j를 포함하는 왼쪽배열에 모이게 되고, 피봇 아이템보다 큰 원소들은 모두 오른쪽 배열에 모이게 된다.
    return j # 퀵소트 재귀 호출을 위해 피봇 아이템이 최종적으로 위치한 인덱스 j를 반환한다. 이 인덱스를 기준으로 왼쪽과 오른쪽 부분 배열로 나누어서 퀵소트를 재귀적으로 호출할 수 있다.

def quicksort(low, high, S):
    if low < high: # 재귀가 진행되면서 구간이 계속 줄어들고, 원소가 0개 또는 1개가 되면 low >= high가 되어 재귀가 멈춥니다.
        pivotpoint = partition(low, high, S)
        quicksort(low, pivotpoint - 1, S)
        quicksort(pivotpoint + 1, high, S)

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def format_array(S, head=10, tail=10):
    if len(S) <= head + tail:
        return str(S)

    head_part = ", ".join(str(x) for x in S[:head])
    tail_part = ", ".join(str(x) for x in S[-tail:])
    return f"[{head_part}, ..., {tail_part}] (len={len(S)})"


def test_partition(S, expected_S, expected_pivot):
    print("Before partition:", format_array(S))
    pivotpoint = partition(0, len(S) - 1, S)
    print("After partition:", format_array(S))
    
    if S == expected_S and pivotpoint == expected_pivot:
        print("✅Test Passed!")
    else:
        print(f"❌Test Failed!")
        print(f"Expected result: {format_array(expected_S)}, {expected_pivot}")
        print(f"Your Result: {format_array(S)}, {pivotpoint}")
    print("-" * 40)


def test_quicksort(S, expected_S):
    print("Before quicksort:", format_array(S))
    quicksort(0, len(S) - 1, S)
    print("After quicksort:", format_array(S))
    
    if S == expected_S:
        print("✅Test Passed!")
    else:
        print(f"❌Test Failed!")
        print(f"Expected result: {format_array(expected_S)}")
        print(f"Your Result: {format_array(S)}")
    print("-" * 40)


def test_quicksort_average_case():
    print("**************Testing average-case scaling**************")

    sizes = [1000, 2000, 4000]
    median_times = []

    for size in sizes:
        trial_times = []

        for seed in range(3):
            random.seed(size * 100 + seed)
            S = random.sample(range(size * 20), size)
            expected_S = sorted(S)

            start_time = time.perf_counter()
            quicksort(0, len(S) - 1, S)
            elapsed_time = time.perf_counter() - start_time

            if S != expected_S:
                print(f"❌Test Failed!")
                print(f"Sorting failed during scaling test for n={size}")
                print("-" * 40)
                return

            trial_times.append(elapsed_time)

        trial_times.sort()
        median_time = trial_times[1]
        median_times.append(median_time)
        print(f"n={size}, median time={median_time:.6f} sec")

    ratio_1 = median_times[1] / median_times[0]
    ratio_2 = median_times[2] / median_times[1]

    print(f"time ratio (2000/1000): {ratio_1:.2f}")
    print(f"time ratio (4000/2000): {ratio_2:.2f}")

    if ratio_1 < 3.2 and ratio_2 < 3.2:
        print("✅Test Passed!")
    else:
        print("❌Test Failed!")
        print("The running time does not scale like average-case O(n lg n) on random inputs.")
    print("-" * 40)



print("**************Testing partition()**************")
print("######Example 1######")
test_partition([17, 19, 39, 41, 73], [17, 19, 39, 41, 73], 0)
print("######Example 2######")
test_partition([73, 41, 39, 19, 17], [17, 41, 39, 19, 73], 4)
print("######Example 3######")
test_partition([39, 41, 19, 74, 17], [17, 19, 39, 74, 41], 2)

print("**************Testing quicksort()**************")
print("######Example 4######")
test_quicksort([22, 98, 17, 16, 19, 73, 94, 41, 39, 66], [16, 17, 19, 22, 39, 41, 66, 73, 94, 98])
print("######Example 5######")
test_quicksort([5, 3, 8, 6, 2, 7, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8])
print("######Example 6######")
random.seed(42)
S = random.sample(range(1000000), 2000)
expected_S = sorted(S)
test_quicksort(S, expected_S)
print("######Example 7######")
random.seed(7)
S = random.sample(range(2000000), 5000)
expected_S = sorted(S)
test_quicksort(S, expected_S)
print("######Example 8######")
random.seed(100)
S = [random.randint(0, 100) for _ in range(3000)]
expected_S = sorted(S)
test_quicksort(S, expected_S)
print("######Example 9######")
test_quicksort_average_case()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 10 (Custom)
# test_partition(S, expected_S, expected_pivot)
# test_quicksort(S, expected_S)
