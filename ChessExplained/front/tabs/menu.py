import customtkinter


class Menu(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        """
        Create the buttons of the menu.
        """
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        button_load = customtkinter.CTkButton(self, 200, 70, text=f"Load from Fen")
        button_load.grid(row=0, column=0, sticky="nsew", pady=10)

        button_chat = customtkinter.CTkButton(self, 200, 70, text=f"Start chat with Bot")
        button_chat.grid(row=0, column=2, sticky="nswe", pady=10)

        self.buttons += [button_load, button_chat]
