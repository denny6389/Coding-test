test_case = int(input())
for i in range(0, test_case):
    data = [int(x) for x in input().split()]
    n = data[0]
    m = data[1]
    l = data[2]
    neighbor = {}

    #set up list for neighbors of each dominoe
    for j in range(1, n+1):
        neighbor[j] = []
    for j in range(0, m):
        w = [int(a) for a in input().split()]
        x = w[0]
        y = w[1]
        neighbor[x].append(y)

    check = []
    knock = []
    for j in range(0, l):
        #put the input in the check lick and knock list since it is going to fall
        test = int(input())
        check.append(test)
        knock.append(test)
        #check if the dominoe has neighbors
        while check:
            for n in check[:]:
                if neighbor[n]:
                    #if the dominoe has neighbors, put it in the check list and knock list 
                    check += neighbor[n]
                    knock += neighbor[n]
                    neighbor[n] = []
                #remove after checking is done
                check.remove(n)
    #print the length of distinct element in knock list
    print(len(set(knock)))