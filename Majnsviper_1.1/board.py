import random

class board():
    blocksize = 60
    size = 500
    num_of_rows = 0
    num_of_mines = 0
    num_of_flags_remaining = num_of_mines
    num_of_free_squares = 0
    num_of_moves_played = 0

    free_squares_array = 0 #stores free squares
    flags_array = 0 #stores flags played
    main_array = 0 #main array
    help_array = 0 #for show_neighbours function

    mute = False

    def __init__(self):
        self.set_number_of_rows()
        self.set_number_of_mines()
        self.num_of_moves_played = 0

    def set_number_of_rows(self):
        self.num_of_rows = int((self.size - 20) / self.blocksize)
        self.free_squares_array = [[0 for i in range(self.num_of_rows)] for j in range(self.num_of_rows)]
        self.flags_array = [[0 for i in range(self.num_of_rows)] for j in range(self.num_of_rows)]
        self.main_array = [[0 for i in range(self.num_of_rows)] for j in range(self.num_of_rows)]
        self.help_array = [[0 for i in range(self.num_of_rows)] for j in range(self.num_of_rows)]

    def set_number_of_mines(self):
        if self.blocksize == 60:
            self.num_of_mines = 10
        elif self.blocksize == 30:
            self.num_of_mines = 40
        elif self.blocksize == 20:
            self.num_of_mines = 170
        self.num_of_flags_remaining = self.num_of_mines
        self.num_of_free_squares = self.num_of_rows * self.num_of_rows - self.num_of_mines

    def set_blocksize_and_size(self, blocksize, size):
        self.blocksize = blocksize
        self.size = size
        self.set_number_of_rows()
        self.set_number_of_mines()

    def generate_new_array(self):
        random.seed()

        helper_num_of_mines = self.num_of_mines

        while helper_num_of_mines > 0:
            x = random.randint(0, self.num_of_rows - 1)
            random.seed()
            y = random.randint(0, self.num_of_rows - 1)
            # ako na random koordinati nema mine -> stavi (0 -> -1)
            if self.main_array[x][y] == 0:
                self.main_array[x][y] = -1
                helper_num_of_mines = helper_num_of_mines - 1

            # za svako polje bez mine spremi broj okolnih polja s minama
        for i in range(0, self.num_of_rows):
            for j in range(0, self.num_of_rows):
                if self.main_array[i][j] == 0:
                    self.has_neighbour(i, j)

    def generate_new_array_with_free_starting_square(self, a, b):
        random.seed()

        helper_num_of_mines = self.num_of_mines

        neighbouring_squares_list = self.neighbouring_squares(a, b)

        while helper_num_of_mines > 0:
            x = random.randint(0, self.num_of_rows - 1)
            random.seed()
            y = random.randint(0, self.num_of_rows - 1)
            # ako na random koordinati nema mine -> stavi (0 -> -1)
            if self.main_array[x][y] == 0 and (x, y) not in neighbouring_squares_list:
                self.main_array[x][y] = -1
                helper_num_of_mines = helper_num_of_mines - 1

            # za svako polje bez mine spremi broj okolnih polja s minama
        for i in range(0, self.num_of_rows):
            for j in range(0, self.num_of_rows):
                if self.main_array[i][j] == 0:
                    self.has_neighbour(i, j)

    def neighbouring_squares(self, i, j):
        neighbouring_squares_list = list()
        for y in range(-1, 2):
            if self.num_of_rows > i + y >= 0:
                for z in range(-1, 2):
                    if self.num_of_rows > j + z >= 0:
                        neighbouring_squares_list.append((i + y, j + z))

        return neighbouring_squares_list

    def has_neighbour(self, i, j):
        counter = 0
        for y in range(-1, 2):
            if self.num_of_rows > i + y >= 0:
                for z in range(-1, 2):
                    if (z == 0 and y == 0):
                        pass
                    elif self.num_of_rows > j + z >= 0:
                        if self.main_array[i + y][j + z] == -1:
                            counter = counter + 1
        self.main_array[i][j] = counter

    def show_mines(self, window, mine_picture):
        for i in range(0, self.num_of_rows):
            for j in range(0, self.num_of_rows):
                if(self.main_array[i][j] == -1):
                    window.blit(mine_picture, (j * self.blocksize + 10, i * self.blocksize + 10))




