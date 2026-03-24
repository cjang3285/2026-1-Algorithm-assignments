# CSE304-2026-1-Algorithms
# Week03-leetcode_215_problem.py
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# • 문제: 정수 배열 nums와 정수 k가 주어질 때, 배열에서 k번째로 큰 원소를 반환하라. (단, k번째 큰 원소는 정렬된 순서 기준이며, 중복 여부는 고려하지 않는다. 또한 배열을 정렬할 때는 mergesort 방식을 활용해야 한다.)
# • 입력: ○ nums: 정수 배열 (길이 1 ≤ nums.length ≤ 10⁵)
# ○ k: 정수 (1 ≤ k ≤ nums.length)
# ○ nums[i]의 범위: -10⁴ ≤ nums[i] ≤ 10⁴
# • 출력: 배열에서 k번째로 큰 원소
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = self.mergeSort(nums) 
        return sorted_nums[-k]

    def mergeSort(self, nums: List[int]) -> List[int]:
        # merge를 타기 전까지는 재귀로 배열을 계속 쪼갤 뿐 아직 정렬이 안 됨
        if len(nums) <= 1:
            # 기저케이스: 길이 1이면 그냥 반환 (아직 정렬이 아니라 그냥 1개 원소)
            return nums
        mid = len(nums) // 2
        left_half = self.mergeSort(nums[:mid])   # 0 ~ mid-1
        right_half = self.mergeSort(nums[mid:])  # mid ~ end
        # merge 통과 순간: 첫 merge에서는 길이 1 혹은 2짜리 조각들이 비교되면서 정렬 시작 <- 1개는 정렬된 상태로 볼 수 있으나 N이 홀수라 조각배열이 숫자 2개인 경우는 정렬 장담 어려움. 그러나 상관없이 merge 함수에서 정렬이 시작된다고 보면 됨.
        # 그 이후부터는 항상 정렬된 배열들 끼리 merge에 인자로 들어감
        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # 이 함수가 호출되는 순간부터 정렬이 시작됨
        # merge 진행 중: 좌우 배열의 앞 원소를 비교해서 더 작은 값을 순서대로 취함
        merged = []
        i, j = 0, 0 # left와 right 배열의 현재 인덱스
        while i < len(left) and j < len(right): # 양쪽 배열 모두에 원소가 남아있는 동안
            if left[i] < right[j]: 
                merged.append(left[i]) # left의 현재 원소가 더 작으면 merged에 추가하고 left 인덱스 증가
                i += 1
            else:
                merged.append(right[j]) # right의 현재 원소가 더 작거나 같으면 merged에 추가하고 right 인덱스 증가
                j += 1
        # 남은 원소들 추가 (한쪽이 이미 다 소진되었을 때)
        merged.extend(left[i:]) # extend는 리스트의 나머지 부분을 한꺼번에 추가하는 메서드
        merged.extend(right[j:]) # 이미 소진된 배열은 j가 len(right)가 되므로 [j:]는 빈 리스트이므로 아무것도 추가되지 않음
        return merged # 정렬된 merged 배열 반환

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_findKthLargest(nums, k, expected_result):
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    
    if result == expected_result:
        print(f"Test Passed!")
    else:
        print(f"Test Failed!")
    
    n = len(nums)
    if n > 20:
        preview = (
            "[" +
            ", ".join(map(str, nums[:10])) +
            ", ... , " +
            ", ".join(map(str, nums[-10:])) +
            "]"
        )
        print(f"Input array: (showing first/last 10 elements)")
        print(preview)
    else:
        print(f"Input array: {nums}")
    
    print(f"k: {k}")
    print(f"Expected result: {expected_result}")
    print(f"Your Result: {result}")
    print("-" * 40)

if __name__ == "__main__":
    print("######Example 1######")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    test_findKthLargest(nums1, k1, 5)
    
    print("######Example 2######")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    test_findKthLargest(nums2, k2, 4)
    
    print("######Example 3######")
    nums3 = [-500] * 90000 + [1000] * 10000
    k3 = 10000
    test_findKthLargest(nums3, k3, 1000)
    
    print("######Example 4######")
    nums4 = [-10000, 10000, -5000, 5000, 0, 9999, -9999]
    k4 = 1
    test_findKthLargest(nums4, k4, 10000)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# nums5 = []
# k5 =
# test_findKthLargest(nums5, k5, expected_result)