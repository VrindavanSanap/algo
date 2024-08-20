import random

    a = random.sample(range(1, 101), 100)

                          def swap(i, j) :a[i], a[j] = a[j], a[i]

                                                         def bubble_sort(a) :len_a = len(a) steps = 0 swapped = True while swapped:swapped = False for i in range(len_a - 1) : if a[i]> a[i + 1] :swap(i, i + 1) swapped = True steps += 1 return steps

                                                                                                                                                                                                       steps = bubble_sort(a) print(steps)
