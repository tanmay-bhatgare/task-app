import customtkinter as ctk
from typing import Callable


class CButton(ctk.CTkButton):
    def __init__(
        self,
        master: ctk.CTk,
        command: Callable = None,
        text: str = "CButton",
        bg_color: str = "transparent",
        fg_color: str = None,
        hover_color: str = None,
        text_color: str = "black",
        width: int = 140,
        height: int = 28,
        font: ctk.CTkFont = None,
        image: ctk.CTkImage = None,
        corner_radius: int = None,
    ) -> None:
        super().__init__(
            master=master,
            text=text,
            height=height,
            width=width,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            command=command,
            font=font,
            image=image,
            corner_radius=corner_radius,
        )
