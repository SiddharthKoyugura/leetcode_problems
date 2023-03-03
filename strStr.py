
# Approach 1
def strStr(haystack, needle):
    m, n = len(haystack), len(needle)
    for i in range(m-n+1):
        j=0
        for j in range(n):
            if haystack[i+j]!=needle[j]: break
        if (j == n-1 ) and (haystack[i+j]==needle[j]): return i
    return -1

## Time Complexity: O(n**2)
## Space Complexity: O(1)


# Approach 2 (KMP Algorithm)

def strStr(haystack, needle):
    m, n = len(haystack), len(needle)
    # Calculate lps array
    lps = lps_array(needle, n)
    i, j = 0, 0
    while((m-i)>=(n-j)):
        if haystack[i] == needle[j]:
            i+=1
            j+=1
            if j==n: return i-j
        elif i<m and haystack[i]!=needle[j]:
            if j!=0: j=lps[j-1]
            else: i+=1
    return -1

def lps_array(needle, n):
    length, i, lps = 0, 1, [0]*n
    while i<n:
        if needle[i] == needle[length]:
            length += 1
            lps[i]=length
            i+=1
        elif length!=0: length = lps[length-1]
        else: 
            lps[i]=0
            i+=1
    return lps


## Time Complexity: O(n)
## Space Complexity: O(m)



print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("hello", "ll"))
print(strStr("mississippi", "issip"))