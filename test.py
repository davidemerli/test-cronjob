from datetime import datetime
import os

def cwd():
    return os.path.abspath(os.path.dirname(sys.argv[0]))

with open(f'{cwd()}/test.txt', 'a') as file:
    file.write(f'test {datetime.now()}\n')
