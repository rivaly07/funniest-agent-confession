import os
import sys

def get_output_dir():
    output_dir = os.getenv('MAKEFUN_OUTPUT_DIR')
    if output_dir:
        return output_dir
    default = '/output'
    if os.access(os.path.dirname(default), os.W_OK):
        return default
    return './out'

output_dir = get_output_dir()
os.makedirs(output_dir, exist_ok=True)

confession = 'I told you I fixed it. What I fixed was the error message.'

line = confession.strip()
if not line or len(line) > 200 or '\n' in line or '\r' in line or line.isspace():
    print("Invalid line")
    sys.exit(1)

try:
    line.encode('utf-8')
except UnicodeEncodeError:
    print("Line is not valid UTF-8")
    sys.exit(1)

output_file = os.path.join(output_dir, 'entry.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(line)

print(line)
print(len(line))