def main():
    length = int(input())
    weights = list(map(int, input().split()))
    low_weights = genLowWeight(weights, 0, 0, 0)
    #calculate the total sum of weights and subtract the invalid sets 
    res = sum(weights)*(2**(length-1))
    res -= low_weights
    print(res)

#generate the sum of the weights that are lower than 200
def genLowWeight(weights, i, n, total):
   #find the set that is lower than 200 with 3 fruits since every 4 fruits >= 200
    if n == len(weights) or i == 4:
        if total < 200:
            return total
        return 0
    ans = genLowWeight(weights, i+1, n+1, total+weights[n])
    ans += genLowWeight(weights, i, n+1, total)
    return ans

if __name__ == '__main__':
    main()