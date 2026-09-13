from urllib.request import urlopen,urlretrieve
from pathlib import Path
from json import dump,loads
def dbJson(n='',i={}):Path(n:=f'{n}.json').exists()and(i:=open(n));dict==type(i)or(i:=loads(i.read()));return type('',(type(i),),{'__call__':lambda s:dump(s,open(n,'w'),ensure_ascii=0,indent=1,separators=',:')})(i)
folder=Path(__file__).parents[1];run=1
branch='main';repo='/pokvi8/leetcode-and-codewars-in-vscode/'
url=f'https://api.github.com/repos{repo}git/trees/{branch}?recursive='
data=dbJson(i=urlopen(url))['tree']
version=dbJson(folder/'src/version')
url='https://raw.githubusercontent.com'+repo+branch+'/'
tree=[(i['path'],i['sha'])for i in data if'blob'==i['type']and'.github'not in i['path']]
for path,sha in tree:
 if(update:=version.get(path,''))!=sha:
  (file:=folder/path).parent.mkdir(511,1,1)
  urlretrieve(url+path,file)
  print(('update ','download ')[update=='']+path)
  version[path]=sha;version();run and(run:=file.name!='run.py')
tree=[i[0]for i in tree]
for i in[*version]:
 if i not in tree:
  file=Path(i);file.exists()and file.unlink()
  version.pop(i);version()
exit(run)