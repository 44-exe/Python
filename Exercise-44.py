# Author: Jeong Bin Lee
# Date: 2021.03.11
# Brief: Write a Python program to find the maximum total from top to bottom of the triangle below. But the numbers can only move adjacent from the previous number

triangle_num = [
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]

max_num = [0] * 15

print(max_num)
index = 0;
max_num[0] = triangle_num[0][0]
for i in range(1, len(triangle_num)):
	if triangle_num[i][index] < triangle_num[i][index+1]:
		max_num[i] = triangle_num[i][index+1]
		index += 1
	else:
		max_num[i] = triangle_num[i][index]


print(max_num)
total = 0
for i in range(len(max_num)):
	total += max_num[i]

print(total)

