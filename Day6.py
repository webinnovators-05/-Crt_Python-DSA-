#factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#mergesort
nums = [1,2,0,4,3]
def s (nums):
    if len(nums)<=1:
        return nums
    L=len(nums)
    left = nums[:L//2]
    right = nums[L//2:]
    print(s(left),s(right))
    return nums
s (nums)



#Merge Two Sorted Lists (or Merge Sorted Arrays)
L1=1,5,6
L2=2,3,7,8
def merge_lists(L1,L2):
    i,j=0,0
    res=[]
    while i<len(L1) and j<len(L2):
      if L1[i]<=L2[j]:
        res.append(L1[i])
        i+=1
      else:
        res.append(L2[j])
        j+=1
    res.extend(L1[i:])
    res.extend(L2[j:])
    return res
ans=merge_lists([1,5,6],[2,3,5,7,8])
print(ans)