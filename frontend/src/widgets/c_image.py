from typing import Tuple
from PIL.Image import Image
import customtkinter as ctk


class CImage(ctk.CTkImage):
    def __init__(
        self,
        light_image: Image = None,
        dark_image: Image = None,
        size: Tuple[int, int] = ...,
    ):
        super().__init__(
            light_image=light_image,
            dark_image=dark_image,
            size=size,
        )
