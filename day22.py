
import re
import copy

MAX_X = 32
MAX_Y = 28

def parse_line(line):
    """
    >>> parse_line("Filesystem              Size  Used  Avail  Use%")

    >>> parse_line("/dev/grid/node-x0-y0     85T   67T    18T   78%")
    (0, 0, 67, 18)

    :param line:
    :return:
    """
    splitted_line = line.split()
    reg = re.compile(".+node-x(\d+)-y(\d+)")
    match = reg.match(splitted_line[0])
    if match:

        x = int(match.group(1))
        y = int(match.group(2))

        used = int(splitted_line[2][:-1])
        available = int(splitted_line[1][:-1])

        return x, y, used, available
    else:
        return match

#
# def read_data(input_file):
#     tnodes = list() # (x,y,used,available)
#     with open(input_file) as f:
#         for line in f:
#             if parse_line(line):
#                 tx, ty, used, available = parse_line(line)
#                 tnodes.append((tx,ty,used, available))
#
#     return tnodes


def read_data(input_file):
    tnodes = [[(0, 0) for j in range(MAX_Y+1)] for i in range(MAX_X+1)]  # (used,total_size)
    with open(input_file) as f:
        for line in f:
            if parse_line(line):
                tx, ty, used, available = parse_line(line)
                tnodes[tx][ty] = (used, available)
    return tnodes

DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

def get_empty_node(nodes):
    for x in range(33):
        for y in range(29):
            used, _ = nodes[x][y]
            if used == 0:
                print("unused node at " + str(x) + "  " + str(y))
                return x,y

def get_steps_to_front(startpos,goalpos,nodes,ignore_point):
    newstnodes = copy.deepcopy(nodes)
    to_expand = [(startpos[0], startpos[1], 0,[], newstnodes)] # x,y,steps,history,map
    visited = [[0 for j in range(MAX_Y + 1)] for i in range(MAX_X + 1)]

    print("Before: ")
    for idx, xline in enumerate(nodes):
        to_print = " "
        for idy,y in enumerate(xline):
            if idx == startpos[0] and idy == startpos[1]:
                to_print += " - start - "
            elif idx == goalpos[0] and idy == goalpos[1]:
                to_print += " - goal - "
            else:
                to_print += "- " + str(y) + " - "
        print(to_print)
    while len(to_expand) > 0:
        expanding = to_expand.pop(0)
    #    print(expanding)
        if expanding[0] == goalpos[0] and expanding[1] == goalpos[1]:
            print("REACHED!!")
            print(expanding[3])
            for hist_node in expanding[3]:
                print(nodes[hist_node[0]][hist_node[1]])
            print("in " + str(expanding[2]) + " steps")
            return expanding[2],expanding[4]
#        print(expanding)

        expx,expy,had_so_far,hist_here,map_here = expanding
        if visited[expx][expy]:
            continue
        visited[expx][expy] = 1

        for dirx,diry in DIRECTIONS:
            newx = expx + dirx
            newy = expy + diry
            if newx >= 0 and newx <= 32 and newy >= 0 and newy <= 28 and (newx,newy) != ignore_point:
                if map_here[newx][newy][0] <= map_here[expx][expy][1]: # used is smaller than available at current expanding place

                    # expand
                    new_hist = list(hist_here)
                    new_hist.append((expx, expy))
                    new_map = copy.deepcopy(map_here)
                    new_map[expx][expy] = (new_map[newx][newy][0],new_map[expx][expy][1])
                    new_map[newx][newy] = (0,new_map[newx][newy][1])

                    to_expand.append((newx, newy, had_so_far+1, new_hist, new_map))


def move_to_zero(start_pos, first_goal_pos,nodes):
    ignore_point = (32, 0)
    steps_to_first,new_map = get_steps_to_front(start_pos,first_goal_pos,nodes,ignore_point)

    total_steps = steps_to_first
    print("for first: " + str(steps_to_first))
    while True:
        total_steps += 1
        if first_goal_pos == (0,0):
            break
        ignore_point = first_goal_pos
        start_pos = (first_goal_pos[0]+1,first_goal_pos[1])

        first_goal_pos = (first_goal_pos[0]-1,first_goal_pos[1]) #x -=1 , y remains y
        print("trying to reach " + str(first_goal_pos) + " from " + str(start_pos))
        extra, new_map =get_steps_to_front(start_pos,first_goal_pos,new_map,ignore_point)
        total_steps += extra
    print(total_steps)

if __name__ == "__main__":
    nodes = read_data('input.txt')
    print(nodes)
    print(len(nodes))
    for xline in nodes:
        print(str(xline[0]) + " and " + str(xline[1]))
    start_pos = get_empty_node(nodes)
    print("Start pos: " + str(start_pos))
    move_to_zero(start_pos,(31,0),nodes)
    # viable_nodes = 0
    # bad_nodes = 0
    # for i, nodeA in enumerate(nodes):
    #     for j, nodeB in enumerate(nodes):
    #         if nodeA[2] > 0: # used
    #             if not (nodeA[0] == nodeB[0] and nodeA[1] == nodeB[1]): # same pos
    #                 if nodeB[3] - nodeA[2] > 0:
    #                     viable_nodes +=1
    #                 else:
    #                     bad_nodes+=1
    #             else:
    #                 bad_nodes +=1
    #         else:
    #
    #             bad_nodes+=1
    # print(viable_nodes)
    # print(bad_nodes)
    # for x in range(MAX_X+1):
    #     for y in range(MAX_Y+1):
    #         for testx in range(MAX_X+1):
    #             for testy in range(MAX_Y+1):
    #
    #                 nodeA = nodes[x][y]
    #                 nodeB = nodes[testx][testy]
    #                 if nodeA[0] > 0 and x != testx and y != testy and nodeA[0] <= nodeB[1]:
    #                     viable_nodes +=1
    #                     #else:
    #                      #   print("Node " + str(nodeA) + " and " + str(nodeB) + " not compatible")
    # print(viable_nodes)


