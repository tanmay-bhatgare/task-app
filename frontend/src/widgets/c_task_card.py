from datetime import datetime
from typing import Any, Callable, Tuple
import customtkinter as ctk

from src.widgets.widget import (
    CSeperator,
    CButton,
    CFrame,
    CLabel,
)
from src.constants.constants import CFont


class CTaskCard(ctk.CTkFrame):
    def __init__(
        self,
        master: Any,
        update_command: Callable,
        delete_command: Callable,
        width: int = 200,
        height: int = 220,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        card_title: str = "",
        card_description: str = "",
        task_id: int = None,
        created_at: datetime = None,
        is_completed: bool | None = None,
        due_date: datetime | None = None,
        completed_at: datetime | None = None,
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            fg_color=fg_color,
            border_color=border_color,
        )

        self.pack_propagate(False)
        self.button_frame = CFrame(master=self, fg_color="transparent")

        self.card_title = CLabel(
            master=self,
            text=card_title,
            bg_color="transparent",
            text_color="white",
            font=CFont.font_small(),
        )
        self.card_description = ctk.CTkTextbox(
            master=self,
            state="normal",
            height=100,
            fg_color="transparent",
            border_width=1.5,
            corner_radius=3,
            border_color="#191919",
            font=CFont.xs_field_lbl(),
            wrap="word",
        )
        self.card_description.insert(ctk.END, card_description)
        self.card_description.configure(state="disabled")

        self.due_date = CLabel(
            master=self,
            text=f"Due: {due_date}",
            bg_color="transparent",
            text_color="white",
            font=CFont.font_sm_text(),
        )
        self.created_at = CLabel(
            master=self,
            text=f"Created At: {created_at}",
            bg_color="transparent",
            text_color="white",
            font=CFont.font_sm_text(),
        )

        self.update_button = CButton(
            self.button_frame,
            command=update_command,
            text="Update Task",
            text_color="white",
            fg_color="#8080ff",
            font=CFont.font_btn_sm(),
            hover_color="#5b5bff",
        )
        self.delete_button = CButton(
            self.button_frame,
            command=delete_command,
            text="Delete Task",
            text_color="white",
            fg_color="#ff0000",
            font=CFont.font_btn_sm(),
            hover_color="#e60000",
        )

        # ? Packing
        self.card_title.pack(anchor=ctk.W, padx=4, pady=4)
        CSeperator(master=self)

        self.card_description.pack(fill="x", padx=8, anchor=ctk.W)
        CSeperator(master=self)

        self.due_date.place(x=220, y=5)
        self.created_at.pack(anchor=ctk.E, padx=10)

        # ? Button Packing
        CSeperator(master=self)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.pack(side="bottom", fill="x", padx=4, pady=4)

        # Place the buttons in the grid
        self.delete_button.grid(row=0, column=0, sticky="w")
        self.update_button.grid(row=0, column=1, sticky="e")
