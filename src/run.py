from playwright.sync_api import sync_playwright
from pathlib import Path
def newFile(name,code):l=Path(name);l.parent.mkdir(511,1,1);l.write_text(code)
def on_response(i):i.url=='https://runner.codewars.com/run'and results.update(i.json())
folder=Path(__file__).parents[1];files=(folder/'solutions').rglob('*.py')
with sync_playwright()as p:
 try:page=p.chromium.launch().new_page()
 except:__import__('subprocess').run((folder/'venv'/('bin','Scripts')[win:=__import__('sys').platform=='win32']/('python'+'.exe'*win),'-m playwright install chromium'));page=p.chromium.launch().new_page()
 while 1:
  url=next(files,0)or input('Enter url Codewars kata: ')
  if file:=type(url)!=str:
   if(folder/f'typings/{url.name}i').exists()or'\n#'not in'\n'+url.read_text():continue
   for i in open(url):
    if'#'in i and'/'in i:url='https://www.codewars.com/kata/'+i.split('/')[-1].strip();break
  url=url.removesuffix('/').removesuffix('/python').removesuffix('/train')
  page.goto(url+'/train/python')
  name=page.wait_for_function("n=document.querySelector('.CodeMirror')?.CodeMirror;i=n?.getValue();i&&n.setValue(i.split('(')[0]+'(*_):print(_)')||i",timeout=9e3)
  page.locator("a:has-text('Attempt')").click()
  results={}
  page.on('response',on_response)
  while{}==results:page.wait_for_timeout(1)
  rank=page.locator('.inner-small-hex').text_content()[0]
  name,parameters=f'{name}'[4:].replace(' ','').split('(')[:2]
  parameters=['results']+parameters.split(')')[0].split(',')
  results=iter(e['v']for q in results['result']['output']for w in q['items']for e in w.get('items',())[:-1])
  results=[eval((print(i),print(f'({i.split('equal ')[1]},*{n})','\n'+'*'*99),f'({i.split('equal ')[1]},*{n})')[2])for n,i in zip(results,results)]
  pyi='\n'.join(i+f':Literal[{','.join((f'{(a:=z[n])}',f'"""{a}"""')[str==type(a)]for z in results)}]'for n,i in enumerate(parameters))
  newFile(f'typings/{name}.pyi','from typing import Literal\n'+pyi)
  file or newFile(f'solutions/{url.split('.')[1]}/{url.split('/')[-1]}/{rank}/{name}.py',f'from {name} import {', '.join(parameters)} #type:ignore\n# {url}\n\nresult = ')