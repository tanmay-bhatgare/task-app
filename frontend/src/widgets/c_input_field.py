import customtkinter as ctk
from typing import Optional, Callable


class CInputField(ctk.CTkEntry):
    def __init__(
        self,
        master: ctk.CTk,
        font: ctk.CTkFont = None,
        textvariable: ctk.StringVar = None,
        width: int = 140,
        height: int = 28,
        validatecommand: Optional[Callable] = None,
        state: str = "normal",
        justify: str = "left",
        is_password: bool = False,
    ) -> None:
        self.is_password = is_password
        kwargs = {
            "master": master,
            "state": state,
            "width": width,
            "height": height,
            "textvariable": textvariable,
            "font": font,
            "justify": justify,
            "show": "•" if is_password else "",
            "validate": "key",
        }
        if validatecommand:
            kwargs["validatecommand"] = validatecommand

        super().__init__(**kwargs)

    def toggle_password(self):
        self.is_password = not self.is_password
        self.configure(show="•" if self.is_password else "")
