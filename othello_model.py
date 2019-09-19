'''This module contains the underlying game logic behind the game of othello. Such functions as if the move is valid,
executing moves, finding which tiles to flip. This module is not executable. It is rather a library of functions for the
main module to draw from.'''

import point

class Gamestate:
    '''contains all the information about the current state of the game as well as methods that act upon that state'''

    _rows_num = 0  # even int from 4 to 16
    _columns_num = 0  # even int from 4 to 16
    _turn = None  # 'B' or 'W'
    _how_to_win = None  # '<' or '>'
    _board = []
    _empty_spot_list = []
    _black_tiles_num = 0
    _white_tiles_num = 0

    def is_move_valid(self, cell: 'GridCell') -> bool:
        '''takes in a row and a column and raises an InvalidMoveError if they are out of the grid, if there is already
        a piece in that cell, or if the move is invalid (no pieces will flip); otherwise returns True '''

        if not self._is_valid_row_and_valid_column(cell):
            raise InvalidMoveError

        elif not cell._is_valid_start_cell():
            raise InvalidMoveError

        elif len(self._get_list_of_valid_endpoints(cell)) == 0:
            raise InvalidMoveError

        else:
            return True


    def execute_move(self, cell: 'GridCell') -> 'Gamestate':
        '''takes in the input row and input column and flips the appropriate tiles, and returns the Gamestate'''

        list_of_valid_endpoints = self._get_list_of_valid_endpoints(cell)
        list_of_tiles_to_flip = self._get_list_of_tiles_to_flip(cell, list_of_valid_endpoints)

        for tile_to_flip in list_of_tiles_to_flip:

            for cell in self._board:

                if tile_to_flip == (cell._row,cell._column):

                    cell._status = self._turn


    def _get_list_of_tiles_to_flip(self, cell: 'GridCell', list_of_valid_endpoints: list) -> list:
        '''takes in the input row and the input column, and a list of valid endpoints, returns a list of the pieces that need
        to be flipped'''

        list_of_tiles_to_flip = []

        for endpoint in list_of_valid_endpoints:

            cell_row = cell._row
            cell_column = cell._column
            rowdelta,coldelta = endpoint._rowdelta_coldelta_tuple

            while (cell_row,cell_column) != (endpoint._row, endpoint._column):

                list_of_tiles_to_flip.append((cell_row,cell_column))

                cell_row = cell_row + rowdelta
                cell_column = cell_column + coldelta

        return list_of_tiles_to_flip

    def _create_list_of_cells(self) -> list:
        '''creates a list of all of the cells on the board'''

        for col in range(self._columns_num):

            for row in range(self._rows_num):
                gridcell = GridCell()
                gridcell._set_row(row)
                gridcell._set_column(col)
                gridcell._set_fracs_from_row_and_column(self._rows_num, self._columns_num)

                self._board.append(gridcell)

        return self._board

    def _create_list_of_empty_cells(self, cell_list: list) -> list:
        '''given a list of cells, this function creates a list of empty cells and stores it in the gamestate'''

        self._empty_spot_list = []

        for cell in cell_list:

            if cell._status == None:

                self._empty_spot_list.append(cell)

        return self._empty_spot_list

    def _remove_empty_spot(self, cell: 'GridCell'):
        '''takes in the cell clicked and deletes the empty spot from the list of empty spots since the
        spot is no longer empty'''

        for empty_spot in self._empty_spot_list:

            if (empty_spot._row, empty_spot._column) == (cell._row, cell._column):

                self._empty_spot_list.remove(empty_spot)

    def _is_valid_column_number(self, cell: 'GridCell or Neighbor') -> bool:
        '''returns True if the given column number is valid; returns False otherwise'''

        return 0 <= cell._column < self._columns_num

    def _is_valid_row_number(self, cell: 'GridCell or Neighbor') -> bool:
        '''returns True if the given row number is valid; returns False otherwise'''

        return 0 <= cell._row < self._rows_num

    def _is_valid_row_and_valid_column(self, cell:'Gridcell or Neighbor') -> bool:
        '''returns True if both the given row and column are valid, returns False otherwise'''

        return self._is_valid_row_number(cell) and self._is_valid_column_number(cell)

    def _is_valid_first_neighbor_cell(self, neighbor_obj: 'Neighbor') -> bool:
        '''takes a surrounding tile and returns True if it is the opposite color, False otherwise'''

        if self._is_valid_row_and_valid_column(neighbor_obj):

            if self._turn == 'Black' and neighbor_obj._status == 'White':
                return True

            elif self._turn == 'White' and neighbor_obj._status == 'Black':
                return True

    def _is_valid_neighbor_past_the_first_neighbor(self, neighbor_obj: 'Neighbor') -> bool:
        '''returns True if the second neighbor cell over or any cell past that is not equal to '.' '''

        if self._is_valid_row_and_valid_column(neighbor_obj):

            return neighbor_obj._status != 'None'

    def _get_list_of_valid_endpoints(self, cell: 'GridCell') -> 'list of objects':
        '''takes in a row and column and searches every direction to find the valid paths. Returns a list of the endpoints
        of the valid directions'''

        list_of_all_neighbor_obj = _get_list_of_all_neighbor_cell(self,cell)
        list_of_valid_neighbors = []

        for neighbor_obj in list_of_all_neighbor_obj:

            if self._is_valid_first_neighbor_cell(neighbor_obj):

                new_neighbor_obj = _create_neighbor_object(self,neighbor_obj,neighbor_obj._rowdelta_coldelta_tuple)

                if self._is_valid_neighbor_past_the_first_neighbor(new_neighbor_obj):

                    farthest_point = self._find_valid_neighbor_past_the_first_neighbor(new_neighbor_obj)

                    if farthest_point._status != None and farthest_point._status == self._turn:

                        list_of_valid_neighbors.append(farthest_point)

        return list_of_valid_neighbors

    def _find_valid_neighbor_past_the_first_neighbor(self, neighbor_obj: 'Neighbor') -> 'Neighbor':
        '''after the first neighbor object has been deemed valid, this function determines whether to continue looking at the
        neighboring cells past the first neighbor to see if they are valid. Returns the farther neighbor if valid or the endpoint
        if not.'''

        if self._do_i_continue(neighbor_obj):

            new_neighbor_obj = _create_neighbor_object(self,neighbor_obj,neighbor_obj._rowdelta_coldelta_tuple)
            returned_new_neighbor_obj = self._find_valid_neighbor_past_the_first_neighbor(new_neighbor_obj)
            return returned_new_neighbor_obj

        else:
             return neighbor_obj

    def _do_i_continue(self, neighbor_obj: 'Neighbor') -> bool:
        '''takes in a neighboring object past the first neighboring object and returns True if that neighbor is still of the
         opposite color. Returns False if they are the same color'''

        if self._is_valid_row_and_valid_column(neighbor_obj):

            if self._turn == 'Black' and neighbor_obj._status == 'White':

                return True

            elif self._turn == 'Black' and neighbor_obj._status == 'Black':

                return False

            elif self._turn == 'White' and neighbor_obj._status == 'Black':

                return True

            elif self._turn == 'White' and neighbor_obj._status == 'White':

                return False

    def _is_move_available(self) -> bool:
        '''returns True if there is a valid move available, otherwise switches turns to the other player and searches for
        valid moves again. If both players don't have valid moves available returns False'''

        if self._try_empty_spots_for_valid_move():
            return True

        else:
            self._opposite_turn()
            if self._try_empty_spots_for_valid_move():
                return True

        return False


    def _opposite_turn(self):
        '''switches turns to the opposite player'''

        if self._turn == 'Black':
            self._turn = 'White'

        elif self._turn == 'White':
            self._turn = 'Black'

    def _decide_color_to_fill_spot(self, cell: 'GridCell'):
        '''takes in a cell that was clicked and returns what color the tile should be'''

        if cell._status == None:
            return self._turn

        else:
            return cell._status

    def _count_number_of_tiles(self):
        '''counts the number of tiles on the board for each player and enters them in their class'''

        black_counter = 0
        white_counter = 0

        for cell in self._board:
            if cell._status == 'Black':
                black_counter += 1
            elif cell._status == 'White':
                white_counter += 1
            else:
                continue

        return white_counter, black_counter

    def _try_empty_spots_for_valid_move(self) -> bool:
        ''' returns True if it finds a valid move within the empty spots, returns false otherwise'''

        for cell in self._empty_spot_list:

            try:
                if self.is_move_valid(cell):
                    return True

            except InvalidMoveError:
                pass

    def is_there_a_winner(self) -> bool:
        '''returns True if there is a winner by looking if all the spots are filled or if there are no available moves'''

        if len(self._empty_spot_list) == 0:

            return True

        elif not self._is_move_available():
            return True

    def determine_winner(self) -> str:
        '''determines who the winner is based off the given rule for how to win'''

        if self._how_to_win == '>':

            if self._black_tiles_num > self._white_tiles_num:
                return 'Black'

            elif self._white_tiles_num > self._black_tiles_num:
                return 'White'

            else:
                return 'NONE'

        elif self._how_to_win == '<':

            if self._black_tiles_num < self._white_tiles_num:
                return 'Black'

            elif self._white_tiles_num < self._black_tiles_num:
                return 'White'

            else:
                return 'NONE'


class Neighbor:
    '''this class is used to store data about the neighboring spots by turning them into objects'''

    _row = 0  # 0 < integer < total_rows
    _column = 0  # 0 < integer < total_columns
    _status = None # string containing the color of the neighbor object
    _rowdelta_coldelta_tuple = None  # tuple containing (rowdelta, coldelta)

    def _assign_values(self, g:'Gamestate', row: int, column: int, rowdelta_coldelta_tuple: tuple):
        '''assigns values to the neighboring spot including its row, column, and which direction it is relative to
        the starting point'''

        rowdelta, coldelta = rowdelta_coldelta_tuple

        self._row = row + rowdelta
        self._column = column + coldelta
        self._rowdelta_coldelta_tuple = rowdelta_coldelta_tuple
        self._status = self._set_neighbor_color_status(g)

    def _set_neighbor_color_status(self, g: 'Gamestate'):
        '''sets the color status of the neighbor object'''

        for cell in g._board:

            if (self._row, self._column) == (cell._row, cell._column):

                return cell._status


def _get_list_of_all_neighbor_cell(g: 'Gamestate', cell: 'GridCell') -> 'list of objects':
    '''takes in a row and column and creates a list of the 8 neighboring direction spots and returns that list'''

    list_of_rowdelta_coldelta_tuples = [(1, -1),
                                        (1, 0),
                                        (1, 1),
                                        (0, -1),
                                        (0, 1),
                                        (-1, -1),
                                        (-1, 0),
                                        (-1, 1)]

    list_of_all_neighbor_obj = []

    for rowdelta_coldelta_tuple in list_of_rowdelta_coldelta_tuples:
        neighbor_obj = _create_neighbor_object(g, cell, rowdelta_coldelta_tuple)
        list_of_all_neighbor_obj.append(neighbor_obj)

    return list_of_all_neighbor_obj


def _create_neighbor_object(g: 'Gamestate', cell: 'GridCell or Neighbor', rowdelta_coldelta_tuple: tuple) -> 'Neighbor':
    '''takes in information needed to create the neighbor spot and returns that neighbor'''

    neighbor_obj = Neighbor()
    neighbor_obj._assign_values(g, cell._row, cell._column, rowdelta_coldelta_tuple)

    return neighbor_obj


class GridCell:
    '''this class contains all of the information about a cell on the board, each cell on the board becomes an object
    which you can get the fractional coordinates from, its color status, as well as which row and column it is located'''

    _frac_x1 = 0
    _frac_y1 = 0
    _frac_x2 = 0
    _frac_y2 = 0
    _status = None  # options are 'None' or 'B' or 'W'
    _row = None  # int containing which row the cell is in
    _column = None  # int containing which column the cell is in
    _corners = None # tuple containing two point objects (top_left_corner,bottom_right_corner)


    def _set_grid_cell_status(self, game_piece_color: str):
        '''takes in a color and sets the grid cell status to that color'''

        self._status = game_piece_color

    def _is_valid_start_cell(self) -> bool:
        '''returns True if the spot given by the column and row numbers is not already occupied'''

        return self._status != 'None'

    def _get_frac_corners(self):
        '''returns a tuple with (frac_x1,frac_y1,frac_x2,frac_y2) which are its top left and bottom right corner points
        in fractional form'''

        return (self._frac_x1, self._frac_y1, self._frac_x2, self._frac_y2)

    def _get_board_cell_row(self):
        '''returns an int representing the board cell's row'''

        return self._row

    def _get_board_cell_column(self):
        '''returns an int representing the board cell's column'''

        return self._column

    def _set_fracs_from_row_and_column(self, total_in_row: int, total_in_column: int):
        '''takes in the total amount of rows and columns and the grid cell's row and column and sets the fractional coordinates
         as well as the top left and bottom right corners of the cell'''

        self._frac_x1 = self._column / total_in_column
        self._frac_y1 = self._row / total_in_row
        self._frac_x2 = ((self._column + 1) / total_in_column)
        self._frac_y2 = ((self._row + 1) / total_in_row)

        self._set_corners()

    def _set_row(self, row: int):

        self._row = row

    def _set_column(self, column: int):

        self._column = column

    def _set_corners(self):

        self._corners = (point.Point(self._frac_x1, self._frac_y1), point.Point(self._frac_x2, self._frac_y2))

    def _get_status(self):

        if self._status == 'Black':
            return 'Black'

        elif self._status == 'White':
            return 'White'

        elif self._status == 'None':
            return None

class InvalidMoveError(Exception):
    '''raised when an invalid move is played'''
    pass
