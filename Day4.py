#Convert the First Input Element to an Integer
nums=input().split()
print(nums)
nums[0]=int(nums[0])
print(nums)


#Convert All Input Elements to Integers
nums=input().split()
print(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])
print(nums)

#find min and max
nums=input().split()
print(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])**2
print(nums)


#Multiply Even-Index Elements by 2 and Odd-Index Elements by 3
nums = input().split()
print(nums)

for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = int(nums[i]) * 2
    else:
        nums[i] = int(nums[i]) * 3

print(nums)


#Square Elements at Square Indices
nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    nums[i*i] = nums[i*i] ** 2

print(nums)


#Square Elements at Valid Square Indice
nums = list(map(int, input().split()))
for i in range(1,len(nums)):
    if i*i>=len(nums):
       break
    nums[i*i]=nums[i*i]**2
print(nums)


#Square Elements and Store Results in a New List
nums = list(map(int, input().split()))
list2=[]
for i in range(1,len(nums)):
    if i*1>=len(nums):
        break
    nums[i*1]=nums[i*1]**2
    list2.append(nums[i])
print(list2)


#Read and Display a List of Integers
nums = list(map(int, input().split()))

print(nums)



#max
nums = list(map(int, input().split()))
curr_max=float('-inf')
for i in range(len(nums)):
    if curr_max<nums[i]:
        curr_max=nums[i]
print(curr_max)



#min
nums = list(map(int, input().split()))
curr_min=float('inf')
for i in range(len(nums)):
    if curr_min>nums[i]:
        curr_min=nums[i]
print(curr_min)



#check Even or odd
num=4
if num%2==0:
    if num>1:
        print("even positive")
    else:
        print("even negative")
else:
    if num>0:
        print("odd positive")
    else:
        print("odd negative")


#Check Number Type with Nested Conditions
num=3
if num%2==0 and num>1:
    print("even positive")
    if 100%num==0:
        print("super number")
elif num%2==0 and num<0:
    print("even negative")
elif num%2==0 and num>1:
    print("odd positive")
elif num%2==0 and num<0:
    print("odd negative")


#Function Without a Return Value
def h():
   for i in range(3):
        print(i)
result=(h())
print(result) 
