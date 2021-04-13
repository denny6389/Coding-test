from collections import Counter

#function for Action 1
#finding A and B such that A + B = 7777
def test1(n,arr):
  #remove all the duplicates to reduce the computation time
  s=set(arr)
  for i in range(1,7777):
      # i + 7777-i = 7777
      if i in s and 7777-i in s:
          return 'Yes'
  return 'No'

#function for Action 2
#finding any duplicates
def test2(n,arr):
    if n == len(set(arr)):
        return "Unique"
    else:
        return "Contains duplicate"

#function for Action 3
#finding and print the integer that appears >𝑁/2 times
def test3(n,arr):
    #find the most common element in the array
    a,b = Counter(arr).most_common(1)[0]
    #Check if it appears more than n/2 times
    return a if b > n/2 else -1

#function for Action 4
#finding median
def test4(n,arr):
    s = sorted(arr)
    #if n is odd print the median
    if n%2 == 1:
        return (s[n//2],)
    #if 𝑁 is even print both median integers of 𝐴 if 𝑁 is even
    else:
        return s[n//2 - 1: n//2 + 1]

#function for Action 5
#finding any elements that are in range 100...999
def test5(n,arr):
    return sorted(filter(lambda z: 99 < z < 1000, arr))

n,t = map(int, input().split())
arr = list(map(int, input().split()))

if t == 1:
  print(test1(n,arr))
elif t == 2:
  print(test2(n,arr))
elif t == 3:
  print(test3(n,arr))
elif t == 4:
  print(" ".join(map(str,test4(n,arr))))
elif t == 5:
  print(" ".join(map(str,test5(n,arr))))