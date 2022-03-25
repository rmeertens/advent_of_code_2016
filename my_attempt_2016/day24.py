import copy

def read_maze(filename):
    with open(filename) as f:
        reachable_maze = list() # Y axis -> X-axis
        important_places = dict()
        for y_place,line in enumerate(f):
            line = line[:-1] # remove the \n
            new_line = []
            for x_place,character in enumerate(line):
                if character =="#":
                    new_line.append(False)
                else:
                    new_line.append(True)
                    if character != ".":
                        important_places[character] = (x_place,y_place) # X - Y for important places
            reachable_maze.append(new_line)
    return reachable_maze,important_places

def print_maze(maze):
    for y_axis in maze:
        to_print = ""
        for x in y_axis:
            if x:
                to_print += "."
            else:
                to_print += "#"
        print(to_print)

def a_star_search_distance(maze, start_location, end_location):
    locations_to_prune = [(0,start_location[0],start_location[1],0)] # F, X - Y - distance_so_far
    # ... visited... ?
    directions_possible = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = []
    while len(locations_to_prune) > 0:
        locations_to_prune.sort()
        prune_now = locations_to_prune.pop(0)

        if prune_now[1] == end_location[0] and prune_now[2] == end_location[1]:
            print("Found in " + str(prune_now[2]) + " steps")
            return prune_now[3]
        for d in directions_possible:
            new_posx = d[0] + prune_now[1]
            new_posy = d[1] + prune_now[2]
            if 0 <= new_posx < len(maze[0]) and new_posy >= 0 and new_posy < len(maze):
                if (new_posx,new_posy) not in visited and maze[new_posy][new_posx]:
                    new_h = end_location[0]-new_posx + end_location[1] - new_posy
                    new_d = prune_now[3]+1
                    new_f = new_d+new_h
                    locations_to_prune.append((new_f,new_posx,new_posy,new_d))
                    visited.append((new_posx,new_posy))
    print("WTF!")
def calc_distances(maze,places):
    distances = dict()
    for place_key in places:
        distances[place_key] = dict()
        for second_place_key in places:
            distances[place_key][second_place_key] = a_star_search_distance(maze, places[place_key], places[second_place_key])
    print("got the distances!")
    return distances


def recursive_calc_route(start_pos_key,remaining_places_key,distances):
    if len(remaining_places_key) == 0:
        now_extra = distances[start_pos_key]['0']

        return now_extra," and back to start from " + start_pos_key
    else:
        distances_local = []

        for next_key in remaining_places_key:
            now_remaining = list(remaining_places_key)
            now_remaining.remove(next_key)
            distance_to_here = distances[start_pos_key][next_key]
            distance_remaining,to_append = recursive_calc_route(next_key,now_remaining,distances)
            distances_local.append((distance_remaining+distance_to_here,start_pos_key + " in " + str(distance_to_here) + " .. "+to_append))
        distances_local.sort()
        return distances_local[0][0], distances_local[0][1]



if __name__ == "__main__":
    reachable,places = read_maze('input.txt')

    print_maze(reachable)
    print(places)
    distances = calc_distances(reachable,places)
    print("Ready for next step")
    to_reach = list(places.keys())
    to_reach.remove('0')
    #note: 264 too low!
    print(recursive_calc_route('0',to_reach,distances))



