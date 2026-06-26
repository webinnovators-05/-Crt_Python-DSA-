nums=input()
s=0
for i in nums:
    if i.isdigit():
        s+=int(i)
print(s)


nums=input()
s=1
for i in nums:
    if i.isdigit():
        s*=int(i)
print(s)

nums=input()
t=int(input())
c=0
for i in nums:
    if i.isdigit() and int(i)==t:
        c+=1
print(c)



nums=input().split()
print(nums)


nums = input()
s = 0
for i in nums:
    if i.isdigit():
        s += int(i) ** 2

print(s)


nums=input().split(",")
l=len(nums)
for j in range(l):
    for i in range (j+1,l):
        print(nums[0],nums[i])