import warnings,pathlib,sys;path=pathlib.Path(sys.argv[-1]);name=path.name;folder=pathlib.Path.cwd()
if'solutions'in path.relative_to(folder)._tail:
 codeArr=[*open(folder/'typings'/(name+'i'))][1:]
 parametrs=[i.split(':Literal')[0]for i in codeArr if':Literal'in i]
 code=''.join(codeArr)
 values=[code.split(':Literal')[n:n+2][0][:n<len(parametrs)and~len(i)or None]for n,i in enumerate(parametrs[1:]+[1],1)]
 with warnings.catch_warnings():
  warnings.simplefilter('ignore',SyntaxWarning)
  db={n:eval(i)for n,i in zip(parametrs,values)}
 countResult=0
 for n,results in enumerate(db.pop('results'),1):
  fileCode=[c for c in open(path)if' import results, 'not in c]
  file='def results():\n '+' '.join(c.replace('result','return').replace(' ='['result'in c],' ',1)for c in fileCode)
  exec(file,l:={k:v[~-n]for k,v in db.items()})
  result=l.pop('results')();del l['__builtins__']
  q=result==results;countResult+=q
  print(f'{'❌✅'[q]}№{n} {f'{l}'[2:-1].replace("':",' =').replace(", '",' ')}, {result = }'+f', {results = }'*(q<1))
 print((f'{n} = {countResult} ✅ + {n-countResult} ❌',f'✅{n}')[countResult==n])
else:
 name=='solution.py'or __import__('subprocess').run((folder/'venv'/('bin','Scripts')[win:=sys.platform=='win32']/('python'+'.exe'*win),path))