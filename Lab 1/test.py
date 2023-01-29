Labyrinth = [[0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 1, 1, 3, 0],
[0, 0, 1, 1, 1, 0, 0, 0],
[0, 1, 2, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0]]

def astar(lab):
    # first, let's look for the beginning position, there is better but it works
    (i_s, j_s) = [[(i, j) for j, cell in enumerate(row) if cell == 2] for i, row in enumerate(lab) if 2 in row][0][0]
    # and take the goal position (used in the heuristic)
    (i_e, j_e) = [[(i, j) for j, cell in enumerate(row) if cell == 3] for i, row in enumerate(lab) if 3 in row][0][0]

    width = len(lab[0])
    height = len(lab)

    heuristic = lambda i, j: abs(i_e - i) + abs(j_e - j)
    comp = lambda state: state[2] + state[3] # get the total cost

    # small variation for easier code, state is (coord_tuple, previous, path_cost, heuristic_cost)
    fringe = [((i_s, j_s), list(), 0, heuristic(i_s, j_s))]
    visited = {} # empty set

    # maybe limit to prevent too long search
    while True:

        # get first state (least cost)
        state = fringe.pop(0)

        # goal check
        (i, j) = state[0]
        if lab[i][j] == 3:
            path = [state[0]] + state[1]
            path.reverse()
            return path

        # set the cost (path is enough since the heuristic won't change)
        visited[(i, j)] = state[2] 

        # explore neighbor
        neighbor = list()
        if i > 0 and lab[i-1][j] > 0: #top
            neighbor.append((i-1, j))
        if i < height and lab[i+1][j] > 0:
            neighbor.append((i+1, j))
        if j > 0 and lab[i][j-1] > 0:
            neighbor.append((i, j-1))
        if j < width and lab[i][j+1] > 0:
            neighbor.append((i, j+1))

        for n in neighbor:
            next_cost = state[2] + 1
            if n in visited and visited[n] >= next_cost:
                continue
            fringe.append((n, [state[0]] + state[1], next_cost, heuristic(n[0], n[1])))

        # resort the list (SHOULD use a priority queue here to avoid re-sorting all the time)
        fringe.sort(key=comp)

print(astar(Labyrinth))