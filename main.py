from window import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(1, 1, 12, 16, 50, win)  
    solved = maze.solve()  
    print("Maze solved:", solved)

    win.wait_for_close()
if __name__ == "__main__":
    main()