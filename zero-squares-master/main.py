import pygame
from GameGui import GridDisplay
from State import State
from Algorithm import dfs_solve, bfs_solve, reconstruct_path, ucs_solve, dfs_solve_recursive, a_star_solve
from Grid import grid

def handle_key_input(event, current_state):
    next_state = None

    if event.key == pygame.K_w:
        next_state = current_state.move_players_up()
        next_state.next_states_create()
    elif event.key == pygame.K_a:
        next_state = current_state.move_players_left()
        next_state.next_states_create()
    elif event.key == pygame.K_s:
        next_state = current_state.move_players_down()
        next_state.next_states_create()
    elif event.key == pygame.K_d:
        next_state = current_state.move_players_right()
        next_state.next_states_create()
    elif event.key == pygame.K_q:
        return None

    return next_state

def run_algorithm(game_display, start_state, algorithm):
    winning_state = algorithm(start_state)

    if winning_state:
        solution_path = reconstruct_path(winning_state)
        print(len(solution_path))
        print("\nSolution Path:")
        for i, state in enumerate(solution_path):
            print(f"\nStep {i}:")
            for row in state.grid:
                print(" ".join(cell.type_of_cell[0].upper() if cell.type_of_cell else '.' for cell in row))

        for state in solution_path:
            game_display.refresh_grid(state)
            pygame.time.wait(500)

        font = pygame.font.SysFont(None, 55)
        win_message = font.render("good for you !", True, (0, 128, 0))
        game_display.display.blit(
            win_message,
            (game_display.screen_width // 2 - win_message.get_width() // 2,
             game_display.screen_height // 2 - win_message.get_height() // 2)
        )
        pygame.display.flip()
        pygame.time.wait(1500)
    else:
            print("No solution found!")

if __name__ == "__main__":
    pygame.init()

    game_display = GridDisplay()

    grids =grid()

    grid_choice = game_display.get_user_choice(["Grid 1", "Grid 2", "Grid 3","Grid 4","Grid 5"])
    chosen_grid = grids[grid_choice]

    game_status = "active"
    start_state = State(chosen_grid, game_status, None)
    start_state.next_states_create()

    mode_choice = game_display.get_user_choice(["Run User ", "Run DFS", "Run BFS","Run Ucs","Run DFS recursive","Run A "])

    if mode_choice == 1:
        run_algorithm(game_display, start_state, dfs_solve)
    elif mode_choice == 2:
        run_algorithm(game_display, start_state, bfs_solve)
    elif mode_choice == 3:
        run_algorithm(game_display, start_state, ucs_solve)
    elif mode_choice == 4:
        run_algorithm(game_display, start_state, lambda state: dfs_solve_recursive(state, set()))
    elif mode_choice == 5:
        run_algorithm(game_display, start_state, a_star_solve)
    else:
        current_state = start_state
        game_display.refresh_grid(current_state)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    next_state = handle_key_input(event, current_state)
                    if next_state is None:
                        running = False
                    elif next_state != current_state:
                        current_state = next_state
                        game_display.refresh_grid(current_state)

            if current_state.check_win():
                font = pygame.font.SysFont(None, 55)
                win_message = font.render("good for you !", True, (0, 128, 0))
                game_display.display.blit(
                    win_message,
                    (game_display.screen_width // 2 - win_message.get_width() // 2,
                     game_display.screen_height // 2 - win_message.get_height() // 2)
                )
                pygame.display.flip()
                pygame.time.wait(1500)
                break

            game_display.game_clock.tick(50)

    pygame.quit()
