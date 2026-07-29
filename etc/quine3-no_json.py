# 3 langs quine relay (python -> js -> ruby -> python) (c) UBB
esc = lambda x: '"' + x.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'
s = '# 3 langs quine relay (python -> js -> ruby -> python) (c) UBB\nesc = lambda x: \'"\' + x.replace(\'\\\\\', \'\\\\\\\\\').replace(\'"\', \'\\\\"\').replace(\'\\n\', \'\\\\n\') + \'"\'\ns = %r\njs = %r\nruby = %r\npython_code = s %% (s, js, ruby)\nruby_code = ruby %% esc(python_code)\njs_code = js %% esc(ruby_code)\nprint(js_code)'
js = 'const s = %s;\nconsole.log(s);'
ruby = 's = %s\nprint "%%s" %% [s]'
python_code = s % (s, js, ruby)
ruby_code = ruby % esc(python_code)
js_code = js % esc(ruby_code)
print(js_code)