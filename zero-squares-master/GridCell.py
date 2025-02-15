class GridCell:
    def __init__(self, type_of_cell, primary_color, secondary_color):
        self.type_of_cell = type_of_cell
        self.primary_color = primary_color
        self.secondary_color = secondary_color

    def update_color(self, new_primary_color):
        self.primary_color = new_primary_color

    def update_type(self, new_type):
        self.type_of_cell = new_type
