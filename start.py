from urllib.request import urlretrieve
from subprocess import run
from pathlib import Path
folder=Path.cwd();script={};venv=folder/'venv'/('bin','Scripts')[win:=__import__('sys').platform=='win32']
extension=run('code --install-extension formulahendry.code-runner',shell=1,capture_output=1,text=1).stdout
if"'.."in extension:print(extension)
 
for i in'pip','python':globals()[i]=venv/(i+'.exe'*win)
for i in'venv','update','run':script[f'src/{i}.py']=(folder/f'src/{i}.py').exists()if i!='venv'else pip.exists()and python.exists()and'playwright'in run((pip,'freeze'),capture_output=1,text=1).stdout
for n,(k,i)in enumerate(script.items()):
 i or(Path(k).parent.mkdir(511,1,1),urlretrieve('https://raw.githubusercontent.com/pokvi8/leetcode-and-codewars-in-vscode/'+'main/'*(n>0)+k,k))
 i and n<1 or run((('python',python)[n>1],k))