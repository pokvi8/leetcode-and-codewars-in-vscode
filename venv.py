venv=__import__('pathlib').Path(__file__);venv.unlink();venv=venv.parents[1]/'venv'
__import__('venv').create(venv,with_pip=1,scm_ignore_files=['git'])
__import__('subprocess').run(f'{venv/('bin','Scripts')[win:=__import__('sys').platform=='win32']/('pip'+'.exe'*win)} install playwright')