import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 0 3, 2,1 순서
dx,dy = [-1,0,1,0],[0,1,0,-1] #방향
graph[r][c] = -1 #처음에 청소해준다

def function(x,y,way,total):
    while True:
        flag = False
        for _ in range(4):
            nway = (way+3) % 4

            nx,ny = x+dx[nway],y+dy[nway]
            way = nway
            if (0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0):
                graph[nx][ny]=-1
                total +=1
                x,y = nx,ny
                flag = True #4방향이동가능
                break
        if flag == False:
            if(0 <= nx < n and 0 <= ny < m and graph[x-dx[way]][y-dy[way]] == 1):
                return total
            else:
                x,y = x-dx[way],y-dy[way] #후진
print(function(r,c,d,1))
