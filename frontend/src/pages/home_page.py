import asyncio
from typing import Dict, NoReturn, Optional
import customtkinter as ctk

from src.app_state import AppState

from src.utils.utils import format_to_date
from src.services.services import get_all_tasks

from src.widgets.widget import (
    CButton,
    CLabel,
    CSeperator,
    CTaskCard,
    CScrollableFrame,
)

from src.constants.constants import (
    CFont,
    Pages,
    Size,
)


class HomePage(ctk.CTkFrame):
    def update_task_btn_func(self, task_id):
        self.app_state.update_task_id = task_id
        self.controller.navigate_to(Pages.update_task_page)

    def __init__(
        self,
        master,
        controller,
        app_state: AppState,
        width=Size.window_size[0],
        height=Size.window_size[1],
        fg_color=None,
    ) -> None:
        super().__init__(master=master, width=width, height=height, fg_color=fg_color)

        self.controller = controller
        self.app_state = app_state

        self.main_frame = CScrollableFrame(
            master=self,
            width=width,
            height=height,
            fg_color="#101010",
        )
        self.create_task_btn = CButton(
            self.main_frame,
            width=30,
            height=35,
            command=lambda: self.controller.navigate_to(Pages.create_task_page),
            text="+",
            text_color="white",
            fg_color="#2864f0",
            font=CFont.font_btn_sm(),
            hover_color="#0d43bf",
            corner_radius=50,
        )
        self.create_task_btn.place(x=310, y=550)

        self.main_frame.pack(fill="both", expand=True)

    def load_tasks(self) -> NoReturn:
        if self.app_state.get_access_token() is not None:
            self.current_tasks = self.fetch_tasks()
            if self.current_tasks:
                self.initialize_task_cards()
            else:
                CLabel(self.main_frame.canvas, text="No Tasks Found!").pack(
                    fill="both", expand=True
                )

    def fetch_tasks(self) -> Optional[Dict]:
        try:
            tasks = asyncio.run(get_all_tasks(self.app_state.get_access_token()))
            return tasks
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            return None

    def initialize_task_cards(self):
        # Clear previous task cards
        for widget in self.main_frame.scrollable_frame.winfo_children():
            widget.destroy()

        # Create new task cards
        for task in self.current_tasks:
            task_id = task["id"]
            self.cards = CTaskCard(
                master=self.main_frame.scrollable_frame,
                height=250,
                width=Size.window_size[0],
                fg_color="#191919",
                card_title=f"{task['title']}",
                card_description=f"{task['description']}",
                task_id=task_id,
                created_at=format_to_date(task["created_at"]),
                update_command=lambda task_id=task_id: self.update_task_btn_func(
                    task_id=task_id
                ),
                delete_command=lambda task_id=task_id: print(f"Delete task {task_id}"),
            )
            self.cards.pack(fill="x", pady=2, padx=3)
            CSeperator(self.main_frame.scrollable_frame, seperation=10)
