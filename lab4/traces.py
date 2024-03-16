# more = [x + 1 for x in [1,2,3,4]]  # Place a breakpoint on this line
# print()
# 1. 1, 2, 3, 4
# 2. [2, 3, 4, 5]


# def square(n: int) -> int:
#     return n * n  # Place a breakpoint on this line
#
# squares = [square(x) for x in [1, 2, 3, 4]]
# print()
# 1. 1 and 1     2 and 4     3 and 9     4 and 16
# 2. [1, 4, 9, 16] each value is squared


# def check(n: int) -> bool:
#     return n > 2  # Place a breakpoint on this line
#
# answer = [x for x in range(5) if check(x)]
# print()
# 1. 0 false, 1 false, 2 false, 3 true, 4 true
# [3, 4] each value is taken out if <=2


# def inc(m: int) -> int:
#     return m + 1  # Place a breakpoint on this line
#
# def check(n: int) -> bool:
#     return n > 2  # Place a breakpoint on this line, too!
#
#
# answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?
# print(answer)
# 1. 0 false 1 false 2 false 3 true 4 true
# 2. 3 4    4 5
# [4, 5]


# def tally(nums: list[int]) -> int:
#     total = 0
#     for num in nums:
#         total = total + num # Place a breakpoint here
#     return total
#
# result = tally([4, 9, 2, 1])
# 1. num and total-- 4 and 4 9 and 13 2 and 15 1 and 16


# def copy(nums: list[int]) -> list[int]:
#     new_list = []
#     for idx in range(len(nums)):
#         new_list.append(nums[idx])
#     return new_list
#
# result = copy([4, 9, 2, 1])
# 1. new_list and idx-- [4] and 0, [4, 9] and 1, [4, 9, 2] and 2, [4, 9, 2, 1] and 3
# 2. this creates a new list instead of keeping the old one


# def increment_all(nums: list[int]) -> list[int]:
#     new_list = []
#     for value in nums:
#         new_list.append(value + 1)
#     return new_list
#
# result = increment_all([4, 9, 2, 1])
# 1. new list and value-- [5] and 4, [5, 10] and 9, [5, 10, 3] and 2, [5, 10, 3, 2] and 1


