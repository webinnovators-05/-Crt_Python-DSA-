#bubblesort
def Bubblesort(nums):
  L=len(nums)
  c=0
  for j in range (L):
        swapped=False
        for i in range(L-1-j):
          c+=1
          if nums[i]>nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            swapped=True
        print(c,j,i,nums)
        if not swapped:
          break
  return nums

nums = [5,4,3,2,1]
print(Bubblesort(nums))

#selectionsort
def selectionsort(arr):
  n=len(arr)
  for i in range (n):
    min_index = i
    for j in range(i+1,n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i],arr[min_index] = arr[min_index] ,arr[i]
  return arr
  nums = [5,4,7,9,1]
print(selectionsort(nums))

#insertionsort
def insertion_sort(arr):
  for i in range(1,len(arr)):
    key = arr [i]
    j = i - 1
    while j>= 0 and arr[j] >key:
      arr[j+1] = arr [j]
      j -= 1
    arr[j + 1] = key
  return arr

nums=[9,10,6,8,18]
print(insertion_sort(nums))

#Recursion
""" recursion is a problem sloving technique where a funtion solves
a problem by calling itself on a smaller version of the same problem
until a stopping condition (base case) is reached"""

i=0
for i in range(1,11):
  print(i)


i=20
while i>10:
  print(i-10)
  i-=1


def count(n):
  if n==0:
    return
  print(n)
  count(n-1)
count(10)                                                                                          
 

def Hello():
    for i in range(5):
      print(i)
      if i==2:
        return
print('Hello')


#recursion
def sum_n(n):
  if n <=0:
    return
  return n + sum_n(n-1)