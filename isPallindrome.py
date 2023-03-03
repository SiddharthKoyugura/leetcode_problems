# Approach 1

def isPallindrome(x):
    x = list(str(x))
    n = len(x)
    i,j = 0, n-1
    while j>=i:
        if x[i]==x[j]:
            i+=1
            j-=1
        else:
            return False
    return True

# Time Complexity: O(n)
# Space Complexity: O(n) 



# Approach 2: Reverse the second half of the number and compare:

def isPallindrome(x):
    if(x<0 or (x%10==0 and x!=0)): return False
    rev = 0
    while rev<x:
        rev = (rev * 10) + (x % 10)
        x //=10
    return (x==rev)or(x==rev//10)

# Time Complexity: O(n) { O(n/2) }
# Space Complexity: O(1) 

print(isPallindrome(1331))