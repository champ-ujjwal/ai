V = {}
E = {}
V = ({'A': 7, 'B': 9, 'C': 6, 'D': 5, 'E': 6, 'F': 4.5, 'H': 4, 'I': 2, 'J': 3, 'K': 3.5, 'G': 0})
E = (
{('B', 'D'): 2, ('A', 'B'): 4, ('A', 'C'): 4, ('A', 'D'): 7, ('D', 'E'): 6, ('E', 'F'): 5, ('D', 'F'): 8, ('D', 'H'): 5,
 ('H', 'I'): 3, ('I', 'J'): 3, ('J', 'K'): 3, ('K', 'H'): 3, ('F', 'G'): 5})
INFINITY = 100000000
cameFrom = {}


def h(node):
    return V[node]


def cost(node, succ):
    return E[node, succ]


def successors(node):
    neighbours = []
    for item in E:
        if node == item[0][0]:
            neighbours.append(item[1][0])
    return neighbours


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    
    return total_path


def ida_star(root, goal):
    global cameFrom

    def search(node, g, bound):
        min_node = None
        global cameFrom
        f = g + h(node)
        if f > bound: return f
        if node == goal: return "FOUND"
        minn = INFINITY
        for succ in successors(node):
            t = search(succ, g + cost(node, succ), bound)
            if t == "FOUND": return "FOUND"
            if t < minn:
                minn = t
                min_node = succ
        cameFrom[min_node] = node
        return minn

    bound = h(root)
    count = 1
    while 1:
        # print("itertion" + str(count))
        count += 1
        t = search(root, 0, bound)
        if t == "FOUND":
            print(reconstruct_path(cameFrom, goal))
            return bound
        if t == INFINITY: return "NOT_FOUND"
        bound = t


print(ida_star('A', 'G'))