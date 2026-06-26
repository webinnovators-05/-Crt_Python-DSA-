# Reverse List Using Slicing
nums=input().split()
L=len(nums)
nums=nums[::-1]
print(nums)


a=[1,2,3,4,5,6]
reve= a[::-1]
print(reve) 


#Reverse a List Without Using Slicing
nums=input().split()
L=len(nums)
list2=[]
for i in range(L):
    print(nums[L-1-i])
print(nums) 


#Reverse a List Using a for Loop and append()
nums = input().split()
L = len(nums)
list2 = []

for i in range(1, L + 1):
    list2.append(nums[L - i])

print(list2)


#Generate All Pairs from a Reversed List
nums = input().split()
L = len(nums)
list2 = []

for i in range(1, L + 1):
    list2.append(nums[L - i])

nums = list2

for i in range(L):
    for j in range(i + 1, L):
        print(nums[i], nums[j])


#Print Even Numbers from 100 to 2 in Descending Order
for i in range(100,0,-2):
    c+=1
    print(i,"hello") 


#Nested Loops with Iteration Counter
c=0
for j in range(5):
  for i in range(3):
    c+=1
    print(c,j*i,"hello")

c = 0

for i in range(5):
    for j in range(100):
        c += 1
        print(c, i, j)


#Nested Loops to Print Iteration Count and Indices
c=0
for i in range(10):
    for j in range (10):
        c+=1
        print(c,j,i)



#Number Repetition Program
n=int(input())

for i in range(n):
    for j in range(3):
        print(i)

#anagram
a="listen"
b="slient"

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("not Anagrams")


#prime number
num=int(input("Enter the number:"))
if num<=1:
    print("not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("not a prime number")
    else:
         print("a prime number")


n=int(input())
c=0
for i in range(2,int(n**0.5)+1):
    if n%1==0:
        c+=1
        print("not a prime number")
        break
if c==0:
    print("prime")


#factors
n=int(input())
c=0
for i in range(1,n//2+1):
    if n%i==0:
       c+=1
       print(c,i)
print(c+1,n)


#Search for an Element in a List
list = []
for i in range(1, 100000):
    list.append(i)

target = 99000000

list2 = list(range(1, 100000))
print(target in list) 