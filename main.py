###############################################################################################################
#    pyKlock2   Copyright (C) <2023>  <Kevin Scott>                                                           #                                                                                                             #    A mini klock built using flet [Flutter].                              .                                  #
#                                                                                                             #
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

import flet as ft
from flet_timer.flet_timer import Timer

from src.pyKlock2 import pyKlock2App

############################################################################################### __main__ ######

if __name__ == "__main__":

    def main(page: ft.Page):
        page.title = "Flet Timer example"

        page.vertical_alignment   = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.window_title_bar_buttons_hidden = True
        page.window_title_bar_hidden = True

        page.window_bgcolor = ft.colors.TRANSPARENT
        page.bgcolor = ft.colors.TRANSPARENT
        page.window_frameless = True
        page.window_opacity = 1

        page.window_height = 200
        page.window_width  = 500

        page.update()

        # create application instance
        pyKlock2 = pyKlock2App(page)

        timer = Timer(name="timer", interval_s=1, callback=pyKlock2.refresh)

        # add application's root control to the page
        page.add(pyKlock2, timer)



    ft.app(target=main)
