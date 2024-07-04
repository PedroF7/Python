import subprocess

ChormeOpen = r'C:\WINDOWS\system32\cmd.exe'
vscodeOpen = r'D:\Microsoft VS Code\Code.exe'

subprocess.run('start cmd /k"color a && dir/s"', shell=True)