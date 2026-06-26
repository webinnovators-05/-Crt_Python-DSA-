#ibonacci Series using Dynamic Programming (Memoization)
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
print(fib(5))

"""Dynamic program  is  an algorithm technique for solving an optimization
 problem by breaking it down into simpler
subproblems and utilizing the fact that the optimal solution to
the overall probelm depends upon the optimal solution to its subproblems""" 


#Fibonacci Series using Dynamic Programming (Tabulation / Bottom-Up Approach)
def fib(n):
    if n <= 1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print (fib(9))


#Fibonacci Series using Dynamic Programming (Space Optimization)
def fib(n):
    if n <= 1:
        return n
    prev2=0
    prev=1
    for i in range(2,n+1):
        i= prev+prev2
        prev2=prev
        prev=i
    return prev
print (fib(9))


#Fibonacci Series using Recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)