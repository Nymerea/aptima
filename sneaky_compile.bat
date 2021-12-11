:: arg1 image path used as icon
:: arg2 file path used as encapsulated datas
python img_to_ico.py %1 
python encapsulator.py %2 main.py
pyinstaller --clean --onefile --noconsole --icon=icon.ico   %2.py
