import flet as ft
from flet_timer.flet_timer import Timer

from src.pyKlock2 import pyKlock2App
from src.colourPicker import ColourPicker

def main(page: ft.Page):

    #  Create the non-visual component timer.
    timer = Timer(name="timer", interval_s=1)

    # add the non-visual component timer to the page.
    page.add(timer)


    colourPicker = ColourPicker(page)

    def change_route(route):

        page.views.clear()  # CLEAR THE VIEWS

        page.window_height = 200
        page.window_width  = 550
        page.views.append(  # BUILD THE VIEW 1

            ft.View(
                route='/',
                controls=[
                    ft.ElevatedButton("Choose Colour", on_click=lambda _: page.go("/colourChooser")),
                ]
            )
        )

        if page.route == "/colourChooser":
            page.window_height = 450
            page.window_width  = 390
            page.views.append(  # BUILD THE VIEW 2
                ft.View(
                    route='/colourChooser',
                    controls=[colourPicker
                    ]
                )
            )

        page.update()

    page.on_route_change = change_route
    page.go(page.route)

ft.app(target=main)
