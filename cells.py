class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    
    def __init__(self, start, end) -> None:
        self.start = start 
        self.end = end
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, x1, y1, x2, y2, win) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "white")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "white")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "white")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black")
        else:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "white")
    
    def draw_move(self, to_cell, undo=False):
        cell_x = (self.__x1 + self.__x2) / 2
        cell_y = (self.__y1 + self.__y2) / 2
        to_cell_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_y = (to_cell.__y1 + to_cell.__y2) / 2
        if undo:
            color = 'gray'
        else:
            color = 'red'
        self.__win.draw_line(Line(Point(cell_x, cell_y), Point(to_cell_x, to_cell_y)), color)