import pygame;

class Sprite_Sheet:
    def __init__(self, sheet, cols, rows):

        self.sheet = pygame.transform.scale(sheet, (400, 800));

        self.cols = cols;
        self.rows = rows;
        self.total_cell_count = cols * rows;

        self.rect = self.sheet.get_rect();

        self.cell_width = int(self.rect.width / cols);
        self.cell_height = int(self.rect.height / rows);
        self.cells = [];

        for index in range(self.total_cell_count):
            self.cells.append((index % self.cols * self.cell_width,
                               int(index / cols) * self.cell_height,
                               self.cell_width, self.cell_height));

    def draw(self, game_display, cell_index, x, y):
        game_display.blit(self.sheet, (x, y), self.cells[cell_index]);