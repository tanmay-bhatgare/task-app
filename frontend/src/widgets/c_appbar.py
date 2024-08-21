import customtkinter as ctk

from src.constants.constants import CFont, Size
from src.widgets.widget import CLabel, CButton


class CAppbar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        height=40,
        width=Size.window_size[0],
        fg_color="transparent",
        title="CAppbar",
        has_option=False,
        option_command=None,
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            fg_color=fg_color,
            corner_radius=0,
        )
        self.pack_propagate(False)
        self.title_lbl = CLabel(master=self, text=title, font=CFont.font_small(22))
        self.title_lbl.pack(side=ctk.LEFT, padx=10)

        if has_option:
            self.option_btn = CButton(
                master=self,
                text="O",
                width=height,
                height=height,
                command=option_command,
                bg_color="transparent",
                fg_color="transparent",
                hover_color=fg_color,
                corner_radius=0,
            )
            self.option_btn.pack(side=ctk.RIGHT, padx=5)
