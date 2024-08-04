import customtkinter as ctk


class CLabel(ctk.CTkLabel):
    def __init__(
        self,
        master: ctk.CTk,
        width: int = 0,
        height: int = 28,
        text: str = "CLabel",
        bg_color: str = "transparent",
        text_color: str = "white",
        font: ctk.CTkFont = None
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            text=text,
            bg_color=bg_color,
            text_color=text_color,
            font=font,
        )
