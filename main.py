data = []

# read data from file
for line in open('data.txt', 'r').readlines():
    data.append(line.strip())

# coordinate system
coordinate_system = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

print(coordinate_system)

# create class for lines
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        coordinate_system[y1][x1] += 1
        coordinate_system[y2][x2] += 1

# sort out coordinate pairs
for line in data:
    pair = line.split(' -> ')

    # print(pair)
    x1 = int((pair[0].split(','))[0])
    y1 = int((pair[0].split(','))[1])
    
    x2 = int((pair[1].split(','))[0])
    y2 = int((pair[1].split(','))[1])

    line = Line(x1, y1, x2, y2)
    line.draw()

print('')
print(coordinate_system)