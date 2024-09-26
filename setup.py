import cx_Freeze
import sys
import os 
base = None
import skimage.filters.edges

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name="Facial Recognition Software",
    options={"build_exe": {"packages": ["tkinter", "os", "skimage"],
                           "include_files": ["face.ico", 'tcl86t.dll', 'tk86t.dll', 'collect_pic', 'data', 'database', 'attendance_report'],
                           "excludes": ["tkinter.test", "tkinter.tkpath"]}},
    version="1.0",
    description="Face Recognition Automatic Attendance System | Developed By Md.Ashikur Rahman",
    executables=executables
)
