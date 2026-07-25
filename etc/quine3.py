# 3 langs quine relay (python -> js -> ruby -> python) (c) UBB
import json
s = '# 3 langs quine relay (python -> js -> ruby -> python) (c) UBB\nimport json\ns = %r\njs = %r\nruby = %r\npython_code = s %% (s, js, ruby)\nruby_code = ruby %% json.dumps(python_code)\njs_code = js %% json.dumps(ruby_code)\nprint(js_code)'
js = 'const s = %s;\nconsole.log(s);'
ruby = 's = %s\nprint "%%s" %% [s]'
python_code = s % (s, js, ruby)
ruby_code = ruby % json.dumps(python_code)
js_code = js % json.dumps(ruby_code)
print(js_code)