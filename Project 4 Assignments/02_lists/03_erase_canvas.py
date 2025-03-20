import tkinter as tk

# Canvas settings
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserTool:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.create_grid()  # Create blue grid
        
        # Create eraser (invisible at first)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")
        self.canvas.tag_raise(self.eraser)  # Bring eraser to top
        self.canvas.bind("<Motion>", self.move_eraser)  # Bind mouse movement
    
    def create_grid(self):
        """Creates a grid of blue squares"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
    
    def move_eraser(self, event):
        """Moves the eraser and erases blue squares"""
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Move eraser

        # Check for overlapping blue squares and erase them
        overlapping_items = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping_items:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Tool")
    EraserTool(root)  # Initialize the eraser tool
    root.mainloop()

if __name__ == "__main__":
    main()

