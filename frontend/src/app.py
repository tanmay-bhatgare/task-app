from typing import Dict
import customtkinter as ctk

from src.app_state import AppState
from src.constants.constants import Pages

from src.pages.pages import (
    HomePage,
    AboutPage,
    SignUpPage,
    SignInPage,
    CreateTaskPage,
    UpdateTaskPage,
    ErrorPage,
)


class App(ctk.CTk):
    def __init__(
        self,
        title: str = "App",
        width: int = 400,
        height: int = 500,
        resizable: bool = True,
    ) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ? App state for token
        self.app_state: AppState = AppState()

        self.frames: Dict[str, ctk.CTkFrame] = {}
        for F in (
            HomePage,
            AboutPage,
            SignUpPage,
            SignInPage,
            CreateTaskPage,
            UpdateTaskPage,
            ErrorPage,
        ):
            page_name: str = F.__name__
            frame: ctk.CTkFrame = F(
                master=self, controller=self, app_state=self.app_state
            )
            self.frames[page_name] = frame
            frame.grid(column=0, row=0, sticky=ctk.NSEW)

        if self.app_state.get_access_token() is None:
            self.navigate_to(Pages.sign_in_page)
        else:
            self.navigate_to(Pages.home_page)

    def navigate_to(self, page_name: str):
        try:
            frame: ctk.CTkFrame = self.frames[page_name]
            frame.tkraise()
        except KeyError:
            self.navigate_to(page_name=Pages.error_page)  #! DON'T EVER MESS WITH THIS
            print(f"Error: The page with name, '{page_name}' does not exist.")
