import asyncio
import customtkinter as ctk

from src.app_state import AppState

from src.models.models import TaskCreateModel

from src.services.services import create_task
from src.utils.utils import convert_date_to_json, format_to_date

from src.widgets.widget import (
    CButton,
    CCalendar,
    CInputField,
    CLabel,
    CSeperator,
    CFrame,
)

from src.constants.constants import (
    CFont,
    Size,
    Url,
    Pages,
)


class CreateTaskPage(ctk.CTkFrame):
    @staticmethod
    def are_values_empty(title: str, description: str) -> bool:
        if (
            title.replace(" ", "") == ""
            or description.replace("\n", "").replace(" ", "") == ""
        ):
            return True

    @staticmethod
    def show_calendar(calendar, x, y):
        calendar.place(x=x, y=y)
        calendar.lift()

    def config_due_btn(self):
        try:
            due_date = convert_date_to_json(self.due_calender.selected_date)
            self.due_cal_btn.configure(text=f"Due Date: {format_to_date(due_date)}")
        except Exception as e:
            print(f"Can't Convert To Date: {e}")
            due_date = None

    def create_task_on_submit(self):
        try:
            due_date = convert_date_to_json(self.due_calender.selected_date)
        except Exception as e:
            print(f"Can't Convert To Date: {e}")
            due_date = None

        title = self.title.get()
        description = self.description.get(1.0, ctk.END)
        is_private = self.is_private_swt.get()

        if self.are_values_empty(title=title, description=description):
            raise ValueError("Title or Description Cannot Be Empty.")

        is_task_created: bool = asyncio.run(
            create_task(
                url=Url.create_task_url,
                token=self.app_state.get_access_token(),
                json_data=TaskCreateModel(
                    title=title,
                    description=description,
                    due_date=due_date,
                    is_private=is_private,
                ),
            )
        )
        if is_task_created:
            self.controller.frames[Pages.home_page].load_tasks()
            self.controller.navigate_to(Pages.home_page)

    def __init__(
        self,
        master,
        controller,
        app_state: AppState,
        width=Size.window_size[0],
        height=Size.window_size[1],
        fg_color=None,
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            fg_color=fg_color,
        )
        self.controller = controller
        self.app_state: AppState = app_state
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.card_frame = CFrame(
            master=self, width=320, height=550, fg_color="#181818", corner_radius=20
        )

        self.frame_title = CLabel(
            master=self.card_frame, font=CFont.font_large(), text="Create Task"
        )

        self.due_calender = CCalendar(
            master=self.card_frame, custom_cmd=self.config_due_btn
        )

        self.title_lbl = CLabel(
            master=self.card_frame, text="Title:", font=CFont.xs_field_lbl()
        )
        self.title = CInputField(master=self.card_frame, font=CFont.font_med())

        self.description_lbl = CLabel(
            master=self.card_frame, text="Description:", font=CFont.xs_field_lbl()
        )
        self.description = ctk.CTkTextbox(self.card_frame, height=150, border_width=2)
        self.due_cal_btn = CButton(
            master=self.card_frame,
            command=lambda: self.show_calendar(self.due_calender, 20, 100),
            text="Due Date",
        )
        self.is_private_lbl = CLabel(
            self.card_frame, text="Private: ", font=CFont.font_small()
        )
        self.is_private_swt = ctk.CTkSwitch(
            self.card_frame,
            text="",
            progress_color="#ff0080",
            onvalue=True,
            offvalue=False,
            command=None,
        )

        self.submit_button = CButton(
            self.card_frame,
            command=self.create_task_on_submit,
            text="Create",
            text_color="white",
            fg_color="#8080ff",
            font=CFont.font_btn_sm(size=24),
            hover_color="#7070df",
        )

        # ? all widgtes packing
        self.card_frame.pack_propagate(False)
        self.card_frame.grid(row=0, column=0)

        CSeperator(master=self.card_frame, color="transparent", padx=30)
        self.frame_title.pack()

        CSeperator(self.card_frame, color="transparent", seperation=20)
        self.title_lbl.place(x=10, y=65)
        self.title.pack(fill="x", padx=5)

        CSeperator(self.card_frame, color="transparent", seperation=20)
        self.description_lbl.place(x=10, y=145)
        self.description.pack(fill="x", padx=5)

        CSeperator(self.card_frame, color="transparent", seperation=5)
        self.due_cal_btn.pack(anchor=ctk.W, padx=10)

        CSeperator(self.card_frame, color="transparent", seperation=10)
        self.is_private_lbl.pack(anchor=ctk.W, padx=10)
        self.is_private_swt.pack(anchor=ctk.W, padx=10)

        CSeperator(master=self.card_frame, color="transparent", seperation=20)
        self.submit_button.pack()
