from urllib.request import urlopen,urlretrieve
from pathlib import Path
from json import dump,loads
def dbJson(n='',i={}):Path(n:=n+'.json').exists()and(i:=open(n));dict==type(i)or(i:=loads(i.read()));return type('',(type(i),),{'__call__':lambda s:dump(s,open(n,'w'),ensure_ascii=0,indent=1,separators=',:')})(i)
folder=Path(__file__).parents[1]
branch='main';repo='/pokvi8/leetcode-and-codewars-in-vscode/'
url=f'https://api.github.com/repos{repo}git/trees/{branch}?recursive='
data=dbJson(i=urlopen(url))['tree']
version=dbJson(folder/'src/version')
url='https://raw.githubusercontent.com'+repo+branch+'/'
for path,sha in((i['path'],i['sha'])for i in data if'blob'==i['type']and'.github'not in i['path']):
 if(update:=version.get(path,''))!=sha:
  (file:=folder/path).parent.mkdir(511,1,1)
  urlretrieve(url+path,file)
  print(('update ','download ')[update=='']+path)
  version[path]=sha;version()