def my_sqrt(x):
  min_ = 0
  max_ = x
  while max_ >= min_:
    mid = (max_ + min_) // 2
    square = mid * mid
    print(mid, max_, min_)
    if square < x:
      min_ = mid + 1
    elif square > x:
      max_ = mid - 1
    else:
      return mid
  return mid


print(my_sqrt(8))
