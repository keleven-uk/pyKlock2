import flet as ft

from src.projectPaths import COLOUR_NAMES

"""
    Flet Color Picker Dialog in Python.

    Flet does not have one so I needed to make my own
    and I thought I would share.

    Author: C. Nichols <mohawke@gmail.com>
    License: WTFPL
        WTFPL — Do What the Fuck You Want to Public License

    https://www.darkartistry.com/flet-color-picker-dialog-class/

"""


class ColourPicker(ft.UserControl):

    def __init__(self, page, my_config):
        super().__init__()

        self.fColour     = my_config.FOREGROUND
        self.bColour     = my_config.BACKGROUND
        self.tarnsparent = ft.colors.TRANSPARENT
        self.MPColors    = COLOUR_NAMES
        self.page        = page
        self.my_config   = my_config

        self.rgPickColour  = ft.RadioGroup(content=ft.Row(
            [ft.Radio(value="fore", label="Foreground"),
             ft.Radio(value="back", label="Background"),
            ]), value="fore")
        self.cbTrans = ft.Checkbox(label="Transparent", value=False, on_change=self.pickedTransparent)
        self.btnDone = ft.TextButton("Done", on_click=self.closeDlg)

        colorGrid   = self.buildColourGrid()

        # Setup the Flet AlertDialog.
        self.dlg_modal = ft.AlertDialog(
            modal=False,
            title=ft.Text("Select Colour"),
            content=ft.Container(colorGrid, bgcolor="#3d2d2f", border=ft.border.all(1, ft.colors.BLUE_400), border_radius=15),
            actions=[ft.Row([self.rgPickColour,
                             self.cbTrans,
                             self.btnDone,
                            ])
                    ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            on_dismiss="",
        )

        self.page.update()

    def buildColourGrid(self):
        """
            Create a Flet GridView to house the colours and populate with a series of IconButtons
            that represent each colour.
        """

        colorGrid = ft.GridView(
                    expand=1,
                    runs_count=5,
                    max_extent=90,
                    child_aspect_ratio=1,
                    spacing=5,
                    run_spacing=5,
                    width=350,
                    height=350,
                )

        for colourName,colourHex in sorted(self.MPColors.items()):
            colorGrid.controls.append(
                ft.IconButton(
                    icon=ft.icons.WATER_DROP,
                    icon_color=colourHex,
                    icon_size=50,
                    tooltip=colourName.title(),
                    on_click=self.pickedColour,
                    data=colourHex,
                )
            )

        return colorGrid

    def pickedTransparent(self, e):

        if self.cbTrans.value:
            self.my_config.TRANSPARENT = True
        else:
            self.my_config.TRANSPARENT = False



    # COLOR PICKER
    def pickedColour(self, e):
        """
            Handle the IconButton click.
        """

        hexColour = e.control.data

        if self.rgPickColour.value == "fore":
            self.my_config.FOREGROUND = hexColour
        else:
            self.my_config.BACKGROUND  = hexColour


    def closeDlg(self, e):
        """
            Opens the dialog.
        """
        self.dlg_modal.open = False
        self.page.update()

    def openDlgModal(self, e):
        """
            Closes the dialog.
        """
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

