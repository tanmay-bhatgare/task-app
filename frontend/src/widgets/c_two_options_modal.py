from typing import Callable
import customtkinter as ctk

from src.widgets.widget import (
    CLabel,
    CButton,
    CFrame,
    CSeperator,
)

from src.constants.constants import CFont


class CTwoOptionsModal(ctk.CTkFrame):
    def __init__(
        self,
        master,
        width: int = 150,
        height: int = 150,
        fg_color: str = None,
        border_width: int = None,
        border_color: str = None,
        modal_title_text: str = "",
        modal_title_text_color: str = None,
        modal_message_text: str = "",
        option_confirm_text: str = "Confirm",
        option_decline_text: str = "Decline",
        option_confirm_func: Callable = None,
        option_decline_func: Callable = None,
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            fg_color=fg_color,
            bg_color=fg_color,
            border_width=border_width,
            border_color=border_color,
        )
        self.is_confirm: bool = None
        self.option_confirm_func = option_confirm_func
        self.option_decline_func = option_decline_func
        self.pack_propagate(False)

        self.button_frame = CFrame(
            master=self, fg_color="transparent", bg_color="transparent"
        )

        self.modal_title = CLabel(
            master=self,
            text=modal_title_text,
            text_color=modal_title_text_color,
            font=CFont.font_med(),
        )
        self.modal_message = ctk.CTkTextbox(
            self,
            height=0.50 * height,
            border_color=fg_color,
            fg_color=fg_color,
            text_color=None,
            font=CFont.font_small(),
        )
        self.modal_message.insert(ctk.END, modal_message_text)
        self.modal_message.configure(state="disabled")

        self.confirm_button = CButton(
            master=self.button_frame,
            command=self.option_confirm_func,
            text=option_confirm_text,
            text_color="white",
            fg_color="#ff6f28",
            hover_color="#b33c00",
            font=CFont.font_btn(16),
            width=100,
        )
        self.decline_button = CButton(
            master=self.button_frame,
            command=self.option_decline_func,
            text=option_decline_text,
            text_color="white",
            fg_color="#14d2a2",
            hover_color="#0fa37e",
            font=CFont.font_btn(16),
            width=80,
        )

        self.modal_title.pack(pady=5)

        CSeperator(self, color="transparent", seperation=4, padx=10)
        self.modal_message.pack(padx=5)

        CSeperator(self, color="transparent", seperation=8)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.pack(fill="x", padx=8, pady=4)

        self.confirm_button.grid(row=0, column=0, sticky="w")
        self.decline_button.grid(row=0, column=1, sticky="e")
