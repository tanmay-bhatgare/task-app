import customtkinter as ctk


class CFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: ctk.CTk,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        bg_color: str = "transparent",
        fg_color: str = "transparent",
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            bg_color=bg_color,
            fg_color=fg_color,
        )
