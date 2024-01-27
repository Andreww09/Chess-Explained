import customtkinter
from PIL import Image

from back.utils import BoardUtils


class Piece(customtkinter.CTkImage):
    def __init__(self, color, piece_type, position):
        self.color = color
        self.piece_type = piece_type
        self.position = position

        super().__init__(light_image=self.get_image(), dark_image=self.get_image(), size=(70, 70))

    def get_image(self):
        icon = ('w' if self.color else 'b') + str.lower(BoardUtils.expand_piece_name(self.piece_type)) + ".png"

        with Image.open(f"front/assets/pieces_icons/{icon}") as img:
            return img