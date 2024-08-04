from src.constants.constants import Size
from src.app import App


def main():
    app: App = App(
        title="Task Manager",
        resizable=False,
        width=Size.window_size[0],
        height=Size.window_size[1],
    )
    app.mainloop()


if __name__ == "__main__":
    main()
