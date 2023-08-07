import unittest
from main import Maze, Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, win)

        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

        win.close()

    def test_maze_size(self):
        num_cols = 15
        num_rows = 20
        win = Window(800, 600)
        m2 = Maze(0, 0, num_rows, num_cols, 10, win)

        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

        win.close()

    def test_maze_creation_with_animation(self):
        num_cols = 5
        num_rows = 5
        win = Window(800, 600)
        m3 = Maze(0, 0, num_rows, num_cols, 50, win)


        for i in range(num_cols):
            for j in range(num_rows):
                self.assertIsNotNone(m3._cells[i][j])


        win.close()

    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        win = Window(800, 600)
        m = Maze(0, 0, num_rows, num_cols, 50, win)

        m._break_entrance_and_exit() 

        self.assertFalse(m._cells[0][0].has_top_wall)
        self.assertFalse(m._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

        win.close()

if __name__ == "__main__":
    unittest.main()