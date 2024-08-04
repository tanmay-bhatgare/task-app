import customtkinter as ctk
from tkcalendar import Calendar


class CCalendar(ctk.CTkFrame):
    def __init__(self, master=None, custom_cmd=None, **kwargs):
        super().__init__(master, **kwargs)
        self.calendar = Calendar(self)
        self.calendar.pack(pady=10, padx=10)
        self.selected_date = None
        self.custom_cmd = custom_cmd

        # Adding a button to close the calendar and get the selected date
        self.select_button = ctk.CTkButton(
            self, text="Done!", command=self.get_date, width=70
        )
        self.select_button.pack(pady=10)

    def get_date(self):
        self.selected_date = self.calendar.get_date()
        if self.custom_cmd:
            self.custom_cmd()
        self.place_forget()  # This hides the frame, you can change this behavior as needed

    def place(self, **kwargs):
        super().place(**kwargs)

    def get_selected_date(self):
        return self.selected_date


# # Example usage in a main application window
# if __name__ == "__main__":
#     root = ctk.CTk()

#     def show_calendar():
#         calendar_frame.place(x=50, y=50)

#     calendar_frame = CCalendar(root)

#     show_calendar_button = ctk.CTkButton(
#         root, text="Show Calendar", command=show_calendar
#     )
#     show_calendar_button.place(x=20, y=20)
#     ctk.CTkButton(
#         root, command=lambda: print("sdjsdjsbdsjbdsjds", calendar_frame.selected_date)
#     ).pack()

#     root.mainloop()
