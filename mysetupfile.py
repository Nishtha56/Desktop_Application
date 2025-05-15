import sys, os
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY']='tcl\\tcl8.6'
os.environ['TK_LIBRARY']='tcl\\tk8.6'

build_exe_options={"packages": ["os","tkinter","babel.numbers"], "include_files": ['tcl86t.dll','tk86t.dll']}

base=None
if sys.platform=='win32':
    base="Win32GUI"

setup(name='Hotel Manager',version="1.0",description="hotel_manager",
      options={"build_exe": build_exe_options},executables=[Executable('HotelManager.py',base=base)])