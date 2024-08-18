import customtkinter as ctk
from PIL import Image
import asyncio

from src.app_state import AppState

from src.models.models import SignInModel

from src.services.services import sign_in

from src.widgets.widget import (
    CImage,
    CInputField,
    CFrame,
    CButton,
    CLabel,
)

from src.constants.constants import (
    Url,
    Pages,
    CFont,
    Paths,
    Size,
)

# ? image data
show_pass_data = Image.open(f"{Paths.assets_path}\\images\\view.png")
hide_pass_data = Image.open(f"{Paths.assets_path}\\images\\hide.png")

# ? actual images
show_pass_img = CImage(dark_image=show_pass_data, size=(20, 20))
hide_pass_img = CImage(dark_image=hide_pass_data, size=(20, 20))


def toggle_password(widget: CInputField, button: CButton) -> None:
    widget.toggle_password()
    widget.configure()

    if widget.is_password:
        button.configure(image=show_pass_img)
    else:
        button.configure(image=hide_pass_img)


class SignInPage(ctk.CTkFrame):
    def submit(self):
        email = self.email_field.get()
        password = self.password_field.get()
        try:
            result, is_success = asyncio.run(
                sign_in(
                    url=Url.sign_in_url,
                    data=SignInModel(
                        username=email,
                        password=password,
                    ),
                )
            )
            if is_success:
                token = result["access_token"]
                self.app_state.set_access_token(token)
                self.controller.navigate_to(Pages.home_page)
                self.controller.frames[Pages.home_page].load_tasks()
            else:
                print(result)

        except TypeError as e:
            print("Invalid Response:", e)
        except Exception as e:
            print("Error:", e)

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
        self.app_state = app_state
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ? Sign Up Form
        self.form_frame = CFrame(
            master=self, width=300, height=360, fg_color="#181818", corner_radius=20
        )
        self.frame_title = CLabel(
            master=self.form_frame, text="Sign In", font=CFont.font_large()
        )
        # ? Email field
        self.email_lbl = CLabel(
            self.form_frame, text="E-mail:", font=CFont.xs_field_lbl()
        )
        self.email_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40
        )
        self.email_field.insert(ctk.END, "t4@g.com") #! |||||||||||||||||||||||||||||

        # ? Password field
        self.password_lbl = CLabel(
            self.form_frame, text="Password:", font=CFont.xs_field_lbl()
        )
        self.password_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40, is_password=True
        )
        self.password_field.insert(ctk.END, "12") #! |||||||||||||||||||||||||||||
        self.pass_show_btn = CButton(
            master=self.form_frame,
            text="",
            bg_color="#343638",
            fg_color="#343638",
            hover_color="#343638",
            width=30,
            height=30,
            image=show_pass_img,
            command=lambda: toggle_password(self.password_field, self.pass_show_btn),
        )
        # ? navigating label
        self.navigate_label = CLabel(
            master=self.form_frame,
            text="Don't have an account? Sign up",
            font=CFont.xs_field_lbl(),
            text_color="#00ffff",
        )

        # ? Submit Button
        self.submit_btn = CButton(
            master=self.form_frame,
            text="Log In",
            bg_color="transparent",
            fg_color="#ffffff",
            hover_color="#acacac",
            width=100,
            height=30,
            font=CFont.font_btn(),
            command=self.submit,
        )

        # @ Packing
        self.form_frame.pack_propagate(False)
        self.form_frame.grid(row=0, column=0)

        self.frame_title.pack(fill="x", pady=15, padx=2)

        # ? Fields
        self.email_field.pack(fill="x", padx=10, pady=20)
        self.password_field.pack(fill="x", padx=10, pady=20)
        self.navigate_label.pack(fill="x", pady=5, padx=10)
        self.submit_btn.pack(pady=10, padx=10)

        # ? Fields labels
        self.email_lbl.place(x=15, y=67)
        self.password_lbl.place(x=15, y=147)

        # ? Show Buttons
        self.pass_show_btn.place(x=248, y=177)
        self.navigate_label.bind(
            "<Button-1>",
            command=lambda x: self.controller.navigate_to(Pages.sign_up_page),
        )
