def flip (tasks,grid):
    grid2=[[1,2],[3,4]]
    print(grid2)
    for r in range(len(grid)):
        for c in range(len(grid)):
            for letter in tasks:
                if flips == "H":
                    grid2[r][c] = grid[1 - r][c]
                    print("Loop1")
                if letter =="V":
                    grid2 [r] [c]= grid[r][c-1]
                    print("loop2")
    return grid2

flips = input()

tasks =[]
tasks.append(flips)
tasks = [char for char in tasks[0]]

grid = [[1, 2], [3, 4]]

final = flip(tasks,grid)

for row in final:
	for item in row:
		print(item, end=" ")
	print()

# 1 2
# 3 4




