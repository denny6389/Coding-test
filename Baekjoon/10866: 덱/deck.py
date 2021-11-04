from collections import deque
import sys 
input = sys.stdin.readline

N = int(input())
deck = deque()

for _ in range(N):
  command = input().split()

  if command[0] == "push_front":
    deck.appendleft(command[1])
  elif command[0] == "push_back":
    deck.append(command[1])
  elif command[0] == "pop_front":
    if len(deck) != 0:
      front = deck.popleft()
      print(front)
    else:
      print(-1)
  elif command[0] == "pop_back":
    if len(deck) != 0:
      back = deck.pop()
      print(back)
    else:
      print(-1)
  elif command[0] == "size":
    print(len(deck))
  elif command[0] == "empty":
    if len(deck) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == "front":
    if len(deck) != 0:
      print(deck[0])
    else:
      print(-1)
  else:
    if len(deck) != 0:
      print(deck[-1])
    else:
      print(-1) 
