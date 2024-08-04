import customtkinter as ctk
from src.widgets.widget import CButton, CLabel
from src.constants.constants import Size


class AboutPage(ctk.CTkFrame):
    def __init__(
        self,
        master,
        controller,
        app_state,
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

        self.label = CLabel(master=self, text="About Page")
        self.label.pack(side=ctk.TOP)

        self.navigate_btn = CButton(
            master=self, command=lambda: controller.navigate_to("SignUpPage")
        )
        self.navigate_btn.pack()
