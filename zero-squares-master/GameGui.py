import pygame
from GridCell import GridCell

class GridDisplay:
    def __init__(self, screen_width=600, screen_height=600):
        self.cell_size = 50
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Grid Game")
        self.game_clock = pygame.time.Clock()

    def render_grid(self, game_state):
        self.display.fill((255, 255, 255))

        grid_width = len(game_state.grid[0]) * self.cell_size
        grid_height = len(game_state.grid) * self.cell_size
        x_offset = (self.screen_width - grid_width) // 2
        y_offset = (self.screen_height - grid_height) // 2

        for row_index, row in enumerate(game_state.grid):
            for col_index, cell in enumerate(row):
                x_start = col_index * self.cell_size + x_offset
                y_start = row_index * self.cell_size + y_offset

                if cell.type_of_cell == "empty":
                    cell_color = (255, 255, 255)
                    pygame.draw.rect(self.display, cell_color, (x_start, y_start, self.cell_size, self.cell_size))
                elif cell.type_of_cell == "wall":
                    cell_color = (0, 0, 0)  # Black
                    pygame.draw.rect(self.display, cell_color, (x_start, y_start, self.cell_size, self.cell_size))
                elif cell.type_of_cell == "player":
                    cell_color = cell.primary_color
                    pygame.draw.rect(self.display, cell_color, (x_start, y_start, self.cell_size, self.cell_size))
                elif cell.type_of_cell == "target":
                    pygame.draw.rect(self.display, (255, 255, 255),
                                     (x_start, y_start, self.cell_size, self.cell_size))
                    pygame.draw.rect(self.display, cell.primary_color,
                                     (x_start, y_start, self.cell_size, self.cell_size), width=3)
                elif cell.type_of_cell == "fake_target":
                    pygame.draw.rect(self.display, cell.primary_color,
                                     (x_start, y_start, self.cell_size, self.cell_size))

                    pygame.draw.rect(self.display, cell.secondary_color,
                                     (x_start, y_start, self.cell_size, self.cell_size), width=6)

        pygame.display.flip()

    def refresh_grid(self, updated_state):
        self.render_grid(updated_state)

    def draw_menu(self, options, selected_option):
        self.display.fill((30, 30, 30))
        font = pygame.font.SysFont("Arial", 40)
        header_font = pygame.font.SysFont("Arial", 50, bold=True)


        header_text = header_font.render("Choose an Option", True, (255, 255, 255))
        self.display.blit(header_text, (self.screen_width // 2 - header_text.get_width() // 2, 50))

        for i, text in enumerate(options):
            if i == selected_option:
                bg_color = (50, 50, 150)
                text_color = (255, 255, 255)
            else:
                bg_color = (70, 70, 70)
                text_color = (200, 200, 200)

            rect = pygame.Rect(
                self.screen_width // 2 - 150,
                150 + i * 80,
                300,
                60
            )
            pygame.draw.rect(self.display, bg_color, rect, border_radius=10)
            pygame.draw.rect(self.display, (255, 255, 255), rect, width=2, border_radius=10)

            option_text = font.render(text, True, text_color)
            self.display.blit(
                option_text,
                (rect.x + rect.width // 2 - option_text.get_width() // 2,
                 rect.y + rect.height // 2 - option_text.get_height() // 2)
            )

        pygame.display.flip()

    def get_user_choice(self, options):
        selected_option = 0
        while True:
            self.draw_menu(options, selected_option)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        selected_option = (selected_option + 1) % len(options)
                    elif event.key == pygame.K_w:
                        selected_option = (selected_option - 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        return selected_option

