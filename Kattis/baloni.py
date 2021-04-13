from collections import defaultdict

#first set the dictionary with default value 0
startH = defaultdict(int)
#each value in dictionary is the position of the balloons

length = input()

heights = list(map(int, input().split()))

ans = 0
for x in heights:
    #if the height that is 1 above the current one was popped then no need to shoot a new arrow
    if startH[x+1] > 0:
        startH[x+1] -= 1
    else:
    #if not we need new one
        ans += 1
    #mark that the balloon was popped
    startH[x] += 1
print(ans)