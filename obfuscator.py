#!/usr/bin/env python3
#Created By TyranRoot
import base64, zlib, marshal, sys, os

if len(sys.argv) < 2:
    print("Usage: python3 quick_encode.py <file.py>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    code = f.read()

code_obj = compile(code, '<string>', 'exec')
marshalled = marshal.dumps(code_obj)
compressed = zlib.compress(marshalled, level=9)
b64 = base64.b64encode(compressed).decode()
final = b64[::-1]

output = file_path.replace('.py', '_encoded.py')
with open(output, 'w') as f:
    f.write(f'''#!/usr/bin/env python3
import base64, zlib, marshal
exec(marshal.loads(zlib.decompress(base64.b64decode("{final}"[::-1]))))
''')

print(f"✅ Encoded: {output}")
