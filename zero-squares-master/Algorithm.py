import heapq
from itertools import count
from collections import deque
from heapq import heappop, heappush
import itertools

def dfs_solve(initial_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()

        if current_state.check_win():
            return current_state

        state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in current_state.grid)
        if state_id in visited:
            continue
        visited.add(state_id)

        current_state.next_states_create()
        if current_state.next_states:
            stack.extend(current_state.next_states.values())


    return None

def dfs_solve_recursive(current_state, visited):
    if current_state.check_win():
        return current_state

    state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in current_state.grid)

    if state_id in visited:
        return None

    visited.add(state_id)

    current_state.next_states_create()

    if current_state.next_states:
        for next_state in current_state.next_states.values():
            result = dfs_solve_recursive(next_state, visited)
            if result:
                return result

    return None

def bfs_solve(initial_state):
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_state = queue.popleft()


        if current_state.check_win():
            return current_state


        state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in current_state.grid)
        if state_id in visited:
            continue
        visited.add(state_id)

        current_state.next_states_create()
        if current_state.next_states:
            queue.extend(current_state.next_states.values())

    return None


def ucs_solve(initial_state):
    priority_queue = []
    counter = count()

    heapq.heappush(priority_queue, (0, next(counter), initial_state))
    visited = set()

    while priority_queue:
        cumulative_cost, _, current_state = heapq.heappop(priority_queue)

        if current_state.check_win():
            return current_state

        state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in current_state.grid)
        if state_id in visited:
            continue
        visited.add(state_id)

        current_state.next_states_create()

        if current_state.next_states:
            for next_state in current_state.next_states.values():
                cost = cumulative_cost + next_state.get_cost()
                heapq.heappush(priority_queue, (cost, next(counter), next_state))

    return None




def heuristic(current_state):
    return current_state.estimate_cost_to_goal()



def a_star_solve(initial_state):
    priority_queue = []
    counter = itertools.count()

    initial_priority = heuristic(initial_state)
    heappush(priority_queue, (initial_priority, next(counter), initial_state))

    visited = set()

    g_cost = {initial_state: 0}

    print("Starting A* algorithm...")
    print(f"Initial state heuristic: {initial_priority}")

    while priority_queue:
        _, _, current_state = heappop(priority_queue)

        print("\nCurrent state:")
        for row in current_state.grid:
            print(" ".join(cell.type_of_cell[0].upper() if cell.type_of_cell else '.' for cell in row))
        print(f"Cost so far: {g_cost[current_state]}")

        if current_state.check_win():
            print("Goal state reached!")
            return current_state

        state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in current_state.grid)
        if state_id in visited:
            print("State already visited, skipping...")
            continue
        visited.add(state_id)

        current_state.next_states_create()
        print(f"Generating {len(current_state.next_states)} next states...")

        for direction, next_state in current_state.next_states.items():
            next_state.parent = current_state

            tentative_g_cost = g_cost[current_state] + 1
            next_state_id = tuple(tuple(cell.type_of_cell for cell in row) for row in next_state.grid)

            if next_state_id not in g_cost or tentative_g_cost < g_cost[next_state]:
                g_cost[next_state] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(next_state)
                heappush(priority_queue, (f_cost, next(counter), next_state))
                print(f"Added to queue: direction={direction}, f_cost={f_cost}, g_cost={tentative_g_cost}")
            else:
                print(f"State in direction {direction} ignored (higher cost).")

    print("No solution found.")
    return None




def reconstruct_path(final_state):
    path = []
    current = final_state
    while current:
        path.append(current)
        current = current.previous
    return path[::-1]
