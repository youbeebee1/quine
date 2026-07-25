import json
python = 'import json\npython = %r\njava = %r\ncpp = %r\npython_code = python %% (python, java, cpp)\njava_code = java %% json.dumps(python_code)\ncpp_code = cpp %% json.dumps(java_code)\nprint(cpp_code)'
java = 'public class Main {\n    public static void main(String[] args) {\n        String s = %s;\n        System.out.print(s);\n    }\n}'
cpp = '#include <iostream>\n#include <string>\nint main() {\n    std::string s = %s;\n    std::cout << s;\n}'
python_code = python % (python, java, cpp)
java_code = java % json.dumps(python_code)
cpp_code = cpp % json.dumps(java_code)
print(cpp_code)