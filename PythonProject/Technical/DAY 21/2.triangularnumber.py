''' Check whether the number is Triangular or not. A number is termed as triangular number if it can represent it in the form of triangular grid of points such that the points form an equilateral triangle and each row contains as many points as the row number, i.e., the first row has one point, second row has two points, third row has three points and so on. The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4). '''


number=int(input())
Total=0
value=1
reach=False
while Total<=number:
	Total+=value
	if number==Total:
		reach=True
		print("1")
		break
	value+=1
if not reach:
	print("0")