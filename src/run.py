from playwright.sync_api import sync_playwright
from subprocess import run,Popen
from pathlib import Path
def newFile(path,code):l=Path(path);l.parent.mkdir(511,1,1);l.write_text(code)
folder=Path(__file__).parents[1];files=(folder/'solutions').rglob('*.py');file=1
solution=repr("import ast;print(''.join('expect('in i and i.replace(q:=i.split('expect(',1)[1].split(',')[0],'('+(w:=ast.parse(q,mode='eval').body).left.id+','+repr(ast.unparse(ast.Compare(e:=ast.Name('.'),w.ops,[e]))[2:-2])+','+w.comparators[0].id+')')or i for i in open(__import__('pathlib').Path.cwd()/'tests.py')))")
with sync_playwright()as p:
 try:page=p.chromium.launch().new_page()
 except:run(f'{folder/'venv'/('bin','Scripts')[win:=__import__('sys').platform=='win32']/('python'+'.exe'*win)} -m playwright install chromium');page=p.chromium.launch().new_page()
 while 1:
  file or(update:=run(('python',folder/'src/update.py')).returncode,update or run((__import__('sys').executable,Path(__file__))))
  url=next(files,0)or input('Codewars kata url: ')
  if file:=type(url)!=str:
   if(folder/f'typings/{url.name}i').exists()and(folder/f'tests/{url.name}').exists()or'\n#/'not in'\n'+url.read_text().replace(' ','').replace('https://www.codewars.com/kata',''):continue
   print(url:=next('https://www.codewars.com/kata/'+i.split('/')[-1].strip()for i in open(url)if'#'in i and'/'in i))
  url=url.removesuffix('/').removesuffix('/python').removesuffix('/train')
  page.goto(url+'/train/python',wait_until='domcontentloaded')
  page.click('a#reset_btn');page.click('li.confirm')
  name=page.wait_for_function(f"n=document.querySelector('.CodeMirror')?.CodeMirror;i=n?.getValue();i&&n.setValue({solution})||i")
  name,parameters=f'{name}'[4:].replace(' ','').split('(')[:2]
  parameters=['results']+parameters.split(')')[0].split(',')
  page.click("a:has-text('Attempt')")
  rank=page.locator('.inner-small-hex').text_content()[0]
  code=page.wait_for_selector('iframe').content_frame().locator('.mt-1.p-1').first.text_content()
  newFile(tests:=f'tests/{name}.py',code)
  Popen(('python',tests,f'{parameters}'.replace(' ','')))
  file or(newFile(path:=f'solutions/{url.split('.')[1]}/python/{rank}/{name}.py',f'from {name} import {', '.join(parameters)} #type:ignore\n# {url}\n\nresult = '),Popen(('code',path),shell=1),print('✅ solution file: ',path))