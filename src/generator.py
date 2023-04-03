import random

def generate_matrix(size, start, end, dead_end_prob=0.7):
    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Set the starting and ending points
    i, j = start
    matrix[i][j] = 8
    i, j = end
    matrix[i][j] = 9

    # Generate a solution path from start to end
    path = [(start[0], start[1])]
    i, j = start
    while (i, j) != end:
        # Find the neighboring cells that are not dead ends or part of the path
        neighbors = []
        if i > 0 and matrix[i-1][j] not in (1, 2):
            neighbors.append((i-1, j))
        if j > 0 and matrix[i][j-1] not in (1, 2):
            neighbors.append((i, j-1))
        if i < size-1 and matrix[i+1][j] not in (1, 2):
            neighbors.append((i+1, j))
        if j < size-1 and matrix[i][j+1] not in (1, 2):
            neighbors.append((i, j+1))

        # Choose a random neighbor and mark it as part of the path
        if neighbors:
            i, j = random.choice(neighbors)
            path.append((i, j))
            # Mark the cell as part of the path, unless it's the starting or ending point
            if (i, j) != start and (i, j) != end:
                matrix[i][j] = 1
        # If there are no neighbors available, backtrack to the previous cell
        else:
            i, j = path[-1]
            path.pop()
    
    # Mark the cells adjacent to the path as part of the path
    for i, j in path:
        if j > 0 and matrix[i][j-1] not in (1, 2):
            matrix[i][j-1] = 1
        if j < size-1 and matrix[i][j+1] not in (1, 2):
            matrix[i][j+1] = 1
        if i > 0 and matrix[i-1][j] not in (1, 2):
            matrix[i-1][j] = 1
        if i < size-1 and matrix[i+1][j] not in (1, 2):
            matrix[i+1][j] = 1
            
    # Mark the cells in the block's path as part of the path
    for i, j in path:
        if matrix[i][j] == 1:
            if i > 0 and matrix[i-1][j] == 0:
                matrix[i-1][j] = 1
            if i < size-1 and matrix[i+1][j] == 0:
                matrix[i+1][j] = 1
            if j > 0 and matrix[i][j-1] == 0:
                matrix[i][j-1] = 1
            if j < size-1 and matrix[i][j+1] == 0:
                matrix[i][j+1] = 1

    i, j = start
    matrix[i][j] = 1
    i, j = end
    matrix[i][j] = 1
            
    return matrix


def print_matrix(matrix,size):
    print("Game Matrix")
    
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print('\n')