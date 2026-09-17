import pathlib,sys
parameters=[i+':Literal[]'for i in eval(sys.argv[-1])]
pyi=pathlib.Path.cwd()/f'typings/{pathlib.Path(sys.argv[0]).name}i'
pyi.parent.mkdir(511,1,1)
pyi.unlink(1)
def solutions(*_):
 code='\n'.join(f'{(a:=i.split('[',1))[0]}[{a[1].strip('\n,')[:-1]},{repr(_[parameters.index(a[0]+'[]')])}]'for i in(pyi.exists()and open(pyi)or parameters)if':Literal['in i)
 pyi.write_text('from typing import Literal\n'+code)

describe=lambda _:lambda _:_()
it=lambda _:lambda _:_()
assert_equals=lambda result,results,_=None:solutions(results,*result['pokvi'])
expect=lambda result,_=None:solutions(*(result[a:=(dict==type(s:=result[0])and'pokvi'in s)*2],*result[~a]['pokvi']))