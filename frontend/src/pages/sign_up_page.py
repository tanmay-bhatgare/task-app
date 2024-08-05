import customtkinter as ctk
import asyncio
from PIL import Image

from src.models.models import SignUpModel
from src.services.services import sign_up

from src.widgets.widget import (
    CImage,
    CInputField,
    CFrame,
    CButton,
    CLabel,
)

from src.constants.constants import (
    Url,
    CFont,
    Size,
    Paths,
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


class SignUpPage(ctk.CTkFrame):
    #! SUBMIT FUNCTION
    def submit(self):
        username = self.username_field.get()
        email = self.email_field.get()
        password = self.password_field.get()
        c_password = self.confirm_pass_field.get()

        if password != c_password:
            print("Passwords don't match")
            raise Exception

        success_signup = asyncio.run(
            sign_up(
                url=Url.sign_up_url,
                json_data=SignUpModel(
                    username=username,
                    email=email,
                    password=password,
                ),
            )
        )
        if success_signup:
            self.controller.navigate_to("SignInPage")
        print(success_signup)

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
        self.app_state = app_state
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ? Sign Up Form
        self.form_frame = CFrame(
            master=self, width=300, height=500, fg_color="#181818", corner_radius=20
        )
        self.frame_title = CLabel(
            master=self.form_frame, text="Sign Up", font=CFont.font_large()
        )
        # ? Username field
        self.username_lbl = CLabel(
            self.form_frame, text="Username:", font=CFont.xs_field_lbl()
        )
        self.username_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40
        )
        # ? Email field
        self.email_lbl = CLabel(
            self.form_frame, text="E-mail:", font=CFont.xs_field_lbl()
        )
        self.email_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40
        )

        # ? Password field
        self.password_lbl = CLabel(
            self.form_frame, text="Password:", font=CFont.xs_field_lbl()
        )
        self.password_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40, is_password=True
        )
        self.pass_show_btn = CButton(
            master=self.form_frame,
            text="",
            bg_color="#343638",
            fg_color="#343638",
            hover_color="#343638",
            command=lambda: toggle_password(self.password_field, self.pass_show_btn),
            width=30,
            height=30,
            image=show_pass_img,
        )

        # ? Confirm Password field
        self.confirm_pass_lbl = CLabel(
            self.form_frame,
            text="Confirm Password:",
            font=CFont.xs_field_lbl(),
        )
        self.confirm_pass_field = CInputField(
            self.form_frame, font=CFont.font_small(), height=40, is_password=True
        )
        self.cpass_show_btn = CButton(
            master=self.form_frame,
            text="",
            bg_color="#343638",
            fg_color="#343638",
            hover_color="#343638",
            command=lambda: toggle_password(
                self.confirm_pass_field, self.cpass_show_btn
            ),
            width=30,
            height=30,
            image=show_pass_img,
        )

        # ? navigating label
        self.navigate_label = CLabel(
            master=self.form_frame,
            text="Already have an account? Sign in",
            font=CFont.xs_field_lbl(),
            text_color="#00ffff",
        )

        # ? Submit Button
        self.submit_btn = CButton(
            master=self.form_frame,
            text="Sign Up",
            bg_color="transparent",
            fg_color="#ffffff",
            hover_color="#acacac",
            command=self.submit,
            width=100,
            height=30,
        )

        # @ Packing
        self.form_frame.pack_propagate(False)
        self.form_frame.grid(row=0, column=0)

        self.frame_title.pack(fill="x", pady=15, padx=2)

        # ? Fields
        self.username_field.pack(fill="x", padx=10, pady=20)
        self.email_field.pack(fill="x", padx=10, pady=20)
        self.password_field.pack(fill="x", padx=10, pady=20)
        self.confirm_pass_field.pack(fill="x", padx=10, pady=20)
        self.navigate_label.pack(fill="x", pady=5, padx=10)
        self.submit_btn.pack(pady=10, padx=10)

        # ? Fields labels
        self.username_lbl.place(x=15, y=70)
        self.email_lbl.place(x=15, y=150)
        self.password_lbl.place(x=15, y=230)
        self.confirm_pass_lbl.place(x=15, y=310)

        # ? Show Buttons
        self.pass_show_btn.place(x=248, y=256)
        self.cpass_show_btn.place(x=248, y=336)
        self.navigate_label.bind(
            "<Button-1>", command=lambda x: self.controller.navigate_to("SignInPage")
        )
