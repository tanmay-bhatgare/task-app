import customtkinter as ctk


class CFont:
    @staticmethod
    def font_small(size: int = 18) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")

    @staticmethod
    def font_med(size: int = 25) -> ctk.CTkFont:
        return ctk.CTkFont(family="Courier", size=size, weight="bold")

    @staticmethod
    def font_large(size: int = 35) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")

    @staticmethod
    def font_xl(size: int = 46) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")

    @staticmethod
    def font_sm_text(size: int = 14) -> ctk.CTkFont:
        return ctk.CTkFont(family="courier", size=size, weight="bold")

    @staticmethod
    def xs_field_lbl(size: int = 13) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")

    @staticmethod
    def font_btn(size: int = 23) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")

    @staticmethod
    def font_btn_sm(size: int = 16) -> ctk.CTkFont:
        return ctk.CTkFont(family="", size=size, weight="bold")
