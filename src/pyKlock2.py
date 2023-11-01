###############################################################################################################
#    pyKlock2   Copyright (C) <2023>  <Kevin Scott>                                                           #                                                                                                             #    A mini klock built using flet [Flutter].                              .                                  #
#                                                                                                             #
#    Uses and builds on the example https://github.com/panos-stavrianos/flet_timer                            #
#                                                                                                             #
#     For changes see history.txt                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2021-23>  <Kevin Scott>                                                                   #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################


from datetime import datetime

import flet as ft

import src.utils.klock_utils as utils


class pyKlock2App(ft.UserControl):

    def __init(page):
        self.page = page

    def build(self):

        self.txt_time  = ft.Text(size=100, color="pink600", value="None")
        self.dte_time  = ft.Text(size=10, color="pink600", value="Friday 26 October 2023")
        self.sts_time  = ft.Text(size=10, color="pink600", value="csN")
        self.idl_time  = ft.Text(size=10, color="pink600", value="Idle time: 1h32s")
        self.close_btn = ft.ElevatedButton("CLOSE", on_click=lambda _:self.page.window_close())
        self.open_btn  = ft.ElevatedButton("OPEN",  on_click=lambda _:self.show_menu())

        return ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.WindowDragArea(ft.Container(self.txt_time)),
                                ft.Column(
                                    [self.close_btn, self.open_btn]
                                    )
                                ]
                        ),
                        ft.Row(
                            controls=[self.dte_time, self.sts_time, self.idl_time], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                    )

    def show_menu(self):
        print("show_menu")

    def refresh(self):
        self.txt_time.value = datetime.now().strftime("%H:%M:%S")
        self.dte_time.value = datetime.now().strftime("%A %d %B %Y")
        self.sts_time.value = utils.get_state()
        self.idl_time.value = utils.get_idle_duration()
        self.update()










