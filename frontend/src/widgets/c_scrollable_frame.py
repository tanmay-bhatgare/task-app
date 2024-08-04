import customtkinter as ctk


class CScrollableFrame(ctk.CTkFrame):
    def __init__(self, master, width, height, fg_color):
        super().__init__(master, width=width, height=height, fg_color=fg_color)

        self.canvas = ctk.CTkCanvas(
            self, borderwidth=0, highlightthickness=0, bg="#191919"
        )
        self.scrollable_frame = ctk.CTkFrame(
            self.canvas,
            fg_color=fg_color
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.bind_events()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def bind_events(self):
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
