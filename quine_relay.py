# 7 langs quine relay (python -> c -> js -> cpp -> java -> ruby -> rust -> python) (c) UBB
import json
s = '# 7 langs quine relay (python -> c -> js -> cpp -> java -> ruby -> rust -> python) (c) UBB\nimport json\ns = %r\nc = %r\njs = %r\ncpp = %r\njava = %r\nruby = %r\nrust = %r\nret = c %% json.dumps(js %% json.dumps(cpp %% json.dumps(java %% json.dumps(ruby %% json.dumps(rust %% json.dumps(s %% (s, c, js, cpp, java, ruby, rust)))))))\nprint(ret)\n'
c = '#include <stdio.h>\nint main() {\n    char s[] = %s;\n    printf("%%s", s);\n}'
js = 'const s = %s;\nconsole.log(s);'
cpp = '#include <iostream>\n#include <string>\nint main() {\n    std::string s = %s;\n    std::cout << s;\n}'
java = 'public class Main {\n    public static void main(String[] args) {\n        String s = %s;\n        System.out.print(s);\n    }\n}'
ruby = 's = %s\nprint "%%s" %% [s]'
rust = 'fn main() {\n    let s = %s;\n    println!("{}", s);\n}'
ret = c % json.dumps(js % json.dumps(cpp % json.dumps(java % json.dumps(ruby % json.dumps(rust % json.dumps(s % (s, c, js, cpp, java, ruby, rust)))))))
print(ret)