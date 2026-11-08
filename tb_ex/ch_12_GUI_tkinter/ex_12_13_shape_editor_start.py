# file: ex_12_13_shape_editor_start.py
import tkinter as tk
from tkinter import ttk, simpledialog


class ShapeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape editor")
        self.root.resizable(False, False)
        self.canvas_width = 500
        self.canvas_height = 350
        self.selected_id = None

        instruction = ttk.Label(root, text="Click a shape to select it.")
        instruction.pack(padx=10, pady=5)

        self.canvas = tk.Canvas(
            root, width=self.canvas_width,
            height=self.canvas_height, bg="white")
        self.canvas.pack(padx=10, pady=5)

        resize_button = ttk.Button(
            root, text="Resize selected", command=self.resize_selected)
        resize_button.pack(padx=10, pady=5)

        self.create_shapes()
        self.canvas.bind("<Button-1>", self.select_shape)

    def create_shapes(self):
        # TODO: create at least two filled rectangles and two filled ovals.
        # Use black outlines of width 1 and dimensions of at least 10.
        # Keep all shapes inside the Canvas and place them apart.
        self.canvas.create_rectangle(50, 50, 150, 120, fill = "red", outline = "black", width = 1)
        self.canvas.create_rectangle(300, 50, 420, 130, fill="blue", outline="black", width=1)
        self.canvas.create_oval(50, 180, 150, 270, fill="green", outline="black", width=1)
        self.canvas.create_oval(300, 180, 420, 280, fill="yellow", outline="black", width=1)
        
    def select_shape(self, event):
        # TODO: restore the previous selection's black outline (width 1).
        # Use find_overlapping() to find the shape at the click position.
        # Store items[-1] as the selected ID, or None if no shape was hit.
        # Mark the new selection with a red outline of width 3.
        if self.selected_id is not None:
            self.canvas.itemconfig(self.selected_id, outline="black", width=1)

        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
            
        if items:
            self.selected_id = items[-1]
            self.canvas.itemconfig(self.selected_id, outline="red", width=3)
        else:
            self.selected_id = None
            
    def resize_selected(self):
        if self.selected_id is None:
            return
            
        # TODO: replace this return with an assignment that reads the
        # selected shape's bounding rectangle into x0, y0, x1, y1.
        # The return keeps the unfinished starter runnable.
        x0, y0, x1, y1 = self.canvas.coords(self.selected_id)
                

        # Dialog code is provided because input dialogs are new.
        # askinteger() returns an integer, or None if the user cancels.
        new_width = simpledialog.askinteger(
            "Resize shape", "New width in pixels:",
            parent=self.root,
            initialvalue=int(x1 - x0),
            minvalue=10,
            maxvalue=int(self.canvas_width - x0))
        if new_width is None:
            return

        new_height = simpledialog.askinteger(
            "Resize shape", "New height in pixels:",
            parent=self.root,
            initialvalue=int(y1 - y0),
            minvalue=10,
            maxvalue=int(self.canvas_height - y0))
        if new_height is None:
            return
        
        # TODO: use coords() to apply new_width and new_height together.
        # Keep x0 and y0 fixed. Do not create a new shape.
        self.canvas.coords(self.selected_id, x0, y0, x0 + new_width, y0 + new_height)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeEditor(root)
    root.mainloop()
