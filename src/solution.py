import warnings,pathlib,sys;path=pathlib.Path(sys.argv[-1]);name=path.name;folder=pathlib.Path.cwd()
if'solutions'in path.relative_to(folder)._tail:
 countResult=0;pyi=[i.split(':Literal')for i in open(folder/f'typings/{name}i')][1:]
 with warnings.catch_warnings(action='ignore',category=SyntaxWarning):
  db={n:eval(i)for n,i in pyi}
  file=f'def results({','.join([*db][1:])}):\n '+' '.join(i.replace('results','pokvi').replace('result','return').replace('pokvi','results').replace(' ='['result'in i],' ',1)for i in open(path)if' import results, 'not in i)
  exec(file,l:={});func=l['results']
 for n,results in enumerate(db.pop('results'),1):
  l={k:v[~-n]for k,v in db.items()}
  result=func(*l.values())
  q=result==results;countResult+=q
  print('❌✅'[q]+f'№{n} {f'{l}'[2:-1].replace("':",' =').replace(", '",', ')}, {results = }'+f', {result = }'*(q<1))
 print(('❌✅'[countResult>0]+f'{n}',f'{n} = {countResult} ✅ + {n-countResult} ❌')[0<countResult<n])
else:
 name=='solution.py'or __import__('subprocess').run((folder/'venv'/('bin','Scripts')[win:=sys.platform=='win32']/('python'+'.exe'*win),path))