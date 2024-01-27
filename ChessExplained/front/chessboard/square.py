import customtkinter


class Square(customtkinter.CTkFrame):
    """
    A square on the chess board.

    Parameters:
        master (Tk): The master window.
        square_color (str): The color of the square.
        **kwargs: Additional keyword arguments.

    Attributes:
        square_color (str): The color of the square.
    """

    def __init__(self, master, width, height, square_color, **kwargs):
        """
        Initialize the Square.

        Parameters:
            master (Tk): The master window.
            square_color (str): The color of the square.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(master, width=width, height=height, **kwargs)

        self.square_color = square_color
        self.configure(fg_color=square_color)

        # self.bind("<Enter>", self.on_enter)
        # self.bind("<Leave>", self.on_leave)

    def on_enter(self):
        """
        Event handler for the mouse entering the square. Highlights the square.
        """
        self.configure(bg="lightblue")

    def on_leave(self):
        """
        Event handler for the mouse leaving the square. Un-highlights the square.
        """
        self.configure(bg=self.square_color)
