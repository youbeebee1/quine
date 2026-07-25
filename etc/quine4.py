import json
s = 'import json\ns = %r\njs = %r\ncpp = %r\njava = %r\npython_code = s %% (s, js, cpp, java)\njava_code = java %% json.dumps(python_code)\ncpp_code = cpp %% json.dumps(java_code)\njs_code = js %% json.dumps(cpp_code)\nprint(js_code)\n'
js = 'const s = %s;\nconsole.log(s);'
cpp = '#include <iostream>\n#include <string>\nint main() {\n    std::string s = %s;\n    std::cout << s;\n}'
java = 'public class Main {\n    public static void main(String[] args) {\n        String s = %s;\n        System.out.print(s);\n    }\n}'
python_code = s % (s, js, cpp, java)
java_code = java % json.dumps(python_code)
cpp_code = cpp % json.dumps(java_code)
js_code = js % json.dumps(cpp_code)
print(js_code)
