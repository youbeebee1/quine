# 7 langs quine relay (python -> c -> js -> cpp -> java -> ruby -> rust -> python) (c) UBB
import json
s = '# 7 langs quine relay (python -> c -> js -> cpp -> java -> ruby -> rust -> python) (c) UBB\nimport json\ns = %r\nc = %r\njs = %r\ncpp = %r\njava = %r\nruby = %r\nrust = %r\npython_code = s %% (s, c, js, cpp, java, ruby, rust)\nrust_code = rust %% json.dumps(python_code)\nruby_code = ruby %% json.dumps(rust_code)\njava_code = java %% json.dumps(ruby_code)\ncpp_code = cpp %% json.dumps(java_code)\njs_code = js %% json.dumps(cpp_code)\nc_code = c %% json.dumps(js_code)\nprint(c_code)\n'
c = '#include <stdio.h>\nint main() {\n    char s[] = %s;\n    printf("%%s", s);\n}'
js = 'const s = %s;\nconsole.log(s);'
cpp = '#include <iostream>\n#include <string>\nint main() {\n    std::string s = %s;\n    std::cout << s;\n}'
java = 'public class Main {\n    public static void main(String[] args) {\n        String s = %s;\n        System.out.print(s);\n    }\n}'
ruby = 's = %s\nprint "%%s" %% [s]'
rust = 'fn main() {\n    let s = %s;\n    println!("{}", s);\n}'
python_code = s % (s, c, js, cpp, java, ruby, rust)
rust_code = rust % json.dumps(python_code)
ruby_code = ruby % json.dumps(rust_code)
java_code = java % json.dumps(ruby_code)
cpp_code = cpp % json.dumps(java_code)
js_code = js % json.dumps(cpp_code)
c_code = c % json.dumps(js_code)
print(c_code)