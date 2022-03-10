


from heap import Heap

nums = [7, 2, 3, 1, 12]
nums = [5, 3, 8, 4, 1, 2]


def kth_largest(arr, k):
    h = Heap()
    for num in nums:
        h.insert(num)

    ans = None
    for idx in range(k):
        ans = h.remove()

    return ans

print(kth_largest(nums, 1))
print(kth_largest(nums, 2))
print(kth_largest(nums, 3))
