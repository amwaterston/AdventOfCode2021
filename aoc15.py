

def getvalue(grid, x, y):
    actualx = x % len(grid[0])
    actualy = y % len(grid)
    dx = (x - actualx) / len(grid[0])
    dy = (y - actualy) / len(grid)
    v = grid[actualy][actualx]
    return int((v + dx + dy - 1) % 9) + 1

with open('input15.txt') as fp:
    grid = [[int(c) for c in line.strip()]for line in fp.readlines()]

    current = (0, 0)
    grid_mult = 5
    gridw = len(grid[0]) * grid_mult
    gridh = len(grid) * grid_mult
    goal = (gridw - 1, gridh - 1)
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dists = [[-1] * gridw for i in range(gridh)]
    open_nodes = [(current, 0)]

    while (len(open_nodes) != 0):
        current, dist = min(open_nodes, key = lambda x: x[1])
        for dx, dy in deltas:
            newx = current[0] + dx
            newy = current[1] + dy
            if newx >= 0 and newx < gridw and newy >= 0 and newy < gridh:
                v = getvalue(grid, newx, newy)
                if dists[newy][newx] == -1 or dists[newy][newx] > dist + v:
                    dists[newy][newx] = dist + v
                    open_nodes.append(((newx, newy), dists[newy][newx]))
        open_nodes.remove((current, dist))

    print(dists[goal[1]][goal[0]])