import pygame as pg
from tkinter import *
from tkinter import messagebox


pg.init()
font = pg.font.Font('freesansbold.ttf', 32)


def draw_window(pos, bool, brojac_1, window, game, color):
    if brojac_1 == 1:
        rect = pg.Rect(10, 10, game.size - 20, game.size - 20)
        window.fill(color, rect)
    info = draw_grid(window, game, pos, bool)
    pg.display.update()
    return info

def show_neighbours(game, i, j):
    #game.help_array = [[0 for i in range(game.num_of_rows)] for j in range(game.num_of_rows)]
    for x in range(-1, 2):
        for y in range(-1, 2):
            if game.num_of_rows > i + x >= 0 and game.num_of_rows > j + y >= 0:
                if x == 0 and y == 0:
                    pass
                else:
                    if game.flags_array[i + x][j + y] == 0:
                        if game.main_array[i + x][j + y] == 0:
                            if game.help_array[i + x][j + y] == 0:
                                game.help_array[i + x][j + y] = 1
                                show_neighbours(game, i + x, j + y)
                        else:
                            game.help_array[i + x][j + y] = 1

def draw_grid(window, game, pos, bool_var):
    x = 0
    y = 0

    gray1 = (154, 156, 154)
    tirkizna = (0, 155, 155)
    blue = (0, 204, 255)
    blue2 = (55, 150, 255)
    orange = (255, 153, 0)
    light_orange = (255, 190, 50)


    square_color = blue2

    text_color_0 = (255, 25, 0)
    text_color_1 = (255, 153, 0)
    text_color_2 = blue

    text_color = light_orange

    line_colour1 = (50, 100, 200)
    line_colour2 = (153, 0, 153)
    line_colour2_2 = (255, 255, 204)
    line_colour3 = (102, 255, 255)
    line_colour4 = (204, 204, 0)
    line_colour5 = (102, 0, 204)

    line_colour = line_colour3

    flag_count_img = pg.image.load('flag_icon.png')
    flag_count_img_resized = pg.transform.scale(flag_count_img, (30, 30))
    window.blit(flag_count_img_resized, (10, game.size))

    for i in range(10, game.size - 10, game.blocksize):
        y = y % game.num_of_rows

        for j in range(10, game.size - 10, game.blocksize):
            x = x % game.num_of_rows

            rect = pg.Rect(i, j, game.blocksize, game.blocksize)
            pg.draw.rect(window, line_colour, rect, 1)

            if bool_var:
                p1 = int(pos[0])
                p2 = int(pos[1])
                if 0 < p1 - i < game.blocksize and 0 < p2 - j < game.blocksize:
                    if game.flags_array[x][y] == 0:
                        if game.main_array[x][y] == 0:
                            if game.free_squares_array[x][y] == 0:
                                game.free_squares_array[x][y] = 1
                                game.num_of_free_squares = game.num_of_free_squares - 1
                                text = font.render("    ", True, text_color, square_color)
                                text = pg.transform.scale(text, (game.blocksize, game.blocksize))
                                window.blit(text, (i, j))

                                game.help_array[x][y] = 1

                                show_neighbours(game, x, y)
                                for m in range(0, game.num_of_rows):
                                    for n in range(0, game.num_of_rows):
                                        if(game.help_array[m][n] == 1) and (game.free_squares_array[m][n] == 0):
                                            if(game.main_array[m][n] != 0):
                                                game.free_squares_array[m][n] = 1
                                                game.num_of_free_squares = game.num_of_free_squares - 1
                                                text = font.render(str(game.main_array[m][n]), True, text_color, square_color)
                                            else:
                                                game.free_squares_array[m][n] = 1
                                                game.num_of_free_squares = game.num_of_free_squares - 1
                                                text = font.render(("   "), True, text_color, square_color)
                                            text = pg.transform.scale(text, (game.blocksize, game.blocksize))
                                            window.blit(text, (10 + (n) * game.blocksize, 10 + (m) * game.blocksize))


                        elif game.main_array[x][y] == -1:
                            if game.mute == False:
                                pg.mixer.music.load('sound_bomb_2.mp3')
                                pg.mixer.music.play(1)
                            backgroundfile = pg.image.load("mine_icon.jpg")
                            picture = pg.transform.scale(backgroundfile, (game.blocksize, game.blocksize))

                            game.show_mines(window, picture)
                            pg.display.flip()

                            Tk().wm_withdraw()  # to hide the main window
                            messagebox.showinfo('Booooom', 'You lost')

                            #window.blit(picture, (i, j))
                            #pg.display.update()
                            #pg.event.clear()
                            #while True:
                             #   window.blit(picture, (i, j))
                              #  event = pg.event.wait()
                               # if event.type == pg.QUIT:
                                #    pg.quit()
                                 #   sys.exit()
                                #elif event.type == pg.MOUSEBUTTONUP:
                                 #   return 1

                            return 1

                        else:
                            if (game.free_squares_array[x][y] == 0):
                                game.free_squares_array[x][y] = 1
                                game.num_of_free_squares = game.num_of_free_squares - 1
                                text = font.render(str(game.main_array[x][y]), True, text_color, square_color)
                                text = pg.transform.scale(text, (game.blocksize, game.blocksize))
                                window.blit(text, (i, j))

                        #window.blit(flag_count_img_resized, (10, game.size))

            x = x + 1

        y = y + 1

    return 0


