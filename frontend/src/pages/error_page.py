import customtkinter as ctk

from src.constants.constants import Size
from src.widgets.widget import CLabel


class ErrorPage(ctk.CTkFrame):
    def __init__(
        self,
        master,
        controller,
        app_state,
        width=Size.window_size[0],
        height=Size.window_size[1],
        fg_color=None,
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            fg_color=fg_color,
        )
        self.controller = controller

        self.label = CLabel(master=self, text="Error Page")
        self.label.pack(side=ctk.TOP)
