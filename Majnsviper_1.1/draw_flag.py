import pygame as pg


def draw_flag(window, pos, game):
    x = 0
    y = 0

    for i in range(10, game.size - 10, game.blocksize):
        y = y % game.num_of_rows

        for j in range(10, game.size - 10, game.blocksize):
            x = x % game.num_of_rows

            p1 = int(pos[0])
            p2 = int(pos[1])
            if 0 < p1 - i < game.blocksize and 0 < p2 - j < game.blocksize:
                if game.flags_array[x][y] == 0 and game.num_of_flags_remaining >= 1:
                    backgroundfile = pg.image.load("flag_icon.png")
                    picture = pg.transform.scale(backgroundfile, (game.blocksize, game.blocksize))
                    window.blit(picture, (i, j))
                    game.flags_array[x][y] = 1
                    game.num_of_flags_remaining = game.num_of_flags_remaining - 1
                    if game.mute == False:
                        pg.mixer.music.load('Mine.mp3')
                        pg.mixer.music.play(1)
                elif game.flags_array[x][y] != 0 and game.num_of_flags_remaining >= 0:
                    #gray_screen = pg.image.load("gray_screen.png")
                    #picture = pg.transform.scale(gray_screen, (game.blocksize, game.blocksize))
                    #window.blit(picture, (i, j))

                    color = (0, 50, 70)
                    rect = pg.Rect(i, j, game.blocksize, game.blocksize)
                    window.fill(color, rect)


                    game.flags_array[x][y] = 0
                    game.num_of_flags_remaining = game.num_of_flags_remaining + 1

            x = x + 1
        y = y + 1
