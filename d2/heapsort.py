


from heap import Heap

nums = [7, 2, 3, 1, 12]
h = Heap()

for num in nums:
    h.insert(num)

for idx in range(len(nums) - 1, -1, -1):
    nums[idx] = h.remove()

print('\n\t', nums, '\n')
