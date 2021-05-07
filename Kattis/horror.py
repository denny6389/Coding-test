#get the number of movie lists and the number of similarities
v,_,e = map(int,input().split())

#queue for Horror index list
#not_visit for bfs 
#graph for graph
queue, not_visit, graph = [], set(range(v)), [[] for _ in range(v)]

#get the movies in the horror list
#remove them on not_visit list and append on the queue
for s in map(int,input().split()):
  not_visit.remove(s)
  queue.append((0,s))

#put the similar movies list in the graph 
for _ in range(e):
  adj = list(map(int,input().split()))
  graph[adj[0]].append(adj[1])
  graph[adj[1]].append(adj[0])

#Horror index and id
H, i = -1,-1

while queue:
  Hindex, aid = queue.pop(0)
  #highest Horror Index and in case of a tie, lowest ID.
  if Hindex > H or (Hindex == H and aid < i):
    H, i = Hindex, aid
  
  #check the similar movie in the graph list for bfs
  for bid in graph[aid]:
    if bid in not_visit:
      not_visit.remove(bid)
      #+1 since the worst directly similar movie has 𝐻𝐼
      queue.append((Hindex+1,bid))

#if every movie is visited print the lowest id
if not not_visit:
  print(i)
#else print the min id that is not similar with the horror movie
else:
  print(min(not_visit))