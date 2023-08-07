from cells import Cell
import random
import time
class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size, win, seed=None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._seed = random.seed(seed)      
        self._break_walls_r(0, 0)
        self._reset_visted()

    def _reset_visted(self):
        for list in self._cells:
            for cell in list:
                cell.visited = False

    def _create_cells(self):
        for i in range(0, self._num_cols):
            col = []
            for j in range(0, self._num_rows):
                cell_x1 = self._x1 + i * self._cell_size
                cell_y1 = self._y1 + j * self._cell_size
                cell_x2 = cell_x1 + self._cell_size
                cell_y2 = cell_y1 + self._cell_size

                col.append(Cell(cell_x1, cell_y1, cell_x2, cell_y2, self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        
        self._cells[0][0].draw()
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()

    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while True:
            directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                directions.append((-1, 0))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                directions.append((1, 0))
            if j > 0 and not self._cells[i][j - 1].visited:
                directions.append((0, -1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                directions.append((0, 1))

            if not directions:
                self._draw_cell(i, j)
                return

            next_cell_i, next_cell_j = random.choice(directions)
            new_i, new_j = i + next_cell_i, j + next_cell_j

            self._break_wall(i, j, next_cell_i, next_cell_j)
            self._break_walls_r(new_i, new_j)

    def _break_wall(self, i, j, next_cell_i, next_cell_j):
        if next_cell_i == -1:  
            self._cells[i][j].has_left_wall = False
            self._cells[i - 1][j].has_right_wall = False
        elif next_cell_i == 1: 
            self._cells[i][j].has_right_wall = False
            self._cells[i + 1][j].has_left_wall = False
        elif next_cell_j == -1: 
            self._cells[i][j].has_top_wall = False
            self._cells[i][j - 1].has_bottom_wall = False
        elif next_cell_j == 1:  
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j + 1].has_top_wall = False
    
    def solve(self):
        return self._solve_r(0, 0)  

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        directions = [
            (-1, 0, self._cells[i][j].has_left_wall, i > 0),
            (1, 0, self._cells[i][j].has_right_wall, i < self._num_cols -1),
            (0, -1, self._cells[i][j].has_top_wall, j > 0 ),
            (0, 1, self._cells[i][j].has_bottom_wall, j < self._num_rows -1)
        ]

        for next_i, next_j, has_wall, is_valid in directions:
            if is_valid and not has_wall and not self._cells[i + next_i][j + next_j].visited:
                self._cells[i][j].draw_move(self._cells[i+next_i][j+next_j])
                if self._solve_r(i+ next_i, j + next_j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+next_i][j+next_j], True)
        return False