nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]


def summary_ranges(nums):
  start = nums[0]
  end = -1
  res = []
  for i in range(len(nums) - 1):
    if nums[i] != nums[i + 1] - 1:
      end = nums[i]
      if start != end:
        res.append(f"{start}->{end}")
      else:
        res.append(f"{start}")
      start = nums[i + 1]
  end = nums[len(nums) - 1]
  if start != end:
    res.append(f"{start}->{end}")
  else:
    res.append(f"{start}")
  return res


print(summary_ranges(nums))
