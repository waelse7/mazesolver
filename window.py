from tkinter import Tk, BOTH, Canvas
class Window:
    
    def __init__(self, width, height) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")

        self._canvas = Canvas(self._root, width=width, height=height, bg='white')
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)
        self.redraw()