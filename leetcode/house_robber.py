def rob(nums) :
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  if len(nums) == 2:
    return max(nums)
  else:
    return max(nums[0] + rob(nums[2:]), rob(nums[1:]))


houses = [1,2,3,1]

print(rob(houses))
