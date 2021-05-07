import math
test_case = int(input())
for i in range(0, test_case):
	command = int(input())
	angle = 90 #turtle is facing forward
	x, y = 0.0, 0.0
	for j in range(0, command):
		cmd = input().split()
		num = int(cmd[1])
		if cmd[0] == "fd":
      #getting the x, y coordinate caused by the fd command
      #based on the angle of the turtle
			x += num * math.cos(math.radians(angle))
			y += num * math.sin(math.radians(angle))
		elif cmd[0] == "bk":
      #getting the x, y coordinate caused by the bk command
      #based on the angle of the turtle
			x -= num*math.cos(math.radians(angle))
			y -= num*math.sin(math.radians(angle))
		elif cmd[0] == "lt":
      #turning its body to the right by num degrees
			angle = (angle - num) % 360
		else:
      #turning its body to the right by num degrees
			angle = (angle + num) % 360
      #Determine the distance from the starting position to the final position by hypotenuse function
	print(round(math.hypot(x, y)))