import pygame;
from spritesheet import Sprite_Sheet;
from level import Level;
import tkinter as tk;

pygame.init();

screen_size = (1400, 800);
game_display = pygame.display.set_mode(screen_size);

def input_image_info():
    u = 0;


def render_screen(level, sidebar):
    game_display.fill((43, 43, 43));
    level.render_level();
    level.display_sidebar(game_display, sidebar);
    pygame.display.update();

def take_screenshot(level):
    game_display.fill((43, 43, 43));
    level.render_level();
    pygame.display.update();
    level.dump_coordinates_and_indeces(image_path);

    #pygame.image.save(game_display, 'a.png');

def main():
    image_info = input_image_info();
    print(image_info);

    sidebar = pygame.image.load('C:\\Users\\Óli\\Desktop\\Python\\Level Editor\\UI\\Sidebar.png').convert_alpha();

    #TODO: Prompt user to choose image and cols and rows
    image = pygame.image.load('C:\\Users\\Óli\\Desktop\\Python\\Level Editor\\Tilesets\\RogueDungeon.png').convert_alpha();
    size = image.get_size();
    sheet = Sprite_Sheet(image, 8, 16);
    level = Level(game_display, sheet, size, 8, 16);
    sidebar = pygame.transform.scale(sidebar, (388, 1000))

    quit_editor = False;

    #TODO: Tag objects as interactive or animated, need to specify which cells to use

    while not quit_editor:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                quit_editor = True;

            if(event.type == pygame.MOUSEBUTTONUP):
                if(event.button == 1):
                    level.insert_coordinates(pygame.mouse.get_pos());
                elif(event.button == 3):
                    level.remove_coordinates(pygame.mouse.get_pos());

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_d):
                    level.display_coordinates();
                if(event.key == pygame.K_w):
                    level.cycle_tile_up();
                if(event.key == pygame.K_s):
                    level.cycle_tile_down();
                if(event.key == pygame.K_k):
                    take_screenshot(level);

                if(event.key == pygame.K_RIGHT):
                    level.scroll_image(event.key);
                if (event.key == pygame.K_LEFT):
                    level.scroll_image(event.key);
                if (event.key == pygame.K_UP):
                    level.scroll_image(event.key);
                if (event.key == pygame.K_DOWN):
                    level.scroll_image(event.key);

        render_screen(level, sidebar);

if __name__ == '__main__':
    main();