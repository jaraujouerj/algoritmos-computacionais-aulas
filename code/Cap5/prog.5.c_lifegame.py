(width, height) = (6, 6)
initial_array = [[0 for x in range(width)] for y in range(height)]
initial_array[0][1] = 1
initial_array[1][2] = 1
initial_array[2][0] = 1
initial_array[2][1] = 1
initial_array[2][2] = 1

for t in range(10):
    initial_array=[[([[sum(array[y1][x1] for array in [[[((-1<x2+dx<width) and (-1<y2+dy<height)) and initial_array[y2+dy][x2+dx] or 0 for x2 in range(width)] for y2 in range(height)] for (dx,dy) in [(dx,dy) for dx in [-1,0,1] for dy in [-1,0,1] if (dy!=0 or dx!=0)]]) for x1 in range(width)] for y1 in range(height)][y][x]== 3 or ([[sum(array[y3][x3] for array in [[[((-1<x4+dx<width) and (-1<y4+dy<height)) and initial_array[y4+dy][x4+dx] or 0 for x4 in range(width)] for y4 in range(height)] for (dx,dy) in [(dx,dy) for dx in [-1,0,1] for dy in [-1,0,1] if (dy!=0 or dx!=0)]]) for x3 in range(width)] for y3 in range(height)][y][x] == 2 and initial_array[y][x]==1)) and 1 or 0 for x in range(width)] for y in range(height)]     
    print ("_"*18)
    for line in initial_array:
        print (line)
