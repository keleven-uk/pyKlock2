# https://github.com/panos-stavrianos/flet_timer


import flet as ft

from datetime import datetime
from flet_timer.flet_timer import Timer

import src.utuls.klock_utils as utils


def main(page: ft.Page):
    page.title = "Flet Timer example"
    page.vertical_alignment   = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window_frameless = True
    page.window_height = 200
    page.window_width  = 500
    page.window_opacity = 1

    txt_time  = ft.Text(size=100, color="pink600", value="None")
    dte_time  = ft.Text(size=10, color="pink600", value="Friday 26 October 2023")
    sts_time  = ft.Text(size=10, color="pink600", value="csN")
    idl_time  = ft.Text(size=10, color="pink600", value="Idle time: 1h32s")
    close_btn = ft.ElevatedButton("CLOSE", on_click=lambda _:page.window_close())
    open_btn  = ft.ElevatedButton("OPEN",  on_click=lambda _:show_menu())

    row_time = ft.Row(
                [
                    ft.WindowDragArea(ft.Container(txt_time)),
                    ft.Column(
                        [
                            close_btn, open_btn
                        ])
                ])

    row_sts = ft.Row(
                    [dte_time, sts_time, idl_time], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )

    def show_menu():
        pass


    def refresh():
        txt_time.value = datetime.now().strftime("%H:%M:%S")
        dte_time.value = datetime.now().strftime("%A %d %B %Y")
        sts_time.value = utils.get_state()
        idl_time.value = utils.get_idle_duration()
        page.update()

    timer = Timer(name="timer", interval_s=1, callback=refresh)

    page.add(
        timer,
        row_time,
        row_sts
        )



