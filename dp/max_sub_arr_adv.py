from typing import List

def max_sub_array(nums: List[int]) -> int:
	memo = {}

	def max_sub_array_(i: int) -> int:
		# Return maximum subarray for nums[:i]
		if i == 0:
			return nums[i]
		if i in memo:
			return memo[i]

		else:
			memo[i] = max(nums[i], nums[i] + max_sub_array_(i - 1))
			return memo[i]

	max_ = -float("inf")
	for i in range(len(nums)):
		t = max_sub_array_(i)
		if max_ < t:
			max_ = t
	return max_

nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(max_sub_array(nums))