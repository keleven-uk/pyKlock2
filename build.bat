@rem
@rem    build.bat   Copyright (C) <2023>  <Kevin Scott>
@rem
@rem    Builds pyKlock2 as a stand alone executable using the flet network.
@rem
@rem    For changes see history.txt
@rem
@rem
@rem
@rem    This program is free software: you can redistribute it and/or modify it under the terms of the
@rem    GNU General Public License as published by the Free Software Foundation, either Version 3 of the
@rem    License, or (at your option) any later Version.
@rem
@rem    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
@rem    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
@rem    GNU General Public License for more details.
@rem
@rem    You should have received a copy of the GNU General Public License along with this program.
@rem    If not, see <http://www.gnu.org/licenses/>.
@rem
@rem    ^ is line continuation, remember that the caret and the newline following it are completely removed.
@rem    So, if there should be a space where you're breaking the line, include a space.

flet pack main.py^
 --name pyklock2^
 --icon resources\tea.ico^
 --product-name "pyKlock2"^
 --product-version "2023.4"^
 --file-version "2023.4"^
 --file-description "A mini klock built using flet [Flutter]."^
 --copyright "Copyright (C) <2023>  <Kevin Scott>"

