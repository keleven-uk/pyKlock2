###############################################################################################################
#    pyKlock2   Copyright (C) <2023>  <Kevin Scott>                                                           #
#                                                                                                             #
#    The Klock displays the time [local], date, key status  and the computers idle time.                      #
#       Key status is the status of Caps Lock, Scroll lock and Num lock.                                      #
#    The time can be displayed in numbers [00:00:00] or in fuzzy time.                                        #
#       Fuzzy time is the time in words rounded to the nearest five minutes.                                  #
#       i.e  twenty past nine in the evening or quarter to six in the morning.                                #
#                                                                                                             #
#    The Klock is moved by dragging the displayed time.                                                       #
#                                                                                                             #
#    The Klock currently has a transparent background.                                                        #
#                                                                                                             #
#    To install dependencies pip install -r requirements.txt                                                  #
#                                                                                                             #
#    For changes see history.txt                                                                              #
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

import platform

import flet as ft
from flet_timer.flet_timer import Timer

from src.pyKlock2 import pyKlock2App

import src.config as Config
import src.logger as Logger

from src.projectPaths import LOGGER_PATH, CONFIG_PATH

############################################################################################### __main__ ######

if __name__ == "__main__":

    my_logger  = Logger.get_logger(str(LOGGER_PATH))    # Create the logger.

    my_logger.info("-" * 100)

    my_config  = Config.Config(CONFIG_PATH, my_logger)  # Create the config.

    my_logger.info(f"  Running {my_config.NAME} Version {my_config.VERSION} ")
    my_logger.debug(f" {platform.uname()}")
    my_logger.debug(f" Python Version {platform.python_version()}")
    my_logger.debug("")

    my_logger.info(f"  Config path {CONFIG_PATH}")
    my_logger.info(f"  Logger path {LOGGER_PATH}")

    def main(page: ft.Page):

        page.title = "pyKlock2 [flet]"

        page.vertical_alignment   = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window_always_on_top = True

        if my_config.TRANSPARENT:
            page.window_title_bar_buttons_hidden = True
            page.window_title_bar_hidden         = True
            page.window_frameless                = True
            page.window_opacity                  = 1
            page.window_bgcolor                  = ft.colors.TRANSPARENT
            page.bgcolor                         = ft.colors.TRANSPARENT
            page.fgcolor                         = my_config.FOREGROUND
        else:
            page.window_bgcolor                  = my_config.BACKGROUND
            page.bgcolor                         = my_config.BACKGROUND
            page.fgcolor                         = my_config.FOREGROUND

        page.window_height = my_config.WIN_HEIGHT
        page.window_width  = my_config.WIN_WIDTH
        page.window_left   = my_config.X_POS
        page.window_top    = my_config.Y_POS

        page.update()

        # create application instance
        pyKlock2 = pyKlock2App(my_config)

        #  Create the non-visual component timer.
        timer = Timer(name="timer", interval_s=1, callback=pyKlock2.refresh)

        # add the non-visual component timer to the page.
        page.add(pyKlock2, timer)


    ft.app(target=main)


    my_logger.info(f"  Ending {my_config.NAME} Version {my_config.VERSION} ")
    my_logger.info("=" * 100)
