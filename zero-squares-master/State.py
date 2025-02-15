import copy

class State:

    def __init__(self, grid, status, previous):
        self.grid = grid
        self.status = status
        self.previous = previous
        self.next_states = None

    def check_win(self):
        for row in self.grid:
            for cell in row:
                if cell.type_of_cell == "player" or cell.type_of_cell == "fake_target":
                    return False
        return True

    def next_states_create(self):
        self.next_states = {
            "down": self.move_players_down(),
            "up": self.move_players_up(),
            "right": self.move_players_right(),
            "left": self.move_players_left()
        }

    def move_players_down(self):
        new_grid = copy.deepcopy(self.grid)
        updated_colors = []
        for col in range(len(new_grid[0])):
            for row in range(len(new_grid)):
                if new_grid[row][col].type_of_cell in ["player", "fake_target"]:
                    if new_grid[row][col].primary_color in updated_colors:
                        continue
                    next_row = row + 1
                    while next_row < len(new_grid) and new_grid[next_row][col].type_of_cell not in ["wall", "player",
                                                                                                    "fake_target"]:
                        if new_grid[row][col].type_of_cell == "player":
                            if new_grid[next_row][col].type_of_cell == "empty":
                                new_grid[next_row][col].type_of_cell = "player"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == new_grid[next_row][col].primary_color:
                                new_grid[next_row][col].type_of_cell = "empty"
                                new_grid[next_row][col].primary_color = None
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                                break
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != new_grid[next_row][col].primary_color:
                                secondary_color = new_grid[next_row][col].primary_color
                                new_grid[next_row][col].type_of_cell = "fake_target"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[next_row][col].secondary_color = secondary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                        else:
                            if new_grid[next_row][col].type_of_cell == "empty":
                                new_grid[next_row][col].type_of_cell = "player"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == new_grid[next_row][col].primary_color:
                                new_grid[next_row][col].type_of_cell = "empty"
                                new_grid[next_row][col].primary_color = None
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != new_grid[next_row][col].primary_color:
                                primary_color = new_grid[next_row][col].primary_color
                                new_grid[next_row][col].type_of_cell = "fake_target"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[next_row][col].secondary_color = primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                        row = next_row
                        next_row += 1
                    updated_colors.append(new_grid[row][col].primary_color)
        new_state = State(new_grid, self.check_win(), self)
        return new_state

    def move_players_up(self):
        new_grid = copy.deepcopy(self.grid)
        updated_colors = []
        for col in range(len(new_grid[0])):
            for row in range(len(new_grid) - 1, -1, -1):
                if new_grid[row][col].type_of_cell in ["player", "fake_target"]:
                    if new_grid[row][col].primary_color in updated_colors:
                        continue
                    next_row = row - 1
                    while next_row >= 0 and new_grid[next_row][col].type_of_cell not in ["wall", "player", "fake_target"]:
                        if new_grid[row][col].type_of_cell == "player":
                            if new_grid[next_row][col].type_of_cell == "empty":
                                new_grid[next_row][col].type_of_cell = "player"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[next_row][col].primary_color:
                                new_grid[next_row][col].type_of_cell = "empty"
                                new_grid[next_row][col].primary_color = None
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                                break
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[next_row][col].primary_color:
                                secondary_color = new_grid[next_row][col].primary_color
                                new_grid[next_row][col].type_of_cell = "fake_target"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[next_row][col].secondary_color = secondary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                        else:
                            if new_grid[next_row][col].type_of_cell == "empty":
                                new_grid[next_row][col].type_of_cell = "player"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[next_row][col].primary_color:
                                new_grid[next_row][col].type_of_cell = "empty"
                                new_grid[next_row][col].primary_color = None
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[next_row][col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[next_row][col].primary_color:
                                primary_color = new_grid[next_row][col].primary_color
                                new_grid[next_row][col].type_of_cell = "fake_target"
                                new_grid[next_row][col].primary_color = new_grid[row][col].primary_color
                                new_grid[next_row][col].secondary_color = primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                        row = next_row
                        next_row -= 1
                    updated_colors.append(new_grid[row][col].primary_color)
        new_state = State(new_grid, self.check_win(), self)
        return new_state

    def move_players_right(self):
        new_grid = copy.deepcopy(self.grid)
        updated_colors = []
        for row in range(len(new_grid)):
            for col in range(len(new_grid[0]) - 1, -1, -1):
                if new_grid[row][col].type_of_cell in ["player", "fake_target"]:
                    if new_grid[row][col].primary_color in updated_colors:
                        continue
                    next_col = col + 1
                    while next_col < len(new_grid[0]) and new_grid[row][next_col].type_of_cell not in ["wall", "player",
                                                                                                       "fake_target"]:
                        if new_grid[row][col].type_of_cell == "player":
                            if new_grid[row][next_col].type_of_cell == "empty":
                                new_grid[row][next_col].type_of_cell = "player"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[row][next_col].primary_color:
                                new_grid[row][next_col].type_of_cell = "empty"
                                new_grid[row][next_col].primary_color = None
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                                break
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[row][next_col].primary_color:
                                secondary_color = new_grid[row][next_col].primary_color
                                new_grid[row][next_col].type_of_cell = "fake_target"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][next_col].secondary_color = secondary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                        else:
                            if new_grid[row][next_col].type_of_cell == "empty":
                                new_grid[row][next_col].type_of_cell = "player"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[row][next_col].primary_color:
                                new_grid[row][next_col].type_of_cell = "empty"
                                new_grid[row][next_col].primary_color = None
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[row][next_col].primary_color:
                                primary_color = new_grid[row][next_col].primary_color
                                new_grid[row][next_col].type_of_cell = "fake_target"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][next_col].secondary_color = primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                        col = next_col
                        next_col += 1
                    updated_colors.append(new_grid[row][col].primary_color)
        new_state = State(new_grid, self.check_win(), self)
        return new_state

    def move_players_left(self):
        new_grid = copy.deepcopy(self.grid)
        updated_colors = []
        for row in range(len(new_grid)):
            for col in range(len(new_grid[0])):
                if new_grid[row][col].type_of_cell in ["player", "fake_target"]:
                    if new_grid[row][col].primary_color in updated_colors:
                        continue
                    next_col = col - 1
                    while next_col >= 0 and new_grid[row][next_col].type_of_cell not in ["wall", "player", "fake_target"]:
                        if new_grid[row][col].type_of_cell == "player":
                            if new_grid[row][next_col].type_of_cell == "empty":
                                new_grid[row][next_col].type_of_cell = "player"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[row][next_col].primary_color:
                                new_grid[row][next_col].type_of_cell = "empty"
                                new_grid[row][next_col].primary_color = None
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                                break
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[row][next_col].primary_color:
                                secondary_color = new_grid[row][next_col].primary_color
                                new_grid[row][next_col].type_of_cell = "fake_target"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][next_col].secondary_color = secondary_color
                                new_grid[row][col].type_of_cell = "empty"
                                new_grid[row][col].primary_color = None
                        else:
                            if new_grid[row][next_col].type_of_cell == "empty":
                                new_grid[row][next_col].type_of_cell = "player"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color == \
                                    new_grid[row][next_col].primary_color:
                                new_grid[row][next_col].type_of_cell = "empty"
                                new_grid[row][next_col].primary_color = None
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                            elif new_grid[row][next_col].type_of_cell == "target" and new_grid[row][
                                col].primary_color != \
                                    new_grid[row][next_col].primary_color:
                                primary_color = new_grid[row][next_col].primary_color
                                new_grid[row][next_col].type_of_cell = "fake_target"
                                new_grid[row][next_col].primary_color = new_grid[row][col].primary_color
                                new_grid[row][next_col].secondary_color = primary_color
                                new_grid[row][col].type_of_cell = "target"
                                new_grid[row][col].primary_color = new_grid[row][col].secondary_color
                                new_grid[row][col].secondary_color = None
                        col = next_col
                        next_col -= 1
                    updated_colors.append(new_grid[row][col].primary_color)
        new_state = State(new_grid, self.check_win(), self)
        return new_state
    def get_cost(self):
        return 1
    def estimate_cost_to_goal(self):
        total_cost = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cell = self.grid[row][col]
                if cell.type_of_cell == "player":
                    closest_target_distance = float('inf')
                    for target_row in range(len(self.grid)):
                        for target_col in range(len(self.grid[target_row])):
                            target_cell = self.grid[target_row][target_col]
                            if target_cell.type_of_cell == "target" and target_cell.primary_color == cell.primary_color:
                                distance = abs(target_row - row) + abs(target_col - col)
                                closest_target_distance = min(closest_target_distance, distance)
                    total_cost += closest_target_distance
        return total_cost
