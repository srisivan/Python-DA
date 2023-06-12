import math
import random

elements = [0,1]


# Maze Template

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1]]


# User Specifications

print("Enter co-ordinates of start seperated by a comma: ")
print("x bounds: 1-5, y-bounds: 1-8")
x,y = input().split(',')

x = int(x)
y = int(y)

print()

print("Enter co-ordinates of goal seperated by a comma: ")
print("x bounds: 1-5, y-bounds: 1-8")
a,b = input().split(',')

a = int(a)
b = int(b)


# Look_2(): A function to look for possible pathways from start to end point

def look_2(pos):
    x = pos[0]
    y = pos[1]

    moves = []
    possible_moves = []

    """
    if (maze[x][y+1] == '‌') or (maze[x][y+1] == '$'):
        possible_moves.append((x,y+1))
    if (maze[x][y-1] == '‌') or (maze[x][y-1] == '$'):
        possible_moves.append((x,y-1))
    if (maze[x+1][y] == '‌') or (maze[x+1][y] == '$'):
        possible_moves.append((x+1,y))
    if (maze[x-1][y] == '‌') or (maze[x-1][y] == '$'):
        possible_moves.append((x-1,y))

    """

    moves = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]

    possible_moves = [(move[0],move[1]) for move in moves if ((maze[move[0]][move[1]] == 2))]

    return possible_moves


def look(pos):
    x = pos[0]
    y = pos[1]

    moves = []
    possible_moves = []

    """
    if (maze[x][y+1] == '‌') or (maze[x][y+1] == '$'):
        possible_moves.append((x,y+1))
    if (maze[x][y-1] == '‌') or (maze[x][y-1] == '$'):
        possible_moves.append((x,y-1))
    if (maze[x+1][y] == '‌') or (maze[x+1][y] == '$'):
        possible_moves.append((x+1,y))
    if (maze[x-1][y] == '‌') or (maze[x-1][y] == '$'):
        possible_moves.append((x-1,y))

    """

    moves = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]

    possible_moves = [(move[0],move[1]) for move in moves if ((maze[move[0]][move[1]] == '‌') or (maze[move[0]][move[1]] == '$'))]



    if len(possible_moves) == 0:
        maze[x][y] = '-'
        possible_moves = backtrack(pos)

    return possible_moves

def backtrack(pos):
    x = pos[0]
    y = pos[1]

    possible_moves = []

    if maze[x][y+1] == '*':
        possible_moves.append((x,y+1))
    if maze[x][y-1] == '*':
        possible_moves.append((x,y-1))
    if maze[x+1][y] == '*':
        possible_moves.append((x+1,y))
    if maze[x-1][y] == '*':
        possible_moves.append((x-1,y))

    return possible_moves


def distance(possible_moves, goal):

    move_distances = {}

    for move in possible_moves:
        move_distances.update({math.sqrt(abs(((goal[0] - move[0])**2) + ((goal[1] - move[1]) ** 2))):move})

    return move_distances


def move(move_distances):

    distances = list(move_distances.keys())
    min_distance = min(distances)

    return move_distances[min_distance]



def make_path():
    start = (x,y)
    end = (a,b)

    pos = start

    min_goal1 = (random.randint(1,5),random.randint(1,8))
    min_goal2 = (random.randint(1,5),random.randint(1,8))
    min_goal3 = (random.randint(1,5),random.randint(1,8))

    while (pos != min_goal1):
    
        maze[pos[0]][pos[1]] = 0
        pos = move(distance(look(pos),min_goal1))

    while (pos != min_goal2):

        maze[pos[0]][pos[1]] = 0
        pos = move(distance(look_2(pos),min_goal2))

    while (pos != min_goal3):

        maze[pos[0]][pos[1]] = 0
        pos = move(distance(look_2(pos),min_goal3))

    while (pos != goal):

        maze[pos[0]][pos[1]] = 0
        pos = move(distance(look_2(pos),goal))

    return 0

make_path()

print("Here!")

def randomize_maze():

    for i in range(7):
        for j in range(10):
            if maze[i][j] == 2:
                r = random.choice(elements)
                maze[i][j] = r

randomize_maze()


start = (x,y)
goal = (a,b)

maze[goal[0]][goal[1]] = '$'


current_position = start

print(f"Start: {start}\nGoal: {goal}")


for i in range(7):
    for j in range(10):
        if (maze[i][j] == 1):
            maze[i][j] = '▀'
        elif (maze[i][j] == 0):
            maze[i][j] = '‌'

def print_maze(maze, m, n):

    print()

    for i in range(m):
        for j in range(n):
            print(maze[i][j], end = " ")
        print()

    print()

# Main driver code

while (current_position != goal):
    # temp = current_position
    maze[current_position[0]][current_position[1]] = '*'
    print_maze(maze, 7, 10)
    current_position = move(distance(look(current_position, goal)))
