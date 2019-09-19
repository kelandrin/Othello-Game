'''This module is the Othello_GUI, all of the functions that deal with making labels, frames, widgets, buttons, and drawing on
 the canvas are contained within. The GUI is executable'''

import tkinter as tk
import othello_model
import point

_CANVAS_BACKGROUND_COLOR_ = '#0AC730'
_ROW_AND_COLUMN_NUM_OPTIONS_ = [4, 6, 8, 10, 12, 14, 16]

class MenuSettings:
    '''this class contains all of the functions that create the menu settings at the start of the game. The values are
    then loaded into the game and upon hitting the ok button, the game will close the menu settings'''

    def __init__(self):

        self._menu_window = tk.Toplevel()
        self._menu_window.wm_title('OTHELLO Settings')
        self.display_buttons_and_labels()

        '''ROW AND COLUMN CONFIGURES'''
        self._menu_window.rowconfigure(0, weight=1)
        self._menu_window.rowconfigure(1, weight=1)
        self._menu_window.rowconfigure(2, weight=1)
        self._menu_window.rowconfigure(3, weight=1)
        self._menu_window.rowconfigure(4, weight=1)
        self._menu_window.rowconfigure(5, weight=1)
        self._menu_window.rowconfigure(6, weight=1)
        self._menu_window.rowconfigure(7, weight=1)
        self._menu_window.columnconfigure(0, weight=1)

    def display_buttons_and_labels(self):
        '''this functions displays all of the buttons and labels needed for the intro menu settings'''

        self._make_menu_title_label()
        self._make_row_num_buttons_labels()
        self._make_column_num_buttons_labels()
        self._make_who_goes_first_buttons_labels()
        self._make_how_to_win_buttons_labels()
        self._make_ok_button_labels()


    def _make_menu_title_label(self):
        '''creates the title label at the top of the menu screen'''

        self._menu_title = tk.Label(master = self._menu_window, text='Othello Settings',
                                    font=('Times New Roman', 30), bg='#10f2ea', fg='black', width=50, relief='raised')\
                                    .grid(row=0, column=0, sticky=tk.N)


    def _make_row_num_buttons_labels(self):
        '''creates the labels, frames and buttons for the ROWS NUMBER on the menu screen. The default is 4 rows'''

        '''ROWS FRAME FOR LABEL AND OPTIONMENU'''
        self._rows_frame = tk.Frame(master = self._menu_window)
        self._rows_frame.grid(row = 1, column = 0, sticky = tk.N)

        '''CHOOSE ROWS LABEL'''
        self._choose_rows_label = tk.Label(master=self._rows_frame, text='Choose how many rows:',
                                           font=('Times New Roman', 20), bg='#5EE058', fg='black', width=40, relief = 'raised')\
                                           .grid(row=1, column=0, pady = 3, sticky = tk.N)

        '''ROWS NUM VARIABLE FOR OPTIONMENU'''
        self._rows_numVar = tk.IntVar()
        self._rows_numVar.set(_ROW_AND_COLUMN_NUM_OPTIONS_[0])

        '''ROWS NUM OPTIONMENU'''
        self._rows_num_options_menu = tk.OptionMenu(self._rows_frame, self._rows_numVar, *_ROW_AND_COLUMN_NUM_OPTIONS_)
        self._rows_num_options_menu.grid(row = 1, column = 1, pady = 3, sticky = tk.N)

    def _make_column_num_buttons_labels(self):
        '''creates the labels, frames and buttons for the COLUMNS NUMBER on the menu screen. The default is 4 columns'''

        '''COLUMN FRAME FOR LABEL AND OPTIONMENU'''
        self._columns_frame = tk.Frame(master=self._menu_window)
        self._columns_frame.grid(row=2, column=0, sticky=tk.N)

        '''CHOOSE COLUMNS LABEL'''
        self._choose_columns_label = tk.Label(master=self._columns_frame, text='Choose how many columns:',
                                              font=('Times New Roman', 20), bg='#5EE058', fg='black', width=40, relief = 'raised')\
                                              .grid(row=2, column=0, pady = 3, sticky=tk.N)

        '''COLUMNS NUM VARIABLE FOR OPTIONMENU'''
        self._columns_numVar = tk.IntVar()
        self._columns_numVar.set(_ROW_AND_COLUMN_NUM_OPTIONS_[0])

        '''COLUMNS NUM OPTIONMENU'''
        self._columns_num_options_menu = tk.OptionMenu(self._columns_frame, self._columns_numVar, *_ROW_AND_COLUMN_NUM_OPTIONS_)
        self._columns_num_options_menu.grid(row=2, column=1, pady = 3, sticky=tk.N)

    def _make_who_goes_first_buttons_labels(self):
        '''creates the labels, frames and buttons for WHO GOES FIRST on the menu screen.
        The default is that the BLACK player goes first'''

        '''WHO GOES FIRST LABEL'''
        self._who_goes_first_label = tk.Label(master=self._menu_window, text='Choose who goes first:',
                                              font=('Times New Roman', 20), bg='#5EE058', fg='black', width=40, relief='raised')\
                                              .grid(row=3, column=0, sticky=tk.N)

        '''WHO GOES FIRST FRAME CONTAINING RADIOBUTTONS'''
        self.who_goes_first_frame = tk.Frame(master = self._menu_window)
        self.who_goes_first_frame.grid(row = 4, column = 0)

        '''WHO GOES FIRST VARIABLE FOR RADIOBUTTONS'''
        self._first_moveVar = tk.StringVar()

        '''RADIOBUTTON FOR BLACK PLAYER'''
        self._black_goes_first_radiobutton = tk.Radiobutton(master = self.who_goes_first_frame, text = 'Black',
                                                             font=('Times New Roman', 20), bg = '#bcccdb', fg = 'black',
                                                             variable = self._first_moveVar, value = 'Black')
        self._black_goes_first_radiobutton.grid(row=4, column=0, sticky= tk.W + tk.N + tk.S + tk.E, padx = 5, pady = 5)
        self._black_goes_first_radiobutton.select()

        '''RADIOBUTTON FOR WHITE PLAYER'''
        self._white_goes_first_radiobutton = tk.Radiobutton(master= self.who_goes_first_frame, text = 'White',
                                                             font=('Times New Roman', 20), bg='#bcccdb', fg='black',
                                                             variable= self._first_moveVar, value = 'White')
        self._white_goes_first_radiobutton.grid(row=4, column=1, sticky=tk.W + tk.N + tk.S + tk.E, padx = 5, pady = 5)


    def _make_how_to_win_buttons_labels(self):
        '''creates_the labels, frames and buttons for HOW YOU WIN on the menu screen.
        The default is that the MOST amount of tiles wins the game'''

        '''HOW TO WIN LABEL'''
        self._how_to_win_label = tk.Label(master=self._menu_window, text='Choose how you would like to win:',
                                          font=('Times New Roman', 20), bg='#5EE058', fg='black', width=40, relief='raised')\
                                          .grid(row=5, column= 0, sticky=tk.N)

        '''HOW TO WIN FRAME CONTAINING RADIOBUTTONS'''
        self.how_to_win_frame = tk.Frame(master=self._menu_window)
        self.how_to_win_frame.grid(row=6, column=0)

        '''HOW TO WIN VARIABLE FOR RADIOBUTTONS'''
        self._how_to_winVar = tk.StringVar()

        '''MOST AMOUNT OF TILES WINS BUTTON'''
        self._most_tiles_to_win_radiobutton = tk.Radiobutton(master=self.how_to_win_frame, text='Most amount of tiles',
                                                             font=('Times New Roman', 20), bg='#bcccdb', fg='black',
                                                             variable=self._how_to_winVar, value='>')
        self._most_tiles_to_win_radiobutton.grid(row=6, column=0, sticky=tk.W + tk.N + tk.S + tk.E, padx=5, pady=10)
        self._most_tiles_to_win_radiobutton.select()

        '''LEAST AMOUNT OF TILES WINS BUTTON'''
        self._least_tiles_to_win_radiobutton = tk.Radiobutton(master = self.how_to_win_frame, text='Least amount of tiles',
                                                              font=('Times New Roman', 20), bg='#bcccdb', fg='black',
                                                              variable=self._how_to_winVar, value='<')
        self._least_tiles_to_win_radiobutton.grid(row=6, column=1, sticky= tk.W + tk.N + tk.S + tk.E, padx = 5, pady = 10)


    def _make_ok_button_labels(self):
        '''creates the labels, frames and buttons for the OK BUTTON on the menu screen.
        The default is that the ok button is NOT clicked'''

        '''OK BUTTON FRAME CONTAINING LABEL AND BUTTON'''
        self.ok_button_frame = tk.Frame(master = self._menu_window)
        self.ok_button_frame.grid(row = 7, column = 0, sticky = tk.E)

        '''OK TO CONTINUE BUTTON'''
        self._ok_button = tk.Button(master = self.ok_button_frame, text = 'OK',
                                    font=('Times New Roman', 30), bg='#10f2ea', fg='black', width = 8,
                                    relief = 'solid', padx = 10, pady = 0, command = self._on_ok_button_clicked)
        self._ok_button.grid(row = 7, column = 1, sticky = tk.S + tk.E)

        '''OK TO CONTINUE INITIAL BUTTON STATUS'''
        self._ok_button = False

    def _was_ok_button_clicked(self) -> bool:
        '''returns a bool for whether the OK button was pressed '''

        return self._ok_button

    def _on_ok_button_clicked(self):
        '''when the ok button is clicked, this function gets the values from the different button widgets'''

        self._ok_button = True

        self._rows_numVar = self._rows_numVar.get()
        self._columns_numVar = self._columns_numVar.get()
        self._first_moveVar = self._first_moveVar.get()
        self._how_to_winVar = self._how_to_winVar.get()

        self._menu_window.destroy()

    def _get_row_num(self) -> 'IntVar':

        return self._rows_numVar

    def _get_column_num(self) -> 'Intvar':

        return self._columns_numVar

    def _get_first_mover(self) -> 'StringVar':

        return self._first_moveVar

    def _get_how_to_win(self) -> 'StringVar':

        return self._how_to_winVar

    def show_settings(self) -> None:
        '''when the click to start button is clicked, this function opens up the Toplevel window and waits to return to
        the root window'''

        self._menu_window.grab_set()
        self._menu_window.wait_window()

class OthelloApp:
    '''this class is the Othello Application, it contains all of the functions needed to create the canvas, relevant buttons, labels,
    and events that occur'''

    def __init__(self):

        self._root_window = tk.Tk()
        self._root_window.wm_title('OTHELLO - FULL')

        self._gamestate = None

        self._canvas = tk.Canvas(
            master = self._root_window,
            width = 700, height = 700,
            background= _CANVAS_BACKGROUND_COLOR_)

        self._canvas.grid(row=2, column=0, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.W + tk.E)

        self._make_menu_settings_button = tk.Button(master=self._root_window, text='CLICK TO START',
                                                    font=('Times New Roman', 30), anchor = 'center',
                                                    padx=7, pady=7, command=self._on_settings_button_clicked)

        self._make_menu_settings_button.grid(row = 2, column = 0)


        '''BINDS'''
        self._canvas.bind('<Configure>', self._on_canvas_resize)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        '''ROW/COLUMN CONFIGURES'''
        self._root_window.columnconfigure(0, weight=1)
        self._root_window.rowconfigure(0, weight=0)
        self._root_window.rowconfigure(1, weight=0)
        self._root_window.rowconfigure(2, weight=1)
        self._root_window.rowconfigure(3, weight=0)

        '''HAS BOARD BEEN SETUP'''
        self._board_is_setup = False

        '''CONTINUE BUTTON CLICK COUNTER'''
        self._continue_button_click_counter = 0

    def _display_buttons(self):
        '''displays all buttons on the board'''

        self._make_title_label()
        self._make_turn_label()
        self._make_scoreboard()
        self._make_init_discs_buttons_labels()
        self._make_continue_button()

    def _make_title_label(self):
        '''creates the title label at the top of the screen'''

        self._title_label = tk.Label(master=self._root_window, text='OTHELLO - FULL',
                                     font=('Times New Roman', 30), bg='#10f2ea', fg='black', width=75, relief='raised')\
                                     .grid(row=0, column=0, sticky=tk.N)

    def _make_turn_label(self):
        '''creates the turn label that displays whose turn it is'''

        self._turn_label = tk.Label(master = self._root_window, text=f'Turn: {self._gamestate._turn}',
                                    font = ('Times New Roman', 25))
        self._turn_label.grid(row=1, column=0, sticky=tk.N)

    def _make_scoreboard(self):
        '''creates the black tiles score board [left side of the screen] and white tiles score board [right side of the screen]'''

        '''BLACK TILES LABEL'''
        self._black_tiles_num_label = tk.Label(master=self._root_window, text='Black: 0',
                                               font=(None, 25), relief='raised')
        self._black_tiles_num_label.grid(row=1, column=0, sticky=tk.W)

        '''WHITE TILES LABEL'''
        self._white_tiles_num_label = tk.Label(master=self._root_window, text='White: 0',
                                               font=(None, 25), relief='raised')
        self._white_tiles_num_label.grid(row=1, column=0, sticky=tk.E)

    def _make_init_discs_buttons_labels(self):
        '''creates the labels, frame, and buttons for dealing with the initial setting of the pieces'''

        '''INITIALIZING DISCS FRAME'''
        self._place_discs_frame = tk.Frame(master = self._root_window)
        self._place_discs_frame.grid(row = 3, column = 0, sticky = tk.N)

        '''INITIALIZING DISCS LABEL'''
        self._place_discs_label = tk.Label(master = self._place_discs_frame,
                                           text = f'Place as many {self._gamestate._turn} discs ' \
                                                  f'and press CONTINUE when finished',
                                           font=('Times New Roman', 25), bg='#10f2ea', fg='black', width=75)
        self._place_discs_label.grid(row = 3, column = 0, sticky = tk.N)

    def _make_continue_button(self):
        '''creates the button for the other player to begin setting up their pieces on the board'''

        self._continue_button = tk.Button(master=self._place_discs_frame, text='CONTINUE',
                                          font=('Times New Roman', 30), bg='#bcccdb', fg='black',
                                          padx=10, pady=10, command=self._on_continue_button_clicked)
        self._continue_button.grid(row = 3, column = 1, sticky = tk.E + tk.S)

    def _make_winner_label(self, winner: str):
        '''creates a label that displays who won as well as the score'''

        if winner != 'NONE':

            self._winner_label = tk.Label(master=self._root_window,
                                    text=f'Winner is {winner}! Final score is Black: {self._gamestate._black_tiles_num}, White: {self._gamestate._white_tiles_num}',
                                    font=('Times New Roman', 30), bg='#10f2ea', width = 75)
        else:

            self._winner_label = tk.Label(master=self._root_window,
                                          text=f'It was a tie game! Final score is Black: {self._gamestate._black_tiles_num}, White: {self._gamestate._white_tiles_num}',
                                          font=('Times New Roman', 30), bg='#10f2ea', width=75)

        self._winner_label.grid(row=3, column=0, sticky=tk.N)

    def _initialize_cells(self):
        '''creates the list of all cells, creates the list of empty cells, and draws the cells'''

        cell_list = self._gamestate._create_list_of_cells()
        self._gamestate._empty_spot_list = self._gamestate._create_list_of_empty_cells(cell_list)

        self._draw_all_cells()


    def _on_settings_button_clicked(self):
        '''this function opens up the menu settings when the settings button has been clicked, it receives the input from the
        user and stores it in variables as well as creates all of the buttons on the screen and initializes the cells'''

        self._gamestate = self._create_gamestate()

        menu = MenuSettings()
        menu.show_settings()

        if menu._was_ok_button_clicked():

            self._gamestate._rows_num = menu._get_row_num()
            self._gamestate._columns_num = menu._get_column_num()
            self._gamestate._turn = menu._get_first_mover()
            self._gamestate._how_to_win = menu._get_how_to_win()

            self._make_menu_settings_button.destroy()
            self._display_buttons()
            self._initialize_cells()


    def _on_continue_button_clicked(self):
        '''when the continue button is clicked, this function updates the labels and scoreboard in the beginning as well as looks for a winner
        in case the user made a board that was unplayable'''

        self._continue_button_click_counter += 1
        self._continue_button['text'] = 'START GAME'
        self._gamestate._opposite_turn()
        self._update_scoreboard()
        self._update_turn_label()

        if self._continue_button_click_counter == 1:
            self._update_place_discs_label()

        else:
            self._board_is_setup = True
            self._place_discs_frame.destroy()
            if self._gamestate.is_there_a_winner():
                winner = self._gamestate.determine_winner()
                self._make_winner_label(winner)


    def _on_canvas_resize(self, event: tk.Event) -> None:
        '''when the canvas is resized, the spots and cells are redrawn'''

        if self._gamestate == None:
            pass

        else:
            self._draw_all_cells()
            self._draw_all_spots()

    def _on_canvas_clicked(self, event: tk.Event):
        '''when the canvas is clicked it is determined whether that move is valid, and if so changes the board, updates
        the labels and switches turns, otherwise, it displays the winner'''

        if self._gamestate != None:

            width = self._canvas.winfo_width()
            height = self._canvas.winfo_height()

            list_of_cells = self._gamestate._board
            click_point = point.from_pixel(event.x, event.y, width, height)

            for cell in list_of_cells:

                if cell._frac_x1 < click_point._frac_x < cell._frac_x2 and cell._frac_y1 < click_point._frac_y < cell._frac_y2 and cell._status == None:

                    if self._board_is_setup == False:

                        cell._set_grid_cell_status(self._gamestate._turn)
                        self._gamestate._remove_empty_spot(cell)
                        self._draw_spot(cell)
                        self._update_scoreboard()

                    else:

                        try:

                            if self._gamestate._try_empty_spots_for_valid_move():
                                self._gamestate.is_move_valid(cell)
                                self._gamestate.execute_move(cell)
                                self._gamestate._remove_empty_spot(cell)
                                self._draw_all_spots()
                                self._gamestate._opposite_turn()
                                self._update_turn_label()
                                self._update_scoreboard()

                                if not self._gamestate._try_empty_spots_for_valid_move():

                                    self._gamestate._opposite_turn()
                                    self._update_turn_label()

                                if self._gamestate.is_there_a_winner():
                                    winner = self._gamestate.determine_winner()
                                    self._make_winner_label(winner)

                        except othello_model.InvalidMoveError:
                            continue


    def _update_place_discs_label(self):
        '''updates the intro directions for placing the discs'''

        self._place_discs_label['text'] = f'Now place {self._gamestate._turn} discs ' \
                                          f'and press START GAME when finished'

    def _draw_spot(self, cell: 'GridCell'):
        '''takes in a cell and draws the spot with the appropriate color'''

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        color = self._gamestate._decide_color_to_fill_spot(cell)

        if color != None:

            self._canvas.create_oval(
                canvas_width * (cell._frac_x1 + .01), canvas_height * (cell._frac_y1 + .01),
                canvas_width * (cell._frac_x2 - .01), canvas_height * (cell._frac_y2 - .01),
                fill = color, outline = 'Gray', width = 4)

    def _draw_all_spots(self):

        for cell in self._gamestate._board:
            if cell._status != None:
                self._draw_spot(cell)

    def _draw_all_cells(self):

        for cell in self._gamestate._board:
            frac_x1, frac_y1, frac_x2, frac_y2 = cell._get_frac_corners()
            self._create_rectangle(frac_x1, frac_y1, frac_x2, frac_y2, 3)  # frac_x1,frac_y1,frac_x2,frac_y2, width of rectangle

    def _create_rectangle(self, frac_x1: float, frac_y1: float, frac_x2: float, frac_y2: float, width: int):

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        self._canvas.create_rectangle(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            outline='black', fill = _CANVAS_BACKGROUND_COLOR_, width = width)

    def _update_scoreboard(self):
        '''updates what the score is on the board'''

        white_counter,black_counter = self._gamestate._count_number_of_tiles()

        self._gamestate._black_tiles_num = black_counter
        self._gamestate._white_tiles_num = white_counter

        self._black_tiles_num_label['text'] = f'Black: {black_counter}'
        self._white_tiles_num_label['text'] = f'White: {white_counter}'

    def _update_turn_label(self):
        '''updates whose turn it is on the board'''

        self._turn_label['text'] = f'Turn: {self._gamestate._turn}'

    def _create_gamestate(self):
        '''initializes the gamestate'''
        
        gamestate = othello_model.Gamestate()
        
        return gamestate

    def run(self) -> None:
        '''runs the mainloop'''

        self._root_window.mainloop()

if __name__ == '__main__':

    GameAPP = OthelloApp()
    GameAPP.run()




