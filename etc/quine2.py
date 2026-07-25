s = 's = %r\ncpp = %r\npython_code = s %% (s, cpp)\nimport json\nprint(cpp %% json.dumps(python_code))'
cpp = '#include <iostream>\n#include <string>\nint main() {\n    std::string s = %s;\n    std::cout << s;\n}'
python_code = s % (s, cpp)
import json
print(cpp % json.dumps(python_code))
