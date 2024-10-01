import flet as ft


def main(page: ft.Page):
    page.title = "Notebook"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def btn_onclick(e):
        print("Here's a secret message :-)")
        page.update()

    page.add(
        ft.Row(
            [
                ft.Text("Hello World!"),
                ft.IconButton("rocket", "red", on_click=btn_onclick),
            ]
        )
    )


ft.app(main)
