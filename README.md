# Othello-Game
Othello/Reversi is another classic boardgame that has been adapted to play on a computer. It requires 2 people to play.

**Rules**  
Player's toss a coin to decide who will play white - white moves first. Each turn, the player places one piece on the board with their colour facing up.

For the first four moves, the players must play to one of the four squares in the middle of the board and no pieces are captured or reversed.

Each piece played must be laid adjacent to an opponent's piece so that the opponent's piece or a row of opponent's pieces is flanked by the new piece and another piece of the player's colour. All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's colour.

It can happen that a piece is played so that pieces or rows of pieces in more than one direction are trapped between the new piece played and other pieces of the same colour. In this case, all the pieces in all viable directions are turned over.

The game is over when neither player has a legal move (i.e. a move that captures at least one opposing piece) or when the board is full.

**To Run**:  
This game is played on a graphical user interface "othello_gui" file which uses the tkinter package

**Supporting files**:  
The logic of the game is running in the "othello_model" file  
Both the GUI and the model use the "point" file as well  

This game was written in Python
