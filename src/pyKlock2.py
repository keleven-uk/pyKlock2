###############################################################################################################
#    pyKlock2   Copyright (C) <2023>  <Kevin Scott>                                                           #                                                                                                             #    A mini klock built using flet [Flutter].                              .                                  #
#                                                                                                             #
#    Uses and builds on the example https://github.com/panos-stavrianos/flet_timer                            #
#                                                                                                             #
#    For changes see history.txt                                                                              #
#                                                                                                             #
###############################################################################################################
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

import src.selectTime as time
import src.utils.klock_utils as utils

class pyKlock2App(ft.UserControl):
    """  A class that builds pyKlock2.
         The class is called from main.py

         The page is passed in, so that the close button will work.
    """

    def __init__(self, my_config, colourPicker):
        super().__init__()
        self.my_config = my_config
        self.colourPicker = colourPicker


    def build(self):

        self.current_time   = time.SelectTime()             #  Object with the varied time codes.
        self.time_type      = self.my_config.TIME_TYPE      #  GMT Time or Local Time

        #  Create the widgets used.
        self.txt_time  = ft.Text(size=28, color="pink600", value="None")
        self.dte_time  = ft.Text(size=10, color="pink600", value="Friday 26 October 2023")
        self.sts_time  = ft.Text(size=10, color="pink600", value="csN")
        self.idl_time  = ft.Text(size=10, color="pink600", value="Idle time: 1h32s")
        self.chg_time  = ft.PopupMenuItem(icon=ft.icons.CHANGE_CIRCLE,
                                          text="Fuzzy Time",
                                          checked=True,
                                          on_click=lambda _:self.change_time())
        self.pck_clr   = ft.PopupMenuItem(icon=ft.icons.COLORIZE,
                                          text="Pick Colour",
                                          on_click=self.colourPicker.openDlgModal)
        self.btn_close = ft.PopupMenuItem(icon=ft.icons.CLOSE,
                                          text="Close",
                                          on_click=lambda _:self.close_page())


        #  Create the pop up button and add the menu items.
        self.pb = ft.PopupMenuButton(
            items=[
                self.chg_time,
                self.pck_clr,
                ft.PopupMenuItem(),      #  Divider
                self.btn_close
            ]
        )

        #  Create the page layout.
        return ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.Container(
                                    content=self.pb,
                                    alignment=ft.alignment.Alignment(-1, 1),
                                    width=40,
                                    height=self.my_config.WIN_HEIGHT-40,
                                ),
                                ft.Container(
                                    content=ft.WindowDragArea(ft.Container(self.txt_time)),
                                    alignment=ft.alignment.Alignment(0, 1),
                                    width=self.my_config.WIN_WIDTH-40,
                                    height=self.my_config.WIN_HEIGHT-40,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            controls=[self.dte_time, self.sts_time, self.idl_time], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ],
                )



    def change_time(self):
        """  Called from the pop up menu item chg_time.
             Changes the displayed time between local time and fuzzy time.
        """
        if self.time_type == "Fuzzy Time":
            self.time_type = "Local Time"
            self.txt_time.size = 120
            self.chg_time.checked = False
        else:
            self.time_type = "Fuzzy Time"
            self.txt_time.size = 30
            self.chg_time.checked = True

    def refresh(self):
        """  Called every second by the non-visual component timer [created in main.py]
             Updated the time, date, key status and idle time.
        """
        self.txt_time.value = self.current_time.getTime(self.time_type)
        self.txt_time.color = self.my_config.FOREGROUND
        self.dte_time.value = datetime.now().strftime("%A %d %B %Y")
        self.dte_time.color = self.my_config.FOREGROUND
        self.sts_time.value = utils.get_state()
        self.sts_time.color = self.my_config.FOREGROUND
        self.idl_time.value = utils.get_idle_duration()
        self.idl_time.color = self.my_config.FOREGROUND

        if self.my_config.TRANSPARENT:
            pass
        else:
            self.page.bgcolor   = self.my_config.BACKGROUND
        self.update()

    def close_page(self):
        """  Saves Klcoks screen position and then closed Klock.
        """
        self.my_config.X_POS     = self.page.window_left
        self.my_config.Y_POS     = self.page.window_top
        self.my_config.TIME_TYPE = self.time_type
        self.my_config.writeConfig()

        self.page.window_close()











