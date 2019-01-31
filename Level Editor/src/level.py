import pygame;

class Level:
    def __init__(self, game_display, sheet, image_size, cols, rows):
        self.level_coordinates = [];
        self.sidebar_tile_coordinates = [];
        self.game_display = game_display;
        self.sheet = sheet;
        self.image_size = image_size;
        self.cols = cols;
        self.rows = rows;

        self.cell_index = 0;

        self.initialize_sidebar();

    def insert_coordinates(self, coordinates):
        if not(coordinates[0] <= 420):
            self.level_coordinates.append([(coordinates[0] -
                                       (coordinates[0] % self.get_frame_size())),
                                       (coordinates[1] - (coordinates[1] %
                                        self.get_frame_size())), self.cell_index]);
        else:
            for i in self.sidebar_tile_coordinates:
                if(i[0] == (coordinates[0] - (coordinates[0] % self.get_frame_size()))):
                    if(i[1] == (coordinates[1] - (coordinates[1] % self.get_frame_size()))):
                        self.cell_index = i[2];

    def remove_coordinates(self, coordinates):
        for i in self.level_coordinates:
            if(i[0] == (coordinates[0] - (coordinates[0] % self.get_frame_size()))):
                if(i[1] == (coordinates[1] - (coordinates[1] % self.get_frame_size()))):
                    self.level_coordinates.remove(i);

    def initialize_sidebar(self):
        index = 0;

        for i in range(0, int((self.get_frame_size() * self.rows)), int(self.get_frame_size())):
            for j in range(0, int(self.get_frame_size() * 8), int(self.get_frame_size())):
                self.sidebar_tile_coordinates.append([j, i, index]);
                index += 1;

    def display_coordinates(self):
        for i in self.level_coordinates:
            print(i);

    def get_image_size(self):
        return self.image_size;

    def get_frame_size(self):
        return(self.image_size[0] / self.cols) * 3;

    def cycle_tile_up(self):
        if(self.cell_index == self.rows * self.cols - 1):
            self.cell_index = 0;
        else:
            self.cell_index += 1;

    def cycle_tile_down(self):
        if(self.cell_index == 0):
            self.cell_index = self.rows * self.cols - 1;
        else:
            self.cell_index -= 1;

    def scroll_image(self, direction):
        if(direction == pygame.K_RIGHT):
            for i in self.level_coordinates:
                i[0] -= self.get_frame_size();
        elif(direction == pygame.K_LEFT):
            for i in self.level_coordinates:
                i[0] += self.get_frame_size();
        elif(direction == pygame.K_UP):
            for i in self.level_coordinates:
                i[1] += self.get_frame_size();
        elif(direction == pygame.K_DOWN):
            for i in self.level_coordinates:
                i[1] -= self.get_frame_size();

    def render_level(self):
        for i in self.level_coordinates:
            self.sheet.draw(self.game_display, i[2], i[0], i[1]);

    def display_sidebar(self, game_display, sidebar):
        game_display.blit(sidebar, (0, 0));
        self.display_sidebar_tiles(game_display);

    def dump_coordinates_and_indeces(self, image_src):
        file = open('filename.txt', 'w');

        file.write(image_src + '\n');

        for i in self.level_coordinates:
            file.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + '\n');


    def display_sidebar_tiles(self, game_display):
        for i in self.sidebar_tile_coordinates:
            self.sheet.draw(game_display, i[2], i[0], i[1]);
            if(i[2] == self.cell_index):
                pygame.draw.rect(game_display, (255, 255, 255), [i[0], i[1], int(self.get_frame_size()), int(self.get_frame_size())]);



