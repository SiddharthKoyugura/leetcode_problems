# Approach 1

def myPow(x, n):
    power = 1
    if n<0:
        for i in range(-n):
            power *= x
        return 1/power

    for i in range(n):
        power *= x
    return power

# Time Complexity: O(n)
# Space Complexity: O(1) 

# Approach 2
def myPow(x, n):
    if n==0: return 1
    elif n==1: return x
    elif n<0: return 1/x * myPow(1/x, -(n + 1))
    return myPow(x*x, n//2) if n%2==0 else x*myPow(x*x, n//2)

print(myPow(2,1)) 

# Time Complexity: O(n)
# Space Complexity: O(1) 