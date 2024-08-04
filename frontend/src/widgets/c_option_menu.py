import customtkinter as ctk


class COptionMenu(ctk.CTkOptionMenu):
    def __init__(
        self,
        master: ctk.CTk,
        values: list,
        variable: ctk.Variable,
        font: ctk.CTkFont = None,
        height: int = 28,
    ) -> None:
        super().__init__(
            master=master,
            height=height,
            bg_color="transparent",
            font=font,
            values=values,
            variable=variable,
        )
