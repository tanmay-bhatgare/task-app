from typing import Any
import customtkinter as ctk


class CSeperator(ctk.CTkFrame):
    def __init__(
        self, master: Any, color: str = "gray40", seperation: int = 3, padx: int = 0
    ):
        super().__init__(master=master, height=2, fg_color=color)
        self.pack(fill="x", pady=seperation, padx=padx)
