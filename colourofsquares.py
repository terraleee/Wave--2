position = input("Enter the position of the piece: ")

column = position[0]
row = float(position[1])

if column in "a,c,e,g":
	blackstart = True
else:
	blackstart = False
	
if blackstart:
	if row % 2 == 0:
		white = True
	else:
		white = False
else:
	if row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("This square is white")
else:
	print("This square is black")