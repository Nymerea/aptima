from cx_Freeze import setup, Executable

base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "pynput", "logging", "mss.tools", "time", "tkinter", "cv2", "numpy", "threading"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="Mon Programme",
    options=options,
    version="1.0",
    description='Voici mon programme',
    executables=executables
)
