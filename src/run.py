from playwright.sync_api import sync_playwright
from subprocess import run
from pathlib import Path
def newFile(path,code):l=Path(path);l.parent.mkdir(511,1,1);l.write_text(code)
def on_response(i):i.url=='https://runner.codewars.com/run'and data.update(i.json())
folder=Path(__file__).parents[1];files=(folder/'solutions').rglob('*.py');file=1
with sync_playwright()as p:
 try:page=p.chromium.launch().new_page()
 except:run(f'{folder/'venv'/('bin','Scripts')[win:=__import__('sys').platform=='win32']/('python'+'.exe'*win)} -m playwright install chromium');page=p.chromium.launch().new_page()
 while 1:
  file or(update:=run(('python',folder/'src/update.py')).returncode,update or run((__import__('sys').executable,Path(__file__))))
  url=next(files,0)or input('Codewars kata url: ')
  if file:=type(url)!=str:
   if(folder/f'typings/{url.name}i').exists()or'\n#/'not in'\n'+url.read_text().replace(' ','').replace('https://www.codewars.com/kata',''):continue
   for i in open(url):
    if'#'in i and'/'in i:url='https://www.codewars.com/kata/'+i.split('/')[-1].strip();print(url);break
  url=url.removesuffix('/').removesuffix('/python').removesuffix('/train')
  page.goto(url+'/train/python')
  page.click('a#reset_btn');page.click('li.confirm')
  name=page.wait_for_function("n=document.querySelector('.CodeMirror')?.CodeMirror;i=n?.getValue();i&&n.setValue(i.split('(')[0]+'(*_):print(_)')||i",timeout=9e3)
  data={};page.click("a:has-text('Attempt')")
  page.on('response',on_response)
  while{}==data:page.wait_for_timeout(1)
  rank=page.locator('.inner-small-hex').text_content()[0]
  name,parameters=f'{name}'[4:].replace(' ','').split('(')[:2]
  parameters=['results']+parameters.split(')')[0].replace('*','').split(',')
  results=[v for n in data['result']['output']for i in n['items']for v in i.get('items',())[:-1]]
  parameter=sum((n['v'][:-1].split('\n')for n in results if'log'==n['t']),[])
  results=(i['v'].split('equal ')[1]for i in results if'log'!=i['t'])
  results=[eval(f'({i},*{n})')for n,i in zip(parameter,results)]
  pyi='\n'.join(i+f':Literal[{','.join(repr(v[n])for v in results)}]'for n,i in enumerate(parameters))
  newFile(f'typings/{name}.pyi','from typing import Literal\n'+pyi)
  file or newFile(path:=f'solutions/{url.split('.')[1]}/python/{rank}/{name}.py',f'from {name} import {', '.join(parameters)} #type:ignore\n# {url}\n\nresult = ')
  file or(run(('code',path),shell=1),print('✅ solution file: ',path))