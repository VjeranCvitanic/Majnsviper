import pygame as pg
from board import board
from tkinter import *
from tkinter import messagebox
from draw_window import *
from draw_flag import draw_flag

def main():
    pg.init()
    pg.mixer.init()

    res = (400, 480)
    mute = False

    surface = pg.image.load('flag_icon.png')
    mine_surface = pg.image.load('mine_icon.jpg')
    pg.display.set_icon(surface)

    level_surface = pg.image.load('level_icon.jpg')
    mute_surface = pg.image.load('mute2_icon.png')
    sound_surface = pg.image.load('sound2_icon.png')
    settings_surface = pg.image.load('settings_icon.png')

    color = (255, 255, 102)
    color_light = (170, 170, 170)
    color_light2 = (220, 220, 220)
    color_dark = (100, 100, 100)
    main_text_color = (153, 204, 255)

    screen = pg.display.set_mode(res)

    pg.display.set_caption('Majnsviper')

    width = screen.get_width()
    height = screen.get_height()

    size = 500

    smallfont = pg.font.SysFont('Corbel', 35)
    #smallfont = pg.font.SysFont('times-bold', 35)

    main_text = smallfont.render('Majnsviper', True, main_text_color)

    text1 = smallfont.render('Quit', True, color)
    text2 = smallfont.render('Start', True, color)

    selection1 = smallfont.render('Small', True, color)
    selection2 = smallfont.render('Normal', True, color)
    selection3 = smallfont.render('Large', True, color)

    text3 = smallfont.render('Mode', True, color)

    is_mode_selected = False

    brojac_1 = 1

    if mute == False:
        pg.mixer.music.load('Wii_music.mp3')
        pg.mixer.music.play(-1)

    while True:
        game = board()
        game.mute = mute
        screen = pg.display.set_mode(res)
        blockSize = 60

        for ev in pg.event.get():

            if ev.type == pg.QUIT:
                pg.quit()

            if ev.type == pg.MOUSEBUTTONUP:
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 80 <= mouse[1] <= height / 2 - 40:
                    pg.mixer.music.stop()
                    game.set_blocksize_and_size(blockSize, size)
                    while main_f(brojac_1, game) == 0:
                        pass

                    pg.display.set_icon(surface)
                    pg.display.set_caption('Majnsviper')

                    mute = game.mute
                    blockSize = game.blocksize
                    pg.mixer.music.load('Wii_music.mp3')
                    game.set_number_of_mines()
                    game.set_blocksize_and_size(blockSize, size)
                    if mute == False:
                        pg.mixer.music.play(-1)


                elif width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 20 <= mouse[1] <= height / 2 + 20:
                    pg.quit()
                    return

                elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 80 <= mouse[
                    1] <= height / 2 + 120:
                    pg.mixer.music.stop()
                    blockSize = 60
                    game.set_blocksize_and_size(blockSize, size)
                    while main_f(brojac_1, game) == 0:
                        pass

                    pg.display.set_icon(surface)
                    pg.display.set_caption('Majnsviper')

                    mute = game.mute
                    blockSize = game.blocksize
                    game.set_number_of_mines()
                    game.set_blocksize_and_size(blockSize, size)
                    pg.mixer.music.load('Wii_music.mp3')
                    if mute == False:
                        pg.mixer.music.play(-1)

                elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 120 <= mouse[
                    1] <= height / 2 + 160:
                    pg.mixer.music.stop()
                    blockSize = 30
                    game.set_blocksize_and_size(blockSize, size)
                    while main_f(brojac_1, game) == 0:
                        pass

                    pg.display.set_icon(surface)
                    pg.display.set_caption('Majnsviper')

                    mute = game.mute
                    blockSize = game.blocksize
                    game.set_number_of_mines()
                    game.set_blocksize_and_size(blockSize, size)
                    pg.mixer.music.load('Wii_music.mp3')
                    if mute == False:
                        pg.mixer.music.play(-1)

                elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 160 <= mouse[
                    1] <= height / 2 + 200:
                    pg.mixer.music.stop()
                    blockSize = 20
                    game.set_blocksize_and_size(blockSize, size)
                    while main_f(brojac_1, game) == 0:
                        pass

                    pg.display.set_icon(surface)
                    pg.display.set_caption('Majnsviper')

                    mute = game.mute
                    blockSize = game.blocksize
                    game.set_number_of_mines()
                    game.set_blocksize_and_size(blockSize, size)
                    pg.mixer.music.load('Wii_music.mp3')
                    if mute == False:
                        pg.mixer.music.play(-1)

                elif width - 60 <= mouse[0] <= width - 20 and height - 60 <= mouse[1] <= height - 20:
                    mute = not mute
                    if mute == True:
                        pg.mixer.music.stop()
                    else:
                        pg.mixer.music.play(-1)

                elif width - 105 <= mouse[0] <= width - 65 and height - 60 <= mouse[1] <= height - 20:
                    settings_window = pg.display.set_mode((width, height))
                    pg.display.set_caption('Settings')
                    pg.display.set_icon(settings_surface)

                    run = True

                    while run:
                        settings_window.fill(color)
                        pg.display.update()
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                run = False

                    pg.display.set_icon(surface)
                    pg.display.set_caption('Majnsviper')

        # fills the screen with a color
        screen.fill(color)

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pg.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade

        pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 - 20, 140, 40])
        pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 - 80, 140, 40])
        pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 40, 140, 40])

        flag_img = pg.transform.scale(surface, (40, 40))
        mine_img = pg.transform.scale(mine_surface, (40, 40))
        level_icon = pg.transform.scale(level_surface, (40, 40))
        sound_icon = pg.transform.scale(sound_surface, (40, 40))
        mute_icon = pg.transform.scale(mute_surface, (40, 40))
        settings_icon = pg.transform.scale(settings_surface, (40, 40))

        screen.blit(flag_img, (width / 2 - 130, height / 2 - 80))
        screen.blit(mine_img, (width / 2 - 130, height / 2 - 20))
        screen.blit(level_icon, (width / 2 - 130, height / 2 + 40))
        if mute == False:
            screen.blit(mute_icon, (width - 60, height - 60))
        else:
            screen.blit(sound_icon, (width - 60, height - 60))
        screen.blit(settings_icon, (width - 105, height - 60))


        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 20 <= mouse[1] <= height / 2 + 20:
            is_mode_selected = False
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 - 20, 140, 40])

        elif width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 80 <= mouse[1] <= height / 2 - 40:
            is_mode_selected = False
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 - 80, 140, 40])

        elif width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 40 <= mouse[1] <= height / 2 + 80:
            is_mode_selected = True
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 40, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 80, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 120, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 160, 140, 40])

        elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 80 <= mouse[
            1] <= height / 2 + 120:
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 80, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 120, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 160, 140, 40])

        elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 120 <= mouse[
            1] <= height / 2 + 160:
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 80, 140, 40])
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 120, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 160, 140, 40])

        elif is_mode_selected and width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 160 <= mouse[
            1] <= height / 2 + 200:
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 80, 140, 40])
            pg.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 120, 140, 40])
            pg.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 160, 140, 40])

        else:
            is_mode_selected = False

        if is_mode_selected:
            pg.draw.rect(screen, color_light2, [width / 2 - 70, height / 2 + 40, 140, 40])
            screen.blit(selection1, (width / 2 - 40, height / 2 + 80))
            screen.blit(selection2, (width / 2 - 50, height / 2 + 120))
            screen.blit(selection3, (width / 2 - 40, height / 2 + 160))

        # superimposing the text onto our button
        screen.blit(text1, (width / 2 - 30, height / 2 - 18))
        screen.blit(text2, (width / 2 - 30, height / 2 - 78))
        screen.blit(text3, (width / 2 - 40, height / 2 + 43))
        pg.draw.rect(screen, color_dark, [width / 2 - 77, height / 2 - 180, 160, 40])
        screen.blit(main_text, (width / 2 - 75, height / 2 - 180))

        # updates the frames of the game
        pg.display.update()

def main_f(brojac_1, game):
    gray1 = (155, 155, 155)
    gray2 = (202, 207, 202)
    gray2 = (224,224,224)
    black = (16,16,16)
    brown = (102, 102, 51)
    green = (0, 102, 0)
    tirkizna = (0, 155, 155)
    white = (255, 255, 255)
    red = (255, 25, 0)
    blue = (0, 102, 255)
    light_green = (153, 255, 204)
    yellow = (255, 255, 102)
    test_color = (0, 50, 70)

    background_color = test_color

    font = pg.font.Font('freesansbold.ttf', 32)
    caption = "MyMineSweeper"
    icon = 'mine_icon.jpg'
    icon_surface = pg.image.load(icon)

    # flag_count_img = pg.image.load('flag_icon.png')

    mute_icon_image = pg.image.load('mute2_icon.png')
    mute_icon_image = pg.transform.scale(mute_icon_image, (40, 40))

    sound_icon_image = pg.image.load('sound2_icon.png')
    sound_icon_image = pg.transform.scale(sound_icon_image, (40, 40))

    if game.mute == False:
        sound_or_mute_image = mute_icon_image
    else:
        sound_or_mute_image = sound_icon_image

    width = game.size
    height = game.size

    window = pg.display.set_mode((width, height + 40))
    pg.display.set_caption(caption)
    pg.display.set_icon(icon_surface)

    run = True

    counter_of_moves_played = 0

    while run:
        if game.num_of_free_squares == 0:
            if game.blocksize == 60:
                if game.mute == False:
                    pg.mixer.music.load('Win_music_1.mp3')
                    pg.mixer.music.play(1)
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Yeah', 'You won!')
                # animation for win
            elif game.blocksize == 30:
                if game.mute == False:
                    pg.mixer.music.load('Win_music_2.mp3')
                    pg.mixer.music.play(1)
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Yeah', 'You won!')
                # animation for win
            elif game.blocksize == 15:
                if game.mute == False:
                    pg.mixer.music.load('Win_music_3.mp3')
                    pg.mixer.music.play(1)
                Tk().wm_withdraw()  # to hide the main window
                messagebox.showinfo('Yeah', 'You won!')
                # animation for win
            game.__init__()
            return 0

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                if (event.button == 1):
                    pos = pg.mouse.get_pos()
                    if 450 <= pos[0] <= 490 and height - 5 <= pos[1] <= height + 35:
                        if game.mute == True:
                            game.mute = False
                            sound_or_mute_image = mute_icon_image
                        else:
                            game.mute = True
                            sound_or_mute_image = sound_icon_image

                    if game.num_of_moves_played == 0:
                        mem_x = -1
                        mem_y = -1
                        x = 0
                        y = 0
                        for i in range(10, game.size - 10, game.blocksize):
                            y = y % game.num_of_rows

                            for j in range(10, game.size - 10, game.blocksize):
                                x = x % game.num_of_rows

                                rect = pg.Rect(i, j, game.blocksize, game.blocksize)
                                pg.draw.rect(window, (50, 100, 200), rect, 2)

                                if 0 < pos[0] - i < game.blocksize and 0 < pos[1] - j < game.blocksize:
                                    mem_x = x
                                    mem_y = y
                                x = x + 1

                            y = y + 1

                        if mem_x != -1 and mem_y != -1:
                            game.generate_new_array_with_free_starting_square(mem_x, mem_y)
                            game.num_of_moves_played = 1

                    info = draw_window(pos, True, brojac_1, window, game, background_color)
                    if info == 1:
                        game.__init__()
                        return 0
                elif event.button == 3 and game.num_of_flags_remaining >= 0 and game.num_of_moves_played != 0:
                    pos = pg.mouse.get_pos()
                    draw_flag(window, pos, game)
                brojac_1 = 0
            elif event.type == pg.QUIT:
                return 1
            else:
                info = draw_window(0, False, brojac_1, window, game, background_color)
                if info == 1:
                    game.__init__()
                    return 0
                brojac_1 = 0

        flag_count_text_1 = font.render(": ", True, white, black)
        flag_count_text = font.render(str(game.num_of_flags_remaining), True, white, black)
        flag_count_text_1 = pg.transform.scale(flag_count_text_1, (28, 21))
        flag_count_text = pg.transform.scale(flag_count_text, (38, 30))
        window.fill((0, 0, 0), (42, height, 110, 40))
        window.blit(flag_count_text_1, (43, height + 4))
        window.blit(flag_count_text, (60, height + 1))
        window.blit(sound_or_mute_image, (450, height - 5))

    pg.quit()




#start of program
main()