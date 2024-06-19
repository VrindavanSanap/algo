def maxSubArray(nums):
  def maxSubArray_(i):
    if i == 0:
      return max(nums[i],0)
    else:
      return max(nums[i],nums[i]+ maxSubArray_(i-1))
  max_ = 0 
  print(nums)
  for i in range(len(nums)):
    t = maxSubArray_(i)
    print(t, end = " ")
    if max_ < t:
      max_ = t
  return max_
nums = [5,4,-1,7,8]

print(maxSubArray(nums))
