


#############################################################################

def most_frequent(nums):
    d = {}
    for num in nums:
        count = d.get(num, 0)
        d.update([(num, count + 1)])
    
    most = -1
    for item in d.items():
        if item[1] > most:
            most = item[1]
            result = item[0]
    return result

#ans = most_frequent([1, 2, 2, 3, 3, 3, 4])
#print(ans)

#############################################################################

def count_pairs(lst, k):
    s = {(a, b) for a in lst for b in lst if a > b and a - b == k}
    return len(s) 

#print(count_pairs([1, 7, 5, 9, 2, 12, 3], k=2))

#############################################################################

def two_sum(lst, target):
    def condition(idx, jdx):
        return lst[idx]+ lst[jdx] == target and idx != jdx
    
    ran = range(len(lst))
    s = {(idx, jdx) for idx in ran for jdx in ran if condition(idx, jdx)}
    return s.pop()

print(two_sum([2, 7, 11, 15], 9))

#############################################################################


