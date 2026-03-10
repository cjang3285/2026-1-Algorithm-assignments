# CSE304-2025-2-Algorithms
# Week01-leetcode_1365.py
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s_nums = sorted(nums)
        count = {}

        # Complete the code here
        
        # 먼저 정답 배열에 각 원소에 대해 자신보다 작은 원소들의 개수를 구해 저장합니다.
        for i, num in enumerate(s_nums): # 오름차순 정렬된 s_nums에 대하여 enumerate로 s_nums의 원소 num과 그 원소의 인덱스 i를 동시에 순회
            # count 딕셔너리에 대하여 in 연산자로 num 값을 가지는 키(key)가 존재하는지 확인합니다.
            if num not in count: # 이번 원소 num이 아직 count 딕셔너리에 아직 없거나 같은 수가 배열에 여러 개 있을 수 있습니다. 
                # 같은 수라면 한번만 저장하면 다른 같은 수들도 자신보다 작은 수의 개수가 같기 때문에 
                # 이번 원소 num이 처음 나오는 위치 i를 저장하면 됩니다. 이후 나오는 같은 수들은 not in에 의해 스킵됩니다.
                count[num] = i # num보다 작은 수의 개수는 num이 s_nums에서 처음 나오는 위치 인덱스 i와 같습니다. (s_nums는 오름차순으로 정렬되어 있기 때문입니다.)
                # 결국 count 딕셔너리는 nums에 중복된 수가 존재한다면 nums보다 크기가 작아질 수 있습니다.
                # 그러나 아래에서 count를 num으로 접근하기 때문에 여러 nums[i]에 대해 같은 count[num] 값을 사용할 수 있습니다.
                 
        for i, num in enumerate(nums): # 정렬되지 않는 nums에 대하여 enumerate로 nums의 원소 num과 그 원소의 인덱스 i를 동시에 순회
            nums[i] = count[num] # count에 저장된 num보다 작은 수의 개수를 nums의 원소 num이 있는 위치 i에 저장합니다.

        return nums        

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################
def test_case(nums, expected):
    sol = Solution()
    result = sol.smallerNumbersThanCurrent(nums[:])  # copy to avoid mutation
    if result == expected:
        print("Test Passed!")
    else:
        print("Test Failed!")
    print(f"Input nums: {nums}")
    print(f"Expected result: {expected}")
    print(f"Your result: {result}")
    print("-" * 40)

# Example 1
print("###### Example 1 ######")
nums = [8, 1, 2, 2, 3]
expected = [4, 0, 1, 1, 3]
test_case(nums, expected)

# Example 2
print("###### Example 2 ######")
nums = [6, 5, 4, 8]
expected = [2, 1, 0, 3]
test_case(nums, expected)

# Example 3
print("###### Example 3 ######")
nums = [7, 7, 7, 7]
expected = [0, 0, 0, 0]
test_case(nums, expected)

# Example 4 
print("###### Example 4 ######")
nums = [1, 2, 3, 4]
expected = [0, 1, 2, 3]
test_case(nums, expected)

# Example 5 
print("###### Example 5 ######")
nums = [4, 3, 2, 1]
expected = [3, 2, 1, 0]
test_case(nums, expected)

# Example 6
print("###### Example 6 ######")
nums = [5, 5, 5, 3, 1]
expected = [2, 2, 2, 1, 0]
test_case(nums, expected)

# Example 7 
print("###### Example 7 ######")
nums = [0, 100, 50]
expected = [0, 2, 1]
test_case(nums, expected)

# Example 8
print("###### Example 8 ######")
nums = [0, 0, 0]
expected = [0, 0, 0]
test_case(nums, expected)

# Example 9
print("###### Example 9 ######")
nums = [100, 100, 100]
expected = [0, 0, 0]
test_case(nums, expected)

# Example 10 
print("###### Example 10 ######")
nums = [1, 3, 5, 3, 1]
expected = [0, 2, 4, 2, 0]
test_case(nums, expected)

# Example 11
print("###### Example 11 ######")
nums = [10, 10, 5, 8, 5]
expected = [3, 3, 0, 2, 0]
test_case(nums, expected)

# Example 12
print("###### Example 12 ######")
nums = [11, 3, 7, 9, 3]
expected = [4, 0, 2, 3, 0]
test_case(nums, expected)
########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 13 (Custom)
# nums = [...]
# expected = [...]
# test_case(nums, expected)