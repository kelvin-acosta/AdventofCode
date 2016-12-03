import re

def navigation(path):
	x = 0
	y = 0
	lCount = 0 # Left turns
	rCount = 0 # Right turns
	for direction in path:
		if direction[0] == "L" :
			lCount += 1
			if lCount == 4:
				y += int(direction[1:]) # North
				lCount = 0
				rCount = 0
			if lCount == 2:
				rCount = 2
				y -= int(direction[1:]) # South
			if lCount == 3:
				rCount = 1
				x += int(direction[1:]) # East
			if lCount == 1:
				rCount = 3
				x -= int(direction[1:]) # West
		elif direction[0] == "R":
			rCount += 1
			if rCount == 4:
				y += int(direction[1:]) # North
				rCount = 0
				lCount = 0
			if rCount == 2:
				lCount = 2
				y -= int(direction[1:]) # South
			if rCount == 1:
				lCount = 3
				x += int(direction[1:]) # East
			if rCount == 3:
				lCount = 1
				x -= int(direction[1:]) # West
	print x + y

def main():
	data = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"
	path = re.split(', ', data)
	navigation(path)

main()
