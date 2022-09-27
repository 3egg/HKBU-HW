import matplotlib.pyplot as plt

def move_left(this_puzzle):
    this_puzzle_copy = this_puzzle.copy()
    for i, l in enumerate(this_puzzle_copy):
        if 0 in l:
            if list(l).index(0) - 1 < 0:
                return False
            value = int(l[list(l).index(0) - 1])  # copy
            o_index = list(l).index(0)
            l[list(l).index(0) - 1] = l[o_index]
            l[o_index] = value
    return this_puzzle_copy


def move_right(this_puzzle):
    this_puzzle_copy = this_puzzle.copy()
    for i, l in enumerate(this_puzzle_copy):
        if 0 in l:
            if list(l).index(0) + 1 > 2:
                return False
            value = int(l[list(l).index(0) + 1])  # copy
            o_index = list(l).index(0)
            l[list(l).index(0) + 1] = l[o_index]
            l[o_index] = value
    return this_puzzle_copy


def move_up(this_puzzle):
    up_index = None
    up_o_index = None
    this_puzzle_copy = this_puzzle.copy()
    for i, l in enumerate(this_puzzle_copy):
        if 0 in l:
            up_index = i - 1
            if up_index < 0:
                return False
            up_o_index = int(list(l).index(0))
    if up_index is not None and up_o_index is not None:
        up_value = this_puzzle_copy[up_index][up_o_index]
        this_puzzle_copy[up_index + 1][up_o_index] = up_value
        this_puzzle_copy[up_index][up_o_index] = 0
    return this_puzzle_copy


def move_down(this_puzzle):
    down_index = None
    down_o_index = None
    this_puzzle_copy = this_puzzle.copy()
    for i, l in enumerate(this_puzzle_copy):
        if 0 in l:
            down_index = i + 1
            if down_index > 2:
                return False
            down_o_index = int(list(l).index(0))
    if down_index is not None and down_o_index is not None:
        down_value = this_puzzle_copy[down_index][down_o_index]
        this_puzzle_copy[down_index - 1][down_o_index] = down_value
        this_puzzle_copy[down_index][down_o_index] = 0
    return this_puzzle_copy


import copy


# %%

def find_index(num, puzzle):
    for i, l in enumerate(puzzle):
        for ii, e in enumerate(l):
            if num == e:
                return [i, ii]
    return [0, 0]


# %%

def dist_to_goal_h2(num, goal_state, this_state):
    goal_index = find_index(num, goal_state)
    int_index = find_index(num, this_state)
    # print(num, abs(goal_index[0] - int_index[0]) + abs(goal_index[1] - int_index[1]))
    return abs(goal_index[0] - int_index[0]) + abs(goal_index[1] - int_index[1])


# %%

def misplaced_tiles_h1(goal_state, this_state):
    misplaced_tiles = 0
    for i, l in enumerate(goal_state):
        for ii, e in enumerate(l):
            if this_state[i][ii] != e:
                misplaced_tiles += 1
    if misplaced_tiles == 9:
        return 8
    if misplaced_tiles == 0:
        return 0
    return misplaced_tiles - 1


init_puzzles = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
# init_puzzles = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
# init_puzzles = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]
goal_puzzles = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def solve_puzzle(loop_times, visited, this_state, goal_state):
    print('loop_times', loop_times, 'this state')
    print(this_state[0])
    print(this_state[1])
    print(this_state[2])
    print('\n')
    actions = []
    pleft = move_left(copy.deepcopy(this_state))
    if False != pleft and pleft not in visited:
        actions.append(pleft)
    pright = move_right(copy.deepcopy(this_state))
    if False != pright and pright not in visited:
        actions.append(pright)
    pup = move_up(copy.deepcopy(this_state))
    if False != pup and pup not in visited:
        actions.append(pup)
    pdown = move_down(copy.deepcopy(this_state))
    if False != pdown and pdown not in visited:
        actions.append(pdown)
    # h1_costs = []
    h2_costs = []
    for l in actions:
        h2_cost = 0
        for e in l:
            for i in e:
                if i != 0:
                    h2_cost += dist_to_goal_h2(i, goal_state, l)
        h2_costs.append(h2_cost)
    if 0 in h2_costs:
        print('Final State', actions[h2_costs.index(min(h2_costs))], 'loop time is', loop_times + 1)
        return actions[h2_costs.index(min(h2_costs))]
    next_action = actions[h2_costs.index(min(h2_costs))]
    visited.append(next_action)
    loop_times += 1
    solve_puzzle(loop_times, visited, next_action, goal_state)


if __name__ == '__main__':
    solve_puzzle(0, [], init_puzzles, goal_puzzles)