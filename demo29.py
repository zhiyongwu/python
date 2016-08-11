

import time
print(time.time())
import sys
PY3 = sys.version_info[0] == 3
WIN = sys.platform[:3] == 'win'
print(time.time())
print(PY3,WIN)